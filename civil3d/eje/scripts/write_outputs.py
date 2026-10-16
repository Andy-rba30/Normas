"""Genera LandXML, tabla de PIs (CSV), script AutoCAD, croquis SVG y reporte a partir del modelo ajustado."""
import numpy as np, math, pickle, sys, os, re, csv, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fit_axis import clothoid_xy, rot90, ang, dist_pts_poly, scs_geom, assemble, Model

V=40.0; RMIN_NORM=45.0; RMIN_8=50.0; RMIN_EXC=25.0; R_VOLTEO=25.0; LMIN_S=56.0; LMIN_O=111.0; LMAX=668.0; R_NO_SPIRAL=150.0; LC_MIN=3*V
CALZADA=6.00; L_VEH=10.55   # B2 (separacion de ejes 8.25 + vuelo delantero 2.30), Tabla 202.01
T30212={6:9.75,7:9.50,8:9.25,10:8.75,12:8.50,15:8.25,20:8.00}   # ancho total Re-Ri maniobra C2 (Tabla 302.12)
T30208=[(40,60,50),(50,75,50),(60,90,50),(70,105,50),(80,120,53),(90,135,60),(100,151,67),(110,166,73),(120,182,80),(130,198,87),(140,215,93),(150,232,100),(160,250,106),(170,269,112),(180,289,119),(190,309,125),(200,332,131),(210,355,137),(220,381,143),(230,408,149),(240,437,154),(250,469,160),(260,503,165),(270,540,171),(280,580,176),(290,623,181),(300,670,186)]

def sta_fmt(s): return f"{int(s//1000)}+{s%1000:06.2f}"
def az_deg(u):  # azimut desde el norte (y) hacia el este (x), en grados
    return (math.degrees(math.atan2(u[0],u[1]))+360)%360
def dms(a):
    d=int(a); m=int((a-d)*60); s=((a-d)*60-m)*60; return f"{d}°{m:02d}'{s:04.1f}\""
def sobreancho(R,n=2,L=L_VEH,V=V):
    if R<=L: return float('nan')
    return n*(R-math.sqrt(R*R-L*L))+V/(10*math.sqrt(R))
def ancho_volteo(Ri):
    ks=sorted(T30212); 
    if Ri<=ks[0]: return T30212[ks[0]]
    if Ri>=ks[-1]: return T30212[ks[-1]]
    for a,b in zip(ks[:-1],ks[1:]):
        if a<=Ri<=b: return T30212[a]+(T30212[b]-T30212[a])*(Ri-a)/(b-a)
def ri_volteo(R):
    """radio interior tal que Ri + ancho(Ri)/2 = R (ancho de calzada en curva de vuelta, Tabla 302.12, maniobra C2)"""
    lo,hi=0.5,R
    for _ in range(40):
        mid=(lo+hi)/2
        if mid+ancho_volteo(mid)/2>R: hi=mid
        else: lo=mid
    return (lo+hi)/2
def ratio_ok(Rin,Rout):
    """Tabla 302.08 (grupo 2): radio de salida admisible para un radio de entrada"""
    if Rin<40: lo,hi=Rin/1.5,Rin*1.5   # fuera de tabla: se asume la misma proporcion que el primer tramo
    elif Rin>300: lo,hi=186*Rin/300,1e9
    else:
        for (r,hi_,lo_),(r2,hi2,lo2) in zip(T30208[:-1],T30208[1:]):
            if r<=Rin<=r2:
                t=(Rin-r)/(r2-r); lo=lo_+(lo2-lo_)*t; hi=hi_+(hi2-hi_)*t; break
    return lo-1e-6<=Rout<=hi+1e-6

def classify(c):
    R=c['R']+0.06
    if R>=RMIN_8: return 'CUMPLE (R>=50, p.max 8%)'
    if R>=RMIN_NORM: return 'CUMPLE (R>=45, p.max 12%)'
    if R>=RMIN_EXC: return 'EXCEPCIONAL (Ve=30 km/h, Rmin 25)'
    return 'CURVA DE VUELTA (volteo)'

def absorb_tiny(m, lim=0.3):
    """elimina tangentes intermedias residuales (< lim m) subiendo levemente el radio de una curva vecina; reconstruye elementos."""
    cs=m['curves']
    def T(c): return c['g']['T']
    def regen(c): c['g']=scs_geom(c['PI'],c['uin'],c['uout'],c['delta'],c['R'],c['Ls'])
    def D(ci): return float(np.dot(cs[ci+1]['PI']-cs[ci]['PI'],cs[ci]['uout']))
    nfix=0
    # 1) ajustar radios que quedaron a milimetros de un valor redondo (p.ej. 44.99 -> 45.00) si hay holgura
    for ci,c in enumerate(cs):
        R=c['R']; mod=5 if R<100 else 10 if R<500 else 50; Rr=round(R/mod)*mod
        if Rr<=R+1e-9 or Rr-R>0.08: continue
        g2=scs_geom(c['PI'],c['uin'],c['uout'],c['delta'],Rr,c['Ls'])
        if g2 is None: continue
        dT=g2['T']-T(c)
        slack_p=(D(ci-1)-T(cs[ci-1])-T(c)) if ci>0 else 1e9
        slack_n=(D(ci)-T(c)-T(cs[ci+1])) if ci+1<len(cs) else 1e9
        if dT<=min(slack_p,slack_n)+1e-9: c['R']=Rr; regen(c)
    for ci in range(len(cs)-1):
        left=D(ci)-T(cs[ci])-T(cs[ci+1])
        if not (1e-6<left<lim): continue
        for c,side in ((cs[ci+1],'next'),(cs[ci],'prev')):
            k=cs.index(c)
            # holgura del otro lado de c
            if side=='next': other=(D(k)-T(c)-T(cs[k+1])) if k+1<len(cs) else 1e9
            else: other=(D(k-1)-T(cs[k-1])-T(c)) if k>0 else 1e9
            if other<left-1e-9: continue
            R0=c['R']; target=T(c)+left; lo,hi=R0,R0*1.2
            for _ in range(40):
                mid=(lo+hi)/2; g=scs_geom(c['PI'],c['uin'],c['uout'],c['delta'],mid,c['Ls'])
                if g is None or g['T']>target: hi=mid
                else: lo=mid
            c['R']=lo; regen(c); nfix+=1; break
    mm=Model(); mm.curves=cs; mm.start=m['els'][0]['A']; mm.end=m['els'][-1]['B']
    els,Ltot,poly=assemble(mm); m['els']=els; m['Ltot']=Ltot; m['poly']=poly
    Q=np.stack([m['x'],m['y']],1); m['d']=dist_pts_poly(Q,poly)
    return nfix

def load(path):
    m=pickle.load(open(path,'rb')); n=absorb_tiny(m); print('tangentes residuales absorbidas:',n); return m

def write_landxml(m, path, name, cs_xml):
    els=m['els']; L=[]
    L.append('<?xml version="1.0" encoding="utf-8"?>')
    L.append('<LandXML xmlns="http://www.landxml.org/schema/LandXML-1.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.landxml.org/schema/LandXML-1.2 http://www.landxml.org/schema/LandXML-1.2/LandXML-1.2.xsd" '
             f'date="{datetime.date.today()}" time="12:00:00" version="1.2" language="English" readOnly="false">')
    L.append('\t<Units>\n\t\t<Metric areaUnit="squareMeter" linearUnit="meter" volumeUnit="cubicMeter" temperatureUnit="celsius" pressureUnit="milliBars" diameterUnit="millimeter" angularUnit="decimal degrees" directionUnit="decimal degrees"></Metric>\n\t</Units>')
    if cs_xml: L.append('\t'+cs_xml)
    L.append('\t<Project name="Eje corregido DG-2018"></Project>')
    L.append('\t<Application name="fit_axis" desc="Eje ajustado al trazo existente" manufacturer="-" version="1.0"></Application>')
    L.append('\t<Alignments name="">')
    L.append(f'\t\t<Alignment name="{name}" length="{m["Ltot"]:.6f}" staStart="0." desc="Eje corregido segun DG-2018, V=40 km/h, ajustado al trazo existente">')
    L.append('\t\t\t<CoordGeom>')
    def P(p): return f'{p[1]:.6f} {p[0]:.6f}'   # N E
    for e in els:
        if e['type']=='Line':
            if e['L']<=1e-4: continue
            L.append(f'\t\t\t\t<Line dir="{az_deg(e["u"]):.12f}" length="{e["L"]:.6f}">\n\t\t\t\t\t<Start>{P(e["A"])}</Start>\n\t\t\t\t\t<End>{P(e["B"])}</End>\n\t\t\t\t</Line>')
        elif e['type']=='Curve':
            g=e['g']; rot='ccw' if e['left'] else 'cw'; delta=math.degrees(e['L']/e['R'])
            chord=float(np.hypot(*(e['B']-e['A'])))
            uin=g['uin'] if g['Ls']==0 else None
            dirS=az_deg(rot90(e['A']-e['C'], not e['left'])) ; dirE=az_deg(rot90(e['B']-e['C'], not e['left']))
            # direccion tangente en A: perpendicular al radio, sentido de avance
            tA=rot90(e['A']-e['C'], left=e['left']); tB=rot90(e['B']-e['C'], left=e['left'])
            # (rot90 left sobre el radio da la tangente de avance en giro ccw; para cw usar el otro)
            tA=rot90(e['A']-e['C'], left=True) if e['left'] else rot90(e['A']-e['C'], left=False)
            tB=rot90(e['B']-e['C'], left=True) if e['left'] else rot90(e['B']-e['C'], left=False)
            PIc=None
            # PI del arco: interseccion de tangentes en A y B
            M=np.array([tA/np.hypot(*tA),-tB/np.hypot(*tB)]).T
            if abs(np.linalg.det(M))>1e-9:
                t=np.linalg.solve(M,e['B']-e['A']); PIc=e['A']+tA/np.hypot(*tA)*t[0]
            s=f'\t\t\t\t<Curve rot="{rot}" chord="{chord:.6f}" delta="{delta:.12f}" dirEnd="{az_deg(tB):.12f}" dirStart="{az_deg(tA):.12f}" external="{(e["R"]/math.cos(math.radians(delta)/2)-e["R"]):.6f}" length="{e["L"]:.6f}" midOrd="{(e["R"]*(1-math.cos(math.radians(delta)/2))):.6f}" radius="{e["R"]:.6f}" tangent="{(e["R"]*math.tan(math.radians(delta)/2)):.6f}">\n'
            s+=f'\t\t\t\t\t<Start>{P(e["A"])}</Start>\n\t\t\t\t\t<Center>{P(e["C"])}</Center>\n\t\t\t\t\t<End>{P(e["B"])}</End>\n'
            if PIc is not None: s+=f'\t\t\t\t\t<PI>{P(PIc)}</PI>\n'
            s+='\t\t\t\t</Curve>'; L.append(s)
        else:
            g=e['g']; rot='ccw' if e['left'] else 'cw'; A=math.sqrt(g['R']*g['Ls']); ths=math.degrees(g['ths'])
            if e['entry']:
                dirS=az_deg(g['uin']); tA=rot90(e['B']-g['C'], left=e['left']); dirE=az_deg(tA)
                # PI de la espiral: interseccion de la tangente en TS con la tangente en SC
                M=np.array([g['uin'],-tA/np.hypot(*tA)]).T; t=np.linalg.solve(M,e['B']-e['A']); PIs=e['A']+g['uin']*t[0]
                rs,re_='INF',f'{g["R"]:.6f}'
            else:
                tA=rot90(e['A']-g['C'], left=e['left']); dirS=az_deg(tA); dirE=az_deg(g['uout'])
                M=np.array([tA/np.hypot(*tA),-g['uout']]).T; t=np.linalg.solve(M,e['B']-e['A']); PIs=e['A']+tA/np.hypot(*tA)*t[0]
                rs,re_=f'{g["R"]:.6f}','INF'
            chord=float(np.hypot(*(e['B']-e['A'])))
            s=f'\t\t\t\t<Spiral length="{g["Ls"]:.6f}" radiusEnd="{re_}" radiusStart="{rs}" rot="{rot}" spiType="clothoid" chord="{chord:.6f}" constant="{A:.6f}" dirEnd="{dirE:.12f}" dirStart="{dirS:.12f}" theta="{ths:.12f}" totalX="{g["Xs"]:.6f}" totalY="{g["Ys"]:.6f}" tanLong="{(g["Xs"]-g["Ys"]/math.tan(g["ths"])):.6f}" tanShort="{(g["Ys"]/math.sin(g["ths"])):.6f}">\n'
            s+=f'\t\t\t\t\t<Start>{P(e["A"])}</Start>\n\t\t\t\t\t<PI>{P(PIs)}</PI>\n\t\t\t\t\t<End>{P(e["B"])}</End>\n\t\t\t\t</Spiral>'; L.append(s)
    L.append('\t\t\t</CoordGeom>\n\t\t</Alignment>\n\t</Alignments>\n</LandXML>')
    open(path,'w',encoding='utf-8',newline='\r\n').write('\n'.join(L)+'\n')

def curve_rows(m):
    els=m['els']; curves=m['curves']; rows=[]
    # estaciones por curva
    idx={}
    for e in els:
        if e['type']=='Curve': idx.setdefault(e['ci'],{})['curve']=e
        elif e['type']=='Spiral': idx.setdefault(e['ci'],{})['sp_in' if e['entry'] else 'sp_out']=e
    lines=[e for e in els if e['type']=='Line']
    for ci,c in enumerate(curves):
        g=c['g']; ec=idx[ci]['curve']; sta_pc=idx[ci]['sp_in']['sta'] if 'sp_in' in idx[ci] else ec['sta']
        sta_pt=(idx[ci]['sp_out']['sta']+idx[ci]['sp_out']['L']) if 'sp_out' in idx[ci] else ec['sta']+ec['L']
        sta_pi=sta_pc+g['T']
        R=c['R']; d=math.degrees(abs(c['delta'])); sentido='I' if c['delta']>0 else 'D'
        tan_prev=lines[ci]['L']; tan_next=lines[ci+1]['L']
        obs=[]
        cl=classify(c)
        if R<R_VOLTEO:
            Ri=ri_volteo(R); w=ancho_volteo(Ri)
            obs.append(f'Ri={Ri:.1f} m (min 8 normal / 6 absoluto), Re={Ri+w:.1f} m, ancho calzada en volteo {w:.2f} m (Tabla 302.12, C2)')
            if Ri<6: obs.append('Ri < 6 m: NO CUMPLE ni el minimo absoluto')
            elif Ri<8: obs.append('Ri entre 6 y 8 m: minimo absoluto, uso excepcional')
        if R<R_NO_SPIRAL and c['Ls']==0: obs.append('requiere clotoide (R<150, Tabla 302.11A)'+(f": {c['spiral_fail']}" if c.get('spiral_fail') else ''))
        if g['Ltot']<LC_MIN: obs.append(f'Lc {g["Ltot"]:.0f} m < 3V = {LC_MIN:.0f} m')
        if d<5 and g['Ltot']<30*(10-d): obs.append(f'deflexion pequena: Lc < 30(10-D)={30*(10-d):.0f} m')
        if c.get('raised'): obs.append('radio subido al minimo normativo (desvio admitido <= 2.0 m)')
        if c.get('forced'): obs.append('REVISAR: radio forzado por geometria de PIs')
        if R<12.5 and R<R_VOLTEO: obs.append('radio de eje < 12.5 m: no alcanza Ri = 8 m con calzada de 6 m; ampliar plataforma o aceptar Ri absoluto')
        if c['kind']=='jog': obs.append('desplazamiento del eje (curvas en S de gran radio)')
        if c['kind']=='fusion': obs.append('curva unica que reemplaza a curvas consecutivas del mismo sentido con tangente corta (Topico 302.06.03)')
        if c.get('compuesta'): obs.append('curva compuesta (policentrica) sin tangente con la curva vecina del mismo sentido (Topico 302.06.03, excepcional)')
        if c.get('S_ajustada'): obs.append('radio reducido (no menor de 45 m) para abrir la tangente en S a 56 m (Tabla 302.01)')
        if c['kind']=='quiebre': obs.append('quiebre de tangente larga')
        # relacion de radios con la siguiente curva (ambos sentidos de circulacion)
        if ci+1<len(curves) and tan_next<=200:
            Rn=curves[ci+1]['R']
            if not (ratio_ok(R,Rn) and ratio_ok(Rn,R)): obs.append(f'relacion de radios con C-{ci+2} ({R:.0f}/{Rn:.0f}) fuera de Tabla 302.08')
        if ci+1<len(curves):
            same=(c['delta']>0)==(curves[ci+1]['delta']>0); need=LMIN_O if same else LMIN_S
            if same and tan_next<=0.05: obs.append(f'sin tangente con C-{ci+2}: curva compuesta del mismo sentido')
            elif tan_next<need-1e-6: obs.append(f'tangente a C-{ci+2} = {tan_next:.1f} m < {need:.0f} m ({"mismo sentido" if same else "S"})')
        rows.append(dict(n=ci+1, PI_N=g['PI'][1], PI_E=g['PI'][0], sta_PI=sta_pi, delta=d, sentido=sentido, R=R, Ls=c['Ls'], T=g['T'], Lc=g['Larc'], Ltot=g['Ltot'], E=g['E'],
                         sta_PC=sta_pc, sta_PT=sta_pt, Sa=sobreancho(R), tan_prev=tan_prev, tan_next=tan_next, dmax=c['dmax'], clase=cl, obs='; '.join(obs), kind=c['kind']))
    return rows

def write_csv(rows, path):
    with open(path,'w',newline='',encoding='utf-8-sig') as f:
        w=csv.writer(f,delimiter=';')
        w.writerow(['Curva','Prog. PI','Norte PI','Este PI','Deflexion (°)','Sentido','Radio (m)','Le clotoide (m)','T (m)','Lc arco (m)','L total curva (m)','Externa (m)','Prog. PC/TS','Prog. PT/ST','Sobreancho (m) B2','Tangente previa (m)','Tangente siguiente (m)','Desvio max. respecto al trazo (m)','Clasificacion DG-2018','Observaciones'])
        for r in rows:
            w.writerow([f"C-{r['n']}",sta_fmt(r['sta_PI']),f"{r['PI_N']:.3f}",f"{r['PI_E']:.3f}",f"{r['delta']:.4f}",r['sentido'],f"{r['R']:.2f}",f"{r['Ls']:.0f}",f"{r['T']:.2f}",f"{r['Lc']:.2f}",f"{r['Ltot']:.2f}",f"{r['E']:.2f}",sta_fmt(r['sta_PC']),sta_fmt(r['sta_PT']),('-' if math.isnan(r['Sa']) else f"{r['Sa']:.2f}"),f"{r['tan_prev']:.2f}",f"{r['tan_next']:.2f}",f"{r['dmax']:.2f}",r['clase'],r['obs']])

def write_pnezd(rows, path):
    with open(path,'w',newline='',encoding='utf-8') as f:
        for r in rows: f.write(f"{r['n']},{r['PI_N']:.4f},{r['PI_E']:.4f},0.000,PI-{r['n']} R={r['R']:.0f}\n")

def write_scr(rows, m, path):
    """script AutoCAD: polilinea por los PIs (para 'Crear alineacion a partir de objetos') + textos con el radio"""
    L=['_.-LAYER _M EJE-PI _C 1 EJE-PI ','_.PLINE']
    c0=m['els'][0]['A']; L.append(f'{c0[0]:.4f},{c0[1]:.4f}')
    for r in rows: L.append(f"{r['PI_E']:.4f},{r['PI_N']:.4f}")
    cE=m['els'][-1]['B']; L.append(f'{cE[0]:.4f},{cE[1]:.4f}'); L.append('')
    L.append('_.-LAYER _M EJE-PI-TXT _C 2 EJE-PI-TXT ')
    for r in rows: L.append(f"_.-TEXT _J _C {r['PI_E']:.3f},{r['PI_N']:.3f} 3 0 PI-{r['n']} R={r['R']:.0f}")
    L.append('_.ZOOM _E'); open(path,'w',newline='\r\n').write('\n'.join(L)+'\n')

def write_svg(m, rows, path, P_orig):
    poly=m['poly']; els=m['els']
    xs=np.concatenate([poly[:,0],P_orig[:,0]]); ys=np.concatenate([poly[:,1],P_orig[:,1]])
    x0,x1,y0,y1=xs.min()-60,xs.max()+60,ys.min()-60,ys.max()+60; W=x1-x0; H=y1-y0
    def X(x): return x-x0
    def Y(y): return y1-y
    S=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {H:.1f}" width="{W*0.5:.0f}" height="{H*0.5:.0f}" style="background:#fff;font-family:Arial">']
    S.append(f'<rect width="{W:.1f}" height="{H:.1f}" fill="#fff"/>')
    S.append('<polyline fill="none" stroke="#9e9e9e" stroke-width="2.5" stroke-dasharray="6 4" points="'+' '.join(f'{X(p[0]):.1f},{Y(p[1]):.1f}' for p in P_orig)+'"/>')
    cols={'CUMPLE (R>=50, p.max 8%)':'#1b9e3a','CUMPLE (R>=45, p.max 12%)':'#4caf50','EXCEPCIONAL (Ve=30 km/h, Rmin 25)':'#ff9800','CURVA DE VUELTA (volteo)':'#d32f2f'}
    for e in els:
        if e['type']=='Line':
            if e['L']<=1e-4: continue
            S.append(f'<line x1="{X(e["A"][0]):.1f}" y1="{Y(e["A"][1]):.1f}" x2="{X(e["B"][0]):.1f}" y2="{Y(e["B"][1]):.1f}" stroke="#1565c0" stroke-width="2"/>')
        elif e['type']=='Curve':
            r=rows[e['ci']]; col=cols[r['clase']]; sw=1 if e['left'] else 0
            S.append(f'<path d="M {X(e["A"][0]):.4f} {Y(e["A"][1]):.4f} A {e["R"]:.4f} {e["R"]:.4f} 0 {1 if e["L"]/e["R"]>math.pi else 0} {0 if e["left"] else 1} {X(e["B"][0]):.4f} {Y(e["B"][1]):.4f}" fill="none" stroke="{col}" stroke-width="3"/>')
        else:
            g=e['g']; xs_,ys_=clothoid_xy(g['Ls'],g['R'],40)
            if e['entry']: pts=g['TS'][None,:]+xs_[:,None]*g['uin'][None,:]+ys_[:,None]*rot90(g['uin'],g['left'])[None,:]
            else: pts=g['ST'][None,:]-xs_[:,None]*g['uout'][None,:]+ys_[:,None]*rot90(g['uout'],g['left'])[None,:]
            S.append('<polyline fill="none" stroke="#8e24aa" stroke-width="3" points="'+' '.join(f'{X(p[0]):.1f},{Y(p[1]):.1f}' for p in pts)+'"/>')
    for r in rows:
        col=cols[r['clase']]
        S.append(f'<circle cx="{X(r["PI_E"]):.1f}" cy="{Y(r["PI_N"]):.1f}" r="2.2" fill="{col}" stroke="#000" stroke-width="0.4"/>')
        S.append(f'<text x="{X(r["PI_E"])+3:.1f}" y="{Y(r["PI_N"])-3:.1f}" font-size="9" fill="#333">C{r["n"]} R{r["R"]:.0f}</text>')
    # progresivas cada 500 m sobre el eje
    sta=0.0; 
    for e in els:
        for k in range(int(sta//500)+1, int((sta+e['L'])//500)+1):
            t=(k*500-sta)/max(e['L'],1e-9)
            if e['type']=='Line': p=e['A']+(e['B']-e['A'])*t
            elif e['type']=='Curve':
                a0=ang(e['A']-e['C']); sgn=1 if e['left'] else -1; a=a0+sgn*(e['L']/e['R'])*t; p=e['C']+e['R']*np.array([math.cos(a),math.sin(a)])
            else: p=e['A']+(e['B']-e['A'])*t
            S.append(f'<circle cx="{X(p[0]):.1f}" cy="{Y(p[1]):.1f}" r="4" fill="#000"/><text x="{X(p[0])+6:.1f}" y="{Y(p[1])+4:.1f}" font-size="14" font-weight="bold" fill="#000">{k*500/1000:.1f} km</text>')
        sta+=e['L']
    # leyenda
    lg=[('#9e9e9e','Trazo actual (poligonal)'),('#1565c0','Tangentes del eje corregido'),('#1b9e3a','Curva R >= 50 m (cumple, p.max 8%)'),('#4caf50','Curva 45 <= R < 50 m (cumple, p.max 12%)'),('#ff9800','Curva 25 <= R < 45 m (excepcional, Ve 30 km/h)'),('#d32f2f','Curva R < 25 m (curva de vuelta)'),('#8e24aa','Clotoides')]
    S.append(f'<rect x="20" y="20" width="430" height="{30+22*len(lg)}" fill="#fff" stroke="#333"/>'); S.append('<text x="30" y="42" font-size="16" font-weight="bold">Eje corregido DG-2018 (V=40 km/h)</text>')
    for i,(c,t) in enumerate(lg): S.append(f'<line x1="30" y1="{62+22*i}" x2="70" y2="{62+22*i}" stroke="{c}" stroke-width="4"/><text x="80" y="{66+22*i}" font-size="13">{t}</text>')
    S.append(f'<line x1="{W-320:.0f}" y1="{H-40:.0f}" x2="{W-120:.0f}" y2="{H-40:.0f}" stroke="#000" stroke-width="4"/><text x="{W-320:.0f}" y="{H-50:.0f}" font-size="14">200 m</text>')
    S.append('</svg>'); open(path,'w',encoding='utf-8').write('\n'.join(S))

def write_report(m, rows, path, title, orig_len):
    d=m['d']; R=np.array([r['R'] for r in rows]); n=len(rows)
    L=[f'# {title}','',f'Fecha: {datetime.date.today()}','','## Parámetros de diseño adoptados (DG-2018)','',
       '| Parámetro | Valor | Fuente DG-2018 |','|---|---|---|',
       '| Clasificación | Carretera de Segunda Clase, orografía escarpada (tipo 4), zona poblada | Tabla 204.01 (40 km/h admisible solo en escarpado) |',
       '| Velocidad de diseño | 40 km/h | Tabla 204.01 |',
       '| Peralte máximo | 12 % (absoluto, rural accidentado/escarpado); 8 % normal | Tabla 304.05 |',
       '| Radio mínimo normativo | 45 m (p = 12 %); 50 m con p = 8 % | Tabla 302.02 |',
       '| Radio mínimo excepcional | 25 m, asociado a velocidad específica 30 km/h y p = 12 % | Tabla 302.02 (V = 30 km/h) |',
       '| Curvas de vuelta | Ri ≥ 8 m normal, 6 m absoluto; Re según Tabla 302.12 (maniobra C2) | Tópico 302.07, Tabla 302.12 |',
       '| Calzada | 6.00 m (6.60 m en orografía accidentada) + sobreancho | Tabla 304.01 |',
       '| Bermas | 0.50 m (escarpado) / 0.90 m (accidentado) | Tabla 304.02 |',
       '| Tangentes mínimas | 56 m entre curvas en S; 111 m entre curvas del mismo sentido; máx. 668 m | Tabla 302.01 |',
       '| Curvas de transición | obligatorias si R < 150 m; Le = 40 m (mín. 30 m); R/3 ≤ A ≤ R | Tablas 302.10 y 302.11A, Tópico 302.05.06 |',
       '| Longitud mínima de curva | 3V = 120 m; deflexiones < 5°: L > 30(10 − Δ) | Tópico 302.02 |',
       '| Sobreancho | Sa = n(R − √(R² − L²)) + V/(10√R), vehículo B2 (L = 10.55 m), mínimo 0.40 m | Tópico 302.09.03 |',
       '','> Nota: el documento de parámetros entregado menciona 30 km/h y clasificación de trocha carrozable, pero adopta un radio mínimo de 45 m, que corresponde a 40 km/h con peralte 12 %. Aquí se adoptó 40 km/h y Segunda Clase según lo indicado. Si finalmente se adopta 30 km/h, el radio mínimo normativo baja a 25 m (p = 12 %) y las curvas aquí llamadas "excepcionales" pasan a cumplir.',
       '','## Resultado global','',
       f'- Longitud del trazo original: {orig_len:.1f} m. Longitud del eje corregido: {m["Ltot"]:.1f} m.',
       f'- Curvas: {n}. Tangentes: {n+1}.',
       f'- Desvío lateral del trazo actual respecto al eje corregido: promedio {d.mean():.2f} m, percentil 95 {np.percentile(d,95):.2f} m, máximo {d.max():.2f} m.',
       f'- Longitud de trazo con desvío mayor a 1.5 m: {(d>1.5).sum()} m ({100*(d>1.5).mean():.1f} %); mayor a 2.5 m: {(d>2.5).sum()} m ({100*(d>2.5).mean():.1f} %); mayor a 4 m: {(d>4).sum()} m.',
       '', '| Clasificación de curvas | Cantidad | % |','|---|---|---|']
    for k in ['CUMPLE (R>=50, p.max 8%)','CUMPLE (R>=45, p.max 12%)','EXCEPCIONAL (Ve=30 km/h, Rmin 25)','CURVA DE VUELTA (volteo)']:
        c=sum(1 for r in rows if r['clase']==k); L.append(f'| {k} | {c} | {100*c/n:.0f} % |')
    tn=[r['tan_next'] for r in rows[:-1]]
    L+=['',f'- Curvas con clotoide: {sum(1 for r in rows if r["Ls"]>0)} de {sum(1 for r in rows if r["R"]<R_NO_SPIRAL)} que la requieren (R < 150 m).',
        f'- Tangentes intermedias que cumplen la longitud mínima de la Tabla 302.01: {sum(1 for r in rows[:-1] if "tangente a C-" not in r["obs"] and "sin tangente con" not in r["obs"])} de {len(tn)}; curvas compuestas del mismo sentido sin tangente (302.06.03): {sum(1 for r in rows[:-1] if "sin tangente con" in r["obs"])}.',
        f'- Curvas con longitud total ≥ 3V = 120 m: {sum(1 for r in rows if r["Ltot"]>=LC_MIN)} de {n}.',
        f'- Pares de curvas consecutivas (tangente ≤ 200 m) con relación de radios dentro de la Tabla 302.08: {sum(1 for r in rows[:-1] if "relacion de radios" not in r["obs"])} de {n-1}.',
        '', '## Curvas con radio menor al normativo (coordenadas de PI)','',
        '| Curva | Prog. PI | Norte | Este | Δ (°) | R (m) | Clasificación | Ri / Re volteo (m) | Desvío máx. (m) |','|---|---|---|---|---|---|---|---|---|']
    for r in rows:
        if r['R']<RMIN_NORM:
            rire=f"{ri_volteo(r['R']):.1f} / {ri_volteo(r['R'])+ancho_volteo(ri_volteo(r['R'])):.1f}" if r['R']<R_VOLTEO else '-'
            L.append(f"| C-{r['n']} | {sta_fmt(r['sta_PI'])} | {r['PI_N']:.3f} | {r['PI_E']:.3f} | {r['delta']:.1f} | {r['R']:.1f} | {r['clase']} | {rire} | {r['dmax']:.2f} |")
    L+=['','## Tabla completa de curvas','','| Curva | Prog. PI | Norte | Este | Δ (°) | Sent. | R (m) | Le (m) | T (m) | Lc (m) | Prog. PC/TS | Prog. PT/ST | Sa (m) | Tang. sig. (m) | Desvío (m) | Clase | Observaciones |','|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in rows:
        L.append(f"| C-{r['n']} | {sta_fmt(r['sta_PI'])} | {r['PI_N']:.2f} | {r['PI_E']:.2f} | {r['delta']:.1f} | {r['sentido']} | {r['R']:.1f} | {r['Ls']:.0f} | {r['T']:.1f} | {r['Lc']:.1f} | {sta_fmt(r['sta_PC'])} | {sta_fmt(r['sta_PT'])} | {('-' if math.isnan(r['Sa']) else f"{r['Sa']:.2f}")} | {r['tan_next']:.1f} | {r['dmax']:.2f} | {r['clase'].split(' ')[0]} | {r['obs']} |")
    # zonas de curvas de vuelta (grupos de curvas consecutivas con R < 25 m)
    L+=['','## Zonas de curvas de vuelta (grupos de curvas consecutivas con R < 25 m)','','| Zona | Prog. inicio | Prog. fin | Curvas | R mínimo (m) | Ri mínimo (m) |','|---|---|---|---|---|---|']
    grp=[]; cur=[]
    for r in rows:
        if r['R']<R_VOLTEO: cur.append(r)
        elif cur: grp.append(cur); cur=[]
    if cur: grp.append(cur)
    for i,g in enumerate(grp):
        rmin=min(r['R'] for r in g)
        L.append(f"| V-{i+1} | {sta_fmt(g[0]['sta_PC'])} | {sta_fmt(g[-1]['sta_PT'])} | {', '.join('C-'+str(r['n']) for r in g)} | {rmin:.1f} | {ri_volteo(rmin):.1f} |")
    L+=['','## Cómo usar los archivos en Civil 3D','',
        '1. **Importar el eje**: Insert > LandXML (o `IMPORTLANDXML`), seleccionar `EJE_DG2018_*.xml`. Se crea un alineamiento con tangentes y curvas (y clotoides en la variante con espirales). Las coordenadas están en UTM WGS84 zona 17S, igual que el trazo original.',
        '2. **Alternativa editable por PIs**: ejecutar el script `*_PI_polilinea.scr` (comando `SCRIPT`) para dibujar la polilínea de PIs con etiquetas, y luego Home > Alignment > Create Alignment from Objects, marcando "Add curves between tangents"; después asignar a cada PI el radio de la columna "Radio (m)" de `*_curvas.csv`.',
        '3. **Puntos de PI**: `*_PI_PNEZD.csv` se importa como grupo de puntos (formato PNEZD, delimitado por comas) para ubicar y etiquetar cada PI.',
        '4. **Criterios de diseño**: asociar al alineamiento el archivo de criterios `DG2018_Corregido_2.xml` (velocidad 40 km/h, tabla de peralte "DG2018 _PMax 12%" o "8%", método de transición "DG2018 METRICO") para que Civil 3D marque las curvas que no cumplen el radio mínimo.',
        '5. **Revisión**: el croquis `*_planta.svg` (abrir en un navegador) muestra el trazo actual en gris y el eje corregido coloreado por clase de curva; el desvío máximo de cada curva respecto al trazo está en la tabla.']
    open(path,'w',encoding='utf-8').write('\n'.join(L)+'\n')

if __name__=='__main__':
    model_path=sys.argv[1]; outdir=sys.argv[2]; tag=sys.argv[3]; name=sys.argv[4]
    os.makedirs(outdir,exist_ok=True); m=load(model_path)
    src=open('in.xml',encoding='utf-8').read(); cs=re.search(r'<CoordinateSystem .*?</CoordinateSystem>',src,re.S); cs_xml=cs.group(0) if cs else ''
    P=np.load('pts.npy')[:,[1,0]]
    rows=curve_rows(m)
    write_landxml(m, f'{outdir}/EJE_DG2018_{tag}.xml', name, cs_xml)
    write_csv(rows, f'{outdir}/EJE_DG2018_{tag}_curvas.csv')
    write_pnezd(rows, f'{outdir}/EJE_DG2018_{tag}_PI_PNEZD.csv')
    write_scr(rows, m, f'{outdir}/EJE_DG2018_{tag}_PI_polilinea.scr')
    write_svg(m, rows, f'{outdir}/EJE_DG2018_{tag}_planta.svg', P)
    write_report(m, rows, f'{outdir}/EJE_DG2018_{tag}_reporte.md', f'Eje corregido DG-2018 ({name})', m['s'][-1])
    print('ok', len(rows), 'curvas ->', outdir)
