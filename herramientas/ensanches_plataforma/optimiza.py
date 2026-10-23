# -*- coding: utf-8 -*-
"""Selección de ubicaciones de ensanches por programación dinámica.

Restricciones (Tabla 304.12 DG-2018 + criterios de diseño):
  - lados alternados (IZQ, DER, IZQ, ...)
  - separación entre ensanches del mismo lado <= sep_max (2,500 m)
  - separación entre ensanches consecutivos (lados opuestos) >= gap_min
  - primer y último ensanche de cada lado a <= sep_max del inicio / fin del tramo
Objetivo: mínimo movimiento de tierras adicional total (m3, corte + relleno ponderados).
"""
import numpy as np


def costo_ensanche(sta, area_lado, w, largo, transicion, k_corte=1.0, k_relleno=1.0):
    """Volumen adicional (m3) de un ensanche centrado en cada progresiva (núcleo 'largo' + 2 transiciones)."""
    ds = sta[1] - sta[0]
    a = k_corte * area_lado['corte_add'] + k_relleno * area_lado['relleno_add']
    a = np.where(area_lado['muro'] > 0, np.nan, a)
    half = largo / 2.0
    rel = np.arange(-(half + transicion), half + transicion + ds / 2, ds)
    peso = np.where(np.abs(rel) <= half, 1.0, np.clip((half + transicion - np.abs(rel)) / transicion, 0, 1))
    n = len(sta); out = np.full(n, np.nan)
    A = np.concatenate([np.full(len(rel), np.nan), a, np.full(len(rel), np.nan)])
    k0 = len(rel)
    acc = np.zeros(n); ok = np.ones(n, bool)
    for r, p in zip(rel, peso):
        sh = int(round(r / ds))
        v = A[k0 + sh: k0 + sh + n]
        ok &= ~np.isnan(v)
        acc += np.nan_to_num(v) * p * ds
    out[ok] = acc[ok]
    return out


def radio_min_en(sta, curv, centro_rel):
    """Radio mínimo (m) dentro de una ventana relativa alrededor de cada progresiva."""
    ds = sta[1] - sta[0]
    R = np.where(curv == 0, np.inf, 1.0 / np.maximum(np.abs(curv), 1e-12))
    n = len(sta); rmin = np.full(n, np.inf)
    for r in centro_rel:
        sh = int(round(r / ds))
        v = np.full(n, np.inf)
        if sh >= 0:
            v[:n - sh] = R[sh:]
        else:
            v[-sh:] = R[:n + sh]
        rmin = np.minimum(rmin, v)
    return rmin


def optimizar(sta, costo, sep_max=2500.0, gap_min=400.0, borde_ini=100.0):
    """costo: dict {'IZQ': array, 'DER': array} (nan = no permitido). Devuelve lista [(idx, lado)]."""
    ds = sta[1] - sta[0]
    n = len(sta); L = sta[-1]
    lados = ['IZQ', 'DER']
    c = np.stack([np.where(np.isnan(costo[l]), np.inf, costo[l]) for l in lados])   # (2, n)
    c[:, sta < borde_ini] = np.inf; c[:, sta > L - borde_ini] = np.inf
    G = int(round(sep_max / ds)); g0 = int(round(gap_min / ds))
    INF = np.inf
    f = np.full((n, G + 1, 2), INF)          # f[i, g, s]: último en i (lado s), anterior en i-g (lado 1-s)
    # inicio: pareja (j, i)
    first = np.nonzero(sta <= sep_max)[0]
    for i in first:
        for s in (0, 1):
            if not np.isfinite(c[s, i]):
                continue
            js = np.arange(max(0, i - G), i - g0 + 1)
            if len(js) == 0:
                continue
            f[i, i - js, s] = c[1 - s, js] + c[s, i]
    pm = np.full((n, G + 1, 2), INF); pm_arg = np.zeros((n, G + 1, 2), dtype=np.int16)
    for i in range(n):
        for s in (0, 1):
            row = f[i, :, s]
            if not np.isfinite(row).any():
                continue
            # prefijo-mínimo sobre g (g >= g0)
            pmin = np.minimum.accumulate(row)
            arg = np.zeros(G + 1, dtype=np.int16)
            best = INF; bi = 0
            for g in range(G + 1):
                if row[g] < best:
                    best, bi = row[g], g
                arg[g] = bi
            pm[i, :, s] = pmin; pm_arg[i, :, s] = arg
            # transiciones al siguiente n (lado opuesto)
            ns = np.arange(i + g0, min(n - 1, i + G) + 1)
            if len(ns) == 0:
                continue
            Gi = i - ns + G                       # g máx permitido del estado previo
            val = c[1 - s, ns] + pmin[Gi]
            cur = f[ns, ns - i, 1 - s]
            upd = val < cur
            f[ns[upd], (ns - i)[upd], 1 - s] = val[upd]
    # terminal
    best = INF; bst = None
    for i in np.nonzero(sta >= L - sep_max)[0]:
        for s in (0, 1):
            gs = np.arange(0, G + 1)
            js = i - gs
            ok = (js >= 0)
            ok[ok] &= sta[js[ok]] >= L - sep_max
            vals = np.where(ok, f[i, :, s], INF)
            g = int(np.argmin(vals))
            if vals[g] < best:
                best, bst = vals[g], (i, g, s)
    if bst is None:
        return None, INF
    # retroceso
    seq = []
    i, g, s = bst
    while True:
        seq.append((i, lados[s]))
        j = i - g
        if j < 0 or not np.isfinite(f[i, g, s]):
            break
        # ¿es pareja inicial? -> si la f[i,g,s] coincide con c[1-s,j]+c[s,i] y sta[i]<=sep_max
        if sta[i] <= sep_max and abs(f[i, g, s] - (c[1 - s, j] + c[s, i])) < 1e-6:
            seq.append((j, lados[1 - s]))
            break
        gp = int(pm_arg[j, G - g, 1 - s])
        i, g, s = j, gp, 1 - s
    seq.reverse()
    return seq, best
