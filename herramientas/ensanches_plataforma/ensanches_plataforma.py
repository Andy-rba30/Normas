#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ubicación de ENSANCHES DE PLATAFORMA (Manual de Carreteras DG-2018, §304.12.03, Tabla 304.12)
a partir de un LandXML de Civil 3D con: eje, rasante, bordes de calzada y superficie de terreno.

Uso:
  python3 ensanches_plataforma.py ARCHIVO.xml [--salida DIR] [--eje "eje 01"] [--rasante "Rs-eje 01"]
         [--superficie TN] [--borde-izq carril] [--borde-der "carril (6)"]
         [--ancho 2.5 --largo 25 --sep-max 2500 --transicion 15 --gap-min 400 --r-min 60 ...]
"""
import argparse, os, sys, csv, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from landxml_vial import leer_landxml
from analisis import offsets_borde, costos_por_progresiva
from optimiza import costo_ensanche, radio_min_en, optimizar
from seccion import PARAM
from salidas import DXF, escribir_landxml, escribir_svg, km


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('xml')
    ap.add_argument('--salida', default='salida')
    ap.add_argument('--eje', default='eje 01'); ap.add_argument('--rasante', default='Rs-eje 01'); ap.add_argument('--superficie', default='TN')
    ap.add_argument('--borde-izq', default='carril'); ap.add_argument('--borde-der', default='carril (6)')
    ap.add_argument('--ancho', type=float, default=2.5, help='ancho mínimo del ensanche (Tabla 304.12)')
    ap.add_argument('--largo', type=float, default=25.0, help='largo mínimo del ensanche (Tabla 304.12)')
    ap.add_argument('--sep-max', type=float, default=2500.0, help='separación máxima a cada lado (Tabla 304.12)')
    ap.add_argument('--transicion', type=float, default=15.0, help='longitud de transición de ingreso y de salida (1:6)')
    ap.add_argument('--gap-min', type=float, default=400.0, help='separación mínima entre ensanches consecutivos de lados opuestos')
    ap.add_argument('--r-min', type=float, default=60.0, help='radio mínimo de curva admitido dentro del núcleo del ensanche')
    ap.add_argument('--borde-tramo', type=float, default=100.0, help='zona excluida al inicio y fin del tramo')
    ap.add_argument('--berma', type=float, default=0.0, help='ancho de berma existente a añadir al borde de calzada')
    ap.add_argument('--paso', type=float, default=5.0, help='paso de análisis a lo largo del eje')
    ap.add_argument('--k-relleno', type=float, default=1.0, help='ponderación del relleno respecto al corte')
    ap.add_argument('--talud-corte', type=float, default=PARAM['talud_corte']); ap.add_argument('--talud-relleno', type=float, default=PARAM['talud_relleno'])
    a = ap.parse_args()
    PARAM['talud_corte'] = a.talud_corte; PARAM['talud_relleno'] = a.talud_relleno
    os.makedirs(a.salida, exist_ok=True)

    t0 = time.time()
    d = leer_landxml(a.xml)
    eje = d['alineamientos'][a.eje]; ras = d['rasantes'][(a.eje, a.rasante)]; tn = d['superficies'][a.superficie]
    bi, bd = d['alineamientos'][a.borde_izq], d['alineamientos'][a.borde_der]
    print('LandXML leído (%.1fs): eje %s L=%.2f m, %d PVI, TIN %d triángulos' % (time.time() - t0, eje.name, eje.length, len(ras.s), len(tn.tri)))

    sta = np.arange(0.0, eje.length, a.paso)
    oi = offsets_borde(eje, bi, sta); od = offsets_borde(eje, bd, sta)
    oi = -(np.nan_to_num(np.abs(oi), nan=3.30) + a.berma); od = np.nan_to_num(np.abs(od), nan=3.30) + a.berma
    res = costos_por_progresiva(eje, ras, tn, oi, od, sta, a.ancho)
    print('Secciones analizadas: %d progresivas x 2 lados (%.1fs)' % (len(sta), time.time() - t0))

    half = a.largo / 2
    rmin_core = radio_min_en(sta, res['curv'], np.arange(-half, half + 0.01, a.paso / 2))
    rmin_full = radio_min_en(sta, res['curv'], np.arange(-half - a.transicion, half + a.transicion + 0.01, a.paso / 2))
    costo = {}; vol_corte = {}; vol_rell = {}
    for lado in ('IZQ', 'DER'):
        vol_corte[lado] = costo_ensanche(sta, res[lado], a.ancho, a.largo, a.transicion, 1.0, 0.0)
        vol_rell[lado] = costo_ensanche(sta, res[lado], a.ancho, a.largo, a.transicion, 0.0, 1.0)
        v = costo_ensanche(sta, res[lado], a.ancho, a.largo, a.transicion, 1.0, a.k_relleno)
        v = np.where(rmin_core < a.r_min, np.nan, v)
        v = np.where(rmin_full < a.r_min, v * 1.2, v)      # transición dentro de curva cerrada: +20 %
        costo[lado] = v
        print('  %s: %d progresivas candidatas de %d' % (lado, int(np.isfinite(v).sum()), len(v)))

    seq, total = optimizar(sta, costo, a.sep_max, a.gap_min, a.borde_tramo)
    if seq is None:
        print('No se encontró una solución que cumpla las restricciones; relaje --r-min, --gap-min o --sep-max'); sys.exit(2)
    print('Solución: %d ensanches, volumen adicional total estimado %.0f m3 (%.1fs)' % (len(seq), total, time.time() - t0))
    # verificación explícita de las restricciones normativas y de diseño
    st = [sta[i] for i, _ in seq]; ld = [l for _, l in seq]
    ok = all(ld[k] != ld[k + 1] for k in range(len(ld) - 1))
    for lado in ('IZQ', 'DER'):
        sl = [s_ for s_, l in zip(st, ld) if l == lado]
        ok &= sl[0] <= a.sep_max and (eje.length - sl[-1]) <= a.sep_max and all(np.diff(sl) <= a.sep_max + 1e-6)
    ok &= all(np.diff(st) >= a.gap_min - 1e-6)
    print('Verificación (alternancia, separación <= %.0f m por lado, inicio/fin, gap >= %.0f m): %s' % (a.sep_max, a.gap_min, 'OK' if ok else 'NO CUMPLE'))

    # ---- geometría de cada ensanche (numeración independiente por lado: EI-xx izquierda, ED-xx derecha)
    ens = []; puntos = []; dxf = DXF()
    contador = {'IZQ': 0, 'DER': 0}

    def marca_centro(dxf, sk, sgn, lay, etiqueta, etiqueta2, R_m=25.0, h=10.0, h2=6.0):
        """Círculo grande + cruz centrados en el eje, flecha hacia el lado del ensanche y rótulo grande."""
        xk, yk, thk, _ = eje.locate(np.array([sk]))
        cx, cy = float(xk[0]), float(yk[0])
        tgx, tgy = float(np.cos(thk[0])), float(np.sin(thk[0])); nnx, nny = float(np.sin(thk[0])), -float(np.cos(thk[0]))
        angk = np.degrees(thk[0]) % 360
        if 90 < angk < 270:
            angk -= 180
        dxf.circle((cx, cy), R_m, lay); dxf.circle((cx, cy), 3.0, lay)
        dxf.line((cx - 1.6 * R_m * tgx, cy - 1.6 * R_m * tgy), (cx + 1.6 * R_m * tgx, cy + 1.6 * R_m * tgy), lay)
        dxf.line((cx - 1.6 * R_m * nnx, cy - 1.6 * R_m * nny), (cx + 1.6 * R_m * nnx, cy + 1.6 * R_m * nny), lay)
        pa_ = (cx + sgn * (R_m + 2) * nnx, cy + sgn * (R_m + 2) * nny); pb_ = (cx + sgn * (R_m + 14) * nnx, cy + sgn * (R_m + 14) * nny)
        dxf.line(pa_, pb_, lay)
        for sg2 in (1, -1):
            dxf.line(pa_, (pa_[0] + sgn * 5 * nnx + sg2 * 4 * tgx, pa_[1] + sgn * 5 * nny + sg2 * 4 * tgy), lay)
        off_t = R_m + 16
        dxf.text((cx + sgn * off_t * nnx, cy + sgn * off_t * nny), etiqueta, lay, h=h, rot=angk, justify='C')
        dxf.text((cx + sgn * (off_t + 1.4 * h) * nnx, cy + sgn * (off_t + 1.4 * h) * nny), etiqueta2, lay, h=h2, rot=angk, justify='C')

    def marca_extremo(dxf, sk, sc, sgn, lay, etiqueta, d_ens, h=4.0):
        """Marca de inicio/fin: línea transversal a la vía, círculo pequeño en el eje y rótulo al lado opuesto
        del ensanche, alineado con el eje y extendido hacia afuera del ensanche (no se superpone con el centro)."""
        xk, yk, thk, _ = eje.locate(np.array([sk]))
        cx, cy = float(xk[0]), float(yk[0])
        tgx, tgy = float(np.cos(thk[0])), float(np.sin(thk[0])); nnx, nny = float(np.sin(thk[0])), -float(np.cos(thk[0]))
        angk = np.degrees(thk[0]) % 360
        if 90 < angk < 270:
            angk -= 180
        dxf.circle((cx, cy), 4.0, lay)
        dxf.line((cx - sgn * 30 * nnx, cy - sgn * 30 * nny), (cx + sgn * (d_ens + 4) * nnx, cy + sgn * (d_ens + 4) * nny), lay)
        # rótulo en el lado opuesto, a 30 m del eje (fuera del círculo central de 25 m), extendido hacia afuera del ensanche
        P = (cx - sgn * 31 * nnx, cy - sgn * 31 * nny)
        afuera = np.sign(sk - sc)                               # +1 fin (hacia adelante), -1 inicio (hacia atrás)
        u = (np.cos(np.radians(angk)), np.sin(np.radians(angk)))  # dirección de lectura del texto
        hacia_afuera = (u[0] * tgx + u[1] * tgy) * afuera > 0
        dxf.text(P, etiqueta, lay, h=h, rot=angk, justify='L' if hacia_afuera else 'R')

    for orden, (i, lado) in enumerate(seq, 1):
        contador[lado] += 1
        nombre = ('EI-%02d' if lado == 'IZQ' else 'ED-%02d') % contador[lado]
        sgn = -1.0 if lado == 'IZQ' else 1.0
        borde = bi if lado == 'IZQ' else bd
        lay = 'ENSANCHE_' + lado
        c = sta[i]; s_a, s_b = c - half - a.transicion, c + half + a.transicion
        ss = np.arange(s_a, s_b + 0.01, 2.5)
        d0 = np.abs(offsets_borde(eje, borde, ss)); d0 = np.maximum(np.nan_to_num(d0, nan=3.30), 3.30) + a.berma
        wss = a.ancho * np.clip((half + a.transicion - np.abs(ss - c)) / a.transicion, 0, 1)
        xi, yi = eje.offset_points(ss, sgn * d0)
        xo, yo = eje.offset_points(ss, sgn * (d0 + wss))
        zo = ras.elev(ss) - PARAM['bombeo'] * (d0 + wss)
        poly = list(zip(xi, yi)) + list(zip(xo[::-1], yo[::-1]))
        r = res[lado]
        corte = float(vol_corte[lado][i]); rell = float(vol_rell[lado][i])
        x, y, th, _ = eje.locate(np.array([c]))
        e = dict(n=orden, nombre=nombre, lado=lado, sta=c, km=km(c), sta_ini_trans=s_a, sta_ini=c - half, sta_fin=c + half, sta_fin_trans=s_b,
                 x=float(x[0]), y=float(y[0]), z_ras=float(ras.elev(np.array([c]))[0]), d0=float(r['d0'][i]),
                 ancho_plataforma_ens=float(r['d0'][i] + np.abs(res['DER' if lado == 'IZQ' else 'IZQ']['d0'][i]) + a.ancho),
                 vol_add=float(costo[lado][i]), corte_add=corte, relleno_add=rell, h_borde=float(r['h_borde'][i]),
                 pend_terreno=float(r['pend_terreno'][i]) if np.isfinite(r['pend_terreno'][i]) else None,
                 seccion='corte' if r['corte_base'][i] > 0 else 'relleno', r_min=float(rmin_core[i]) if np.isfinite(rmin_core[i]) else None,
                 tin_extrapolado=bool(np.nanmax(r['extrapolado'][max(0, i - 6):i + 7]) > 0),
                 desc='Ensanche %s lado %s km %s (%.1f x %.0f m + transiciones %.0f m)' % (nombre, lado, km(c), a.ancho, a.largo, a.transicion),
                 poligono=[(float(px), float(py)) for px, py in poly])
        ens.append(e)
        dxf.polyline(poly, lay, closed=True)
        dxf.polyline(list(zip(xo, yo, zo)), lay + '_BORDE_3D', is3d=True)
        ang = np.degrees(th[0]) % 360
        if 90 < ang < 270:
            ang -= 180
        dc = float(np.interp(c, ss, d0))
        pc = eje.offset_points(np.array([c]), np.array([sgn * (dc + a.ancho + 2.0)]))
        dxf.text((pc[0][0], pc[1][0]), '%s %s km %s' % (nombre, lado, km(c)), lay + '_TEXTO', h=2.5, rot=ang)
        pc2 = eje.offset_points(np.array([c]), np.array([sgn * (dc + a.ancho + 5.5)]))
        dxf.text((pc2[0][0], pc2[1][0]), '%.1fx%.0f m  +%.0f m3' % (a.ancho, a.largo, costo[lado][i]), lay + '_TEXTO', h=2.0, rot=ang)
        # marcas de ubicación rápida: centro (grande), inicio y fin del ensanche (medianas)
        marca_centro(dxf, c, sgn, lay + '_MARCA', '%s %s' % (nombre, lado), 'km %s' % km(c))
        marca_extremo(dxf, c - half, c, sgn, lay + '_MARCA', '%s INICIO km %s' % (nombre, km(c - half)), dc + a.ancho)
        marca_extremo(dxf, c + half, c, sgn, lay + '_MARCA', '%s FIN km %s' % (nombre, km(c + half)), dc + a.ancho)
        for tag, sk in (('inicio transicion', s_a), ('fin transicion', s_b)):      # extremos de las transiciones: tic + texto pequeño
            dk = float(np.interp(sk, ss, d0))
            p1 = eje.offset_points(np.array([sk]), np.array([sgn * (dk - 1.0)])); p2 = eje.offset_points(np.array([sk]), np.array([sgn * (dk + 3.0)]))
            dxf.line((p1[0][0], p1[1][0]), (p2[0][0], p2[1][0]), lay + '_MARCA')
            dxf.text((p2[0][0], p2[1][0]), '%s km %s' % (tag, km(sk)), lay + '_TEXTO', h=1.5, rot=ang)
        for tag, sk, w_ in (('INI-TRANS', s_a, 0.0), ('INI', c - half, a.ancho), ('CEN', c, a.ancho), ('FIN', c + half, a.ancho), ('FIN-TRANS', s_b, 0.0)):
            dd = float(np.interp(sk, ss, d0)) + w_
            px, py = eje.offset_points(np.array([sk]), np.array([sgn * dd]))
            pz = float(ras.elev(np.array([sk]))[0]) - PARAM['bombeo'] * dd
            puntos.append(('%s-%s' % (nombre, tag), 'ENS-' + lado, '%s %s %s km %s' % (nombre, lado, tag, km(sk)), float(px[0]), float(py[0]), pz))
            dxf.point((float(px[0]), float(py[0]), pz), lay + '_PUNTOS')

    # ---- alternativas (mínimos locales baratos no elegidos) para ajuste manual
    alternativas = []
    for lado in ('IZQ', 'DER'):
        v = costo[lado]; sgn = -1.0 if lado == 'IZQ' else 1.0; borde = bi if lado == 'IZQ' else bd
        umbral = np.nanpercentile(v, 10)
        win = int(round((a.largo + 2 * a.transicion) / a.paso))
        for i in range(win, len(sta) - win):
            if not np.isfinite(v[i]) or v[i] > umbral:
                continue
            if v[i] > np.nanmin(np.where(np.isfinite(v[i - win:i + win + 1]), v[i - win:i + win + 1], np.inf)):
                continue
            if any(abs(sta[i] - e['sta']) < a.largo + 2 * a.transicion for e in ens if e['lado'] == lado):
                continue
            c = sta[i]; ss = np.arange(c - half - a.transicion, c + half + a.transicion + 0.01, 2.5)
            d0 = np.maximum(np.nan_to_num(np.abs(offsets_borde(eje, borde, ss)), nan=3.30), 3.30) + a.berma
            wss = a.ancho * np.clip((half + a.transicion - np.abs(ss - c)) / a.transicion, 0, 1)
            xi, yi = eje.offset_points(ss, sgn * d0); xo, yo = eje.offset_points(ss, sgn * (d0 + wss))
            dxf.polyline(list(zip(xi, yi)) + list(zip(xo[::-1], yo[::-1])), 'ENSANCHE_ALTERNATIVAS', closed=True)
            pc = eje.offset_points(np.array([c]), np.array([sgn * (d0[len(d0) // 2] + a.ancho + 2.0)]))
            dxf.text((pc[0][0], pc[1][0]), 'ALT %s km %s +%.0f m3' % (lado, km(c), v[i]), 'ENSANCHE_ALTERNATIVAS', h=1.5)
            alternativas.append(dict(lado=lado, sta=float(c), km=km(c), vol_add=float(v[i]), vol_corte=float(vol_corte[lado][i]), vol_relleno=float(vol_rell[lado][i])))

    # ---- archivos
    base = os.path.join(a.salida, 'ensanches_plataforma')
    dxf.write(base + '.dxf')
    escribir_landxml(base + '.xml', d['crs'], ens, puntos)
    with open(base + '_puntos_PNEZD.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        for n, (nm, code, desc, x, y, z) in enumerate(puntos, 1):
            w.writerow([n, '%.4f' % y, '%.4f' % x, '%.3f' % z, '%s %s' % (nm, desc)])
    cols = ['orden', 'nombre', 'lado', 'km', 'sta', 'sta_ini_trans', 'sta_ini', 'sta_fin', 'sta_fin_trans', 'x', 'y', 'z_ras', 'd0', 'ancho_plataforma_ens', 'vol_add', 'corte_add', 'relleno_add', 'h_borde', 'pend_terreno', 'seccion', 'r_min', 'tin_extrapolado']
    with open(base + '_tabla.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow([{'x': 'x_este', 'y': 'y_norte'}.get(c, c) for c in cols])
        for e in sorted(ens, key=lambda e: (e['lado'] != 'IZQ', e['sta'])):      # primero todos los IZQ, luego los DER
            w.writerow([e['n'], e['nombre'], e['lado'], e['km']] + ['%.2f' % e[c] if isinstance(e[c], float) else e[c] for c in cols[4:]])
    with open(base + '_costo_por_progresiva.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['sta', 'km', 'x_este', 'y_norte', 'R_min_nucleo', 'd0_izq', 'area_corte_izq', 'area_relleno_izq', 'vol_ensanche_izq', 'd0_der', 'area_corte_der', 'area_relleno_der', 'vol_ensanche_der'])
        for i in range(len(sta)):
            w.writerow(['%.1f' % sta[i], km(sta[i]), '%.3f' % res['x'][i], '%.3f' % res['y'][i], '%.0f' % rmin_core[i] if np.isfinite(rmin_core[i]) else 'tangente'] +
                       sum([['%.2f' % res[l]['d0'][i], ('%.2f' % res[l]['corte_add'][i]) if np.isfinite(res[l]['corte_add'][i]) else '', ('%.2f' % res[l]['relleno_add'][i]) if np.isfinite(res[l]['relleno_add'][i]) else '', ('%.0f' % costo[l][i]) if np.isfinite(costo[l][i]) else ''] for l in ('IZQ', 'DER')], []))
    x, y, _, _ = eje.locate(sta)
    escribir_svg(base + '_vista_previa.svg', (x, y), ens, sta, costo, [i for i, _ in seq], eje.length)
    with open(base + '_resumen.json', 'w', encoding='utf-8') as f:
        json.dump(dict(parametros=vars(a), seccion=PARAM, total_m3=total, ensanches=[{k: v for k, v in e.items() if k != 'poligono'} for e in ens], alternativas=alternativas), f, ensure_ascii=False, indent=1)
    print('Archivos escritos en', os.path.abspath(a.salida))
    print('\n %-3s %-6s %-4s %-12s %-22s %8s %8s %8s %7s %7s %-8s %s' % ('Ord', 'Nombre', 'Lado', 'km centro', 'tramo (inicio-fin trans.)', 'Vol m3', 'Corte', 'Relleno', 'h bor.', 'Rmin', 'Secc.', 'TIN ext.'))
    for e in ens:
        print(' %-3d %-6s %-4s %-12s %-22s %8.0f %8.0f %8.0f %7.2f %7s %-8s %s' % (e['n'], e['nombre'], e['lado'], e['km'], '%s - %s' % (km(e['sta_ini_trans']), km(e['sta_fin_trans'])), e['vol_add'], e['corte_add'], e['relleno_add'], e['h_borde'], ('%.0f' % e['r_min']) if e['r_min'] else 'tang.', e['seccion'], 'si' if e['tin_extrapolado'] else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
