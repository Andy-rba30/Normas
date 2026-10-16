"""Pasada de tangentes (Tabla 302.01 y Topico 302.06.03) sobre un modelo ajustado:
 1) curvas del mismo sentido con tangente corta -> una sola curva (o compuesta sin tangente);
 2) curvas en S con tangente < 56 m -> reducir radios (sin bajar de 45 m) hasta abrir 56 m, si el desvio lo permite.
Uso: python3 tangent_pass.py model.pkl model_t.pkl [TOL]"""
import numpy as np, math, pickle, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fit_axis import scs_geom, dist_circ, fit_R, wrap, ang, rot90, assemble, Model, dist_pts_poly, sample_scs

def intersect(P1,u1,P2,u2):
    M=np.array([u1,-u2]).T
    if abs(np.linalg.det(M))<1e-9: return None
    t=np.linalg.solve(M,P2-P1); return P1+u1*t[0]

def run(model_path, out_path, TOL=1.5, LMIN_S=56.0, LMIN_O=111.0, RMIN=45.0, V=40.0, LS_NORM=40.0, LS_MIN=30.0, R_NO_SPIRAL=150.0, log=print):
    m=pickle.load(open(model_path,'rb')); cs=m['curves']; x=m['x']; y=m['y']
    start=m['els'][0]['A'].copy(); end=m['els'][-1]['B'].copy()
    for c in cs: c['Q']=np.stack([x[c['qa']:c['qb']+1],y[c['qa']:c['qb']+1]],1)
    def geo(c,R=None,Ls=None): return scs_geom(c['PI'],c['uin'],c['uout'],c['delta'],c['R'] if R is None else R,c['Ls'] if Ls is None else Ls)
    def T(c,R=None,Ls=None): g=geo(c,R,Ls); return g['T'] if g else 1e9
    def dev(c,R=None,Ls=None):
        R=c['R'] if R is None else R; Ls=c['Ls'] if Ls is None else Ls
        if Ls>0:
            g=geo(c,R,Ls); return float(dist_pts_poly(c['Q'],sample_scs(g)).max()) if g else 1e9
        return float(dist_circ(c['Q'],c['PI'],c['uin'],c['uout'],c['delta'],R).max())
    def D(i): return float(np.dot(cs[i+1]['PI']-cs[i]['PI'],cs[i]['uout']))
    def tlen(i): return D(i)-T(cs[i])-T(cs[i+1])
    def slack_prev(i): return float(np.dot(cs[i]['PI']-start,cs[i]['uin'])) if i==0 else D(i-1)-T(cs[i-1])-T(cs[i])
    def slack_next(i): return float(np.dot(end-cs[i]['PI'],cs[i]['uout'])) if i==len(cs)-1 else D(i)-T(cs[i])-T(cs[i+1])
    def rnd(R):
        mstep=5 if R<100 else 10 if R<500 else 50; Rr=math.floor(R/mstep+1e-9)*mstep
        return Rr if (Rr>=12.5 and (R-Rr<0.4*mstep or Rr>=RMIN)) else round(R,1)
    def R_for_T(c,Tt):
        """radio tal que la tangente valga Tt (biseccion, admite espiral)"""
        lo,hi=6.0,5000.0
        for _ in range(60):
            mid=(lo+hi)/2; g=geo(c,mid)
            if g is None or g['T']>Tt: hi=mid
            else: lo=mid
        return lo
    stats=dict(fusion=0,compuesta=0,S_ok=0,S_fail=0,fusion_fail=0)
    same=lambda i:(cs[i]['delta']>0)==(cs[i+1]['delta']>0)
    def census():
        tn=[tlen(i) for i in range(len(cs)-1)]; sm=[same(i) for i in range(len(cs)-1)]
        return dict(n_curvas=len(cs), n_tang=len(tn),
            mismo_total=sum(1 for s in sm if s), mismo_ok=sum(1 for t,s in zip(tn,sm) if s and t>=LMIN_O-1e-6), mismo_cero=sum(1 for t,s in zip(tn,sm) if s and t<=1e-6), mismo_corta=sum(1 for t,s in zip(tn,sm) if s and 1e-6<t<LMIN_O-1e-6),
            S_total=sum(1 for s in sm if not s), S_ok=sum(1 for t,s in zip(tn,sm) if (not s) and t>=LMIN_S-1e-6), S_cero=sum(1 for t,s in zip(tn,sm) if (not s) and t<=1e-6), S_corta=sum(1 for t,s in zip(tn,sm) if (not s) and 1e-6<t<LMIN_S-1e-6),
            S_20_56=sum(1 for t,s in zip(tn,sm) if (not s) and 20<=t<LMIN_S-1e-6))
    antes=census()
    # ---------- 1) mismo sentido: fundir / compuesta ----------
    changed=True
    while changed:
        changed=False
        cands=sorted([i for i in range(len(cs)-1) if same(i) and 1e-6<tlen(i)<LMIN_O-1e-6 and not (cs[i].get('no_merge') and cs[i+1].get('no_merge'))],key=lambda i:tlen(i))
        for i in cands:
            a,b=cs[i],cs[i+1]; delta=wrap(ang(b['uout'])-ang(a['uin']))
            ok=False
            if abs(delta)>1e-4 and abs(delta)<math.radians(170) and (delta>0)==(a['delta']>0):
                PI=intersect(a['PI'],a['uin'],b['PI'],b['uout'])
                if PI is not None and np.dot(PI-a['PI'],a['uin'])>-1e-6 and np.dot(b['PI']-PI,b['uout'])>-1e-6:
                    new=dict(a); new.update(PI=PI,uout=b['uout'],delta=delta,i1=b['i1'],qb=b['qb'],Ls=0.0,kind='fusion')
                    new['Q']=np.stack([x[new['qa']:new['qb']+1],y[new['qa']:new['qb']+1]],1)
                    Rf,_=fit_R(PI,new['uin'],new['uout'],delta,new['Q']); Rc=Rf
                    if Rc<RMIN and dev(new,RMIN)<=TOL: Rc=RMIN
                    # factibilidad con vecinos externos
                    Lp=0.0 if i==0 else max(tlen(i-1),0.0); Ln=0.0 if i+1==len(cs)-1 else max(tlen(i+1),0.0)
                    Dp=float(np.dot(PI-start,new['uin'])) if i==0 else float(np.dot(PI-cs[i-1]['PI'],new['uin']))-T(cs[i-1])-Lp
                    Dn=float(np.dot(end-PI,new['uout'])) if i+1==len(cs)-1 else float(np.dot(cs[i+2]['PI']-PI,new['uout']))-T(cs[i+2])-Ln
                    Tn=T(new,Rc)
                    if Tn>min(Dp,Dn): 
                        Rc=min(Dp,Dn)/math.tan(abs(delta)/2)
                    if Rc>=6.0 and dev(new,Rc)<=TOL and T(new,Rc)<=min(Dp,Dn)+1e-6:
                        Rr=rnd(Rc)
                        if dev(new,Rr)>TOL or T(new,Rr)>min(Dp,Dn)+1e-6: Rr=round(Rc,1)
                        new['R']=Rr; new['Rfit']=Rf; new['raised']=(Rr>Rf+0.05)
                        for k in ('forced','volteo_bajo','spiral_fail'): new.pop(k,None)
                        cs[i:i+2]=[new]; stats['fusion']+=1; changed=True; ok=True
            if ok: break
            # compuesta: consumir la tangente subiendo radios (primero el menor)
            L=tlen(i); done=False
            order=sorted([(i,'next'),(i+1,'prev')],key=lambda t:cs[t[0]]['R'])
            for k,side in order:
                c=cs[k]; Tt=T(c)+L; Rn=R_for_T(c,Tt)
                # 'side' es el lado compartido; el otro lado es el opuesto
                other=slack_next(k) if side=='prev' else slack_prev(k)
                other_S=(k<len(cs)-1 and not same(k)) if side=='prev' else (k>0 and not same(k-1))
                # al subir T de c, consume L en el lado compartido y L en el otro lado: no se toca una tangente en S
                if other_S: continue
                if other>=L-1e-6 and dev(c,Rn)<=TOL:
                    c['R']=Rn; c['kind']=c.get('kind','curva'); c['compuesta']=True; cs[i if k==i+1 else i+1]['compuesta']=True
                    stats['compuesta']+=1; done=True; break
            if not done:
                # repartir L entre ambas
                a,b=cs[i],cs[i+1]; Ra=R_for_T(a,T(a)+L/2); Rb=R_for_T(b,T(b)+L/2)
                prevS=(i>0 and not same(i-1)); nextS=(i+1<len(cs)-1 and not same(i+1))
                if (not prevS) and (not nextS) and slack_prev(i)>=L/2-1e-6 and slack_next(i+1)>=L/2-1e-6 and dev(a,Ra)<=TOL and dev(b,Rb)<=TOL:
                    a['R']=Ra; b['R']=Rb; a['compuesta']=True; b['compuesta']=True; stats['compuesta']+=1; done=True
            if not done:
                a['no_merge']=True; b['no_merge']=True; stats['fusion_fail']+=1
            else:
                changed=True; break
    # ---------- 2) curvas en S: abrir la tangente a 56 m reduciendo radios (no por debajo de 45 m) ----------
    for i in range(len(cs)-1):
        if same(i): continue
        L=tlen(i)
        if L>=LMIN_S-1e-6 or L<0: continue
        need=LMIN_S-L; a,b=cs[i],cs[i+1]
        capa=max(0.0,T(a)-T(a,RMIN)) if a['R']>RMIN+1e-6 else 0.0
        capb=max(0.0,T(b)-T(b,RMIN)) if b['R']>RMIN+1e-6 else 0.0
        if capa+capb<need-1e-6: stats['S_fail']+=1; continue
        fa=need*capa/(capa+capb); fb=need-fa
        Ra=R_for_T(a,T(a)-fa) if fa>0 else a['R']; Rb=R_for_T(b,T(b)-fb) if fb>0 else b['R']
        Ra=max(Ra,RMIN); Rb=max(Rb,RMIN)
        if dev(a,Ra)<=TOL and dev(b,Rb)<=TOL:
            # redondear hacia abajo (abre mas la tangente) sin bajar de RMIN
            Ra2=rnd(Ra); Rb2=rnd(Rb)
            if Ra2<RMIN: Ra2=Ra
            if Rb2<RMIN: Rb2=Rb
            if dev(a,Ra2)<=TOL and dev(b,Rb2)<=TOL: Ra,Rb=Ra2,Rb2
            a['R'],b['R']=Ra,Rb; a['S_ajustada']=True; b['S_ajustada']=True; stats['S_ok']+=1
        else: stats['S_fail']+=1
    # ---------- 3) espirales en curvas fundidas (si el modelo las usa) ----------
    if any(c['Ls']>0 for c in cs):
        for i,c in enumerate(cs):
            if c['Ls']>0 or c['R']>=R_NO_SPIRAL or c['R']<LS_MIN: continue
            Ls=LS_NORM if c['R']>=LS_NORM else LS_MIN
            if Ls>c['R']: continue
            g=geo(c,None,Ls)
            if g is None or g['Larc']<V/3.6: continue
            if g['T']<=min(slack_prev(i)+T(c),slack_next(i)+T(c))+1e-6: c['Ls']=Ls
    # ---------- factibilidad exacta (solapes residuales por redondeo) ----------
    for _ in range(20):
        bad=0
        for i in range(len(cs)-1):
            Dv=D(i); T1=T(cs[i]); T2=T(cs[i+1])
            if T1+T2>Dv+1e-9:
                bad+=1; f=Dv/(T1+T2)
                for c in (cs[i],cs[i+1]): c['R']=max(c['R']*f,6.0)
        if not bad: break
    # ---------- geometria final ----------
    for c in cs:
        c['g']=geo(c); c['dmax']=dev(c); 
    mm=Model(); mm.curves=cs; mm.start=start; mm.end=end
    els,Ltot,poly=assemble(mm); Q=np.stack([x,y],1); d=dist_pts_poly(Q,poly)
    despues=census(); out=dict(m); out.update(els=els,Ltot=Ltot,poly=poly,d=d,curves=[{k:v for k,v in c.items() if k!='Q'} for c in cs],tpass=dict(TOL=TOL,stats=stats,antes=antes,despues=despues))
    pickle.dump(out,open(out_path,'wb'))
    tn=np.array([tlen(i) for i in range(len(cs)-1)]); sm=np.array([same(i) for i in range(len(cs)-1)])
    ok=sum(1 for t,s in zip(tn,sm) if t>=(LMIN_O if s else LMIN_S)-1e-6)
    log(f"  curvas {len(cs)} | fusiones {stats['fusion']} compuestas {stats['compuesta']} (fallidas {stats['fusion_fail']}) | S abiertas a 56 m: {stats['S_ok']} (no posibles {stats['S_fail']})")
    log(f"  tangentes que cumplen Tabla 302.01: {ok} de {len(tn)} | mismo sentido con tangente >0 y <111: {sum(1 for t,s in zip(tn,sm) if s and 1e-6<t<LMIN_O)} | en S <56: {sum(1 for t,s in zip(tn,sm) if (not s) and t<LMIN_S)}")
    log(f"  desvio: max {d.max():.2f} med {d.mean():.2f} p95 {np.percentile(d,95):.2f}; >1.5m: {(d>1.5).sum()} m >2.5m: {(d>2.5).sum()} m")
    R=np.array([c['R'] for c in cs]); log(f"  R>=45: {(R>=45-0.06).sum()} 25-45: {((R>=25)&(R<45-0.06)).sum()} <25: {(R<25).sum()}")
    return out

if __name__=='__main__':
    run(sys.argv[1], sys.argv[2], TOL=float(sys.argv[3]) if len(sys.argv)>3 else 1.5)
