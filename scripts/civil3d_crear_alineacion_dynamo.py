# -*- coding: utf-8 -*-
"""
Crea en Civil 3D la alineación del eje DG-2018 ENTIDAD POR ENTIDAD, con las restricciones de
tangencia que permiten editarla por PI:

  - cada tangente        -> línea FIJA
  - curva aislada        -> curva LIBRE (entre las dos líneas, radio)      => tiene PI y pinzamientos
  - curvas pegadas       -> curvas FLOTANTES (radio, punto de paso) y la última LIBRE (radio)
    (compuestas / en S)     => el grupo queda unido y editable (sin PI de grupo, que Civil 3D no modela)
  - si el tramo EMPIEZA dentro de una curva -> esa curva recortada se crea FIJA por 3 puntos

TRAMO DE PROGRESIVAS (opcional): se puede dibujar solo una parte del eje, por ejemplo de 1+080 a 4+500.
  El primer y el último elemento se recortan en la progresiva exacta y la alineación creada arranca
  con esa progresiva (ReferencePointStation), de modo que sus estacas coinciden con las del eje completo.
  Las progresivas se aceptan como número (1080) o como texto "1+080" / "1+080.50".

Cómo usarlo (Civil 3D 2020 a 2027, con Dynamo para Civil 3D):
  1. Ficha Administrar > Dynamo. Nuevo gráfico.
  2. Añadir un nodo "Python Script" (motor CPython3 o IronPython2, ambos valen) y pegar este archivo.
  3. Conectar en IN[0] un nodo String con la ruta del LandXML, por ejemplo
         C:\\proyecto\\EJE_DG2018_circular.xml
     Opcional: IN[1] nombre de la alineación; IN[2] ruta del archivo de criterios DG2018_Corregido_2.xml
               IN[3] progresiva inicial del tramo (p.ej. 1080);  IN[4] progresiva final (p.ej. 4500)
               Si IN[3] / IN[4] se dejan vacíos se dibuja desde el inicio / hasta el final del eje.
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
VELOCIDAD = 40.0                                      # km/h, velocidad de diseño desde el inicio del tramo
PROG_INI = None                                       # progresiva inicial del tramo (None = inicio del eje); se usa si no se conecta IN[3]
PROG_FIN = None                                       # progresiva final del tramo (None = fin del eje);      se usa si no se conecta IN[4]
TOL = 1e-4                                            # m, longitud mínima de un elemento

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
    """Devuelve (elementos, progresiva_inicial_del_eje).
    elementos = [{'tipo':'L'|'C', 'A':(x,y), 'B':(x,y), 'C':(x,y), 'R', 'L', 'ccw'}]"""
    root = ET.parse(resolver_ruta(ruta)).getroot()
    cg = None; sta0 = 0.0
    for el in root.iter():
        if _tag(el) == 'Alignment' and el.get('staStart'):
            try:
                sta0 = float(el.get('staStart'))
            except ValueError:
                pass
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
            if L <= TOL:
                continue
            elems.append({'tipo': 'L', 'A': A, 'B': B, 'L': L})
        elif t == 'Curve':
            A = _pt(hijos['Start']); B = _pt(hijos['End']); C = _pt(hijos['Center'])
            R = float(el.get('radius')); L = float(el.get('length'))
            elems.append({'tipo': 'C', 'A': A, 'B': B, 'C': C, 'R': R, 'L': L, 'ccw': el.get('rot') == 'ccw'})
        else:
            raise Exception('Elemento no soportado en CoordGeom: %s (este script es solo para ejes circulares)' % t)
    return elems, sta0

# ----------------------------------------------------------------------------------------------
# 1b) Tramo de progresivas: recorte de los elementos entre dos progresivas
# ----------------------------------------------------------------------------------------------
def parsear_progresiva(v):
    """None/'' -> None;  1080 -> 1080.0;  '1+080' -> 1080.0;  '1+080.50' -> 1080.5;  '1080,5' -> 1080.5"""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(' ', '').replace('+', '')
    if s == '':
        return None
    if ',' in s and '.' not in s:
        s = s.replace(',', '.')
    return float(s)

def punto_en_elemento(e, d):
    """Punto del elemento a la distancia d medida desde su inicio A (a lo largo de la línea o del arco)"""
    if e['tipo'] == 'L':
        f = d / e['L']
        return (e['A'][0] + f * (e['B'][0] - e['A'][0]), e['A'][1] + f * (e['B'][1] - e['A'][1]))
    cx, cy = e['C']; R = e['R']
    a0 = math.atan2(e['A'][1] - cy, e['A'][0] - cx)
    a = a0 + (d / R if e['ccw'] else -d / R)
    return (cx + R * math.cos(a), cy + R * math.sin(a))

def subelemento(e, d0, d1):
    """Copia del elemento recortada entre las distancias d0 y d1 desde su inicio"""
    s = dict(e)
    s['A'] = punto_en_elemento(e, d0) if d0 > 0 else e['A']
    s['B'] = punto_en_elemento(e, d1) if d1 < e['L'] else e['B']
    s['L'] = d1 - d0
    return s

def recortar_tramo(elems, sta0, prog_ini, prog_fin):
    """Devuelve (elementos del tramo, prog_ini efectiva, prog_fin efectiva, avisos).
    Las progresivas se miden acumulando longitudes desde sta0 (staStart del XML)."""
    avisos = []
    L_total = sum(e['L'] for e in elems)
    sta_fin_eje = sta0 + L_total
    p0 = sta0 if prog_ini is None else prog_ini
    p1 = sta_fin_eje if prog_fin is None else prog_fin
    if p0 < sta0 - TOL:
        avisos.append('La progresiva inicial %.3f es menor que el inicio del eje (%.3f): se usa %.3f' % (p0, sta0, sta0)); p0 = sta0
    if p1 > sta_fin_eje + TOL:
        avisos.append('La progresiva final %.3f supera el fin del eje (%.3f): se usa %.3f' % (p1, sta_fin_eje, sta_fin_eje)); p1 = sta_fin_eje
    if p1 - p0 <= TOL:
        raise Exception('El tramo %.3f a %.3f no tiene longitud (el eje va de %.3f a %.3f)' % (p0, p1, sta0, sta_fin_eje))
    out = []; s = sta0
    for e in elems:
        a, b = s, s + e['L']; s = b
        if b <= p0 + TOL or a >= p1 - TOL:
            continue
        d0 = max(0.0, p0 - a); d1 = min(e['L'], p1 - a)
        if d1 - d0 <= TOL:
            continue
        out.append(subelemento(e, d0, d1))
    if not out:
        raise Exception('No hay elementos entre las progresivas %.3f y %.3f' % (p0, p1))
    return out, p0, p1, avisos

# ----------------------------------------------------------------------------------------------
# 1c) Plan de construcción
# ----------------------------------------------------------------------------------------------
def punto_medio_arco(c):
    """punto medio del arco, para la curva fija por 3 puntos y la alternativa 'curva por punto de paso'"""
    return punto_en_elemento(c, c['L'] / 2.0)

def direccion_salida(c):
    """vector tangente unitario al final del arco (en B)"""
    cx, cy = c['C']; R = c['R']
    rx, ry = (c['B'][0] - cx) / R, (c['B'][1] - cy) / R
    return (-ry, rx) if c['ccw'] else (ry, -rx)

def plan(elems):
    """Secuencia de operaciones:
       ('L', k) líneas fijas; ('CFIJA', k) curva fija inicial; ('FLOT', k, prev); ('LIBRE', k, prev, next)"""
    if not elems:
        raise Exception('No hay elementos que dibujar')
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
                ops.append(('CFIJA', j))                 # el tramo empieza en curva: no hay entidad anterior
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

def preparar(ruta_xml, prog_ini, prog_fin):
    """Lee el XML, recorta el tramo y arma el plan. Devuelve (elems, ops, p0, p1, avisos)"""
    elems, sta0 = leer_landxml(ruta_xml)
    elems, p0, p1, avisos = recortar_tramo(elems, sta0, parsear_progresiva(prog_ini), parsear_progresiva(prog_fin))
    return elems, plan(elems), p0, p1, avisos

# ----------------------------------------------------------------------------------------------
# 2) Construcción en Civil 3D
# ----------------------------------------------------------------------------------------------
def construir(ruta_xml, nombre, ruta_criterios, velocidad, prog_ini=None, prog_fin=None):
    import clr
    clr.AddReference('AcMgd'); clr.AddReference('AcCoreMgd'); clr.AddReference('AcDbMgd')
    clr.AddReference('AecBaseMgd'); clr.AddReference('AeccDbMgd')
    from Autodesk.AutoCAD.ApplicationServices import Application
    from Autodesk.AutoCAD.DatabaseServices import OpenMode
    from Autodesk.AutoCAD.Geometry import Point3d, Vector3d
    from Autodesk.Civil.ApplicationServices import CivilApplication
    from Autodesk.Civil.DatabaseServices import Alignment
    try:
        from Autodesk.Civil.DatabaseServices import CurveParamType, CurveType
    except ImportError:
        from Autodesk.Civil import CurveParamType, CurveType

    msgs = []
    elems, ops, p0, p1, avisos = preparar(ruta_xml, prog_ini, prog_fin)
    msgs.extend(avisos)
    msgs.append('tramo: %.3f a %.3f | inicio en (%.3f, %.3f) | fin en (%.3f, %.3f)' % (
        p0, p1, elems[0]['A'][0], elems[0]['A'][1], elems[-1]['B'][0], elems[-1]['B'][1]))
    adoc = Application.DocumentManager.MdiActiveDocument
    civdoc = CivilApplication.ActiveDocument
    db = adoc.Database

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
            # progresiva de inicio del tramo (para que las estacas coincidan con las del eje completo)
            try:
                align.ReferencePointStation = float(p0)
            except Exception as ex:
                msgs.append('No se pudo fijar la progresiva inicial %.3f: %s' % (p0, ex))
            # velocidad de diseño y archivo de criterios (opcional)
            try:
                align.DesignSpeeds.Add(float(align.StartingStation), float(velocidad))
            except Exception as ex:
                msgs.append('No se pudo fijar la velocidad de diseño: %s' % ex)
            if ruta_criterios:
                try:
                    align.UseDesignCriteriaFile = True
                    align.DesignCriteriaFileName = ruta_criterios
                except Exception as ex:
                    msgs.append('No se pudo asociar el archivo de criterios: %s' % ex)
            t.Commit()
    resumen = 'Alineación "%s" (prog. %.3f a %.3f): %d líneas fijas, %d curvas fijas, %d curvas flotantes, %d curvas libres (%d elementos). Longitud esperada %.3f m.' % (
        nombre, p0, p1, n_lin, n_fij, n_flot, n_lib, len(elems), sum(e['L'] for e in elems))
    return [resumen] + msgs

# ----------------------------------------------------------------------------------------------
# 3) Punto de entrada: en Dynamo existe IN; fuera de Dynamo solo muestra el plan (prueba en seco)
# ----------------------------------------------------------------------------------------------
try:
    IN  # noqa
    _en_dynamo = True
except NameError:
    _en_dynamo = False

def _in(i, por_defecto):
    try:
        v = IN[i]
    except Exception:
        return por_defecto
    return por_defecto if v is None or v == '' else v

if _en_dynamo:
    OUT = construir(_in(0, RUTA_XML), _in(1, NOMBRE), _in(2, RUTA_CRITERIOS), VELOCIDAD, _in(3, PROG_INI), _in(4, PROG_FIN))
elif __name__ == '__main__':
    # prueba en seco:  python civil3d_crear_alineacion_dynamo.py EJE.xml [prog_ini] [prog_fin]
    import sys
    _ruta = sys.argv[1] if len(sys.argv) > 1 else RUTA_XML
    _p0 = sys.argv[2] if len(sys.argv) > 2 else PROG_INI
    _p1 = sys.argv[3] if len(sys.argv) > 3 else PROG_FIN
    elems, ops, p0, p1, avisos = preparar(_ruta, _p0, _p1)
    for a in avisos:
        print('AVISO:', a)
    cuenta = lambda tipo: sum(1 for o in ops if o[0] == tipo)
    print('tramo %.3f a %.3f | elementos: %d | líneas fijas: %d | curvas fijas: %d | curvas flotantes: %d | curvas libres: %d | longitud %.3f m' % (
        p0, p1, len(elems), cuenta('L'), cuenta('CFIJA'), cuenta('FLOT'), cuenta('LIBRE'), sum(e['L'] for e in elems)))
    print('inicio (%.3f, %.3f)  fin (%.3f, %.3f)' % (elems[0]['A'][0], elems[0]['A'][1], elems[-1]['B'][0], elems[-1]['B'][1]))
    print('primeras operaciones (en orden de creación de curvas):')
    for o in [o for o in ops if o[0] != 'L'][:12]:
        print('  ', o, 'R=%.2f' % elems[o[1]]['R'], tipo_curva(elems, o[1]) if o[1] > 0 else '-')
