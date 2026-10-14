#!/usr/bin/env python3
"""Genera Reporte_Trazabilidad_DG2018.pdf: registro de los cambios entre
DG2018_original.xml y DG2018_Corregido.xml con su cita a la DG-2018.

Los valores "antes" y "después" se leen de los dos XML; los parámetros
normativos vienen de generar_dg2018_corregido.py.

Uso:
    python3 generar_reporte_trazabilidad.py
"""
import datetime
import hashlib
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import (KeepTogether, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

import generar_dg2018_corregido as gen

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parent
ORIGINAL = AQUI / "DG2018_original.xml"
CORREGIDO = AQUI / "DG2018_Corregido.xml"
NORMA = REPO / "normas" / "Manual.de.Carreteras.DG-2018.pdf"
SALIDA = AQUI / "Reporte_Trazabilidad_DG2018.pdf"
NS = "{urn:Civil3DRoadwayDesignStandards-schema}"
PMAX = [4, 6, 8, 10, 12]
NOMBRE_ORIGINAL = {e: f"DG2018 _PMax {e}%" for e in PMAX}
NOMBRE_ORIGINAL[10] = "AASHTO 2011 Metric eMax 10%"
NOMBRE_CORREGIDO = {e: f"DG2018 _PMax {e}%" for e in PMAX}

# Páginas según la numeración impresa del manual (en el PDF del repositorio
# corresponden a la página impresa + 1).
PAG = {
    "T204.01": "97", "204.02": "96", "T205.01": "104", "T205.03": "109",
    "302.04.02": "128", "T302.02": "129", "F302.02-05": "130–131",
    "T302.03": "132", "T302.04": "132", "302.04.04": "132–134",
    "T302.05": "133", "contra60": "134", "T302.09": "139",
    "302.05.04": "139", "T302.10": "140", "N302.10": "141",
    "302.08": "152", "T302.13": "152", "T302.14-18": "153–155",
    "desvan": "158", "302.09.03": "160–161", "Sa040": "161",
    "303.04.03": "177–179", "h1h2": "178", "h5": "179", "T303.02": "180",
    "303.04.04": "180", "T303.03": "182", "T304.04": "196", "T304.05": "196",
    "T304.06": "197",
}


def ref(texto, *claves):
    pags = ", ".join(PAG[c] for c in claves)
    return f"{texto} (pág. {pags})"


# ---------------------------------------------------------------------------
# Lectura de los XML
# ---------------------------------------------------------------------------

def leer(path):
    root = ET.parse(path).getroot()
    radios = {t.get("name"): {int(x.get("speed")): int(x.get("radius"))
                              for x in t.findall(NS + "MinimumRadius")}
              for t in root.iter(NS + "MinimumRadiusTable")}
    peralte, transicion = {}, {}
    for st in root.iter(NS + "SuperelevationTable"):
        nombre = st.get("name")
        peralte[nombre] = {
            int(d.get("speed")): [(x.get("eRate"), int(float(x.get("radius"))))
                                  for x in d.findall(NS + "SuperelevationRate")]
            for d in st.iter(NS + "SuperelevationDesignSpeed")}
        transicion[nombre] = {
            tl.get("name"): {
                int(d.get("speed")): [(int(float(x.get("radius"))), int(float(x.get("tLength"))))
                                      for x in d.findall(NS + "TransitionLength")]
                for d in tl.iter(NS + "TransitionLengthDesignSpeed")}
            for tl in st.iter(NS + "TransitionLengthTable")}
    formula = {k: v for f in root.iter(NS + "TransitionLengthFormula") for k, v in f.attrib.items()}
    sobreancho = {m.get("name"): m.find(f".//{NS}WideningFormula").get("formula")
                  for m in root.iter(NS + "WideningMethod")
                  if m.find(f".//{NS}WideningFormula") is not None}
    k = {}
    for t in root.iter(NS + "MinimumKTable"):
        k[t.get("name")] = {c: {int(x.get("speed")): int(x.get("K")) for x in t.iter(NS + f"MinimumK_{c}")}
                            for c in ("SSD", "PSD", "HSD")}
    return dict(radios=radios, peralte=peralte, transicion=transicion,
                formula=formula, sobreancho=sobreancho, k=k)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def commit_de(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%h (%ad)", "--date=short", "--", str(path)],
                             cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()
        return out or "sin registrar"
    except (OSError, subprocess.CalledProcessError):
        return "no disponible"


def fila_de(filas, rate):
    for r, rad in filas or []:
        if r == rate:
            return rad
    return None


def radio_nc_rc(filas, tasa):
    # En 4% a 30 km/h la fila equivalente a RC se llama "2.0".
    if tasa == "RC":
        return fila_de(filas, "RC") or fila_de(filas, "2.0")
    return fila_de(filas, tasa)


# ---------------------------------------------------------------------------
# Estilos
# ---------------------------------------------------------------------------

FUENTES = Path("/usr/share/fonts/truetype/dejavu")
pdfmetrics.registerFont(TTFont("DejaVu", str(FUENTES / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(FUENTES / "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("DejaVuSerif", str(FUENTES / "DejaVuSerif.ttf")))
pdfmetrics.registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold",
                              italic="DejaVu", boldItalic="DejaVu-Bold")

AZUL = colors.HexColor("#1F3A5F")
AZUL_CLARO = colors.HexColor("#E8EEF5")
GRIS = colors.HexColor("#5A6270")
GRIS_LINEA = colors.HexColor("#C9CFD8")
AMBAR = colors.HexColor("#FFF4D6")

ESTILO = {
    "titulo": ParagraphStyle("titulo", fontName="DejaVu-Bold", fontSize=17, leading=21, textColor=AZUL),
    "subtitulo": ParagraphStyle("subtitulo", fontName="DejaVu", fontSize=10.5, leading=14, textColor=GRIS),
    "h1": ParagraphStyle("h1", fontName="DejaVu-Bold", fontSize=12.5, leading=16, textColor=AZUL,
                         spaceBefore=10, spaceAfter=5, keepWithNext=1),
    "h2": ParagraphStyle("h2", fontName="DejaVu-Bold", fontSize=10.5, leading=14, textColor=AZUL,
                         spaceBefore=7, spaceAfter=3, keepWithNext=1),
    "h1_partible": ParagraphStyle("h1_partible", fontName="DejaVu-Bold", fontSize=12.5, leading=16,
                                  textColor=AZUL, spaceBefore=10, spaceAfter=5),
    "cuerpo": ParagraphStyle("cuerpo", fontName="DejaVu", fontSize=9, leading=12.5, spaceAfter=4),
    "nota": ParagraphStyle("nota", fontName="DejaVu", fontSize=8, leading=11, textColor=GRIS, spaceAfter=4),
    "celda": ParagraphStyle("celda", fontName="DejaVu", fontSize=7.6, leading=9.6, alignment=TA_LEFT),
    "celda_b": ParagraphStyle("celda_b", fontName="DejaVu-Bold", fontSize=7.6, leading=9.6,
                              textColor=colors.white),
    "cita": ParagraphStyle("cita", fontName="DejaVuSerif", fontSize=8.4, leading=11.5),
}


def P(markup, estilo="cuerpo"):
    return Paragraph(markup, ESTILO[estilo])


def T(texto, estilo="celda"):
    return Paragraph(escape(str(texto)), ESTILO[estilo])


def tabla(encabezado, filas, anchos, zebra=True, resaltar=()):
    datos = [[T(h, "celda_b") for h in encabezado]]
    datos += [[c if isinstance(c, Paragraph) else T(c) for c in f] for f in filas]
    t = Table(datos, colWidths=[a * mm for a in anchos], repeatRows=1, spaceAfter=6)
    estilo = [
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, GRIS_LINEA),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
    ]
    if zebra:
        for i in range(2, len(datos), 2):
            estilo.append(("BACKGROUND", (0, i), (-1, i), AZUL_CLARO))
    for i in resaltar:
        estilo.append(("BACKGROUND", (0, i + 1), (-1, i + 1), AMBAR))
    t.setStyle(TableStyle(estilo))
    return t


def cita(texto, fuente):
    t = Table([[Paragraph(f"“{escape(texto)}”<br/><font name='DejaVu' size='7.5' color='#5A6270'>"
                          f"{escape(fuente)}</font>", ESTILO["cita"])]],
              colWidths=[174 * mm])
    t.setStyle(TableStyle([
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, AZUL),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F6F8FB")),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return KeepTogether([t, Spacer(1, 4)])


class LienzoNumerado(canvas.Canvas):
    """Encabezado, pie y 'Página X de Y' en cada hoja."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._paginas = []

    def showPage(self):
        self._paginas.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._paginas)
        for estado in self._paginas:
            self.__dict__.update(estado)
            self._decorar(total)
            super().showPage()
        super().save()

    def _decorar(self, total):
        ancho, alto = A4
        self.setStrokeColor(GRIS_LINEA)
        self.setLineWidth(0.5)
        self.line(18 * mm, alto - 13 * mm, ancho - 18 * mm, alto - 13 * mm)
        self.line(18 * mm, 13 * mm, ancho - 18 * mm, 13 * mm)
        self.setFont("DejaVu", 7.5)
        self.setFillColor(GRIS)
        self.drawString(18 * mm, alto - 11 * mm, "Reporte de trazabilidad · DG2018_Corregido.xml")
        self.drawRightString(ancho - 18 * mm, alto - 11 * mm,
                             "Manual de Carreteras: Diseño Geométrico DG-2018")
        self.drawString(18 * mm, 9 * mm, f"Emitido: {FECHA}")
        self.drawRightString(ancho - 18 * mm, 9 * mm, f"Página {self._pageNumber} de {total}")


FECHA = datetime.date.today().isoformat()


# ---------------------------------------------------------------------------
# Contenido
# ---------------------------------------------------------------------------

def validar(d):
    """Comprobaciones de consistencia; devuelve conteos de incumplimientos."""
    res = dict(no_decreciente=0, inversiones=0, tl_distinto=0, tl_filas=0)
    for nombre, bloques in d["peralte"].items():
        if not bloques:
            continue
        for filas in bloques.values():
            rad = [r for _, r in filas]
            res["no_decreciente"] += sum(a <= b for a, b in zip(rad, rad[1:]))
        tasas = {r for f in bloques.values() for r, _ in f if r not in ("NC", "RC", "2.0")}
        for tasa in tasas:
            serie = [fila_de(bloques[v], tasa) for v in sorted(bloques) if fila_de(bloques[v], tasa)]
            res["inversiones"] += sum(b <= a for a, b in zip(serie, serie[1:]))
        for carriles, tl in d["transicion"][nombre].items():
            if carriles not in ("2 Lane", "4 Lane"):
                continue
            for v, filas in tl.items():
                se = [r for _, r in bloques.get(v, [])]
                res["tl_filas"] += len(filas)
                res["tl_distinto"] += sum(1 for i, (r, _) in enumerate(filas)
                                          if i >= len(se) or se[i] != r)
    return res


def construir():
    o, c = leer(ORIGINAL), leer(CORREGIDO)
    s = []

    # --- Portada -----------------------------------------------------------
    s.append(P("Reporte de trazabilidad de cambios", "titulo"))
    s.append(P("Normas de diseño de Autodesk Civil 3D ajustadas al Manual de Carreteras: "
               "Diseño Geométrico DG-2018", "subtitulo"))
    s.append(Spacer(1, 8))
    meta = [
        ["Norma de referencia", "Manual de Carreteras: Diseño Geométrico (DG-2018), MTC. "
                                "Revisada y corregida a enero de 2018."],
        ["Archivo de la norma", f"normas/{NORMA.name}  ·  SHA-256 {sha256(NORMA)}"],
        ["Archivo original", f"civil3d/{ORIGINAL.name}  ·  SHA-256 {sha256(ORIGINAL)}"],
        ["Archivo corregido", f"civil3d/{CORREGIDO.name}  ·  SHA-256 {sha256(CORREGIDO)}"],
        ["Versión del corregido", f"Commit {commit_de(CORREGIDO)}, rama claude/dazzling-euler-ln6owg, "
                                  "repositorio Andy-rba30/Normas"],
        ["Generación", "generar_dg2018_corregido.py (corrección) y generar_reporte_trazabilidad.py "
                       "(este reporte). Los valores antes/después se leen de los dos XML."],
        ["Convención de citas", "Las páginas citadas son las impresas en el manual. En el PDF del "
                                "repositorio, la página del visor es la impresa + 1."],
    ]
    t = Table([[T(a, "celda_b"), T(b)] for a, b in meta], colWidths=[38 * mm, 136 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), AZUL),
        ("GRID", (0, 0), (-1, -1), 0.4, GRIS_LINEA),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    s += [t, Spacer(1, 6)]
    control = Table([[T("Elaborado", "celda_b"), T("Revisado", "celda_b"), T("Aprobado", "celda_b")],
                     [T("Generado automáticamente con Claude Code a partir de los archivos citados. "
                        "Requiere revisión de un ingeniero responsable."), T(""), T("")]],
                    colWidths=[58 * mm] * 3, rowHeights=[None, 16 * mm])
    control.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), AZUL),
                                 ("GRID", (0, 0), (-1, -1), 0.4, GRIS_LINEA),
                                 ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    s.append(control)

    # --- 1. Objeto ---------------------------------------------------------
    s.append(P("1. Objeto y alcance", "h1"))
    s.append(P("Este reporte deja constancia de cada cambio aplicado al archivo de normas de diseño de "
               "Civil 3D <b>DG2018.xml</b> para ajustarlo a la DG-2018. Para cada cambio indica el "
               "elemento del XML, el valor original, el valor corregido y el tópico o tabla de la "
               "norma que lo sustenta, con su página. También registra los criterios adoptados donde "
               "la propia norma es inconsistente y los valores que no están tabulados en ella y se "
               "derivaron por cálculo."))
    s.append(P("Abarca radios mínimos, tablas de peralte y de longitud de transición, fórmula de la "
               "clotoide, sobreancho y parámetro K de curvas verticales. Las tablas de sobreancho por "
               "vehículo de diseño (WB-19, SU-9, etc.) no se modificaron ni se revisaron."))

    # --- 2. Referencias normativas ------------------------------------------
    s.append(P("2. Disposiciones de la DG-2018 citadas", "h1_partible"))
    refs = [
        ["Tabla 204.01", "Rangos de la velocidad de diseño: 30 a 130 km/h", PAG["T204.01"]],
        ["Tabla 205.01", "Distancia de visibilidad de parada (Dp)", PAG["T205.01"]],
        ["Tabla 205.03", "Distancia de visibilidad de adelantamiento (Da)", PAG["T205.03"]],
        ["Tópico 302.04.02", "Radio mínimo: Rmín = V²/127(Pmáx + fmáx)", PAG["302.04.02"]],
        ["Tabla 302.02", "Radios mínimos y peraltes máximos (4, 6, 8 y 12%)", PAG["T302.02"]],
        ["Figuras 302.02–302.05", "Peralte en función del radio y la velocidad", PAG["F302.02-05"]],
        ["Tablas 302.03 y 302.04", "Fricción máxima y radios mínimos, Tercera Clase", PAG["T302.04"]],
        ["Tópico 302.04.04", "Curvas en contraperalte; prohibido con V < 60 km/h", PAG["302.04.04"]],
        ["Tabla 302.05", "Radios límite en contraperalte", PAG["T302.05"]],
        ["Tabla 302.09", "Variación de la aceleración transversal J", PAG["T302.09"]],
        ["Tabla 302.10 y nota", "Longitud mínima de curva de transición; mínimo 30 m",
         f"{PAG['T302.10']}–{PAG['N302.10']}"],
        ["Tópico 302.08 y Tabla 302.13", "Transición de peralte; Tercera Clase", PAG["T302.13"]],
        ["Tablas 302.14–302.18", "Longitud de transición por ancho y eje de giro", PAG["T302.14-18"]],
        ["Tópico 302.09.03", "Valores del sobreancho: Sa = n(R − √(R² − L²)) + V/(10√R)",
         PAG["302.09.03"]],
        ["Tópico 303.04.03", "Curvas convexas: h1 = 1.07 m, h2 = 0.15 m y 1.30 m", PAG["303.04.03"]],
        ["Tabla 303.02", "Índice K convexo, Tercera Clase", PAG["T303.02"]],
        ["Tópico 303.04.04", "Curvas cóncavas: L = A·D²/(120 + 3.5D), D = Dp", PAG["303.04.04"]],
        ["Tabla 303.03", "Índice K cóncavo, Tercera Clase", PAG["T303.03"]],
        ["Tabla 304.04", "Radio a partir del cual no es necesario peralte", PAG["T304.04"]],
        ["Tabla 304.05", "Valores de peralte máximo", PAG["T304.05"]],
        ["Tabla 304.06", "Peralte mínimo de 2%", PAG["T304.06"]],
    ]
    s.append(tabla(["Disposición", "Contenido", "Pág."], refs, [42, 117, 15]))

    # --- 3. Resumen ---------------------------------------------------------
    s.append(P("3. Resumen de cambios", "h1"))
    resumen = [
        ["Radios mínimos", "R-01 a R-05", "Rango 30–130 km/h; 8% a 110 km/h; tabla de 10% a fricción DG; "
                                          "tabla sin peralte reemplazada por la Tabla 302.05",
         "Tablas 204.01, 302.02, 302.04, 302.05, 302.10"],
        ["Peralte", "P-01 a P-05", "Escalón máximo igual a la Tabla 302.02; 7 erratas; NC y RC según "
                                    "la regla general; bloques faltantes; nombre de la tabla de 10%",
         "Tablas 302.02, 304.04, 304.06; Tópico 302.04.04"],
        ["Transición", "T-01 a T-05", "Radios iguales a los de peralte; bloques huérfanos eliminados; "
                                       "clotoide con mínimo de 30 m y J = 0.4",
         "Tablas 302.09, 302.10, 302.13"],
        ["Sobreancho", "S-01", "Término empírico V/(10√R)", "Tópico 302.09.03"],
        ["Parámetro K", "K-01 a K-03", "Dos tablas: Red Vial General y Tercera Clase",
         "Tópicos 303.04.03 y 303.04.04; Tablas 303.02, 303.03"],
    ]
    s.append(tabla(["Sección", "IDs", "Cambio", "Sustento principal"], resumen, [25, 21, 78, 50]))

    # --- 4. Criterios -------------------------------------------------------
    s.append(P("4. Criterios adoptados donde la norma es inconsistente", "h1"))
    s.append(P("La DG-2018 da valores distintos para un mismo parámetro en algunas tablas. Estos son los "
               "criterios aplicados, que se referencian en el registro de cambios.", "nota"))
    criterios = [
        ["C-01", "8% a 50 km/h: la Tabla 302.04 da 80 m, pero redondea hacia abajo un valor calculado "
                 "de 82.0 m; la Tabla 302.02 da 85 m.", "Se mantiene 85 m (valor oficial mayor).",
         ref("Tablas 302.02 y 302.04", "T302.02", "T302.04")],
        ["C-02", "130 km/h: la Tabla 302.02 usa fmáx = 0.08 (8%: 835 m; 12%: 665 m); la Tabla 302.10 usa "
                 "≈ 0.07 (8%: 887 m; 10%: 783 m; 12%: 700 m).",
         "Se adopta la Tabla 302.02, tabla rectora de radios mínimos (decisión del usuario). 10%: "
         "130²/127(0.10 + 0.08) = 739 m.", ref("Tablas 302.02 y 302.10", "T302.02", "T302.10")],
        ["C-03", "10% de 30 a 70 km/h: la Tabla 302.04 (25, 45, 75, 115) y la Tabla 302.10 "
                 "(26, 47, 76, 113, 161) difieren.", "Se toma el mayor valor oficial en cada velocidad: "
                                                     "26, 47, 76, 115, 161 m.",
         ref("Tablas 302.04 y 302.10", "T302.04", "T302.10")],
        ["C-04", "Bombeo normal: la Tabla 302.05 regula el contraperalte como solución opcional; las "
                 "Tablas 304.04 y 304.06 fijan la regla general.",
         "Se aplica la regla general. 90 km/h se agrupa con 40 ≤ V < 100 km/h, como indica la "
         "Tabla 304.06.", ref("Tablas 302.05, 304.04, 304.06", "T302.05", "T304.04", "T304.06")],
        ["C-05", "V < 60 km/h: el Tópico 302.04.04 prohíbe el contraperalte, pero la Tabla 304.04 "
                 "admite curvas sin peralte desde 3,500 m a 40 km/h.",
         "Se elimina la fila NC y se extiende RC (2%) hasta 3,500 m.",
         ref("Tópico 302.04.04; Tabla 304.04", "contra60", "T304.04")],
        ["C-06", "K de Tercera Clase: la Tabla 303.02 da en adelantamiento valores con el criterio AASHTO "
                 "(Da²/864), distintos de la fórmula del Tópico 303.04.03 (Da²/946).",
         "Tercera Clase: Tabla 303.02. Red Vial General: fórmulas del Tópico 303.04.03.",
         ref("Tópico 303.04.03; Tabla 303.02", "303.04.03", "T303.02")],
        ["C-07", "Redondeo de K calculado.", "Hacia arriba, como en las Tablas 303.02 y 303.03.",
         ref("Tablas 303.02 y 303.03", "T303.02", "T303.03")],
        ["C-08", "J depende de la velocidad, pero Civil 3D admite un solo q por fórmula.",
         "q = 0.4 m/s³: cumple para V ≥ 80 km/h y es conservador para V < 80 km/h (J = 0.5).",
         ref("Tabla 302.09", "T302.09")],
    ]
    s.append(tabla(["ID", "Situación en la norma", "Criterio adoptado", "Referencia"],
                   criterios, [11, 70, 55, 38]))

    # --- 5. Registro --------------------------------------------------------
    s.append(P("5. Registro detallado de cambios", "h1"))

    # 5.1 Radios mínimos
    s.append(P("5.1 Radios mínimos (MinimumRadiusTables)", "h2"))
    filas = []
    quitadas = []
    for e in PMAX:
        ro, rc_ = o["radios"][f"DG2018 _PMax {e}%"], c["radios"][f"DG2018 _PMax {e}%"]
        for v in sorted(set(ro) - set(rc_)):
            quitadas.append(f"{e}% {v} km/h ({ro[v]} m)")
    filas.append(["R-01", "Todas con peralte", "Filas fuera de rango: " + "; ".join(quitadas),
                  "Eliminadas", ref("Tabla 204.01: 30 a 130 km/h", "T204.01")])
    ro8, rc8 = o["radios"]["DG2018 _PMax 8%"], c["radios"]["DG2018 _PMax 8%"]
    filas.append(["R-02", "DG2018 _PMax 8%", f"110 km/h: {ro8[110]} m", f"{rc8[110]} m",
                  ref("Tabla 302.02", "T302.02") + ". 50 km/h se mantiene en 85 m (C-01)"])
    ro10, rc10 = o["radios"]["DG2018 _PMax 10%"], c["radios"]["DG2018 _PMax 10%"]
    cambios10 = [v for v in range(30, 80, 10) if ro10[v] != rc10[v]]
    filas.append(["R-03", "DG2018 _PMax 10%",
                  "30–70 km/h: " + ", ".join(str(ro10[v]) for v in cambios10) + " m (fricción AASHTO)",
                  ", ".join(str(rc10[v]) for v in cambios10) + " m",
                  ref("Tablas 302.03, 302.04 y 302.10", "T302.03", "T302.10") + "; criterio C-03"])
    filas.append(["R-04", "DG2018 _PMax 10%", f"130 km/h: {ro10[130]} m", "Sin cambio (verificado)",
                  ref("Tópico 302.04.02 con fmáx de la Tabla 302.02", "302.04.02", "T302.02") + "; C-02"])
    rsp_o, rsp_c = o["radios"]["DG2018_METRIC SIN PERALTE"], c["radios"]["DG2018_METRIC SIN PERALTE"]
    filas.append(["R-05", "DG2018_METRIC SIN PERALTE",
                  "Radios AASHTO con e = −2%: " + ", ".join(f"{v}: {r}" for v, r in rsp_o.items()) + " m",
                  ", ".join(f"{v}: {r}" for v, r in rsp_c.items()) + " m",
                  ref("Tabla 302.05 (RL adoptado)", "T302.05") + "; "
                  + ref("Tópico 302.04.04: sin contraperalte con V < 60 km/h", "contra60")])
    s.append(tabla(["ID", "Tabla", "Original", "Corregido", "Sustento DG-2018"],
                   filas, [11, 30, 50, 33, 50]))
    s.append(P("Verificado sin cambio: 4%, 6% y 12% de 30 a 130 km/h coinciden con la Tabla 302.02; "
               "10% de 80 a 120 km/h coincide con la Tabla 302.10.", "nota"))

    # 5.2 Peralte
    s.append(P("5.2 Tablas de peralte (SuperelevationTables)", "h2"))
    s.append(P("<b>P-01. Nombre.</b> “AASHTO 2011 Metric eMax 10%” pasa a “DG2018 _PMax 10%”, para "
               "uniformarlo con las demás tablas."))
    s.append(P("<b>P-02. Escalón de peralte máximo.</b> El radio de la fila de peralte máximo se iguala al "
               "radio mínimo de la Tabla 302.02 (" + f"pág. {PAG['T302.02']}" + "). No incluye los "
               "bloques generados, que se registran en P-05."))
    filas = []
    for e in PMAX:
        po, pc = o["peralte"][NOMBRE_ORIGINAL[e]], c["peralte"][NOMBRE_CORREGIDO[e]]
        for v in sorted(pc):
            if v in gen.GENERAR.get(e, []) or v not in po:
                continue
            a, b = po[v][-1][1], pc[v][-1][1]
            if a != b:
                filas.append([f"{e}%", v, f"{a} m", f"{b} m"])
    s.append(tabla(["Tabla", "V (km/h)", "Original", "Corregido"], filas, [40, 40, 47, 47]))

    s.append(P("<b>P-03. Erratas en radios intermedios.</b> La norma no tabula los escalones intermedios "
               f"(los da en ábacos, Figuras 302.02–302.05, págs. {PAG['F302.02-05']}). Se corrigen por "
               "interpolación entre los escalones vecinos: son valores derivados."))
    filas = []
    for (e, v, tasa), nuevo in gen.ERRATAS.items():
        fo = o["peralte"][NOMBRE_ORIGINAL[e]][v]
        idx = [r for r, _ in fo].index(tasa)
        filas.append([f"E-{len(filas) + 1:02d}", f"{e}%", v, tasa, fo[idx - 1][1], fo[idx][1],
                      fo[idx + 1][1], nuevo])
    s.append(tabla(["ID", "Tabla", "V (km/h)", "eRate (%)", "Radio anterior", "Original",
                    "Radio siguiente", "Corregido"], filas, [12, 18, 18, 20, 28, 24, 28, 26],
                   ))

    s.append(P("<b>P-04. Bombeo normal (NC) y peralte mínimo de 2% (RC).</b> Regla general de las Tablas "
               f"304.04 (pág. {PAG['T304.04']}) y 304.06 (pág. {PAG['T304.06']}): sin peralte desde "
               "3,500 m (40 ≤ V &lt; 100 km/h) y 7,500 m (V ≥ 100 km/h); 2% mínimo desde 2,500 m y "
               "5,000 m. Con V &lt; 60 km/h no hay contraperalte (Tópico 302.04.04, pág. "
               f"{PAG['contra60']}) y RC se extiende hasta 3,500 m (criterio C-05). Radios en metros; "
               "“—” = bloque inexistente en el original."))
    for tasa, titulo in (("NC", "Radio NC (original → corregido)"), ("RC", "Radio RC (original → corregido)")):
        filas = []
        for v in gen.VELOCIDADES:
            fila = [v]
            for e in PMAX:
                bo = o["peralte"][NOMBRE_ORIGINAL[e]].get(v)
                bc = c["peralte"][NOMBRE_CORREGIDO[e]].get(v)
                a, b = radio_nc_rc(bo, tasa), radio_nc_rc(bc, tasa)
                antes = "—" if bo is None else (a or "sin fila")
                fila.append(f"{antes} → {b or 'sin fila'}")
            filas.append(fila)
        s.append(KeepTogether([P(titulo, "nota"),
                               tabla(["V (km/h)"] + [f"{e}%" for e in PMAX], filas,
                                     [19, 31, 31, 31, 31, 31])]))
    s.append(P("En la tabla de 4% a 30 km/h la fila equivalente a RC se llama “2.0”.", "nota"))

    s.append(P("<b>P-05. Bloques generados.</b> Se calculan con el método 5 de AASHTO, que es la "
               f"distribución de los ábacos (Figuras 302.02–302.05, págs. {PAG['F302.02-05']}), con fmáx "
               f"de las Tablas 302.02 y 302.03 (págs. {PAG['T302.02']} y {PAG['T302.03']}) y el radio "
               "mínimo del criterio aplicable en la fila de peralte máximo. NC y RC siguen P-04. El mismo "
               "cálculo reproduce la tabla AASHTO de 10% original con error menor al 1% entre 40 y "
               "130 km/h."))
    filas = []
    for e, velocidades in gen.GENERAR.items():
        for v in velocidades:
            bo = o["peralte"][NOMBRE_ORIGINAL[e]].get(v)
            bc = c["peralte"][NOMBRE_CORREGIDO[e]][v]
            situacion = (f"Existía con fricción AASHTO (R a {e}% = {bo[-1][1]} m)" if bo
                         else "No existía")
            filas.append([f"{e}%", v, situacion, len(bc), f"{bc[-1][1]} m"])
    s.append(tabla(["Tabla", "V (km/h)", "Situación original", "Filas", f"R peralte máx."],
                   filas, [18, 18, 80, 18, 30]))
    s.append(P("Se eliminó además el bloque de 20 km/h de la tabla de 10% (fuera del rango de la "
               f"Tabla 204.01, pág. {PAG['T204.01']}).", "nota"))

    # 5.3 Transición
    s.append(P("5.3 Longitudes de transición y clotoide", "h2"))
    vo, vc = validar(o), validar(c)
    filas = [
        ["T-01", "Radios de TransitionLengthTables (2 Lane y 4 Lane)",
         f"{vo['tl_distinto']} de {vo['tl_filas']} filas con radio distinto al de la tabla de peralte",
         f"{vc['tl_distinto']} de {vc['tl_filas']} (radios idénticos fila por fila)",
         "Consistencia interna: la longitud debe corresponder al peralte asignado al mismo radio"],
        ["T-02", "Bloques sin tabla de peralte", "12%: 20 km/h; 10%: 20 km/h; 8% “2 Lane” sin 130 km/h",
         "Eliminados o completados", ref("Tabla 204.01", "T204.01")],
        ["T-03", "tLength", "L = 3.6·e/Δ por carril girado (×1.5 en 4 Lane)",
         "Se conservan; en bloques nuevos, la misma regla",
         ref("Tabla 302.13 (coincide hasta 90 km/h); sobre 90 km/h es extensión derivada", "T302.13")],
        ["T-04", "TransitionLengthFormula · minimumValue", o["formula"].get("minimumValue"),
         c["formula"].get("minimumValue"), ref("Nota de la Tabla 302.10: mínimo 30 m", "N302.10")],
        ["T-05", "TransitionLengthFormula · q", o["formula"].get("q"), c["formula"].get("q"),
         ref("Tabla 302.09 y Tópico 302.05.04", "T302.09") + "; criterio C-08"],
    ]
    s.append(tabla(["ID", "Elemento", "Original", "Corregido", "Sustento DG-2018"],
                   filas, [11, 38, 42, 38, 45]))

    # 5.4 Sobreancho
    s.append(P("5.4 Sobreancho (WideningMethods)", "h2"))
    s.append(tabla(["ID", "Método", "Original", "Corregido", "Sustento DG-2018"], [[
        "S-01", "DG2018 formula simple", o["sobreancho"]["DG2018 formula simple"],
        c["sobreancho"]["DG2018 formula simple"],
        ref("Tópico 302.09.03: Sa = n(R − √(R² − L²)) + V/(10√R)", "302.09.03")]],
        [11, 27, 44, 44, 48]))
    s.append(P("El método “DG2018 formula estandar” ya usaba el coeficiente 0.1 y no se modificó.", "nota"))

    # 5.5 K
    s.append(P("5.5 Parámetro K de curvas verticales (MinimumKTables)", "h2"))
    s.append(P("<b>K-01.</b> La tabla “DG2018  metrico Standard” (valores AASHTO 2011) se reemplaza por "
               "“DG2018 Red Vial General” y “DG2018 Tercera Clase”. <b>K-02.</b> Red Vial General: "
               "K<sub>parada</sub> = Dp²/404 (h1 = 1.07 m, h2 = 0.15 m) y K<sub>paso</sub> = Da²/946 "
               f"(h2 = 1.30 m), Tópico 303.04.03 (págs. {PAG['303.04.03']}); K<sub>cóncava</sub> = "
               f"Dp²/(120 + 3.5Dp), Tópico 303.04.04 (pág. {PAG['303.04.04']}); Dp y Da de las Tablas "
               f"205.01 y 205.03 (págs. {PAG['T205.01']} y {PAG['T205.03']}). <b>K-03.</b> Tercera "
               f"Clase: Tablas 303.02 (pág. {PAG['T303.02']}) y 303.03 (pág. {PAG['T303.03']})."))
    ko = o["k"]["DG2018  metrico Standard"]
    rvg, ter = c["k"]["DG2018 Red Vial General"], c["k"]["DG2018 Tercera Clase"]
    filas = []
    for v in range(20, 140, 10):
        g = lambda d, cl: d[cl].get(v, "—")
        filas.append([v, g(ko, "SSD"), g(rvg, "SSD"), g(ter, "SSD"), g(ko, "PSD"), g(rvg, "PSD"),
                      g(ter, "PSD"), g(ko, "HSD"), g(rvg, "HSD"), g(ter, "HSD")])
    s.append(tabla(["V (km/h)", "Parada orig.", "Parada RVG", "Parada 3ra", "Paso orig.", "Paso RVG",
                    "Paso 3ra", "Cóncava orig.", "Cóncava RVG", "Cóncava 3ra"],
                   filas, [16, 17, 17, 17, 17, 17, 17, 18, 19, 19]))
    s.append(P("RVG = Red Vial General (Autopistas, Primera y Segunda Clase). 3ra = Tercera Clase. "
               "Valores redondeados hacia arriba (criterio C-07); en Parada 3ra, los 0.6, 1.9, 3.8 y 6.4 "
               "de la Tabla 303.02 quedan en 1, 2, 4 y 7.", "nota"))

    # --- 6. Valores derivados ----------------------------------------------
    s.append(P("6. Valores derivados (no tabulados en la norma)", "h1"))
    s.append(P("Los siguientes valores no se leen directamente de una tabla de la DG-2018; se obtuvieron "
               "por cálculo a partir de sus fórmulas o por interpolación, y deben entenderse así:"))
    derivados = [
        ["Radios intermedios corregidos (P-03)", "Interpolación entre escalones vecinos del propio XML"],
        ["Bloques de peralte generados (P-05)", "Método 5 de AASHTO con fmáx y Rmín de la DG-2018"],
        ["Radio mínimo de 10% a 130 km/h (739 m)", "Tópico 302.04.02 con fmáx = 0.08 de la Tabla 302.02"],
        ["tLength por encima de 90 km/h (T-03)", "Extensión de la regla de la Tabla 302.13 con Δ AASHTO"],
        ["K de Red Vial General (K-02)", "Fórmulas de los Tópicos 303.04.03 y 303.04.04"],
    ]
    s.append(tabla(["Valor", "Origen"], derivados, [70, 104]))

    # --- 7. Validación -------------------------------------------------------
    s.append(P("7. Validación del archivo corregido", "h1"))
    validacion = [
        ["XML bien formado; codificación UTF-8 y saltos de línea CRLF conservados", "Cumple", "—"],
        ["Radios que no decrecen al subir el peralte, dentro de cada bloque",
         str(vc["no_decreciente"]), str(vo["no_decreciente"])],
        ["Radios que no crecen con la velocidad para un mismo peralte",
         str(vc["inversiones"]), str(vo["inversiones"])],
        ["Filas de transición con radio distinto al de la tabla de peralte",
         str(vc["tl_distinto"]), str(vo["tl_distinto"])],
        ["Tablas DG2018 con los 11 bloques de 30 a 130 km/h",
         str(sum(sorted(c["peralte"][NOMBRE_CORREGIDO[e]]) == list(gen.VELOCIDADES) for e in PMAX)) + " de 5",
         str(sum(sorted(o["peralte"][NOMBRE_ORIGINAL[e]]) == list(gen.VELOCIDADES) for e in PMAX)) + " de 5"],
    ]
    s.append(tabla(["Comprobación", "Corregido", "Original"], validacion, [118, 28, 28]))

    # --- 8. Pendientes -------------------------------------------------------
    s.append(P("8. Limitaciones y verificaciones pendientes", "h1"))
    for texto in [
        "El archivo no se ha importado ni probado en Autodesk Civil 3D. Antes de usarlo en producción, "
        "trazar un alineamiento de prueba y comprobar el peralte asignado: a 40 km/h, R = 1,000 m debe "
        "recibir al menos 2% y R = 4,000 m ninguno; a 100 km/h, R = 6,000 m debe recibir 2% y "
        "R = 8,000 m ninguno.",
        "Las referencias a las tablas renombradas (“AASHTO 2011 Metric eMax 10%” y “DG2018  metrico "
        "Standard”) deben actualizarse en la pestaña de criterios de diseño de las propiedades del "
        "alineamiento y del perfil.",
        "La tabla “Superelevation Rate By Formula” conserva la fórmula de peralte {v}^2/(2.82528*{r}), "
        "que no proviene de la DG-2018; solo se ajustaron q y minimumValue.",
        "Para Primera y Segunda Clase y Autopistas, la longitud mínima de transición de peralte se rige "
        f"por Lmín = (pf − pi)/(1.8 − 0.01V)·B (Tópico 302.08, Tablas 302.14–302.18, págs. "
        f"{PAG['302.08']}–{PAG['T302.14-18'].split('–')[-1]}); los tLength del XML siguen la base de "
        "la Tabla 302.13 (Tercera Clase).",
        f"El sobreancho mínimo de 0.40 m (pág. {PAG['Sa040']}) no se puede imponer desde la fórmula de "
        "Civil 3D; debe verificarse en el diseño.",
    ]:
        s.append(P("• " + escape(texto)))

    # --- Anexo A: citas ------------------------------------------------------
    s.append(P("Anexo A. Citas textuales de la DG-2018", "h1"))
    citas = [
        ("A cada tramo homogéneo se le puede asignar la Velocidad de Diseño en el rango que se indica "
         "en la Tabla 204.01.", f"Tópico 204.02, pág. {PAG['204.02']}"),
        ("Los radios mínimos de curvatura horizontal son los menores radios que pueden recorrerse con "
         "la velocidad de diseño y la tasa máxima de peralte, en condiciones aceptables de seguridad y "
         "comodidad, para cuyo cálculo puede utilizarse la siguiente fórmula: Rmín = V² / 127 (Pmáx + "
         "fmáx)", f"Tópico 302.04.02, pág. {PAG['302.04.02']}"),
        ("Puede resultar conveniente adoptar esta solución cuando el radio de la curva es igual o mayor "
         "que el indicado en la Tabla 302.05, en alguna de las siguientes situaciones:",
         "Tópico 302.04.04, pág. 132"),
        ("En caminos de velocidad de diseño inferior a 60 km/h o cuya vía no cuente con pavimento, no "
         "se usarán contraperaltes.", f"Tópico 302.04.04, pág. {PAG['contra60']}"),
        ("Se adoptarán para J los valores indicados en la Tabla 302.09.",
         f"Tópico 302.05.03, pág. {PAG['T302.09']}"),
        ("Nota: En ningún caso se adoptarán longitudes de transición menores a 30 m.",
         f"Tabla 302.10, pág. {PAG['N302.10']}"),
        ("En carreteras de Tercera Clase, se tomarán los valores que muestra la Tabla 302.13 para "
         "definir las longitudes mínimas de transición de bombeo y de transición de peralte en función "
         "a la velocidad de diseño y valor del peralte.", f"Tópico 302.08, pág. {PAG['302.08']}"),
        ("El sobreancho variará en función del tipo de vehículo, del radio de la curva y de la "
         "velocidad de diseño y se calculará con la siguiente figura y fórmula:",
         "Tópico 302.09.03, pág. 160"),
        ("Se considera apropiado un valor mínimo de 0.40 m de sobreancho para justificar su adopción.",
         f"Tópico 302.09.03, pág. {PAG['Sa040']}"),
        ("La Figura 303.06, presenta los gráficos para resolver las ecuaciones planteadas, para el caso "
         "más común con h1 = 1.07 m y h2 = 0.15 m.", f"Tópico 303.04.03, pág. {PAG['h1h2']}"),
        ("...asimismo se aplicarán las mismas fórmulas que en (a); utilizándose como h2 = 1.30 m, "
         "considerando h1 = 1.07 m.", f"Tópico 303.04.03, pág. {PAG['h5']}"),
        ("Los valores del Índice K al que se refiere el Art. 303.04.01 para la determinación de la "
         "longitud de las curvas verticales convexas para carreteras de Tercera Clase, serán los "
         "indicados en la Tabla 303.02.", f"Tópico 303.04.03, pág. {PAG['h5']}"),
        ("Las curvas horizontales deben ser peraltadas; con excepción de los valores establecidos "
         "fijados en la Tabla 304.04.", f"Tópico 304.06.01, pág. {PAG['T304.04']}"),
        ("El peralte mínimo será del 2%, para los radios y velocidades de diseño indicadas en la "
         "Tabla 304.06.", f"Tópico 304.06.01, pág. {PAG['T304.06']}"),
    ]
    for texto, fuente in citas:
        s.append(cita(texto, fuente))
    s.append(P("Tabla 304.04 (pág. 196): radio a partir del cual no es necesario peralte — 40, 60 y "
               "80 km/h: 3,500 m; ≥ 100 km/h: 7,500 m. Tabla 304.06 (pág. 197): peralte mínimo 2% — "
               "V ≥ 100 km/h: 5,000 ≤ R &lt; 7,500 m; 40 ≤ V &lt; 100 km/h: 2,500 ≤ R &lt; 3,500 m.",
               "nota"))
    return s


def main():
    doc = SimpleDocTemplate(str(SALIDA), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                            topMargin=18 * mm, bottomMargin=18 * mm,
                            title="Reporte de trazabilidad DG2018_Corregido.xml",
                            author="Generado con Claude Code", subject="Trazabilidad DG-2018")
    doc.build(construir(), canvasmaker=LienzoNumerado)
    print(f"Generado: {SALIDA}")


if __name__ == "__main__":
    main()
