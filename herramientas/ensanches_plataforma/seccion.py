# -*- coding: utf-8 -*-
"""
Modelo simplificado de sección transversal para estimar el movimiento de tierras ADICIONAL
que genera un ensanche de plataforma de ancho w en un lado de la vía.

Sección base (sin berma): borde de calzada en d0 -> cuneta triangular (si corte) -> talud
hasta empalmar con el terreno. Sección ensanchada: la plataforma se prolonga w metros con la
misma pendiente transversal y luego se desarrolla la misma cuneta/talud.
Devuelve áreas (m2/m) de corte y relleno adicionales, altura de borde, pendiente del terreno.
"""
import numpy as np

PARAM = dict(
    bombeo=0.02,        # pendiente transversal de la plataforma (hacia afuera)
    talud_corte=1.0,    # H:V  (1.0 => 1H:1V)
    talud_relleno=1.5,  # H:V
    cuneta_ancho=1.0,   # cuneta triangular en corte (m)
    cuneta_prof=0.5,    # profundidad de cuneta (m)
    alcance=30.0,       # distancia máxima buscada para empalme con terreno (m)
    extrap=60.0,        # extrapolación del terreno (misma pendiente de los últimos 5 m) si el TIN termina (m)
    paso=0.5,           # paso de muestreo transversal (m)
)


def _linea_diseno(o, d_e, z_e, zt_e, P):
    """Cota de la línea de diseño en los offsets o (>= d_e) a partir del borde (d_e, z_e).
    zt_e: cota del terreno en el borde (decide corte o relleno)."""
    zd = np.full_like(o, np.nan)
    x = o - d_e
    if zt_e > z_e:   # corte: cuneta + talud de corte
        a, p = P['cuneta_ancho'], P['cuneta_prof']
        m1 = x <= a / 2
        m2 = (x > a / 2) & (x <= a)
        m3 = x > a
        zd[m1] = z_e - p * x[m1] / (a / 2)
        zd[m2] = z_e - p + p * (x[m2] - a / 2) / (a / 2)
        zd[m3] = z_e + (x[m3] - a) / P['talud_corte']
    else:            # relleno
        zd = z_e - x / P['talud_relleno']
    return zd


def _areas(o, zt, zd, tipo_corte):
    """Integra corte y relleno desde el borde hasta el primer empalme con el terreno."""
    dif = zd - zt                       # >0 relleno, <0 corte
    # empalme: primer cruce de signo después del inicio (ignorando la zona de cuneta en corte)
    if tipo_corte:
        cruce = np.nonzero(dif[1:] >= 0)[0]
    else:
        cruce = np.nonzero(dif[1:] <= 0)[0]
    if len(cruce) == 0:
        return np.nan, np.nan, np.nan
    j = cruce[0] + 1
    do = o[1] - o[0]
    seg = dif[:j + 1]
    fill = np.clip(seg, 0, None); cut = np.clip(-seg, 0, None)
    return np.trapezoid(cut, dx=do), np.trapezoid(fill, dx=do), o[j]


def areas_ensanche(d0, z_ras, zt_fn, w, P=PARAM):
    """
    d0: offset (positivo) del borde de calzada en este lado; z_ras: cota de rasante en el eje;
    zt_fn: función offset(array, positivo hacia afuera) -> cota de terreno.
    Devuelve dict con áreas adicionales (m2/m) y datos de la sección.
    """
    o = d0 + np.arange(-2.0, P['alcance'] + w + P['paso'], P['paso'])
    zt = zt_fn(o)
    extrapolado = False
    if np.isnan(zt).any():
        nv = np.nonzero(~np.isnan(zt))[0]
        if len(nv) < int(round(7.0 / P['paso'])) or nv[0] != 0 or np.isnan(zt[:nv[-1] + 1]).any():
            return None
        # el TIN termina: prolongar con la pendiente media de los últimos 5 m
        j = nv[-1]
        m = max(0, j - int(round(5.0 / P['paso'])))
        pend = (zt[j] - zt[m]) / (o[j] - o[m])
        o_ext = o[j] + np.arange(P['paso'], P['extrap'] + P['paso'], P['paso'])
        o = np.concatenate([o[:j + 1], o_ext])
        zt = np.concatenate([zt[:j + 1], zt[j] + pend * (o_ext - o[j])])
        extrapolado = True
    z_e = z_ras - P['bombeo'] * d0
    i0 = int(round(2.0 / P['paso']))                # índice del borde d0
    # --- sección base
    ob = o[i0:]
    ztb = zt[i0:]
    corte_b = ztb[0] > z_e
    zdb = _linea_diseno(ob, d0, z_e, ztb[0], P)
    cb, fb, emp_b = _areas(ob, ztb, zdb, corte_b)
    # --- sección ensanchada
    iw = i0 + int(round(w / P['paso']))
    z_ew = z_e - P['bombeo'] * w
    ow = o[iw:]
    ztw = zt[iw:]
    corte_w = ztw[0] > z_ew
    zdw = _linea_diseno(ow, d0 + w, z_ew, ztw[0], P)
    cw, fw, emp_w = _areas(ow, ztw, zdw, corte_w)
    # franja de plataforma nueva [d0, d0+w]
    op = o[i0:iw + 1]
    zp = z_e - P['bombeo'] * (op - d0)
    dif = zp - zt[i0:iw + 1]
    fp = np.trapezoid(np.clip(dif, 0, None), dx=P['paso'])
    cp = np.trapezoid(np.clip(-dif, 0, None), dx=P['paso'])
    pend = (zt[i0 + int(round(5.0 / P['paso']))] - zt[0]) / 7.0 if len(zt) > i0 + 10 else np.nan
    res = dict(h_borde=z_e - ztb[0], pend_terreno=pend, corte_base=corte_b, corte_ens=corte_w,
               empalme_base=emp_b, empalme_ens=emp_w, extrapolado=extrapolado)
    if np.isnan(cb) or np.isnan(cw):
        res.update(corte_add=np.nan, relleno_add=np.nan, muro=True)
        return res
    res.update(corte_add=max(cw + cp - cb, 0.0), relleno_add=max(fw + fp - fb, 0.0), muro=False)
    return res
