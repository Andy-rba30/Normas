# -*- coding: utf-8 -*-
"""
Lectura de un LandXML 1.2 exportado por Civil 3D para análisis vial:
  - alineamientos (Line / Curve) con función progresiva -> (E, N, azimut, curvatura)
  - perfil de diseño (ProfAlign con PVI / ParaCurve) -> cota de rasante
  - superficie TIN (Pnts / Faces) con consulta vectorizada de cotas
Convención interna: x = Este, y = Norte; el LandXML escribe "Norte Este".
"""
import math
import xml.etree.ElementTree as ET
import numpy as np

NS = {'l': 'http://www.landxml.org/schema/LandXML-1.2'}


def _pt(text):
    n, e = text.split()[:2]
    return float(e), float(n)          # (x=E, y=N)


# ----------------------------------------------------------------------------- alineamiento
class Alineamiento:
    def __init__(self, el):
        self.name = el.get('name')
        self.length = float(el.get('length'))
        sta = float(el.get('staStart', '0') or 0)
        self.sta0 = sta
        segs = []
        for g in el.find('l:CoordGeom', NS):
            tag = g.tag.split('}')[1]
            if tag == 'Line':
                p0 = _pt(g.find('l:Start', NS).text)
                p1 = _pt(g.find('l:End', NS).text)
                L = float(g.get('length') or math.dist(p0, p1))
                segs.append(('L', sta, L, p0, p1, None, 0.0, 0.0))
            elif tag == 'Curve':
                p0 = _pt(g.find('l:Start', NS).text)
                c = _pt(g.find('l:Center', NS).text)
                p1 = _pt(g.find('l:End', NS).text)
                R = float(g.get('radius'))
                L = float(g.get('length'))
                rot = 1.0 if g.get('rot') == 'ccw' else -1.0
                segs.append(('C', sta, L, p0, p1, c, R, rot))
            else:
                raise NotImplementedError('Elemento no soportado en CoordGeom: ' + tag)
            sta += L
        self.segs = segs
        self.sta_ini = np.array([s[1] for s in segs])
        self.sta_fin = sta

    def locate(self, sta):
        """sta: array -> x, y, theta (rad, antihorario desde el Este), curvatura (1/R con signo, +izq)"""
        sta = np.asarray(sta, dtype=float)
        idx = np.clip(np.searchsorted(self.sta_ini, sta, side='right') - 1, 0, len(self.segs) - 1)
        x = np.empty_like(sta); y = np.empty_like(sta); th = np.empty_like(sta); k = np.zeros_like(sta)
        for i in np.unique(idx):
            m = idx == i
            typ, s0, L, p0, p1, c, R, rot = self.segs[i]
            ds = sta[m] - s0
            if typ == 'L':
                dx, dy = p1[0] - p0[0], p1[1] - p0[1]
                ang = math.atan2(dy, dx)
                x[m] = p0[0] + ds * math.cos(ang)
                y[m] = p0[1] + ds * math.sin(ang)
                th[m] = ang
            else:
                a0 = math.atan2(p0[1] - c[1], p0[0] - c[0])
                a = a0 + rot * ds / R
                x[m] = c[0] + R * np.cos(a)
                y[m] = c[1] + R * np.sin(a)
                th[m] = a + rot * math.pi / 2
                k[m] = rot / R
        return x, y, th, k

    def offset_points(self, sta, off):
        """Punto a 'off' metros del eje (positivo a la derecha en el sentido de avance)."""
        x, y, th, _ = self.locate(sta)
        off = np.asarray(off, dtype=float)
        return x + off * np.sin(th), y - off * np.cos(th)


# ----------------------------------------------------------------------------- perfil (rasante)
class Rasante:
    def __init__(self, prof_align_el):
        pvis = []
        for ch in prof_align_el:
            tag = ch.tag.split('}')[1]
            s, z = [float(v) for v in ch.text.split()[:2]]
            if tag == 'PVI':
                pvis.append((s, z, 0.0))
            elif tag == 'ParaCurve':
                pvis.append((s, z, float(ch.get('length'))))
            else:
                raise NotImplementedError('Elemento de perfil no soportado: ' + tag)
        self.s = np.array([p[0] for p in pvis]); self.z = np.array([p[1] for p in pvis]); self.L = np.array([p[2] for p in pvis])
        self.g = np.diff(self.z) / np.diff(self.s)          # pendiente de cada tangente i (entre PVI i e i+1)
        self.name = prof_align_el.get('name')

    def elev(self, sta):
        sta = np.asarray(sta, dtype=float)
        i = np.clip(np.searchsorted(self.s, sta, side='right') - 1, 0, len(self.g) - 1)
        z = self.z[i] + self.g[i] * (sta - self.s[i])          # tangente
        # curva vertical del PVI i (lado de salida)
        for j in range(1, len(self.s) - 1):
            if self.L[j] <= 0:
                continue
            a, b = self.s[j] - self.L[j] / 2, self.s[j] + self.L[j] / 2
            m = (sta >= a) & (sta <= b)
            if not m.any():
                continue
            g1, g2 = self.g[j - 1], self.g[j]
            zb = self.z[j] - g1 * self.L[j] / 2
            xx = sta[m] - a
            z[m] = zb + g1 * xx + (g2 - g1) * xx ** 2 / (2 * self.L[j])
        return z

    def grade(self, sta):
        sta = np.asarray(sta, dtype=float)
        i = np.clip(np.searchsorted(self.s, sta, side='right') - 1, 0, len(self.g) - 1)
        g = self.g[i].copy()
        for j in range(1, len(self.s) - 1):
            if self.L[j] <= 0:
                continue
            a, b = self.s[j] - self.L[j] / 2, self.s[j] + self.L[j] / 2
            m = (sta >= a) & (sta <= b)
            if m.any():
                g[m] = self.g[j - 1] + (self.g[j] - self.g[j - 1]) * (sta[m] - a) / self.L[j]
        return g


# ----------------------------------------------------------------------------- superficie TIN
class SuperficieTIN:
    def __init__(self, surf_el, cell=25.0):
        self.name = surf_el.get('name')
        d = surf_el.find('l:Definition', NS)
        pts = {}
        for p in d.find('l:Pnts', NS):
            n, e, z = [float(v) for v in p.text.split()[:3]]
            pts[int(p.get('id'))] = (e, n, z)
        maxid = max(pts) + 1
        P = np.full((maxid, 3), np.nan)
        for i, v in pts.items():
            P[i] = v
        tri = []
        for f in d.find('l:Faces', NS):
            if f.get('i') == '1':          # cara invisible
                continue
            tri.append([int(v) for v in f.text.split()[:3]])
        self.tri = np.array(tri, dtype=np.int64)
        self.P = P
        T = P[self.tri]                      # (nt, 3, 3)
        self.T = T
        self.cell = cell
        self.x0 = np.nanmin(T[:, :, 0]); self.y0 = np.nanmin(T[:, :, 1])
        xmin = ((T[:, :, 0].min(axis=1) - self.x0) // cell).astype(int)
        xmax = ((T[:, :, 0].max(axis=1) - self.x0) // cell).astype(int)
        ymin = ((T[:, :, 1].min(axis=1) - self.y0) // cell).astype(int)
        ymax = ((T[:, :, 1].max(axis=1) - self.y0) // cell).astype(int)
        grid = {}
        for t in range(len(self.tri)):
            for cx in range(xmin[t], xmax[t] + 1):
                for cy in range(ymin[t], ymax[t] + 1):
                    grid.setdefault((cx, cy), []).append(t)
        self.grid = {k: np.array(v) for k, v in grid.items()}
        # precálculo para baricéntricas
        self.ax = T[:, 0, 0]; self.ay = T[:, 0, 1]
        self.v0x = T[:, 1, 0] - self.ax; self.v0y = T[:, 1, 1] - self.ay
        self.v1x = T[:, 2, 0] - self.ax; self.v1y = T[:, 2, 1] - self.ay
        self.den = self.v0x * self.v1y - self.v1x * self.v0y

    def elev(self, x, y, tol=1e-6):
        x = np.asarray(x, dtype=float).ravel(); y = np.asarray(y, dtype=float).ravel()
        z = np.full(x.shape, np.nan)
        okq = np.isfinite(x) & np.isfinite(y)
        cx = np.where(okq, (np.nan_to_num(x) - self.x0) // self.cell, -1e9).astype(np.int64); cy = np.where(okq, (np.nan_to_num(y) - self.y0) // self.cell, -1e9).astype(np.int64)
        key = cx.astype(np.int64) * 1000003 + cy
        uk, inv = np.unique(key, return_inverse=True)
        for u_i, u in enumerate(uk):
            qi = np.nonzero(inv == u_i)[0]
            cand = self.grid.get((int(cx[qi[0]]), int(cy[qi[0]])))
            if cand is None:
                continue
            qx = x[qi][:, None] - self.ax[cand][None, :]
            qy = y[qi][:, None] - self.ay[cand][None, :]
            den = self.den[cand][None, :]
            l1 = (qx * self.v1y[cand][None, :] - self.v1x[cand][None, :] * qy) / den
            l2 = (self.v0x[cand][None, :] * qy - qx * self.v0y[cand][None, :]) / den
            inside = (l1 >= -tol) & (l2 >= -tol) & (l1 + l2 <= 1 + tol)
            has = inside.any(axis=1)
            if not has.any():
                continue
            first = inside.argmax(axis=1)
            r = np.nonzero(has)[0]
            t = np.asarray(cand)[first[r]]
            l1r = l1[r, first[r]]; l2r = l2[r, first[r]]
            Tz = self.T[t]
            z[qi[r]] = Tz[:, 0, 2] + l1r * (Tz[:, 1, 2] - Tz[:, 0, 2]) + l2r * (Tz[:, 2, 2] - Tz[:, 0, 2])
        return z


# ----------------------------------------------------------------------------- lectura
def leer_landxml(path):
    root = ET.parse(path).getroot()
    out = {'alineamientos': {}, 'rasantes': {}, 'superficies': {}, 'crs': None, 'units': None}
    cs = root.find('l:CoordinateSystem', NS)
    if cs is not None:
        out['crs'] = dict(cs.attrib)
    for al in root.iter('{%s}Alignment' % NS['l']):
        out['alineamientos'][al.get('name')] = Alineamiento(al)
        for pa in al.iter('{%s}ProfAlign' % NS['l']):
            out['rasantes'][(al.get('name'), pa.get('name'))] = Rasante(pa)
    for su in root.iter('{%s}Surface' % NS['l']):
        out['superficies'][su.get('name')] = SuperficieTIN(su)
    return out
