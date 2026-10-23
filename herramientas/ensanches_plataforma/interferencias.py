# -*- coding: utf-8 -*-
"""
Interferencias (viviendas, cercos, postes, canales, etc.) tomadas de un DXF (p. ej. el DWG del proyecto
convertido con dwg2dxf de LibreDWG o exportado desde Civil 3D) y proyectadas al eje como (progresiva, offset).
"""
import math
import numpy as np


def _densificar(pts, paso, cerrado):
    out = []
    n = len(pts)
    rng = range(n) if cerrado else range(n - 1)
    for i in rng:
        a = pts[i]; b = pts[(i + 1) % n]
        d = math.dist(a, b)
        k = max(1, int(d / paso))
        for j in range(k):
            t = j / k
            out.append((a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])))
    if not cerrado and n:
        out.append(tuple(pts[-1][:2]))
    return out


def cargar_interferencias(dxf_path, capas, paso=1.0, patrones=None):
    """Devuelve lista de dicts {capa, tipo, handle, pts[(x,y)...]} para las entidades de las capas indicadas.
    capas: lista de nombres exactos (sin distinguir mayúsculas); patrones: subcadenas a buscar en el nombre de capa."""
    import ezdxf
    from ezdxf import recover
    try:
        doc = ezdxf.readfile(dxf_path)
    except Exception:
        doc, _ = recover.readfile(dxf_path)
    capas_u = {c.upper() for c in capas}
    patrones = [p.upper() for p in (patrones or [])]
    ents = []
    for e in doc.modelspace():
        lay = e.dxf.layer
        lu = lay.upper()
        if lu not in capas_u and not any(p in lu for p in patrones):
            continue
        t = e.dxftype()
        pts = None; cerrado = False
        try:
            if t == 'LWPOLYLINE':
                pts = [(p[0], p[1]) for p in e.get_points('xy')]; cerrado = e.closed
            elif t == 'POLYLINE':
                pts = [(v.dxf.location.x, v.dxf.location.y) for v in e.vertices]; cerrado = e.is_closed
            elif t == 'LINE':
                pts = [(e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)]
            elif t == 'POINT':
                pts = [(e.dxf.location.x, e.dxf.location.y)]
            elif t == 'INSERT':
                pts = [(e.dxf.insert.x, e.dxf.insert.y)]
            elif t in ('CIRCLE', 'ARC'):
                c = e.dxf.center; r = e.dxf.radius
                a0, a1 = (0.0, 360.0) if t == 'CIRCLE' else (e.dxf.start_angle, e.dxf.end_angle)
                if a1 < a0:
                    a1 += 360
                n = max(8, int(math.radians(a1 - a0) * r / paso))
                pts = [(c.x + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c.y + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
            elif t == 'HATCH':
                pts = []
                for path in e.paths:
                    if hasattr(path, 'vertices'):
                        pts += [(v[0], v[1]) for v in path.vertices]
                    elif hasattr(path, 'edges'):
                        for ed in path.edges:
                            if hasattr(ed, 'start'):
                                pts.append((ed.start[0], ed.start[1]))
                cerrado = True
            elif t in ('SPLINE',):
                pts = [(p[0], p[1]) for p in e.control_points]
            elif t in ('TEXT', 'MTEXT'):
                pts = [(e.dxf.insert.x, e.dxf.insert.y)]
            elif t == 'ELLIPSE':
                pts = [(p[0], p[1]) for p in e.vertices(np.linspace(e.dxf.start_param, e.dxf.end_param, 32))]
        except Exception:
            pts = None
        if not pts:
            continue
        ents.append(dict(capa=lay, tipo=t, handle=e.dxf.handle, pts=_densificar(pts, paso, cerrado) if len(pts) > 1 else list(pts),
                         vertices=pts))
    return ents


class ProyectorEje:
    """Proyección rápida de puntos (x, y) al eje: progresiva y offset con signo (+ derecha)."""

    def __init__(self, eje, paso=1.0, celda=50.0):
        self.eje = eje
        self.s = np.arange(0.0, eje.length + paso, paso); self.s = self.s[self.s <= eje.length]
        self.x, self.y, self.th, _ = eje.locate(self.s)
        self.celda = celda
        self.x0, self.y0 = self.x.min(), self.y.min()
        cx = ((self.x - self.x0) // celda).astype(int); cy = ((self.y - self.y0) // celda).astype(int)
        self.grid = {}
        for i in range(len(self.s)):
            self.grid.setdefault((cx[i], cy[i]), []).append(i)
        self.grid = {k: np.array(v) for k, v in self.grid.items()}

    def proyectar(self, px, py, dmax=100.0):
        px = np.asarray(px, float); py = np.asarray(py, float)
        sta = np.full(px.shape, np.nan); off = np.full(px.shape, np.nan)
        cx = ((px - self.x0) // self.celda).astype(int); cy = ((py - self.y0) // self.celda).astype(int)
        r = int(math.ceil(dmax / self.celda))
        for i in range(len(px)):
            cand = []
            for a in range(cx[i] - r, cx[i] + r + 1):
                for b in range(cy[i] - r, cy[i] + r + 1):
                    v = self.grid.get((a, b))
                    if v is not None:
                        cand.append(v)
            if not cand:
                continue
            cand = np.concatenate(cand)
            d2 = (self.x[cand] - px[i]) ** 2 + (self.y[cand] - py[i]) ** 2
            j = cand[int(np.argmin(d2))]
            if d2.min() > dmax ** 2:
                continue
            # refinar sobre la tangente local
            tx, ty = math.cos(self.th[j]), math.sin(self.th[j])
            dx, dy = px[i] - self.x[j], py[i] - self.y[j]
            along = dx * tx + dy * ty
            sta[i] = self.s[j] + along
            off[i] = dx * ty - dy * tx          # + derecha
        return sta, off


def tabla_interferencias(ents, proyector, sta_grid, dmax=100.0):
    """Para cada progresiva de análisis y lado: offset mínimo |off| de una interferencia (en ±paso/2) y
    lista de entidades. Devuelve dict lado -> (min_off array, listas de índices de entidad)."""
    ds = sta_grid[1] - sta_grid[0]
    n = len(sta_grid)
    res = {l: dict(min_off=np.full(n, np.inf), ents=[set() for _ in range(n)]) for l in ('IZQ', 'DER')}
    for k, e in enumerate(ents):
        P = np.array(e['pts'])
        s, o = proyector.proyectar(P[:, 0], P[:, 1], dmax)
        ok = np.isfinite(s)
        e['sta'] = s; e['off'] = o
        for sk, ok_ in zip(s[ok], o[ok]):
            i = int(round(sk / ds))
            if i < 0 or i >= n:
                continue
            lado = 'DER' if ok_ >= 0 else 'IZQ'
            a = abs(ok_)
            if a < res[lado]['min_off'][i]:
                res[lado]['min_off'][i] = a
            res[lado]['ents'][i].add(k)
    return res
