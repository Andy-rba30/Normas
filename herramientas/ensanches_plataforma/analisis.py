# -*- coding: utf-8 -*-
"""Cálculo del costo (m3 adicionales) de un ensanche en cada progresiva y lado."""
import numpy as np
from seccion import areas_ensanche, PARAM


def offsets_borde(eje, borde, sta, ventana=400.0, paso_b=1.0):
    """Offset del alineamiento 'borde' respecto al eje en las progresivas 'sta' (intersección con la normal)."""
    sb = np.arange(0.0, borde.length + paso_b, paso_b)
    sb = sb[sb <= borde.length]
    bx, by, _, _ = borde.locate(sb)
    x, y, th, _ = eje.locate(sta)
    tx, ty = np.cos(th), np.sin(th)
    nx, ny = np.sin(th), -np.cos(th)        # normal derecha
    out = np.full(len(sta), np.nan)
    n = len(sb)
    for i in range(len(sta)):
        c = int(sta[i] / eje.length * n)
        a, b = max(0, c - int(ventana / paso_b)), min(n, c + int(ventana / paso_b))
        f = (bx[a:b] - x[i]) * tx[i] + (by[a:b] - y[i]) * ty[i]
        g = (bx[a:b] - x[i]) * nx[i] + (by[a:b] - y[i]) * ny[i]
        s = np.nonzero((f[:-1] <= 0) & (f[1:] > 0))[0]
        if len(s) == 0:
            continue
        # tomar el cruce con menor |offset|
        offs = []
        for j in s:
            t = -f[j] / (f[j + 1] - f[j])
            offs.append(g[j] + t * (g[j + 1] - g[j]))
        out[i] = min(offs, key=abs)
    return out


def costos_por_progresiva(eje, ras, tn, off_izq, off_der, sta, w, P=PARAM):
    """Para cada progresiva y lado: áreas adicionales de corte/relleno (m2/m) y datos de sección."""
    x, y, th, k = eje.locate(sta)
    zr = ras.elev(sta)
    nx, ny = np.sin(th), -np.cos(th)
    offs_rel = np.arange(-2.0, P['alcance'] + w + P['paso'], P['paso'])
    off_izq = -np.maximum(np.nan_to_num(np.abs(off_izq), nan=3.30), 3.30); off_der = np.maximum(np.nan_to_num(np.abs(off_der), nan=3.30), 3.30)
    res = {}
    for lado, sgn, off in (('IZQ', -1.0, off_izq), ('DER', +1.0, off_der)):
        d0 = np.abs(off)
        # muestreo masivo del terreno: (n_sta, n_off)
        O = d0[:, None] + offs_rel[None, :]
        X = x[:, None] + sgn * O * nx[:, None]
        Y = y[:, None] + sgn * O * ny[:, None]
        Z = tn.elev(X.ravel(), Y.ravel()).reshape(O.shape)
        cols = dict(corte_add=[], relleno_add=[], h_borde=[], pend_terreno=[], muro=[], corte_base=[], empalme_ens=[], empalme_base=[], extrapolado=[])
        for i in range(len(sta)):
            zrow = Z[i]
            r = areas_ensanche(d0[i], zr[i], lambda o, zrow=zrow, oi=O[i]: np.interp(o, oi, zrow, left=np.nan, right=np.nan), w, P)
            if r is None:
                for c in cols:
                    cols[c].append(np.nan)
                cols['muro'][-1] = True
                continue
            for c in cols:
                cols[c].append(r[c])
        res[lado] = {c: np.array(v, dtype=float) for c, v in cols.items()}
        res[lado]['d0'] = d0
    res['x'], res['y'], res['theta'], res['curv'], res['z_ras'] = x, y, th, k, zr
    return res
