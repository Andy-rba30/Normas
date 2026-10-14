#!/usr/bin/env python3
"""Genera DG2018_Corregido.xml a partir de DG2018_original.xml.

Aplica las correcciones verificadas contra el Manual de Carreteras: Diseño
Geométrico DG-2018 (normas/Manual.de.Carreteras.DG-2018.pdf). El detalle de
cada cambio y su sustento normativo está en CAMBIOS_DG2018.md.

Uso:
    python3 generar_dg2018_corregido.py [entrada.xml] [salida.xml]
"""
import math
import sys
from pathlib import Path

from lxml import etree

NS = "urn:Civil3DRoadwayDesignStandards-schema"
AQUI = Path(__file__).resolve().parent
VELOCIDADES = range(30, 140, 10)  # Tabla 204.01: 30 a 130 km/h


def q(tag):
    return f"{{{NS}}}{tag}"


# ---------------------------------------------------------------------------
# Parámetros normativos
# ---------------------------------------------------------------------------

# Fricción transversal máxima (Tablas 302.02 y 302.03).
FMAX = {30: .17, 40: .17, 50: .16, 60: .15, 70: .14, 80: .14, 90: .13,
        100: .12, 110: .11, 120: .09, 130: .08}

# Radio mínimo redondeado por peralte máximo (Tabla 302.02). El 10% no figura
# en la 302.02: se toma el mayor valor oficial entre las Tablas 302.04 y
# 302.10 (30-70 km/h), la 302.10 (80-120 km/h) y V²/127(0.10+0.08) a 130 km/h,
# mismo fmáx que la 302.02.
RMIN = {
    4: [35, 60, 100, 150, 215, 280, 375, 495, 635, 875, 1110],
    6: [30, 55, 90, 135, 195, 255, 335, 440, 560, 755, 950],
    8: [30, 50, 85, 125, 175, 230, 305, 395, 500, 670, 835],
    10: [26, 47, 76, 115, 161, 210, 277, 358, 454, 597, 739],
    12: [25, 45, 70, 105, 150, 195, 255, 330, 415, 540, 665],
}
RMIN = {e: dict(zip(VELOCIDADES, radios)) for e, radios in RMIN.items()}

# Radio límite en contraperalte adoptado (Tabla 302.05).
R_CONTRAPERALTE = {60: 1000, 70: 1000, 80: 1200, 90: 1600, 100: 2000,
                   110: 2800, 120: 4000, 130: 5500}


def radios_nc_rc(v):
    """Bombeo normal (NC) y peralte mínimo de 2% (RC), Tablas 304.04 y 304.06.

    Para V < 60 km/h no hay fila NC (el Tópico 302.04.04 prohíbe el
    contraperalte) y el 2% se extiende hasta 3,500 m (Tabla 304.04), para que
    el resultado no dependa de cómo trate Civil 3D los radios mayores que el
    de la primera fila.
    """
    if v < 60:
        return None, 3500
    if v < 100:
        return 3500, 2500
    return 7500, 5000


# Correcciones de erratas en radios intermedios (interpolación de vecinos).
ERRATAS = {
    (8, 40, "2.6"): 449,
    (8, 40, "3.8"): 286,
    (8, 80, "3.4"): 1070,
    (8, 80, "4.4"): 792,
    (12, 70, "2.4"): 1296,
    (12, 100, "6.8"): 744,
    (12, 110, "8.4"): 696,
}

# Bloques de peralte que se generan con el método 5 de AASHTO usando la
# fricción de la DG-2018 (faltantes o calculados con fricción AASHTO).
GENERAR = {
    4: [110, 120, 130],
    8: [130],
    10: [30, 40, 50, 60, 70],
    12: [130],
}

# Velocidad media de marcha para el método 5 (AASHTO 2011).
V_MARCHA = {30: 30, 40: 40, 50: 47, 60: 55, 70: 63, 80: 70, 90: 77,
            100: 85, 110: 91, 120: 98, 130: 102}

# Pendiente relativa máxima de borde (%), base de la Tabla 302.13:
# L = 3.6 m · e / Δ por carril girado. Reproduce los tLength del XML original.
DELTA = {30: .75, 40: .70, 50: .65, 60: .60, 70: .55, 80: .50, 90: .47,
         100: .44, 110: .41, 120: .38, 130: .35}
FACTOR_CARRILES = {"2 Lane": 1.0, "4 Lane": 1.5}

# Parámetro K (Tópicos 303.04.03 y 303.04.04; Tablas 205.01, 205.03,
# 303.02 y 303.03).
DP = {20: 20, 30: 35, 40: 50, 50: 65, 60: 85, 70: 105, 80: 130, 90: 160,
      100: 185, 110: 220, 120: 250, 130: 285}
DA = {20: 130, 30: 200, 40: 270, 50: 345, 60: 410, 70: 485, 80: 540,
      90: 615, 100: 670, 110: 730, 120: 775, 130: 815}
K_TERCERA = {  # Tablas 303.02 (SSD redondeado hacia arriba) y 303.03
    "SSD": {20: 1, 30: 2, 40: 4, 50: 7, 60: 11, 70: 17, 80: 26, 90: 39},
    "PSD": {30: 46, 40: 84, 50: 138, 60: 195, 70: 272, 80: 338, 90: 438},
    "HSD": {20: 3, 30: 6, 40: 9, 50: 13, 60: 18, 70: 23, 80: 30, 90: 38},
}


def redondear(x):
    return math.floor(x + 0.5)


def ceil_k(x):
    # Redondeo hacia arriba, como en las Tablas 303.02 y 303.03.
    return math.ceil(round(x, 6))


def k_red_general():
    h1, h2, h5 = 1.07, 0.15, 1.30
    c_ssd = 200 * (math.sqrt(h1) + math.sqrt(h2)) ** 2  # ≈ 404
    c_psd = 200 * (math.sqrt(h1) + math.sqrt(h5)) ** 2  # ≈ 946
    return {
        "SSD": {v: ceil_k(d * d / round(c_ssd)) for v, d in DP.items()},
        "PSD": {v: ceil_k(d * d / round(c_psd)) for v, d in DA.items()},
        "HSD": {v: ceil_k(d * d / (120 + 3.5 * d)) for v, d in DP.items()},
    }


# ---------------------------------------------------------------------------
# Distribución de peralte: método 5 de AASHTO
# ---------------------------------------------------------------------------

def metodo5(v, emax_pct):
    """Devuelve una función e(%) -> radio (m) para V y peralte máximo dados."""
    e, f, vr = emax_pct / 100, FMAX[v], V_MARCHA[v]
    d_max = 127 * (e + f) / v ** 2
    d_pi = 127 * e / vr ** 2
    f_pi = e * (v ** 2 / vr ** 2 - 1)
    s1 = f_pi / d_pi
    s2 = (f - f_pi) / (d_max - d_pi)
    m0 = d_pi * (d_max - d_pi) * (s2 - s1) / (2 * d_max)

    def friccion(d):
        if d <= d_pi:
            return m0 * (d / d_pi) ** 2 + s1 * d
        return m0 * ((d_max - d) / (d_max - d_pi)) ** 2 + f_pi + s2 * (d - d_pi)

    def radio(e_pct):
        objetivo, lo, hi = e_pct / 100, 1e-9, d_max
        for _ in range(200):
            mid = (lo + hi) / 2
            if v ** 2 * mid / 127 - friccion(mid) < objetivo:
                lo = mid
            else:
                hi = mid
        return 1 / ((lo + hi) / 2)

    return radio


def valor_e(rate):
    # Convención de los tLength del XML: NC se calcula con 1.5% y RC con 2.0%.
    return {"NC": 1.5, "RC": 2.0}.get(rate) or float(rate)


def tlength(v, rate, carriles):
    return redondear(FACTOR_CARRILES[carriles] * 3.6 * valor_e(rate) / DELTA[v])


def generar_bloque(v, emax):
    radio = metodo5(v, emax)
    pasos = [f"{x / 10:.1f}" for x in range(22, int(emax * 10) + 1, 2)]
    filas = [["NC", redondear(radio(1.5))], ["RC", redondear(radio(2.0))]]
    filas += [[p, redondear(radio(float(p)))] for p in pasos]
    return filas


# ---------------------------------------------------------------------------
# Edición del XML
# ---------------------------------------------------------------------------

def elem(tag, **attrs):
    return etree.Element(q(tag), {k: str(v) for k, v in attrs.items()})


def comentario(texto):
    return etree.Comment(texto)


def corregir_radios_minimos(root):
    for tabla in root.iter(q("MinimumRadiusTable")):
        nombre = tabla.get("name")
        for hijo in list(tabla):
            tabla.remove(hijo)
        if nombre == "DG2018_METRIC SIN PERALTE":
            tabla.append(comentario(
                "DG-2018 Tabla 302.05: radio limite en contraperalte (RL adoptado). "
                "No se usan contraperaltes con V < 60 km/h (Topico 302.04.04)."))
            for v, r in R_CONTRAPERALTE.items():
                tabla.append(elem("MinimumRadius", speed=v, radius=r))
            continue
        emax = int(nombre.split()[-1].rstrip("%"))
        for v in VELOCIDADES:
            tabla.append(elem("MinimumRadius", speed=v, radius=RMIN[emax][v]))


def corregir_peraltes(root):
    for tabla in root.iter(q("SuperelevationTable")):
        if tabla.get("name") == "AASHTO 2011 Metric eMax 10%":
            tabla.set("name", "DG2018 _PMax 10%")
        nombre = tabla.get("name")
        if not nombre.startswith("DG2018 _PMax"):
            continue
        emax = int(nombre.split()[-1].rstrip("%"))
        por_tabla = tabla.find(q("SuperelevationTypeByTable"))

        bloques = {}
        for ds in por_tabla.findall(q("SuperelevationDesignSpeed")):
            v = int(ds.get("speed"))
            filas = [[x.get("eRate"), float(x.get("radius"))]
                     for x in ds.findall(q("SuperelevationRate"))]
            bloques[v] = filas
            por_tabla.remove(ds)

        longitudes = {}  # (carriles, V) -> lista de tLength alineada por fila
        tl_tablas = por_tabla.find(q("TransitionLengthTables"))
        for tl in tl_tablas.findall(q("TransitionLengthTable")):
            for d in tl.iter(q("TransitionLengthDesignSpeed")):
                longitudes[(tl.get("name"), int(d.get("speed")))] = [
                    float(x.get("tLength")) for x in d.findall(q("TransitionLength"))]

        nuevos = {}
        for v in VELOCIDADES:
            if v in GENERAR.get(emax, []):
                filas = generar_bloque(v, emax)
                tls = {c: [tlength(v, f[0], c) for f in filas] for c in FACTOR_CARRILES}
            elif v in bloques:
                filas = bloques[v]
                tls = {}
                for c in FACTOR_CARRILES:
                    tls[c] = longitudes.get((c, v)) or [tlength(v, f[0], c) for f in filas]
                    assert len(tls[c]) == len(filas), (nombre, v, c)
            else:
                continue

            for fila in filas:
                fila[1] = ERRATAS.get((emax, v, fila[0]), fila[1])
            filas[-1][1] = RMIN[emax][v]
            assert float(filas[-1][0]) == emax

            nc, rc = radios_nc_rc(v)
            for fila in filas:
                if fila[0] == "NC" and nc:
                    fila[1] = nc
                elif fila[0] in ("RC", "2.0") and rc:  # 4% a 30 km/h usa "2.0"
                    fila[1] = rc
            if v < 60 and filas[0][0] == "NC":
                filas = filas[1:]
                tls = {c: t[1:] for c, t in tls.items()}

            radios = [f[1] for f in filas]
            assert all(a > b for a, b in zip(radios, radios[1:])), (nombre, v, radios)
            nuevos[v] = (filas, tls)

        ancla = tl_tablas
        for v, (filas, _) in nuevos.items():
            ds = elem("SuperelevationDesignSpeed", speed=v)
            for rate, r in filas:
                ds.append(elem("SuperelevationRate", radius=int(r), eRate=rate))
            ancla.addprevious(ds)

        for tl in tl_tablas.findall(q("TransitionLengthTable")):
            cont = tl.find(q("TransitionLengthTypeByTable"))
            for hijo in list(cont):
                cont.remove(hijo)
            for v, (filas, tls) in nuevos.items():
                d = elem("TransitionLengthDesignSpeed", speed=v)
                for (rate, r), t in zip(filas, tls[tl.get("name")]):
                    d.append(elem("TransitionLength", radius=int(r), tLength=int(t)))
                cont.append(d)


def corregir_formula_transicion(root):
    for f in root.iter(q("TransitionLengthFormula")):
        f.set("minimumValue", "30.0")  # Nota de la Tabla 302.10
        f.set("q", "0.4")  # Tabla 302.09: J = 0.4 m/s³ (conservador para V < 80)


def corregir_sobreancho(root):
    for m in root.iter(q("WideningMethod")):
        if m.get("name") != "DG2018 formula simple":
            continue
        for hijo in m:
            if isinstance(hijo, etree._Comment):
                hijo.text = (" DG-2018 Topico 302.09.03: Sa = n(R - sqrt(R^2 - L^2)) "
                             "+ V/(10 sqrt(R)). Sobreancho minimo a aplicar: 0.40 m. ")
        formula = m.find(f".//{q('WideningFormula')}")
        formula.set("formula", "{n}*({r}-sqrt({r}^2-{wl}^2))+0.1*{v}/{r}^.5")


def tabla_k(nombre, valores, notas):
    t = elem("MinimumKTable", name=nombre)
    secciones = [("StoppingSightDistance", "MinimumK_SSD", "SSD"),
                 ("PassingSightDistance", "MinimumK_PSD", "PSD"),
                 ("HeadlightSightDistance", "MinimumK_HSD", "HSD")]
    for seccion, etiqueta, clave in secciones:
        s = elem(seccion)
        s.append(comentario(notas[clave]))
        for v, k in valores[clave].items():
            s.append(elem(etiqueta, speed=v, K=k))
        t.append(s)
    return t


def corregir_k(root):
    tablas = root.find(f".//{q('MinimumKTables')}")
    for hijo in list(tablas):
        tablas.remove(hijo)
    tablas.append(tabla_k("DG2018 Red Vial General", k_red_general(), {
        "SSD": " DG-2018 Topico 303.04.03 a): K = Dp^2/404 (h1 = 1.07 m, h2 = 0.15 m); Dp de Tabla 205.01 ",
        "PSD": " DG-2018 Topico 303.04.03 b): K = Da^2/946 (h1 = 1.07 m, h2 = 1.30 m); Da de Tabla 205.03 ",
        "HSD": " DG-2018 Topico 303.04.04: K = Dp^2/(120 + 3.5 Dp) ",
    }))
    tablas.append(tabla_k("DG2018 Tercera Clase", K_TERCERA, {
        "SSD": " DG-2018 Tabla 303.02 (visibilidad de parada), Carreteras de Tercera Clase ",
        "PSD": " DG-2018 Tabla 303.02 (visibilidad de paso), Carreteras de Tercera Clase ",
        "HSD": " DG-2018 Tabla 303.03, Carreteras de Tercera Clase ",
    }))


def actualizar_comentarios(root):
    reemplazos = {
        'Source: AASHTO 2011 "A Policy on Geometric Design of Highways and Streets," 6th edition':
            "Fuente: DG-2018 Tablas 302.02, 302.04, 302.05 y 302.10 (ver CAMBIOS_DG2018.md)",
        " AASHTO Green Book 2011 - Superelevation table extracts                        ":
            " DG-2018: radios de peralte segun Tablas 302.02, 304.04 y 304.06 (metodo 5)    ",
    }
    for c in root.iter(etree.Comment):
        if c.text in reemplazos:
            c.text = reemplazos[c.text]


def main():
    entrada = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI / "DG2018_original.xml"
    salida = Path(sys.argv[2]) if len(sys.argv) > 2 else AQUI / "DG2018_Corregido.xml"
    parser = etree.XMLParser(remove_blank_text=True)
    arbol = etree.parse(str(entrada), parser)
    root = arbol.getroot()

    corregir_radios_minimos(root)
    corregir_peraltes(root)
    corregir_formula_transicion(root)
    corregir_sobreancho(root)
    corregir_k(root)
    actualizar_comentarios(root)

    etree.indent(arbol, space="\t")
    texto = etree.tostring(arbol, encoding="utf-8", xml_declaration=True).decode("utf-8")
    texto = texto.replace("<?xml version='1.0' encoding='utf-8'?>",
                          '<?xml version="1.0" encoding="utf-8"?>', 1)
    salida.write_bytes((texto.rstrip("\n") + "\n").replace("\n", "\r\n").encode("utf-8"))
    print(f"Generado: {salida}")


if __name__ == "__main__":
    main()
