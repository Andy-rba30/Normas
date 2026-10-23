# -*- coding: utf-8 -*-
"""Escritura de salidas: DXF R12 (sin dependencias), LandXML (CgPoints + Parcels), CSV, SVG."""
import math
import numpy as np
import xml.etree.ElementTree as ET


def km(sta):
    return '%d+%06.2f' % (int(sta // 1000), sta % 1000)


# ----------------------------------------------------------------------------- DXF (AC1009 / R12)
class DXF:
    LAYERS = [  # nombre, color ACI
        ('ENSANCHE_IZQ', 1), ('ENSANCHE_DER', 5), ('ENSANCHE_NUCLEO', 3), ('ENSANCHE_BORDE_3D', 6),
        ('ENSANCHE_TEXTO', 2), ('ENSANCHE_PUNTOS', 4), ('ENSANCHE_ALTERNATIVAS', 8), ('ENSANCHE_MARCA', 1),
    ]

    def __init__(self):
        self.ent = []
        self.ext = [np.inf, np.inf, -np.inf, -np.inf]

    def _upd(self, x, y):
        self.ext[0] = min(self.ext[0], x); self.ext[1] = min(self.ext[1], y)
        self.ext[2] = max(self.ext[2], x); self.ext[3] = max(self.ext[3], y)

    def polyline(self, pts, layer, closed=False, is3d=False):
        flag = (1 if closed else 0) | (8 if is3d else 0)
        e = ['0\nPOLYLINE\n8\n%s\n66\n1\n70\n%d\n10\n0.0\n20\n0.0\n30\n0.0\n' % (layer, flag)]
        for p in pts:
            z = p[2] if len(p) > 2 else 0.0
            e.append('0\nVERTEX\n8\n%s\n10\n%.4f\n20\n%.4f\n30\n%.4f\n%s' % (layer, p[0], p[1], z, '70\n32\n' if is3d else ''))
            self._upd(p[0], p[1])
        e.append('0\nSEQEND\n8\n%s\n' % layer)
        self.ent.append(''.join(e))

    def line(self, p, q, layer):
        self.ent.append('0\nLINE\n8\n%s\n10\n%.4f\n20\n%.4f\n30\n0.0\n11\n%.4f\n21\n%.4f\n31\n0.0\n' % (layer, p[0], p[1], q[0], q[1]))
        self._upd(p[0], p[1]); self._upd(q[0], q[1])

    def text(self, p, txt, layer, h=2.5, rot=0.0):
        self.ent.append('0\nTEXT\n8\n%s\n10\n%.4f\n20\n%.4f\n30\n0.0\n40\n%.3f\n1\n%s\n50\n%.4f\n' % (layer, p[0], p[1], h, txt, rot))
        self._upd(p[0], p[1])

    def circle(self, p, r, layer):
        self.ent.append('0\nCIRCLE\n8\n%s\n10\n%.4f\n20\n%.4f\n30\n0.0\n40\n%.4f\n' % (layer, p[0], p[1], r))
        self._upd(p[0] - r, p[1] - r); self._upd(p[0] + r, p[1] + r)

    def point(self, p, layer):
        z = p[2] if len(p) > 2 else 0.0
        self.ent.append('0\nPOINT\n8\n%s\n10\n%.4f\n20\n%.4f\n30\n%.4f\n' % (layer, p[0], p[1], z))

    def write(self, path):
        out = ['0\nSECTION\n2\nHEADER\n9\n$ACADVER\n1\nAC1009\n9\n$DWGCODEPAGE\n3\nANSI_1252\n9\n$INSBASE\n10\n0.0\n20\n0.0\n30\n0.0\n']
        out.append('9\n$EXTMIN\n10\n%.3f\n20\n%.3f\n30\n0.0\n9\n$EXTMAX\n10\n%.3f\n20\n%.3f\n30\n0.0\n9\n$PDMODE\n70\n35\n9\n$PDSIZE\n40\n1.0\n0\nENDSEC\n' % tuple(self.ext))
        out.append('0\nSECTION\n2\nTABLES\n0\nTABLE\n2\nLTYPE\n70\n1\n0\nLTYPE\n2\nCONTINUOUS\n70\n0\n3\nSolid line\n72\n65\n73\n0\n40\n0.0\n0\nENDTAB\n')
        out.append('0\nTABLE\n2\nLAYER\n70\n%d\n' % (len(self.LAYERS) + 1))
        out.append('0\nLAYER\n2\n0\n70\n0\n62\n7\n6\nCONTINUOUS\n')
        for nm, col in self.LAYERS:
            out.append('0\nLAYER\n2\n%s\n70\n0\n62\n%d\n6\nCONTINUOUS\n' % (nm, col))
        out.append('0\nENDTAB\n0\nENDSEC\n0\nSECTION\n2\nENTITIES\n')
        out.extend(self.ent)
        out.append('0\nENDSEC\n0\nEOF\n')
        with open(path, 'w', encoding='cp1252', errors='replace', newline='\r\n') as f:
            f.write(''.join(out))


# ----------------------------------------------------------------------------- LandXML
def escribir_landxml(path, crs, ensanches, puntos):
    """ensanches: lista de dicts con 'nombre', 'poligono' [(x,y),...]; puntos: lista de (nombre, codigo, desc, x, y, z)."""
    NSU = 'http://www.landxml.org/schema/LandXML-1.2'
    ET.register_namespace('', NSU)
    import datetime
    now = datetime.datetime.now()
    root = ET.Element('{%s}LandXML' % NSU, {'date': now.strftime('%Y-%m-%d'), 'time': now.strftime('%H:%M:%S'), 'version': '1.2', 'language': 'Spanish', 'readOnly': 'false'})
    u = ET.SubElement(root, '{%s}Units' % NSU)
    ET.SubElement(u, '{%s}Metric' % NSU, {'areaUnit': 'squareMeter', 'linearUnit': 'meter', 'volumeUnit': 'cubicMeter', 'temperatureUnit': 'celsius', 'pressureUnit': 'milliBars', 'angularUnit': 'decimal degrees', 'directionUnit': 'decimal degrees'})
    if crs:
        ET.SubElement(root, '{%s}CoordinateSystem' % NSU, crs)
    ET.SubElement(root, '{%s}Application' % NSU, {'name': 'ensanches_plataforma.py', 'desc': 'Ubicacion de ensanches de plataforma DG-2018 Tabla 304.12', 'manufacturer': '-', 'version': '1.0'})
    cg = ET.SubElement(root, '{%s}CgPoints' % NSU, {'name': 'ENSANCHES_PLATAFORMA', 'desc': 'Puntos de ensanches (borde exterior)'})
    for nombre, code, desc, x, y, z in puntos:
        p = ET.SubElement(cg, '{%s}CgPoint' % NSU, {'name': nombre, 'code': code, 'desc': desc})
        p.text = '%.4f %.4f %.3f' % (y, x, z)
    pa = ET.SubElement(root, '{%s}Parcels' % NSU, {'name': 'ENSANCHES_PLATAFORMA', 'desc': 'Huella de ensanches (nucleo + transiciones)'})
    for e in ensanches:
        poly = e['poligono']
        area = 0.5 * abs(sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1] for i in range(len(poly))))
        par = ET.SubElement(pa, '{%s}Parcel' % NSU, {'name': e['nombre'], 'desc': e['desc'], 'area': '%.3f' % area, 'parcelType': 'ensanche'})
        c = ET.SubElement(par, '{%s}CoordGeom' % NSU)
        for i in range(len(poly)):
            a, b = poly[i], poly[(i + 1) % len(poly)]
            ln = ET.SubElement(c, '{%s}Line' % NSU)
            ET.SubElement(ln, '{%s}Start' % NSU).text = '%.4f %.4f' % (a[1], a[0])
            ET.SubElement(ln, '{%s}End' % NSU).text = '%.4f %.4f' % (b[1], b[0])
    ET.ElementTree(root).write(path, encoding='utf-8', xml_declaration=True)


# ----------------------------------------------------------------------------- SVG
def escribir_svg(path, eje_xy, ensanches, sta, costo, sel_idx, L):
    W = 1400
    xs, ys = eje_xy
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    pw = W - 80
    ph = int(min(820, max(300, pw * (y1 - y0) / (x1 - x0 + 1e-9))))
    sc = min(pw / (x1 - x0 + 1e-9), ph / (y1 - y0 + 1e-9))
    def tx(x): return 40 + (x - x0) * sc
    def ty(y): return 40 + (y1 - y) * sc
    H = ph + 100 + 500 + 60
    s = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" font-family="sans-serif" font-size="12">' % (W, H, W, H),
         '<rect width="100%" height="100%" fill="white"/>',
         '<text x="40" y="24" font-size="16" font-weight="bold">Ensanches de plataforma (DG-2018 Tabla 304.12) - planta (UTM 17S)</text>']
    pts = ' '.join('%.1f,%.1f' % (tx(x), ty(y)) for x, y in zip(xs[::4], ys[::4]))
    s.append('<polyline points="%s" fill="none" stroke="#555" stroke-width="1.2"/>' % pts)
    for k in range(0, int(L) + 1, 1000):
        i = min(int(k / (sta[1] - sta[0])), len(xs) - 1)
        s.append('<circle cx="%.1f" cy="%.1f" r="2" fill="#555"/><text x="%.1f" y="%.1f" font-size="9" fill="#555">%d</text>' % (tx(xs[i]), ty(ys[i]), tx(xs[i]) + 3, ty(ys[i]) - 3, k // 1000))
    for e in ensanches:
        col = '#d62728' if e['lado'] == 'IZQ' else '#1f77b4'
        cx, cy = tx(e['x']), ty(e['y'])
        s.append('<circle cx="%.1f" cy="%.1f" r="6" fill="%s" fill-opacity="0.85" stroke="black" stroke-width="0.5"/>' % (cx, cy, col))
        s.append('<text x="%.1f" y="%.1f" font-size="10" font-weight="bold" fill="%s">%s %s</text>' % (cx + 8, cy + 4, col, e['nombre'], km(e['sta'])))
    s.append('<text x="40" y="%d" font-size="12">Rojo = lado IZQUIERDO, Azul = lado DERECHO (sentido de progresivas crecientes)</text>' % (ph + 60))
    # perfil de costos
    top, hgt = ph + 100, 500
    s.append('<text x="40" y="%d" font-size="14" font-weight="bold">Volumen adicional estimado de un ensanche (2.5 x 25 m + transiciones) en cada progresiva [m3]</text>' % (top - 10))
    vmax = 600.0
    def px(st): return 40 + st / L * (W - 80)
    def py(v): return top + hgt - min(v, vmax) / vmax * hgt
    s.append('<rect x="40" y="%d" width="%d" height="%d" fill="none" stroke="#999"/>' % (top, W - 80, hgt))
    for v in (0, 100, 200, 300, 400, 500, 600):
        s.append('<line x1="40" y1="%.1f" x2="%d" y2="%.1f" stroke="#eee"/><text x="4" y="%.1f" font-size="9">%d</text>' % (py(v), W - 40, py(v), py(v) + 3, v))
    for k in range(0, int(L) + 1, 1000):
        s.append('<text x="%.1f" y="%d" font-size="9" text-anchor="middle">%d</text>' % (px(k), top + hgt + 12, k // 1000))
    for lado, col in (('IZQ', '#d62728'), ('DER', '#1f77b4')):
        v = costo[lado]
        seg = []
        for i in range(len(sta)):
            if np.isfinite(v[i]):
                seg.append('%.1f,%.1f' % (px(sta[i]), py(v[i])))
            else:
                if len(seg) > 1:
                    s.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="0.8" stroke-opacity="0.7"/>' % (' '.join(seg), col))
                seg = []
        if len(seg) > 1:
            s.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="0.8" stroke-opacity="0.7"/>' % (' '.join(seg), col))
    for e in ensanches:
        col = '#d62728' if e['lado'] == 'IZQ' else '#1f77b4'
        s.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.5" stroke-dasharray="4 3"/>' % (px(e['sta']), top, px(e['sta']), top + hgt, col))
        s.append('<text x="%.1f" y="%d" font-size="9" text-anchor="middle" fill="%s">%s</text>' % (px(e['sta']), top - 2 if e['lado'] == 'IZQ' else top + hgt + 24, col, e['nombre']))
    s.append('<text x="40" y="%d" font-size="11">km (eje "eje 01"); tramos sin curva = sin candidato (nucleo en curva R &lt; R min, sin empalme de talud o fuera del TIN)</text>' % (top + hgt + 40))
    s.append('</svg>')
    open(path, 'w', encoding='utf-8').write('\n'.join(s))
