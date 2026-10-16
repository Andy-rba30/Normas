#!/usr/bin/env python3
"""Genera un DXF (R2000) con el eje corregido como POLILINEA CON ARCOS (bulges), para
'Crear alineación a partir de objetos' en Civil 3D sin tener que teclear los radios.

La geometría se reconstruye por el método del PI (PC = PI - T·uin, PT = PI + T·uout,
T = R·tan(Δ/2)) a partir de los PIs y radios del modelo, de modo que cada arco es
EXACTAMENTE tangente a las dos alineaciones de PIs vecinas (doble precisión).

Capas:
  EJE          polilínea del eje: tangentes + arcos circulares con su radio exacto
  EJE-PI       polilínea solo por los PIs (alternativa: 'Añadir curvas entre tangentes' + radios del CSV)
  EJE-PI-TXT   texto en cada PI: C-n R=xx
Uso: python3 write_dxf.py <model.pkl> <salida.dxf> [LandXML de referencia para verificar]
(el modelo se carga con write_outputs.load, que absorbe las tangentes residuales igual que al escribir el LandXML)
"""
import sys, os, math, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import ezdxf
from ezdxf.enums import TextEntityAlignment
import write_outputs

TOL_ZERO = 1e-4   # tangentes menores a 0.1 mm se consideran nulas (curvas compuestas / en S pegadas)

def unit(v):
    v = np.asarray(v, float); return v / np.linalg.norm(v)

def pi_geometry(m):
    """por cada curva: PI, PC, PT, R, delta, left, bulge (convención AutoCAD: + antihorario)"""
    cs = m['curves']; els = m['els']
    nodes = [np.asarray(els[0]['A'], float)] + [np.asarray(c['PI'], float) for c in cs] + [np.asarray(els[-1]['B'], float)]
    out = []
    for i, c in enumerate(cs):
        uin = unit(nodes[i + 1] - nodes[i]); uout = unit(nodes[i + 2] - nodes[i + 1])
        cross = uin[0] * uout[1] - uin[1] * uout[0]
        delta = math.acos(max(-1.0, min(1.0, float(np.dot(uin, uout)))))
        R = float(c['R']); T = R * math.tan(delta / 2.0)
        left = cross > 0
        n = np.array([-uin[1], uin[0]]) if left else np.array([uin[1], -uin[0]])
        PC = nodes[i + 1] - T * uin; PT = nodes[i + 1] + T * uout
        out.append(dict(n=i + 1, PI=nodes[i + 1], uin=uin, uout=uout, R=R, delta=delta, left=left, T=T, n_=n))
    # tangentes nulas (curvas compuestas / S pegadas): escalar ambos radios para que T1 + T2 = D exactamente
    # (cambio relativo ~1e-8, micras) y así el PT de una curva coincide con el PC de la siguiente sin quiebre
    for i in range(len(out) - 1):
        D = float(np.linalg.norm(nodes[i + 2] - nodes[i + 1])); s = out[i]['T'] + out[i + 1]['T']
        if abs(D - s) <= TOL_ZERO and abs(D - s) > 0:
            f = D / s
            for g in (out[i], out[i + 1]):
                g['R'] *= f; g['T'] *= f
    for g in out:
        g['PC'] = g['PI'] - g['T'] * g['uin']; g['PT'] = g['PI'] + g['T'] * g['uout']
        g['C'] = g['PC'] + g['R'] * g['n_']; g['bulge'] = (1 if g['left'] else -1) * math.tan(g['delta'] / 4.0); g['L'] = g['R'] * g['delta']
    return nodes, out

def build_vertices(nodes, G):
    """lista de [x, y, bulge]; el bulge va en el vértice donde EMPIEZA el arco"""
    V = []; merged = 0
    def push(p):
        nonlocal merged
        if V and math.hypot(V[-1][0] - p[0], V[-1][1] - p[1]) <= TOL_ZERO:
            merged += 1; return
        V.append([float(p[0]), float(p[1]), 0.0])
    push(nodes[0])
    for g in G:
        push(g['PC']); V[-1][2] = g['bulge']; push(g['PT'])
    push(nodes[-1])
    return V, merged

def arc_from_bulge(p1, p2, b):
    """reconstruye centro, radio y longitud de un tramo (p1, p2, bulge) con la convención de AutoCAD"""
    p1 = np.asarray(p1, float); p2 = np.asarray(p2, float)
    theta = 4.0 * math.atan(b); c = float(np.linalg.norm(p2 - p1))
    R = abs(c / (2.0 * math.sin(theta / 2.0)))
    u = (p2 - p1) / c; n_left = np.array([-u[1], u[0]])
    C = (p1 + p2) / 2.0 + n_left * (c / 2.0) / math.tan(theta / 2.0)
    return C, R, abs(theta) * R

def main(model_pkl, out_dxf, ref_xml=None):
    m = write_outputs.load(model_pkl)
    if any(e['type'] == 'Spiral' for e in m['els']):
        raise SystemExit('Este escritor solo admite ejes circulares (sin clotoides)')
    nodes, G = pi_geometry(m)
    # control: la reconstrucción por PI debe coincidir con los elementos del modelo (y del LandXML)
    curv = [e for e in m['els'] if e['type'] == 'Curve']
    dev = max(max(np.linalg.norm(g['PC'] - np.asarray(e['A'])), np.linalg.norm(g['PT'] - np.asarray(e['B']))) for g, e in zip(G, curv))
    dR = max(abs(g['R'] - float(c['R'])) for g, c in zip(G, m['curves']))
    V, merged = build_vertices(nodes, G)

    doc = ezdxf.new('R2000', setup=True)
    doc.header['$INSUNITS'] = 6          # metros
    doc.header['$MEASUREMENT'] = 1
    doc.layers.add('EJE', color=1); doc.layers.add('EJE-PI', color=4); doc.layers.add('EJE-PI-TXT', color=2)
    msp = doc.modelspace()
    msp.add_lwpolyline([(x, y, b) for x, y, b in V], format='xyb', dxfattribs={'layer': 'EJE'})
    msp.add_lwpolyline([(float(p[0]), float(p[1])) for p in nodes], format='xy', dxfattribs={'layer': 'EJE-PI'})
    for g in G:
        t = msp.add_text(f"C-{g['n']} R={g['R']:.0f}", height=3.0, dxfattribs={'layer': 'EJE-PI-TXT'})
        t.set_placement((float(g['PI'][0]), float(g['PI'][1])), align=TextEntityAlignment.MIDDLE_CENTER)
    doc.saveas(out_dxf)

    # verificación: releer el DXF, reconstruir cada arco desde su bulge y comparar con la geometría de PI
    doc2 = ezdxf.readfile(out_dxf)
    lw = [e for e in doc2.modelspace().query('LWPOLYLINE') if e.dxf.layer == 'EJE'][0]
    pts = list(lw.get_points(format='xyb'))
    k = 0; Ltot = 0.0; wC = wR = wT = 0.0; prev = None
    for (x1, y1, b), (x2, y2, _) in zip(pts, pts[1:]):
        p1 = np.array([x1, y1]); p2 = np.array([x2, y2])
        if abs(b) < 1e-12:
            L = float(np.linalg.norm(p2 - p1)); d0 = d1 = (p2 - p1) / L
        else:
            C, R, L = arc_from_bulge(p1, p2, b); g = G[k]; k += 1
            wC = max(wC, float(np.linalg.norm(C - g['C']))); wR = max(wR, abs(R - g['R']))
            s = 1.0 if b > 0 else -1.0; r1 = p1 - C; r2 = p2 - C
            d0 = s * np.array([-r1[1], r1[0]]) / R; d1 = s * np.array([-r2[1], r2[0]]) / R
        if prev is not None:   # ángulo con atan2 (acos amplifica errores de 1e-10 en la norma)
            wT = max(wT, abs(math.degrees(math.atan2(prev[0] * d0[1] - prev[1] * d0[0], float(np.dot(prev, d0))))))
        prev = d1; Ltot += L
    print(f'DXF: {out_dxf}')
    print(f'  vertices: {len(pts)}  arcos: {k}/{len(G)}  tangentes nulas fusionadas: {merged}')
    print(f'  desvio PC/PT respecto al modelo/LandXML: {dev*1000:.4f} mm   ajuste max de radio: {dR*1e6:.3f} um')
    print(f'  longitud polilinea: {Ltot:.3f} m  (modelo: {m["Ltot"]:.3f} m)')
    print(f'  error max centro: {wC*1e6:.3f} um   error max radio: {wR*1e6:.3f} um   quiebre max de tangencia: {wT:.2e} deg')
    assert k == len(G) and dev < 1e-3 and wC < 1e-4 and wR < 1e-4 and wT < 1e-4 and abs(Ltot - m['Ltot']) < 0.01
    if ref_xml:   # comparar con las curvas del LandXML entregado (coordenadas a 6 decimales)
        import xml.etree.ElementTree as ET
        ns = {'l': 'http://www.landxml.org/schema/LandXML-1.2'}
        cg = ET.parse(ref_xml).getroot().find('.//l:CoordGeom', ns)
        def pt(t): a = [float(v) for v in t.split()]; return np.array([a[1], a[0]])
        xc = [(pt(e.find('l:Start', ns).text), pt(e.find('l:End', ns).text), pt(e.find('l:Center', ns).text), float(e.get('radius')))
              for e in cg if e.tag.endswith('Curve')]
        assert len(xc) == len(G)
        dx = max(max(np.linalg.norm(a - g['PC']), np.linalg.norm(b - g['PT']), np.linalg.norm(c - g['C']), abs(R - g['R'])) for (a, b, c, R), g in zip(xc, G))
        print(f'  desvio max respecto a {os.path.basename(ref_xml)}: {dx*1000:.4f} mm')
        assert dx < 1e-4

if __name__ == '__main__':
    main(*sys.argv[1:4])
