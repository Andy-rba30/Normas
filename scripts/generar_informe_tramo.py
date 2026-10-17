# -*- coding: utf-8 -*-
import json, math, re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

els = json.load(open('els.json'))
mem = json.load(open('memoria_tramo.json'))
P0, P1 = 1080.0, 4503.6656
def fmt(s): return '%d+%06.2f' % (s // 1000, s % 1000)
def prog(s):
    m = re.match(r'(\d+)\+(\d+\.?\d*)', s.strip()); return float(m.group(1))*1000+float(m.group(2))
curvas = [e for e in els if e['t'] == 'C']
for n, e in enumerate(curvas, 1): e['n'] = n; e['pi_sta'] = e['sta'] + e['T']; e['sent'] = 'D' if e['rot'] == 'cw' else 'I'

# ---- cruce con la memoria (misma curva si el PI coincide a 0.5 m y el radio a 0.05 m)
memrows = []
for k, rows in mem.items():
    for r in rows:
        try: memrows.append((k, float(r['Norte PI']), float(r['Este PI']), float(r['R (m)'] if 'R (m)' in r else r['R eje (m)']), r))
        except Exception: pass
for e in curvas:
    e['mem'] = None; e['origen'] = ''; e['sep'] = None
    for k, n, es, R, r in memrows:
        if math.hypot(n - e['PI'][0], es - e['PI'][1]) < 0.5 and abs(R - e['R']) < 0.05:
            e['mem'] = k
            if r.get('Origen'): e['origen'] = r['Origen']
            for key in ('Sep.\xa0máx. trazo (m)', 'Sep.\xa0(m)', 'Separación máx. (m)'):
                if r.get(key):
                    try: e['sep'] = max(e['sep'] or 0, float(r[key]))
                    except ValueError: pass
    if e['mem'] is None: e['origen'] = 'editada en Civil 3D (no está en la memoria)'

# ---- clasificacion
def clase(R):
    if R >= 49.99: return 'Normativa (peralte 8 %)'
    if R >= 44.99: return 'Radio mínimo (peralte 12 %)'
    if R >= 24.99: return 'Excepcional (Ve = 30 km/h)'
    return 'Curva de vuelta'
for e in curvas: e['clase'] = clase(e['R'])
# ---- radio interior en curvas de vuelta (Tabla 302.12, maniobra C2, calzada 6 m)
anchoC2 = [(6, 9.75), (7, 9.5), (8, 9.25), (10, 8.75), (12, 8.5), (15, 8.25), (20, 8.0)]
def ancho(ri):
    if ri <= 6: return 9.75
    if ri >= 20: return 8.0
    for (a, wa), (b, wb) in zip(anchoC2, anchoC2[1:]):
        if a <= ri <= b: return wa + (wb - wa) * (ri - a) / (b - a)
def radio_interior(R):
    ri = R - 4.0
    for _ in range(50): ri = R - ancho(max(ri, 0.1)) / 2.0
    return ri
def eval_ri(ri):
    return 'cumple (Ri ≥ 8 m)' if ri >= 8 else 'mínimo absoluto (6 ≤ Ri < 8 m)' if ri >= 6 else 'no cumple (Ri < 6 m)'
# ---- velocidad especifica (Tabla 302.02: p=12 %, f=0.17)
def ve(R): return min(40.0, math.sqrt(127 * R * 0.29))
# ---- grupos sin tangente intermedia y cadenas con tangentes < 5 m
def grupos(umbral):
    out = []; i = 0
    while i < len(els):
        if els[i]['t'] == 'C':
            g = [els[i]]; j = i
            while j + 1 < len(els):
                if els[j+1]['t'] == 'C': g.append(els[j+1]); j += 1
                elif els[j+1]['t'] == 'L' and els[j+1]['L'] < umbral and j + 2 < len(els) and els[j+2]['t'] == 'C': g.append(els[j+2]); j += 2
                else: break
            if len(g) > 1: out.append(g)
            i = j + 1
        else: i += 1
    return out
G0 = grupos(1e-9); G5 = grupos(5.0)
def tabla30208(Ri, Ro):
    if Ri < 40: return 'fuera de tabla (R entrada < 40 m)'
    mx = 1.5 * Ri; mn = max(50.0, Ri / 1.5)
    return 'cumple' if mn - 0.01 <= Ro <= mx + 0.01 else 'no cumple (admite %.0f a %.0f m)' % (mn, mx)

# ================= documento =================
doc = Document()
st = doc.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10.5)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
for s in doc.sections:
    s.left_margin = s.right_margin = Cm(2.0); s.top_margin = s.bottom_margin = Cm(2.0)

def H(txt, lvl=1):
    h = doc.add_heading(txt, lvl)
    for r in h.runs: r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)
    return h
def Pp(txt, bold=False, italic=False, size=None, after=4):
    p = doc.add_paragraph(); r = p.add_run(txt); r.bold = bold; r.italic = italic
    if size: r.font.size = Pt(size)
    p.paragraph_format.space_after = Pt(after); return p
def cita(txt, ref):
    p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.8); p.paragraph_format.space_after = Pt(4)
    r = p.add_run('“' + txt + '” '); r.italic = True; r.font.size = Pt(9.5)
    r2 = p.add_run('(' + ref + ')'); r2.font.size = Pt(9); r2.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexcolor); tcPr.append(shd)
def tabla(hdr, filas, anchos=None, size=8, align_num=True):
    t = doc.add_table(rows=1, cols=len(hdr)); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(hdr):
        c = t.rows[0].cells[i]; c.text = ''; r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(size); shade(c, 'D9E2F3')
    for f in filas:
        cells = t.add_row().cells
        for i, v in enumerate(f):
            cells[i].text = ''; p = cells[i].paragraphs[0]; r = p.add_run(str(v)); r.font.size = Pt(size)
            if align_num and re.fullmatch(r'[-\d.,+ °%/]+', str(v) or 'x'): p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if anchos:
        t.autofit = False
        tblPr = t._tbl.tblPr; lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
        for i, w in enumerate(anchos): t.columns[i].width = Cm(w)
        for row in t.rows:
            for i, w in enumerate(anchos): row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t

n_tot = len(curvas); cl_cnt = {}
for e in curvas: cl_cnt[e['clase']] = cl_cnt.get(e['clase'], 0) + 1
L_tramo = P1 - P0

# ---------- portada / titulo
t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run('INFORME DE DISEÑO GEOMÉTRICO EN PLANTA'); r.bold = True; r.font.size = Pt(16); r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)
t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run('Eje EJE_DG2018, tramo 1+080 a 4+500\nPuntos de intersección (PI), radios de giro, curvas consecutivas y radios mínimos y excepcionales según el Manual de Carreteras DG-2018'); r.font.size = Pt(11.5)
t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run('Fuente geométrica: ALINEAMIENTO - DISEÑO.xml (LandXML 1.2 exportado de Civil 3D), alineación "EJE_DG2018", staStart 1+080, longitud %.2f m. Sistema de coordenadas UTM WGS84 zona 17 Sur (EPSG 32717). Norma de sustento: MTC, Manual de Carreteras: Diseño Geométrico DG-2018, revisada y corregida a enero de 2018.' % L_tramo); r.font.size = Pt(9); r.italic = True

# ---------- 1
H('1. Objeto y premisas')
Pp('Este informe describe el eje en planta del tramo 1+080 a 4+500 tal como quedó dibujado en Civil 3D, y explica, curva por curva, las coordenadas de los PI, los radios adoptados, los sitios donde se usan curvas consecutivas (dobles y triples) y los sitios donde se recurre al radio mínimo normativo, a radios excepcionales o a curvas de vuelta, con el sustento del Manual DG-2018. No repite el detalle de peraltes, sobreanchos y transiciones, que está en la memoria del eje completo (EJE_DG2018_circular_memoria).')
Pp('Premisas del proyecto, iguales a las de la memoria: carretera de Segunda Clase, orografía escarpada (tipo 4), velocidad de diseño 40 km/h, calzada de 6.00 m, peralte máximo 12 % y tramos en zona poblada donde se busca la mínima expropiación. Por esa última premisa el eje sigue el trazo existente y sólo regulariza su geometría en tangentes rectas y curvas circulares; donde el terreno o las edificaciones no dejan sitio para el radio normativo se aceptan radios excepcionales, curvas de vuelta y curvas enlazadas sin tangente.')

# ---------- 2
H('2. Criterios de la DG-2018 que se aplican')
Pp('Se transcriben sólo los artículos que sustentan las decisiones de este tramo. Las páginas son las impresas en el manual.')
Pp('Radio mínimo y velocidad específica', bold=True)
cita('Los radios mínimos de curvatura horizontal son los menores radios que pueden recorrerse con la velocidad de diseño y la tasa máxima de peralte, en condiciones aceptables de seguridad y comodidad (…) Rmín = V² / 127 (Pmáx + fmáx)', 'Tópico 302.04.02, pág. 128')
cita('Área rural (accidentada o escarpada): 40 km/h, p máx 12.00 %, f máx 0.17, radio calculado 43.4 m, radio redondeado 45 m. (…) 30 km/h, 12.00 %, 0.17, 24.4 m, 25 m.', 'Tabla 302.02, pág. 129')
cita('En general en el trazo en planta de un tramo homogéneo (…) debe evitarse el empleo de curvas de radio mínimo; se tratará de usar curvas de radio amplio, reservando el empleo de radios mínimos para las condiciones críticas.', 'Tópico 302.04.02, pág. 129')
cita('La velocidad máxima con que sería abordado cada elemento geométrico, es la Velocidad Específica con la que se debe diseñar (…) La condición deseable es que a la mayoría de los elementos geométricos que integran el tramo homogéneo se les pueda asignar como Velocidad Específica, el valor de la Velocidad de Diseño del tramo.', 'Tópico 204.03, pág. 97')
Pp('Curvas de vuelta', bold=True)
cita('Son aquellas curvas que se proyectan sobre una ladera, en terrenos accidentados, con el propósito de obtener o alcanzar una cota mayor (…) y que no es posible lograr mediante trazos alternativos. (…) la curva de vuelta quedará definida por dos arcos circulares de radio interior "Ri" y radio exterior "Re".', 'Tópico 302.07, pág. 150')
cita('El radio interior de 8 m, representa un mínimo normal. El radio interior de 6 m, representa un mínimo absoluto y sólo podrá ser usado en forma excepcional.', 'Tabla 302.12 y texto siguiente, pág. 151')
Pp('Curvas consecutivas (compuestas, policéntricas y en S sin tangente)', bold=True)
cita('Consisten en dos o más curvas simples de diferente radio, orientadas en la misma dirección, y dispuestas una a continuación de la otra. En general, se evitará el empleo de curvas compuestas, tratando de reemplazarlas por una sola curva.', 'Tópico 302.06.01, pág. 146')
cita('En caso excepcional se podrá usar curvas compuestas, aclarando las razones, técnico-económicas u otras, que justifican el empleo de dos curvas continuas de radio diverso. En el caso de usar una curva compuesta de tres centros denominada policéntrica, deberán respetarse las siguientes condiciones: el radio de una de las curvas no será mayor de 1.5 veces el radio de la otra; (…) se empleará una transición de peralte determinada acorde a lo establecido en el Tópico 302.08; para una sucesión de curvas de radio decreciente cada curva debe ser de longitud suficiente para permitir una desaceleración gradual.', 'Tópico 302.06.02, pág. 147')
cita('En general se evitará el empleo de curvas del mismo sentido, cuando estén separadas por un tramo en tangente de una longitud menor a 400 m, en longitudes menores excepcionalmente puede utilizarse una curva policéntrica.', 'Tópico 302.06.03, pág. 147')
cita('Para todo tipo de carretera, cuando se enlacen curvas circulares consecutivas sin tangente intermedia, así como mediante tangente de longitud menor o igual a 200 m, la relación de radios de las curvas circulares no sobrepasará los valores obtenidos (…) Grupo 2: Carreteras de Segunda y Tercera Clase.', 'Tópico 302.04.05 y Tabla 302.08, págs. 134 y 137. La tabla del grupo 2 empieza en 40 m de radio de entrada y nunca admite un radio de salida menor de 50 m.')
cita('V = 40 km/h: L mín.s 56 m (trazados en S), L mín.o 111 m (curvas del mismo sentido), L máx 668 m.', 'Tabla 302.01, pág. 127')

# ---------- 3
H('3. Resumen del tramo')
filas = [['Longitud del tramo', '%.2f m (1+080.00 a %s)' % (L_tramo, fmt(P1))], ['Curvas / tangentes', '%d / %d' % (n_tot, sum(1 for e in els if e['t']=='L'))],
         ['Curvas con R ≥ 50 m (radio normativo con peralte 8 %)', '%d (%.0f %%)' % (cl_cnt.get('Normativa (peralte 8 %)', 0), 100.0*cl_cnt.get('Normativa (peralte 8 %)', 0)/n_tot)],
         ['Curvas en el radio mínimo, 45 ≤ R < 50 m (peralte 12 %)', '%d (%.0f %%)' % (cl_cnt.get('Radio mínimo (peralte 12 %)', 0), 100.0*cl_cnt.get('Radio mínimo (peralte 12 %)', 0)/n_tot)],
         ['Curvas excepcionales, 25 ≤ R < 45 m (Ve = 30 km/h)', '%d (%.0f %%)' % (cl_cnt.get('Excepcional (Ve = 30 km/h)', 0), 100.0*cl_cnt.get('Excepcional (Ve = 30 km/h)', 0)/n_tot)],
         ['Curvas de vuelta, R < 25 m', '%d (%.0f %%)' % (cl_cnt.get('Curva de vuelta', 0), 100.0*cl_cnt.get('Curva de vuelta', 0)/n_tot)],
         ['Grupos de curvas enlazadas sin tangente intermedia', '%d (%d dobles y %d triple)' % (len(G0), sum(1 for g in G0 if len(g)==2), sum(1 for g in G0 if len(g)==3))],
         ['Cadenas de curvas con tangentes menores de 5 m (funcionan como enlazadas)', '%d' % sum(1 for g in G5 if g not in G0)],
         ['Tangentes intermedias que cumplen la Tabla 302.01 (56 m en S / 111 m mismo sentido)', '%d de %d' % (sum(1 for i, e in enumerate(els[1:-1], 1) if e['t']=='L' and e['L'] >= (56 if els[i-1]['rot'] != els[i+1]['rot'] else 111)), sum(1 for e in els[1:-1] if e['t']=='L'))],
         ['Radio mínimo / máximo del tramo', '%.2f m / %.2f m' % (min(e['R'] for e in curvas), max(e['R'] for e in curvas))]]
tabla(['Indicador', 'Valor'], filas, anchos=[10.5, 6.5], size=9, align_num=False)
Pp('Lectura: casi dos tercios de las curvas (%d de %d) están en radio normativo o en el radio mínimo de 45 m; el tercio restante son curvas excepcionales y curvas de vuelta que vienen impuestas por el trazo existente en zona poblada. El tramo está lleno de curvas (una cada %.0f m en promedio), de modo que no hay espacio para las tangentes mínimas de la Tabla 302.01 ni para curvas de transición; ésa es la razón de fondo de todas las excepciones que siguen.' % (cl_cnt.get('Normativa (peralte 8 %)', 0) + cl_cnt.get('Radio mínimo (peralte 12 %)', 0), n_tot, L_tramo / n_tot))

corta = {'Normativa (peralte 8 %)': 'Normativa 8 %', 'Radio mínimo (peralte 12 %)': 'Mínimo 45 m, 12 %', 'Excepcional (Ve = 30 km/h)': 'Excepcional, 30 km/h', 'Curva de vuelta': 'Curva de vuelta'}
# ---------- 4 PI
H('4. Coordenadas de los PI y radios de giro')
Pp('Una fila por curva, en el orden del eje. La progresiva del PI es la del PC más la subtangente T. Sentido D = curva a la derecha, I = a la izquierda, en el sentido de avance de las progresivas. La columna "Clase" remite a los capítulos 5 (mínimo 45 m), 6 (excepcional) y 7 (curva de vuelta).')
filas = [[e['n'], fmt(e['pi_sta']), '%.3f' % e['PI'][0], '%.3f' % e['PI'][1], '%.2f' % e['R'], '%.1f' % e['delta'], e['sent'], '%.1f' % e['L'], '%.1f' % e['T'], corta[e['clase']]] for e in curvas]
tabla(['N°', 'Prog. PI', 'Norte PI (m)', 'Este PI (m)', 'R (m)', 'Δ (°)', 'Sent.', 'Lc (m)', 'T (m)', 'Clase'], filas, anchos=[0.9, 1.9, 2.4, 2.2, 1.4, 1.3, 1.0, 1.3, 1.3, 3.3], size=7.5)

# ---------- 5 radio minimo
H('5. Curvas en el radio mínimo normativo (R = 45 m)')
mins = [e for e in curvas if e['clase'].startswith('Radio mínimo')]
sub = sum(1 for e in mins if 'subido' in e['origen']); aj = sum(1 for e in mins if 'ajuste' in e['origen']); mod = sum(1 for e in mins if 'editada' in e['origen'])
Pp('Por qué 45 m: es el radio mínimo de la Tabla 302.02 para 40 km/h en área rural accidentada o escarpada, con peralte máximo 12 %% y fricción 0.17 (43.4 m calculado, redondeado a 45 m). La DG-2018 pide reservar el radio mínimo para "condiciones críticas"; en este tramo la condición crítica es que el eje debe quedar dentro de la franja del trazo existente, entre edificaciones, sin expropiar. Por eso %d de las %d curvas de este grupo nacieron con un radio ajustado al trazo menor de 45 m y se subieron al mínimo (columna "Origen", separación máxima admitida 2.0 m respecto al trazo), y %d ya se ajustaban al trazo con 45 m.%s Todas deben peraltarse con el máximo de 12 %% (Tabla 304.05) y recorrerse a la velocidad de diseño de 40 km/h.' % (sub, len(mins), aj, (' Las otras %d se editaron en Civil 3D después de la memoria (en general partiendo una curva de radio mayor en dos de 45 m) y no tienen dato de separación.' % mod) if mod else ''))
filas = [[e['n'], fmt(e['pi_sta']), '%.3f' % e['PI'][0], '%.3f' % e['PI'][1], '%.1f' % e['delta'], e['sent'], '%.1f' % e['L'], ('%.2f' % e['sep']) if e['sep'] is not None else '-', e['origen']] for e in mins]
tabla(['N°', 'Prog. PI', 'Norte PI', 'Este PI', 'Δ (°)', 'Sent.', 'Lc (m)', 'Sep. trazo (m)', 'Origen'], filas, anchos=[0.8, 1.9, 2.4, 2.2, 1.2, 1.0, 1.3, 1.6, 4.0], size=7.5)

# ---------- 6 excepcionales
H('6. Curvas excepcionales (25 m ≤ R < 45 m)')
exc = [e for e in curvas if e['clase'].startswith('Excepcional')]
Pp('Por qué se aceptan: la DG-2018 no define un radio mínimo excepcional para carreteras de Segunda Clase. Se aplica el Tópico 204.03: a cada elemento se le asigna la velocidad específica con la que puede recorrerse con seguridad, y para estas curvas esa velocidad es la de la fila de 30 km/h de la Tabla 302.02 (radio mínimo 25 m con peralte 12 %). Es decir, se diseñan como curvas de 30 km/h dentro de un tramo de 40 km/h, con peralte 12 % y señalización preventiva y reglamentaria de velocidad. La razón técnico-económica es la misma en todas: subirlas a 45 m habría separado el eje más de 2 m del trazo actual y afectado edificaciones. La columna Ve es la velocidad específica calculada con V = √(127·R·(0.12 + 0.17)), acotada a 40 km/h.')
filas = [[e['n'], fmt(e['pi_sta']), '%.3f' % e['PI'][0], '%.3f' % e['PI'][1], '%.2f' % e['R'], '%.1f' % e['delta'], e['sent'], '%.1f' % e['L'], '%.0f' % ve(e['R']), ('%.2f' % e['sep']) if e['sep'] is not None else '-', 'sí (cap. 8)' if any(e in g for g in G5) else 'no'] for e in exc]
tabla(['N°', 'Prog. PI', 'Norte PI', 'Este PI', 'R (m)', 'Δ (°)', 'Sent.', 'Lc (m)', 'Ve (km/h)', 'Sep. trazo (m)', 'Enlazada'], filas, anchos=[0.8, 1.9, 2.3, 2.1, 1.3, 1.2, 1.0, 1.2, 1.4, 1.6, 1.6], size=7.5)
nr = sorted(set('%.2f' % e['R'] for e in exc if abs(e['R'] / 5.0 - round(e['R'] / 5.0)) > 1e-3), key=float)
Pp('Las curvas de 25.0, 30.0 y 35.0 m son valores redondeados a múltiplos de 5 m; las de radio no redondeado (' + ', '.join(nr) + ' m) son radios ajustados por mínimos cuadrados al trazo que no se pudieron subir sin salir de la franja admitida, o radios editados a mano en Civil 3D. Las de 43.10, 43.90 y 44.89 m están a menos de 2 m del radio mínimo y pueden llevarse a 45 m en Civil 3D si el pinzamiento resultante no invade edificaciones.', size=9.5)

# ---------- 7 curvas de vuelta
H('7. Curvas de vuelta y esquinas urbanas (R < 25 m)')
vue = [e for e in curvas if e['clase'] == 'Curva de vuelta']
for e in vue: e['ri'] = radio_interior(e['R']); e['ev'] = eval_ri(e['ri'])
cnt = {k: sum(1 for e in vue if e['ev'].startswith(k)) for k in ('cumple', 'mínimo', 'no cumple')}
Pp('Son %d curvas con radio de eje menor de 25 m, por debajo incluso del radio de 30 km/h. La DG-2018 sólo admite radios así como curvas de vuelta (Tópico 302.07), definidas por un radio interior Ri y uno exterior Re según la maniobra prevista (Tabla 302.12). Se evalúan con la maniobra C2 (camión de dos ejes cruzándose con un vehículo ligero), que es la que corresponde a una vía de Segunda Clase con calzada de 6 m: el radio interior se obtiene de Ri = R − ancho/2, con el ancho Re − Ri de la Tabla 302.12. Resultado: %d cumplen el mínimo normal (Ri ≥ 8 m), %d quedan en el mínimo absoluto de uso excepcional (6 ≤ Ri < 8 m) y %d no alcanzan ni el mínimo absoluto.' % (len(vue), cnt['cumple'], cnt['mínimo'], cnt['no cumple']))
Pp('Por qué existen: son esquinas y volteos del trazo actual entre edificaciones; en la mayoría la deflexión supera 60° y el radio está dictado por el ancho de la calle. Las que no cumplen el mínimo absoluto (Ri < 6 m) no pueden justificarse con la DG-2018: la única salida normativa es ampliar la plataforma o expropiar en la esquina, y así debe quedar indicado en el expediente para decisión del proyecto.')
filas = [[e['n'], fmt(e['pi_sta']), '%.3f' % e['PI'][0], '%.3f' % e['PI'][1], '%.2f' % e['R'], '%.1f' % e['delta'], e['sent'], '%.1f' % e['ri'], '%.1f' % (e['ri'] + ancho(max(e['ri'], 0.1))), e['ev'], ('%.2f' % e['sep']) if e['sep'] is not None else '-'] for e in vue]
tabla(['N°', 'Prog. PI', 'Norte PI', 'Este PI', 'R eje (m)', 'Δ (°)', 'Sent.', 'Ri (m)', 'Re (m)', 'Evaluación DG-2018', 'Sep. trazo (m)'], filas, anchos=[0.8, 1.9, 2.3, 2.1, 1.3, 1.2, 1.0, 1.2, 1.2, 3.6, 1.5], size=7.5)

# ---------- 8 consecutivas
H('8. Curvas consecutivas: dobles, triples y en S sin tangente')
cadenas = [g for g in G5 if g not in G0]
Pp('Dónde están y por qué. Hay %d grupos de curvas unidas sin tangente intermedia (%d dobles y %d triple) y, además, %d cadenas donde la tangente entre curvas mide menos de 5 m, que para el conductor y para la transición del peralte funcionan como curvas enlazadas. Vienen de dos orígenes: (a) el propio trazo existente, que tiene cadenas de curvatura variable (volteos y esquinas que no se pueden representar con una sola curva circular), y (b) la "pasada de tangentes" del ajuste, que al reemplazar una tangente muy corta entre dos curvas del mismo sentido las convirtió en una curva compuesta, como permite el Tópico 302.06.03 cuando la tangente sería menor de 400 m. Para la DG-2018 son un caso excepcional (302.06.02) que exige dejar escritas las razones técnico-económicas: aquí, seguir el trazo actual en zona poblada para no expropiar.' % (len(G0), sum(1 for g in G0 if len(g)==2), sum(1 for g in G0 if len(g)==3), len(cadenas)))
Pp('Tipos. "Compuesta" = dos o más curvas del mismo sentido (dos centros o policéntrica de tres centros). "Inversa" = curvas de sentido contrario unidas sin tangente (S sin tangente); para éstas la DG-2018 pide una tangente mínima de 56 m (Tabla 302.01) que permita la transición del peralte, lo que no es posible aquí, de modo que el peralte debe invertirse dentro de los propios arcos. La columna "Relación R/r" se compara con el límite 1.5 del 302.06.02 y "Tabla 302.08" con el 302.04.05; ambas quedan fuera de rango en casi todos los grupos porque la tabla del grupo 2 empieza en 40 m de radio de entrada y no admite salidas menores de 50 m, valores que el trazo no tiene.', size=9.5)
Pp('8.1 Grupos enlazados sin tangente intermedia', bold=True)
origen_g = {'7-8': 'trazo existente: volteo de curvatura variable', '12-13': 'trazo existente: cadena de curvatura variable', '21-22': 'pasada de tangentes (302.06.03): sustituye una tangente corta entre curvas del mismo sentido',
            '23-24': 'trazo existente: cadena de curvatura variable', '25-26': 'trazo existente: volteo de curvatura variable', '38-39-40': 'pasada de tangentes (302.06.03) y edición en Civil 3D: en la memoria era compuesta de dos centros (37.30 / 11.50 m)',
            '58-59': 'trazo existente: volteo entre edificaciones', '68-69': 'trazo existente: cadena de curvatura variable', '85-86': 'trazo existente: cadena de curvatura variable'}
filas = []
for g in G0:
    tipos = ['compuesta' if a['rot'] == b['rot'] else 'inversa' for a, b in zip(g, g[1:])]
    rel = ['%.2f' % (max(a['R'], b['R'])/min(a['R'], b['R'])) for a, b in zip(g, g[1:])]
    t308 = [tabla30208(a['R'], b['R']) for a, b in zip(g, g[1:])]
    if len(g) == 3 and all(x == 'compuesta' for x in tipos): nombre = 'triple: policéntrica de 3 centros'
    elif len(g) == 2: nombre = 'doble: ' + ('compuesta de 2 centros' if tipos[0] == 'compuesta' else 'inversa (S sin tangente)')
    else: nombre = '%d curvas: %s' % (len(g), ' + '.join(tipos))
    k = '-'.join(str(e['n']) for e in g)
    filas.append([k, fmt(g[0]['sta']) + ' a ' + fmt(g[-1]['sta'] + g[-1]['L']), nombre, ' / '.join('%.2f %s' % (e['R'], e['sent']) for e in g), ', '.join(rel), '; '.join(t308), origen_g.get(k, 'trazo existente')])
tabla(['Curvas', 'Progresivas', 'Tipo', 'Radios (m) y sentido', 'Relación R/r', 'Tabla 302.08', 'Origen y justificación (302.06.02)'], filas, anchos=[1.2, 2.6, 2.9, 2.5, 1.2, 2.9, 3.7], size=7.5, align_num=False)
Pp('Comentario por grupo:', bold=True)
coment = {
 '7-8': 'S sin tangente que resuelve un volteo de 167° de deflexión total (curva de vuelta de 24.20 m seguida de 40.48 m). Es la geometría de la calle existente; el peralte de 12 % de una curva debe invertirse dentro de la otra.',
 '12-13': 'S sin tangente con radios casi iguales (38.90 y 39.31 m, relación 1.01): es la única unión del tramo que cumple la relación 1.5 del 302.06.02. Ambas son excepcionales (Ve = 30 km/h).',
 '21-22': 'Compuesta de dos centros creada por la pasada de tangentes: una curva de 43.90 m seguida de una esquina de 8.01 m del mismo sentido. La relación 5.5 está muy fuera de la condición 1.5; la esquina de 8.01 m (Ri ≈ 3 m) no cumple el mínimo absoluto de curva de vuelta.',
 '23-24': 'S sin tangente entre una curva de radio mínimo (45 m) y una esquina de 19.40 m; viene del trazo. Con la curva 22 forma, de hecho, una cadena de cuatro curvas (tangente de 3.4 m entre 22 y 23).',
 '25-26': 'S sin tangente que resuelve un volteo de 172°: curva de 37.28 m seguida de una curva de vuelta de 11.30 m (Ri ≈ 6.5 m, mínimo absoluto).',
 '38-39-40': 'Policéntrica de tres centros (37.30, 11.32 y 62.14 m, todas a la derecha) con relaciones 3.3 y 5.5: no cumple la condición 1.5 ni la Tabla 302.08. Es el único grupo triple sin tangente del tramo y proviene de la pasada de tangentes sobre una esquina; la tercera curva (62.14 m, Δ = 3.6°) se añadió en Civil 3D y conviene revisar si puede absorberse en la tangente siguiente.',
 '58-59': 'Compuesta de dos centros con la curva de vuelta más cerrada del tramo (8.60 m, Δ = 147°) seguida de 35.01 m. Ri ≈ 3.7 m: no cumple el mínimo absoluto; es el volteo del trazo entre edificaciones.',
 '68-69': 'S sin tangente entre 32.50 m y una esquina de 10.02 m (Ri ≈ 5.1 m, no cumple). En este sitio el eje se separa 4.64 m del trazo actual: es el punto del tramo a verificar en campo con prioridad.',
 '85-86': 'S sin tangente entre 44.89 m (prácticamente radio mínimo) y una curva de vuelta de 12.40 m (Ri ≈ 7.7 m, mínimo absoluto).',
}
for g in G0:
    k = '-'.join(str(e['n']) for e in g)
    Pp('Curvas %s (%s): %s' % (k, fmt(g[0]['sta']), coment.get(k, '')), size=9.5)
Pp('8.2 Cadenas de curvas con tangentes menores de 5 m', bold=True)
Pp('No son curvas compuestas en sentido estricto, pero la tangente intermedia es tan corta que no cabe en ella ninguna transición de peralte (a 40 km/h la pendiente relativa máxima es 1.4 %, Tópico 302.08), por lo que en Civil 3D deben tratarse como un solo grupo al definir peraltes y sobreanchos. Las cadenas que incluyen un grupo del cuadro 8.1 se indican en la última columna.', size=9.5)
filas = []
for g in cadenas:
    tg = []
    for a in g[:-1]:
        ia = els.index(a); tg.append('0' if els[ia+1]['t'] == 'C' else '%.1f' % els[ia+1]['L'])
    incl = ['-'.join(str(e['n']) for e in h) for h in G0 if all(e in g for e in h)]
    filas.append(['-'.join(str(e['n']) for e in g), fmt(g[0]['sta']) + ' a ' + fmt(g[-1]['sta'] + g[-1]['L']), '%d' % len(g), ' / '.join('%.2f %s' % (e['R'], e['sent']) for e in g), ', '.join(tg), ('incluye grupo ' + ', '.join(incl)) if incl else '-'])
tabla(['Curvas', 'Progresivas', 'N°', 'Radios (m) y sentido', 'Tangentes intermedias (m)', 'Observación'], filas, anchos=[2.0, 3.0, 0.8, 5.2, 2.6, 3.0], size=7.5, align_num=False)

ntg = sum(1 for i, e in enumerate(els[1:-1], 1) if e['t']=='L' and e['L'] >= (56 if els[i-1]['rot'] != els[i+1]['rot'] else 111))
# ---------- 9 conclusiones
H('9. Conclusiones y recomendaciones')
for s in [
 'El tramo 1+080 a 4+500 cumple el radio mínimo de la DG-2018 (45 m a 40 km/h, Tabla 302.02) en %d de sus %d curvas; en %d de ellas se usa exactamente el radio mínimo, que la norma reserva para condiciones críticas, aquí justificadas por el trazo existente en zona poblada.' % (cl_cnt.get('Normativa (peralte 8 %)', 0) + cl_cnt.get('Radio mínimo (peralte 12 %)', 0), n_tot, len(mins)),
 'Las %d curvas excepcionales (25 a 45 m) se diseñan con velocidad específica de 30 km/h (Tópico 204.03 y fila de 30 km/h de la Tabla 302.02), peralte 12 %% y señalización de velocidad. Las de 43.10, 43.90 y 44.89 m conviene llevarlas a 45 m si el pinzamiento lo permite.' % len(exc),
 'Las %d curvas de vuelta (R < 25 m) se evalúan con la Tabla 302.12: %d cumplen el radio interior normal de 8 m, %d están en el mínimo absoluto de 6 m y %d no lo alcanzan (curvas %s). Estas últimas sólo pueden resolverse ampliando la plataforma o expropiando en la esquina; la decisión no es geométrica sino del proyecto.' % (len(vue), cnt['cumple'], cnt['mínimo'], cnt['no cumple'], ', '.join(str(e['n']) for e in vue if e['ev'].startswith('no'))),
 'Los %d grupos de curvas enlazadas y las cadenas con tangentes menores de 5 m son casos excepcionales del Tópico 302.06.02; la justificación técnico-económica que exige la norma es evitar la expropiación siguiendo el trazo actual, y debe quedar escrita en el expediente. En todos ellos el peralte y el sobreancho deben definirse como grupo (transición dentro de los arcos, Tópico 302.08).' % len(G0),
 ('Sólo %d de las 82 tangentes intermedias cumple' % ntg if ntg == 1 else 'Sólo %d de las 82 tangentes intermedias cumplen' % ntg) + ' las longitudes mínimas de la Tabla 302.01 y ninguna curva alcanza la longitud mínima de 3V = 120 m; no es un defecto del ajuste sino consecuencia de seguir un trazo con una curva cada %.0f m. Si el proyecto exige cumplir esos parámetros, habrá que rediseñar subtramos completos con expropiación.' % (L_tramo / n_tot),
 '%d de las %d curvas del XML no coinciden con la memoria del eje completo porque se editaron en Civil 3D (en la mayoría una curva de radio mayor se partió en dos curvas de 45 m, y las curvas 82 y 83 subieron de 45 a 65 y 70 m). Al cerrar el diseño conviene regenerar la memoria y el cuadro de peraltes y sobreanchos a partir de este XML.' % (sum(1 for e in curvas if 'editada' in e['origen']), n_tot),
 'Puntos a verificar en campo o sobre la ortofoto antes de aprobar el eje: la curva 69 (3+682.94), donde el eje se separa 4.64 m del trazo actual, y las esquinas con Ri < 6 m listadas en el capítulo 7.',
]:
    p = doc.add_paragraph(s, style='List Bullet'); p.paragraph_format.space_after = Pt(3)

# ---------- Anexo: excel
H('Anexo. Ubicación de las curvas del listado en Excel')
Pp('El listado en Excel "Curvas menores a 45 m y mayores a 25 m de radio" y "Curvas menores a 25 m de radio" se cotejó contra los PI del eje completo (EJE_DG2018_circular.xml): las 26 coordenadas coinciden exactamente con PI del eje, pero todas están entre las progresivas 4+522.71 y 7+963.19, es decir, en el tramo siguiente al de este informe. Se dejan ubicadas para el informe de ese tramo.', size=9.5)
excel = [(9472297.505,609198.596,34.2,'5+752.32'),(9471869.912,608662.043,30,'6+702.86'),(9471856.784,608672.342,33.14,'6+719.09'),(9471803.158,608604.034,34,'6+884.43'),(9471765.017,608581.692,34.5,'6+928.53'),(9471643.281,608471.076,40,'7+116.15'),(9471666.658,608430.695,42.46,'7+251.05'),(9471556.942,608362.774,40,'7+536.52'),(9471559.037,608419.344,39.2,'7+706.76'),(9471472.167,608452.241,27.3,'7+800.71'),(9471432.294,608334.781,25,'7+963.19'),
 (9472540.972,610218.57,15,'4+522.71'),(9472502.142,610145.809,11.4,'4+606.08'),(9472500.023,610140.36,6.31,'4+611.93'),(9472499.66,610139.619,6,'4+612.75'),(9472499.32,610138.552,24.06,'4+613.87'),(9472442.07,610070.965,13.8,'4+705.94'),(9472456.007,609952.809,15,'4+825.98'),(9472442.261,609940.648,19.7,'4+839.96'),(9472406.297,609928.172,15,'4+877.93'),(9472444.464,609892.798,8,'4+914.17'),(9472172.908,609260.939,12.91,'5+612.31'),(9472283.454,609112.203,24,'5+830.61'),(9471953.327,608663.664,11.03,'6+615.79'),(9471940.939,608645.255,13.35,'6+631.54'),(9471929.222,608648.383,18.4,'6+641.16')]
filas = [['%.3f' % n, '%.3f' % e, '%.2f' % r, p, 'excepcional (Ve = 30 km/h)' if r >= 25 else 'curva de vuelta'] for n, e, r, p in sorted(excel, key=lambda x: prog(x[3]))]
tabla(['Norte PI', 'Este PI', 'R (m)', 'Prog. PI (eje completo)', 'Clase'], filas, anchos=[2.6, 2.4, 1.4, 3.0, 4.0], size=8)

out = '/home/user/Normas/informes/Informe_eje_DG2018_tramo_1080-4500.docx'
import os; os.makedirs(os.path.dirname(out), exist_ok=True)
doc.save(out); print('guardado', out)
print('minimos', len(mins), 'subidos', sub, 'ajuste', aj, 'mod', mod, '| exc', len(exc), '| vuelta', len(vue), cnt, '| G0', len(G0), 'G5', len(G5))
print('no cumplen Ri:', [(e['n'], round(e['R'],2), round(e['ri'],1)) for e in vue if e['ev'].startswith('no')])
print('modificadas:', [(e['n'], e['R']) for e in curvas if e['origen'] == 'modificada en Civil 3D'])
print('G5 extra:', [[e['n'] for e in g] for g in G5 if g not in G0])
