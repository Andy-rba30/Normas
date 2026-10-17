# -*- coding: utf-8 -*-
"""
Crea en Civil 3D la alineación del eje DG-2018 ENTIDAD POR ENTIDAD, con las restricciones de
tangencia que permiten editarla por PI:

  - cada tangente        -> línea FIJA
  - curva aislada        -> curva LIBRE (entre las dos líneas, radio)      => tiene PI y pinzamientos
  - curvas pegadas       -> curvas FLOTANTES (radio, punto de paso) y la última LIBRE (radio)
    (compuestas / en S)     => el grupo queda unido y editable (sin PI de grupo, que Civil 3D no modela)
  - si el eje EMPIEZA con una curva (solo posible desde polilínea) -> curva FIJA por 3 puntos

FUENTE DE LA GEOMETRÍA (IN[0]), dos opciones:
  a) Ruta de un LandXML (String), por ejemplo  C:\\proyecto\\EJE_DG2018_circular.xml
  b) Una POLILÍNEA con arcos seleccionada en el dibujo:
       - nodo "Select Object" (Dynamo for Civil 3D)  -> conectar su salida a IN[0]
       - o un String con el HANDLE de la polilínea (comando LIST en AutoCAD lo muestra), p.ej. "2F3A"
     Sirven polilíneas ligeras (PLINE) y polilíneas 2D antiguas; una polilínea 3D no admite arcos.
     El sentido de la alineación es el sentido de dibujo de la polilínea (si sale al revés, usa
     el comando REVERSE / INVERTIR sobre la polilínea y vuelve a ejecutar).

Cómo usarlo (Civil 3D 2020 a 2027, con Dynamo para Civil 3D):
  1. Ficha Administrar > Dynamo. Nuevo gráfico.
  2. Añadir un nodo "Python Script" (motor CPython3 o IronPython2, ambos valen) y pegar este archivo.
  3. Conectar en IN[0] la fuente (String con la ruta del XML, o "Select Object" con la polilínea).
     Opcional: IN[1] nombre de la alineación; IN[2] ruta del archivo de criterios DG2018_Corregido_2.xml
  4. Ejecutar UNA vez (en modo manual). La salida OUT es el resumen y los avisos.
  La alineación se crea en el dibujo activo, sin emplazamiento (site), en la capa actual, con el primer
  estilo de alineación y el primer conjunto de etiquetas del dibujo.

API usada (Autodesk.Civil.DatabaseServices.AlignmentEntityCollection):
  AddFixedLine(Point3d, Point3d)
  AddFixedCurve(Point3d inicio, Point3d medio, Point3d fin)
  AddFloatingCurve(Int32 entidadAnterior, Point3d puntoDePaso, Double radio, Boolean mayorDe180, CurveType)
  AddFreeCurve(Int32 anterior, Int32 siguiente, Double radio, CurveParamType.Radius, Boolean mayorDe180, CurveType)
  Alternativas si una firma no existe en la versión instalada:
  AddFloatingCurve(Int32 anterior, Point3d puntoDePaso, Vector3d direccionEnElPunto)
  AddFreeCurve(Int32 anterior, Int32 siguiente, Point3d puntoDePaso)
"""
import math
import os
import xml.etree.ElementTree as ET

RUTA_XML = r'C:\proyecto\EJE_DG2018_circular.xml'   # se usa si no se conecta IN[0]
NOMBRE = 'EJE_DG2018'
RUTA_CRITERIOS = ''                                   # p.ej. r'C:\ProgramData\Autodesk\C3D 2027\esp\Data\Corridor Design Standards\Metric\DG2018_Corregido_2.xml'
VELOCIDAD = 40.0                                      # km/h, velocidad de diseño desde la progresiva 0

# ----------------------------------------------------------------------------------------------
# 1) Lectura del LandXML (independiente de Civil 3D, para poder probarla fuera)
# ----------------------------------------------------------------------------------------------
def _tag(e):
    return e.tag.split('}')[-1]

def _pt(txt):
    n, e = [float(v) for v in txt.split()[:2]]   # LandXML: Norte Este -> (X=Este, Y=Norte)
    return (e, n)

def resolver_ruta(ruta):
    """Acepta la ruta sin extensión (Windows la oculta) y da un mensaje claro si no existe"""
    ruta = (ruta or '').strip().strip('"')
    if os.path.isfile(ruta):
        return ruta
    for ext in ('.xml', '.XML'):
        if os.path.isfile(ruta + ext):
            return ruta + ext
    carpeta = os.path.dirname(ruta) or '.'
    xmls = [f for f in os.listdir(carpeta) if f.lower().endswith('.xml')] if os.path.isdir(carpeta) else []
    raise Exception('No encuentro el archivo "%s". Escribe la ruta completa con extension .xml. '
                    'Archivos .xml en esa carpeta: %s' % (ruta, ', '.join(xmls) if xmls else 'ninguno'))

def leer_landxml(ruta):
    """Devuelve la lista de elementos [{'tipo':'L'|'C', 'A':(x,y), 'B':(x,y), 'C':(x,y), 'R', 'L', 'ccw'}]"""
    root = ET.parse(resolver_ruta(ruta)).getroot()
    cg = None
    for el in root.iter():
        if _tag(el) == 'CoordGeom':
            cg = el; break
    if cg is None:
        raise Exception('El archivo no tiene <CoordGeom>')
    elems = []
    for el in cg:
        t = _tag(el)
        hijos = {_tag(h): h.text for h in el}
        if t == 'Line':
            A = _pt(hijos['Start']); B = _pt(hijos['End'])
            L = math.hypot(B[0] - A[0], B[1] - A[1])
            if L <= 1e-4:
                continue
            elems.append({'tipo': 'L', 'A': A, 'B': B, 'L': L})
        elif t == 'Curve':
            A = _pt(hijos['Start']); B = _pt(hijos['End']); C = _pt(hijos['Center'])
            R = float(el.get('radius')); L = float(el.get('length'))
            elems.append({'tipo': 'C', 'A': A, 'B': B, 'C': C, 'R': R, 'L': L, 'ccw': el.get('rot') == 'ccw'})
        else:
            raise Exception('Elemento no soportado en CoordGeom: %s (este script es solo para ejes circulares)' % t)
    return elems

# ----------------------------------------------------------------------------------------------
# 1b) Lectura de una polilínea de AutoCAD (misma estructura de elementos que el LandXML)
# ----------------------------------------------------------------------------------------------
def elems_de_polilinea(pl):
    """pl: Autodesk.AutoCAD.DatabaseServices.Polyline abierta para lectura.
    Cada segmento con bulge 0 es una línea; con bulge != 0 es un arco (bulge > 0 = antihorario)."""
    n = pl.NumberOfVertices
    if n < 2:
        raise Exception('La polilínea tiene menos de 2 vértices')
    nseg = n if pl.Closed else n - 1
    elems = []
    for i in range(nseg):
        p0 = pl.GetPoint2dAt(i); p1 = pl.GetPoint2dAt((i + 1) % n)
        A = (p0.X, p0.Y); B = (p1.X, p1.Y)
        cuerda = math.hypot(B[0] - A[0], B[1] - A[1])
        if cuerda <= 1e-6:
            continue                                   # vértices repetidos
        b = pl.GetBulgeAt(i)
        if abs(b) < 1e-9:
            elems.append({'tipo': 'L', 'A': A, 'B': B, 'L': cuerda})
        else:
            arc = pl.GetArcSegment2dAt(i)              # CircularArc2d: Center, Radius
            R = float(arc.Radius)
            delta = 4.0 * math.atan(abs(b))            # ángulo central del arco
            elems.append({'tipo': 'C', 'A': A, 'B': B, 'C': (arc.Center.X, arc.Center.Y),
                          'R': R, 'L': R * delta, 'ccw': b > 0})
    if not elems:
        raise Exception('La polilínea no tiene segmentos con longitud')
    return elems

def es_ruta_xml(fuente):
    """IN[0] es una ruta de archivo si es texto y existe el archivo (con o sin .xml) o lleva separadores de carpeta"""
    if not isinstance(fuente, str):
        return False
    f = fuente.strip().strip('"')
    if f.lower().endswith('.xml') or '\\' in f or '/' in f:
        return True
    return os.path.isfile(f) or os.path.isfile(f + '.xml')

def punto_medio_arco(c):
    """punto medio del arco, para la curva fija por 3 puntos y la alternativa 'curva por punto de paso'"""
    cx, cy = c['C']; R = c['R']
    a0 = math.atan2(c['A'][1] - cy, c['A'][0] - cx)
    delta = c['L'] / R
    am = a0 + (delta / 2.0 if c['ccw'] else -delta / 2.0)
    return (cx + R * math.cos(am), cy + R * math.sin(am))

def direccion_salida(c):
    """vector tangente unitario al final del arco (en B)"""
    cx, cy = c['C']; R = c['R']
    rx, ry = (c['B'][0] - cx) / R, (c['B'][1] - cy) / R
    return (-ry, rx) if c['ccw'] else (ry, -rx)

def plan(elems):
    """Secuencia de operaciones:
       ('L', k) líneas fijas; ('CFIJA', k) curva fija inicial; ('FLOT', k, prev); ('LIBRE', k, prev, next)"""
    if not elems:
        raise Exception('No hay elementos en la fuente')
    ops = [('L', k) for k, e in enumerate(elems) if e['tipo'] == 'L']
    k = 0
    while k < len(elems):
        if elems[k]['tipo'] != 'C':
            k += 1; continue
        i0 = k
        while k + 1 < len(elems) and elems[k + 1]['tipo'] == 'C':
            k += 1
        i1 = k; k += 1
        hay_linea_despues = i1 + 1 < len(elems)
        ultimo_libre = i1 if hay_linea_despues else None
        for j in range(i0, i1 + 1):
            if j == 0:
                ops.append(('CFIJA', j))                 # el eje empieza en curva: no hay entidad anterior
            elif j == ultimo_libre:
                ops.append(('LIBRE', j, j - 1, i1 + 1))   # anterior: la línea (curva aislada) o la flotante previa
            else:
                ops.append(('FLOT', j, j - 1))
    return ops

def tipo_curva(elems, j):
    """Compound si gira igual que la curva anterior pegada (o si viene de una línea); Reverse si cambia de sentido"""
    prev = elems[j - 1]
    if prev['tipo'] != 'C':
        return 'Compound'
    return 'Compound' if prev['ccw'] == elems[j]['ccw'] else 'Reverse'

# ----------------------------------------------------------------------------------------------
# 2) Construcción en Civil 3D
# ----------------------------------------------------------------------------------------------
def construir(fuente, nombre, ruta_criterios, velocidad):
    import clr
    clr.AddReference('AcMgd'); clr.AddReference('AcCoreMgd'); clr.AddReference('AcDbMgd')
    clr.AddReference('AecBaseMgd'); clr.AddReference('AeccDbMgd')
    from Autodesk.AutoCAD.ApplicationServices import Application
    from Autodesk.AutoCAD.DatabaseServices import OpenMode, ObjectId, Handle, Polyline, Polyline2d
    from Autodesk.AutoCAD.Geometry import Point3d, Vector3d
    from Autodesk.Civil.ApplicationServices import CivilApplication
    from Autodesk.Civil.DatabaseServices import Alignment
    try:
        from Autodesk.Civil.DatabaseServices import CurveParamType, CurveType
    except ImportError:
        from Autodesk.Civil import CurveParamType, CurveType

    msgs = []
    adoc = Application.DocumentManager.MdiActiveDocument
    civdoc = CivilApplication.ActiveDocument
    db = adoc.Database

    def object_id_de(f):
        """Acepta: nodo Select Object de Dynamo, ObjectId, handle (texto) o una lista con uno de ellos"""
        if isinstance(f, (list, tuple)):
            if not f:
                raise Exception('IN[0] es una lista vacía')
            f = f[0]
        if isinstance(f, ObjectId):
            return f
        oid = getattr(f, 'InternalObjectId', None)       # Autodesk.AutoCAD.DynamoNodes.Object
        if oid is not None:
            return oid
        h = f if isinstance(f, str) else getattr(f, 'Handle', None)
        if h is not None:
            try:
                return db.GetObjectId(False, Handle(int(str(h).strip(), 16)), 0)
            except Exception as ex:
                raise Exception('No encuentro una entidad con el handle "%s": %s' % (h, ex))
        raise Exception('IN[0] debe ser la ruta del LandXML (String) o una polilínea (nodo Select Object '
                        'o su handle). Recibido: %s' % type(f).__name__)

    def leer_polilinea(oid):
        with db.TransactionManager.StartTransaction() as t:
            ent = t.GetObject(oid, OpenMode.ForRead)
            tmp = None
            if isinstance(ent, Polyline):
                pl = ent
            elif isinstance(ent, Polyline2d):
                tmp = Polyline(); tmp.ConvertFrom(ent, False); pl = tmp
            else:
                raise Exception('La entidad seleccionada es "%s"; debe ser una polilínea (PLINE) con arcos. '
                                'Si es una polilínea 3D o líneas y arcos sueltos, únelos con PEDIT > Juntar.'
                                % ent.GetType().Name)
            elems = elems_de_polilinea(pl)
            if tmp is not None:
                tmp.Dispose()
            t.Commit()
        return elems

    with adoc.LockDocument():
        if es_ruta_xml(fuente):
            elems = leer_landxml(fuente); origen = 'LandXML'
        else:
            elems = leer_polilinea(object_id_de(fuente)); origen = 'polilínea'
        ops = plan(elems)
        msgs.append('fuente: %s | inicio en (%.3f, %.3f) | fin en (%.3f, %.3f)' % (
            origen, elems[0]['A'][0], elems[0]['A'][1], elems[-1]['B'][0], elems[-1]['B'][1]))

    def P(p): return Point3d(p[0], p[1], 0.0)
    def V(v): return Vector3d(v[0], v[1], 0.0)
    def firmas(metodo):
        ov = getattr(metodo, '__overloads__', None) or getattr(metodo, 'Overloads', None)
        return str(ov) if ov is not None else '?'
    ctype = {'Compound': CurveType.Compound, 'Reverse': CurveType.Reverse}

    with adoc.LockDocument():
        # nombre libre, capa actual, primer estilo y primer conjunto de etiquetas
        with db.TransactionManager.StartTransaction() as t:
            for aid in civdoc.GetAlignmentIds():
                if t.GetObject(aid, OpenMode.ForRead).Name == nombre:
                    raise Exception('Ya existe una alineación llamada "%s": bórrala o cambia el nombre (IN[1])' % nombre)
            capa = t.GetObject(db.Clayer, OpenMode.ForRead).Name
            def primer_estilo(coleccion, por_defecto):
                # la colección de estilos no admite índice numérico: se recorre y se toma el primero
                try:
                    for sid in coleccion:
                        return t.GetObject(sid, OpenMode.ForRead).Name
                except Exception:
                    en = coleccion.GetEnumerator()
                    if en.MoveNext():
                        return t.GetObject(en.Current, OpenMode.ForRead).Name
                return por_defecto
            estilo = primer_estilo(civdoc.Styles.AlignmentStyles, 'Standard')
            etiquetas = primer_estilo(civdoc.Styles.LabelSetStyles.AlignmentLabelSetStyles, 'Standard')
            msgs.append('capa: %s | estilo: %s | etiquetas: %s' % (capa, estilo, etiquetas))
            t.Commit()
        align_id = Alignment.Create(civdoc, nombre, '', capa, estilo, etiquetas)   # '' = sin emplazamiento (site)

        with db.TransactionManager.StartTransaction() as t:
            align = t.GetObject(align_id, OpenMode.ForWrite)
            ents = align.Entities
            ids = {}
            n_lin = n_fij = n_flot = n_lib = 0
            for op in ops:
                k = op[1]; e = elems[k]
                try:
                    if op[0] == 'L':
                        ids[k] = ents.AddFixedLine(P(e['A']), P(e['B'])).EntityId; n_lin += 1
                    elif op[0] == 'CFIJA':
                        ids[k] = ents.AddFixedCurve(P(e['A']), P(punto_medio_arco(e)), P(e['B'])).EntityId; n_fij += 1
                    elif op[0] == 'FLOT':
                        prev = ids[op[2]]; mayor180 = e['L'] / e['R'] > math.pi
                        try:
                            arc = ents.AddFloatingCurve(prev, P(e['B']), float(e['R']), mayor180, ctype[tipo_curva(elems, k)])
                        except Exception as ex1:
                            if n_flot == 0:
                                msgs.append('AddFloatingCurve(radio) falló: %s | firmas: %s' % (ex1, firmas(ents.AddFloatingCurve)))
                            arc = ents.AddFloatingCurve(prev, P(e['B']), V(direccion_salida(e)))
                        ids[k] = arc.EntityId; n_flot += 1
                    else:  # LIBRE
                        prev = ids[op[2]]; nxt = ids[op[3]]; mayor180 = e['L'] / e['R'] > math.pi
                        try:
                            arc = ents.AddFreeCurve(prev, nxt, float(e['R']), CurveParamType.Radius, mayor180, ctype[tipo_curva(elems, k)])
                        except Exception as ex1:
                            if n_lib == 0:
                                msgs.append('AddFreeCurve(radio) falló: %s | firmas: %s' % (ex1, firmas(ents.AddFreeCurve)))
                            arc = ents.AddFreeCurve(prev, nxt, P(punto_medio_arco(e)))
                        ids[k] = arc.EntityId; n_lib += 1
                except Exception as ex:
                    if len([m for m in msgs if m.startswith('ERROR')]) < 10:
                        msgs.append('ERROR elem %d (%s, R=%s): %s' % (k + 1, op[0], e.get('R', '-'), ex))
            # velocidad de diseño y archivo de criterios (opcional)
            try:
                align.DesignSpeeds.Add(0.0, float(velocidad))
            except Exception as ex:
                msgs.append('No se pudo fijar la velocidad de diseño: %s' % ex)
            if ruta_criterios:
                try:
                    align.UseDesignCriteriaFile = True
                    align.DesignCriteriaFileName = ruta_criterios
                except Exception as ex:
                    msgs.append('No se pudo asociar el archivo de criterios: %s' % ex)
            t.Commit()
    resumen = 'Alineación "%s": %d líneas fijas, %d curvas fijas, %d curvas flotantes, %d curvas libres (%d elementos de la %s). Longitud esperada %.3f m.' % (
        nombre, n_lin, n_fij, n_flot, n_lib, len(elems), origen, sum(e['L'] for e in elems))
    return [resumen] + msgs

# ----------------------------------------------------------------------------------------------
# 3) Punto de entrada: en Dynamo existe IN; fuera de Dynamo solo muestra el plan (prueba en seco)
# ----------------------------------------------------------------------------------------------
try:
    IN  # noqa
    _en_dynamo = True
except NameError:
    _en_dynamo = False

if _en_dynamo:
    _fuente = IN[0] if len(IN) > 0 and IN[0] is not None and IN[0] != '' else RUTA_XML
    _nombre = IN[1] if len(IN) > 1 and IN[1] else NOMBRE
    _crit = IN[2] if len(IN) > 2 and IN[2] else RUTA_CRITERIOS
    OUT = construir(_fuente, _nombre, _crit, VELOCIDAD)
elif __name__ == '__main__':
    import sys
    elems = leer_landxml(sys.argv[1] if len(sys.argv) > 1 else RUTA_XML)
    ops = plan(elems)
    nl = sum(1 for o in ops if o[0] == 'L'); nf = sum(1 for o in ops if o[0] == 'FLOT'); nb = sum(1 for o in ops if o[0] == 'LIBRE')
    print('elementos: %d  | líneas fijas: %d | curvas flotantes: %d | curvas libres: %d | longitud %.3f m' % (len(elems), nl, nf, nb, sum(e['L'] for e in elems)))
    print('primeras operaciones (en orden de creación de curvas):')
    for o in [o for o in ops if o[0] != 'L'][:12]:
        print('  ', o, 'R=%.2f' % elems[o[1]]['R'], tipo_curva(elems, o[1]))
