"""Ajuste de un eje (tangentes + curvas circulares, opcionalmente con clotoides) a una poligonal densa.
x = Este, y = Norte; angulo matematico; delta>0 = giro a la izquierda (ccw)."""
import numpy as np, math, sys, pickle, time

PRM = dict(
    V=40.0, RMIN_NORM=45.0, RMIN_EXC=25.0, R_FLOOR=12.5,
    R_THR=250.0, H_HEAD=4, W_CURV=6,
    LT_MIN=10.0, TOL_TAN=0.8, E_SMALL=0.5, DELTA_SMALL=8.0, DELTA_SPLIT=170.0,
    TOL_UP=2.0, EXT=15.0,
    LS_NORM=40.0, LS_MIN=30.0, R_NO_SPIRAL=150.0,
    SWEEPS=5, SWEEPS_REAL=2, T_MERGE=4.0, R_ABS=6.0, CORE_DELTA=100.0, CORE_FRAC=0.6, TOL_SPLIT=2.5,
)

def rot90(v, left=True): return np.array([-v[1], v[0]]) if left else np.array([v[1], -v[0]])
def ang(v): return math.atan2(v[1], v[0])
def wrap(a): return (a+math.pi)%(2*math.pi)-math.pi

def resample(P, step=1.0):
    seg=np.diff(P,axis=0); L=np.hypot(seg[:,0],seg[:,1]); sta=np.concatenate([[0],np.cumsum(L)])
    s=np.arange(0, sta[-1], step); s=np.append(s, sta[-1])
    return s, np.interp(s,sta,P[:,0]), np.interp(s,sta,P[:,1])

def heading_curv(x,y,h,w):
    n=len(x); i=np.arange(n); a=np.clip(i-h,0,n-1); b=np.clip(i+h,0,n-1)
    th=np.unwrap(np.arctan2(y[b]-y[a], x[b]-x[a]))
    a=np.clip(i-w,0,n-1); b=np.clip(i+w,0,n-1); k=(th[b]-th[a])/np.maximum(b-a,1)
    return th,k

def seg_runs(k, kthr):
    st=np.where(k>kthr,1,np.where(k<-kthr,-1,0)); runs=[]; i=0
    while i<len(st):
        j=i
        while j<len(st) and st[j]==st[i]: j+=1
        runs.append([int(st[i]), i, j]); i=j
    return runs

def merge_same(runs):
    out=[]
    for r in runs:
        if out and out[-1][0]==r[0]: out[-1][2]=r[2]
        else: out.append(list(r))
    return out

def cleanup(runs, th, k, prm):
    n=len(th); changed=True
    while changed:
        changed=False
        for idx in range(len(runs)):
            st,i0,i1=runs[idx]; m=i1-i0
            prev=runs[idx-1] if idx>0 else None; nxt=runs[idx+1] if idx+1<len(runs) else None
            if st==0 and m<prm['T_MERGE'] and prev and nxt and prev[0]==nxt[0]!=0: runs[idx][0]=prev[0]; changed=True; break
            if st!=0 and m<4 and (prev is None or prev[0]==0) and (nxt is None or nxt[0]==0): runs[idx][0]=0; changed=True; break
            if st!=0 and (prev is None or prev[0]==0) and (nxt is None or nxt[0]==0):
                d=abs(th[min(i1,n-1)]-th[i0]); R=1/max(np.abs(k[i0:i1]).mean(),1e-9)
                E=R*(1/math.cos(d/2)-1) if d<2.8 else 1e9
                if E<prm['E_SMALL'] and d<math.radians(prm.get('DELTA_SMALL',8.0)): runs[idx][0]=0; changed=True; break
        runs=merge_same(runs)
    return runs

def fit_line(x,y):
    c=np.array([x.mean(),y.mean()]); X=np.stack([x-c[0],y-c[1]],1)
    _,_,vt=np.linalg.svd(X,full_matrices=False); d=vt[0]
    if np.dot(d,[x[-1]-x[0],y[-1]-y[0]])<0: d=-d
    res=X@rot90(d); return c,d,float(np.abs(res).max()),int(np.argmax(np.abs(res)))

def clothoid_xy(Ls,R,n=None):
    if Ls<=0: return np.array([0.0]),np.array([0.0])
    n=n or max(int(Ls)+1,8); l=np.linspace(0,Ls,n); t=l*l/(2*R*Ls); cx=np.cos(t); sy=np.sin(t)
    x=np.concatenate([[0],np.cumsum((cx[1:]+cx[:-1])/2*np.diff(l))]); y=np.concatenate([[0],np.cumsum((sy[1:]+sy[:-1])/2*np.diff(l))])
    return x,y

def scs_geom(PI,uin,uout,delta,R,Ls):
    ad=abs(delta); left=delta>0
    if Ls>0:
        xs,ys=clothoid_xy(Ls,R); Xs,Ys=xs[-1],ys[-1]; ths=Ls/(2*R); p=Ys-R*(1-math.cos(ths)); kk=Xs-R*math.sin(ths)
    else: Xs=Ys=ths=p=kk=0.0
    arc=ad-2*ths
    if arc< -1e-9: return None
    T=(R+p)*math.tan(ad/2)+kk; TS=PI-uin*T; ST=PI+uout*T
    nin=rot90(uin,left); nout=rot90(uout,left); SC=TS+uin*Xs+nin*Ys; CS=ST-uout*Xs+nout*Ys
    sgn=1 if left else -1; c,s_=math.cos(sgn*ths),math.sin(sgn*ths); usc=np.array([c*uin[0]-s_*uin[1], s_*uin[0]+c*uin[1]])
    C=SC+rot90(usc,left)*R
    return dict(T=T,TS=TS,SC=SC,CS=CS,ST=ST,C=C,arc=arc,ths=ths,p=p,k=kk,Xs=Xs,Ys=Ys,left=left,R=R,Ls=Ls,delta=delta,PI=PI,uin=uin,uout=uout,
                Larc=R*arc, Ltot=R*arc+2*Ls, E=(R+p)/math.cos(ad/2)-R)

def sample_scs(g, ext=30.0, step=1.0):
    pts=[g['TS']-g['uin']*ext]; uin,uout,left,R=g['uin'],g['uout'],g['left'],g['R']
    if g['Ls']>0:
        xs,ys=clothoid_xy(g['Ls'],R); pts.append(g['TS'][None,:]+xs[:,None]*uin[None,:]+ys[:,None]*rot90(uin,left)[None,:])
    a0=ang(g['SC']-g['C']); n=max(int(g['Larc']/step)+2,3); sgn=1 if left else -1; aa=a0+sgn*np.linspace(0,g['arc'],n)
    pts.append(np.stack([g['C'][0]+R*np.cos(aa), g['C'][1]+R*np.sin(aa)],1))
    if g['Ls']>0:
        xs,ys=clothoid_xy(g['Ls'],R); q=g['ST'][None,:]-xs[:,None]*uout[None,:]+ys[:,None]*rot90(uout,left)[None,:]; pts.append(q[::-1])
    pts.append(g['ST']+g['uout']*ext)
    return np.vstack([p if p.ndim==2 else p[None,:] for p in pts])

def dist_pts_poly(Q, Pl):
    A=Pl[:-1]; B=Pl[1:]; AB=B-A; L2=np.maximum((AB**2).sum(1),1e-12); d=np.full(len(Q),np.inf)
    for i0 in range(0,len(Q),400):
        q=Q[i0:i0+400]; t=((q[:,None,:]-A[None,:,:])*AB[None,:,:]).sum(2)/L2[None,:]; t=np.clip(t,0,1)
        pr=A[None,:,:]+t[:,:,None]*AB[None,:,:]; d[i0:i0+400]=np.hypot(*(q[:,None,:]-pr).transpose(2,0,1)).min(1)
    return d

def dist_circ(Q,PI,uin,uout,delta,R):
    """distancia analitica de puntos Q a tangente-arco-tangente (sin espiral)."""
    ad=abs(delta); left=delta>0; sgn=1.0 if left else -1.0
    T=R*math.tan(ad/2); PC=PI-uin*T; PT=PI+uout*T; C=PC+rot90(uin,left)*R
    v=Q-C; r=np.hypot(v[:,0],v[:,1]); a=np.arctan2(v[:,1],v[:,0]); a0=ang(PC-C)
    rel=(sgn*(a-a0))%(2*math.pi); inside=rel<=ad
    darc=np.abs(r-R)
    # rayos de las tangentes
    w1=Q-PC; t1=w1@uin; d1=np.where(t1<=0, np.abs(w1@rot90(uin)), np.hypot(w1[:,0],w1[:,1]))
    w2=Q-PT; t2=w2@uout; d2=np.where(t2>=0, np.abs(w2@rot90(uout)), np.hypot(w2[:,0],w2[:,1]))
    dout=np.minimum(d1,d2)
    return np.where(inside, np.minimum(darc,dout), dout)

def fit_R(PI,uin,uout,delta,Q,Rlo=8.0,Rhi=5000.0):
    def f(R): d=dist_circ(Q,PI,uin,uout,delta,R); return float((d*d).mean())
    grid=np.geomspace(Rlo,Rhi,30); vals=[f(R) for R in grid]; i=int(np.argmin(vals))
    la,lb=math.log(grid[max(i-1,0)]),math.log(grid[min(i+1,len(grid)-1)]); gr=(math.sqrt(5)-1)/2
    c=lb-gr*(lb-la); d_=la+gr*(lb-la); fc=f(math.exp(c)); fd=f(math.exp(d_))
    for _ in range(14):
        if fc<fd: lb,d_,fd=d_,c,fc; c=lb-gr*(lb-la); fc=f(math.exp(c))
        else: la,c,fc=c,d_,fd; d_=la+gr*(lb-la); fd=f(math.exp(d_))
    R=math.exp((la+lb)/2); return R, f(R)

class Model: pass

def intersect(A,B):
    M=np.array([A['u'],-B['u']]).T
    if abs(np.linalg.det(M))<1e-9: return None
    t=np.linalg.solve(M,B['p']-A['p']); return A['p']+A['u']*t[0]

def build(P, prm=PRM, spirals=False, log=print):
    t0=time.time()
    s,x,y=resample(P); n=len(s); th,k=heading_curv(x,y,prm['H_HEAD'],prm['W_CURV'])
    runs=seg_runs(k,1/prm['R_THR']); runs=cleanup(runs,th,k,prm)
    # curvas de gran deflexion (volteos): separar nucleo de curvatura alta y ramas
    out=[]
    for st,i0,i1 in runs:
        d=abs(th[min(i1,n-1)]-th[i0]) if st!=0 else 0
        if st!=0 and d>math.radians(prm['CORE_DELTA']) and i1-i0>=30:
            kk=np.abs(k[i0:i1]); km=kk.max(); core=kk>=prm['CORE_FRAC']*km
            idx=np.where(core)[0]; a=i0+idx[0]; b=i0+idx[-1]+1
            if (a-i0)>=8 or (i1-b)>=8:
                if (a-i0)>=8: out.append([st,i0,a]); out.append([9,a,a])
                else: a=i0
                if (i1-b)>=8: out.append([st,a,b]); out.append([9,b,b]); out.append([st,b,i1])
                else: out.append([st,a,i1])
                continue
        out.append([st,i0,i1])
    runs=out
    out=[]
    for st,i0,i1 in runs:
        if st!=0:
            d=abs(th[min(i1,n-1)]-th[i0])
            if d>math.radians(prm['DELTA_SPLIT']):
                parts=int(math.ceil(d/math.radians(prm['DELTA_SPLIT']*0.6)))
                tgt=[th[i0]+(th[min(i1,n-1)]-th[i0])*(j/parts) for j in range(1,parts)]
                cuts=[i0]+[i0+int(np.argmin(np.abs(th[i0:i1]-t))) for t in tgt]+[i1]
                for a,b in zip(cuts[:-1],cuts[1:]): out.append([st,a,b]); out.append([9,b,b])
                out.pop(); continue
        out.append([st,i0,i1])
    runs=out
    def virtual_at(i,j=None):
        j=i if j is None else j; i=min(max(i,0),n-1); j=min(max(j,0),n-1); m=(i+j)//2
        a=max(m-3,0); b=min(m+3,n-1); u=np.array([x[b]-x[a],y[b]-y[a]]); u/=np.hypot(*u)
        return dict(p=np.array([x[m],y[m]]),u=u,virtual=True,i0=i,i1=j,res=0.0)
    def real_lines(i0,i1):
        tr=2 if i1-i0>=16 else 0
        c,d,res,im=fit_line(x[i0+tr:i1-tr],y[i0+tr:i1-tr])
        if res>prm['TOL_TAN'] and i1-i0>=2*prm['LT_MIN']+4:
            m=i0+tr+im; m=min(max(m,i0+int(prm['LT_MIN'])),i1-int(prm['LT_MIN']))
            return real_lines(i0,m)+[None]+real_lines(m,i1)
        return [dict(p=c,u=d,virtual=False,i0=i0,i1=i1,res=res)]
    seq=[]
    if runs[0][0]!=0: seq.append(('T',virtual_at(0)))
    for idx,(st,i0,i1) in enumerate(runs):
        if st==0:
            if i1-i0>=prm['LT_MIN']:
                for ln in real_lines(i0,i1):
                    if ln is None: seq.append(('C',dict(i0=seq[-1][1]['i1'],i1=seq[-1][1]['i1'],sign=0,kind='quiebre')))
                    else: seq.append(('T',ln))
            else: seq.append(('T',virtual_at(i0,i1)))
        elif st==9: seq.append(('T',virtual_at(i0)))
        else:
            if seq and seq[-1][0]=='C': seq.append(('T',virtual_at(i0)))
            seq.append(('C',dict(i0=i0,i1=i1,sign=st,kind='curva')))
    if seq[-1][0]=='C': seq.append(('T',virtual_at(n-1)))
    # ---- validacion de PIs: jogs y tangentes casi paralelas ----
    def pi_info(j):
        A=seq[j-1][1]; B=seq[j+1][1]; return A,B,intersect(A,B),wrap(ang(B['u'])-ang(A['u']))
    for _round in range(4):
        bad=[]; merge=[]
        for j in range(1,len(seq)-1):
            if seq[j][0]!='C': continue
            c=seq[j][1]; A,B,PI,delta=pi_info(j)
            if abs(delta)<math.radians(0.3): merge.append(j); continue
            if PI is None: bad.append(j); continue
            mid=np.array([x[(c['i0']+min(c['i1'],n-1))//2],y[(c['i0']+min(c['i1'],n-1))//2]])
            L=max(c['i1']-c['i0'],1.0); dPI=np.hypot(*(PI-mid))
            inv=np.dot(PI-A['p'],A['u'])<-1.0 or np.dot(B['p']-PI,B['u'])<-1.0
            if inv or dPI>max(3*L,60.0): bad.append(j)
        if not bad and not merge: break
        for j in sorted(set(bad)|set(merge),reverse=True):
            if j in merge:   # fundir tangentes A y B en una sola linea
                A=seq[j-1][1]; B=seq[j+1][1]; i0=min(A['i0'],B['i0']); i1=max(A['i1'],B['i1'])
                if i1-i0<4: i0=max(i0-3,0); i1=min(i1+3,n)
                c,d,res,_=fit_line(x[i0:i1],y[i0:i1]); seq[j-1:j+2]=[('T',dict(p=c,u=d,virtual=(A['virtual'] and B['virtual']),i0=i0,i1=i1,res=res))]
            else:
                c=seq[j][1]; i0=c['i0']; i1=min(c['i1'],n-1); m=(i0+i1)//2
                a=max(i0-5,0); b=min(i1+5,n-1); u=np.array([x[b]-x[a],y[b]-y[a]]); u/=np.hypot(*u)
                vt=dict(p=np.array([x[m],y[m]]),u=u,virtual=True,i0=m,i1=m,res=0.0)
                seq[j:j+1]=[('C',dict(i0=i0,i1=m,sign=0,kind='jog')),('T',vt),('C',dict(i0=m,i1=i1,sign=0,kind='jog'))]
    # ---- curvas (con particion de las de mal ajuste en compuestas) ----
    def refresh(c):
        A,B,PI,delta=pi_info(c['j']); c['uin']=A['u']; c['uout']=B['u']; c['PI']=PI; c['delta']=delta
    def build_curves():
        curves=[]
        for j in range(1,len(seq)-1):
            if seq[j][0]!='C': continue
            c=dict(seq[j][1]); c['j']=j; curves.append(c)
        for c in curves: refresh(c)
        for ci,c in enumerate(curves):
            a=c['i0']; b=min(c['i1'],n-1); pa=curves[ci-1]['i1'] if ci>0 else 0; nb=curves[ci+1]['i0'] if ci+1<len(curves) else n-1
            ea=min(prm['EXT'],max((a-pa)/2,2)); eb=min(prm['EXT'],max((nb-b)/2,2))
            c['qa']=int(max(a-ea,0)); c['qb']=int(min(b+eb,n-1)); c['Q']=np.stack([x[c['qa']:c['qb']+1],y[c['qa']:c['qb']+1]],1)
            if c['PI'] is None or abs(c['delta'])<1e-4: c['R']=50.0; c['sse']=1e9; c['Rfit']=50.0; c['Ls']=0.0; continue
            c['R'],c['sse']=fit_R(c['PI'],c['uin'],c['uout'],c['delta'],c['Q']); c['Rfit']=c['R']; c['Ls']=0.0
        return curves
    curves=build_curves()
    for _round in range(2):
        splits=[]
        for c in curves:
            if c['kind']!='curva' or c['i1']-c['i0']<30 or c['PI'] is None: continue
            d=dist_circ(c['Q'],c['PI'],c['uin'],c['uout'],c['delta'],c['R'])
            if d.max()>prm['TOL_SPLIT']:
                im=c['qa']+int(np.argmax(d)); im=min(max(im,c['i0']+10),min(c['i1'],n-1)-10)
                splits.append((c['j'],im))
        if not splits: break
        for j,im in sorted(splits,reverse=True):
            c=seq[j][1]; seq[j:j+1]=[('C',dict(i0=c['i0'],i1=im,sign=c['sign'],kind='curva')),('T',virtual_at(im)),('C',dict(i0=im,i1=c['i1'],sign=c['sign'],kind='curva'))]
        log(f'  particion de {len(splits)} curvas con mal ajuste')
        curves=build_curves()
    curves=[c for c in curves if c['PI'] is not None and abs(c['delta'])>=1e-4]
    start=np.array([x[0],y[0]]); end=np.array([x[-1],y[-1]])
    def Tlen(c,R=None,Ls=None):
        R=c['R'] if R is None else R; Ls=c['Ls'] if Ls is None else Ls
        g=scs_geom(c['PI'],c['uin'],c['uout'],c['delta'],R,Ls); return g['T'] if g else 1e9
    def Dside(ci):
        """distancias PI->PI vecino (o extremo) a cada lado, sin descontar tangentes vecinas"""
        c=curves[ci]
        Dp=np.dot(c['PI']-start,c['uin']) if ci==0 else np.dot(c['PI']-curves[ci-1]['PI'],c['uin'])
        Dn=np.dot(end-c['PI'],c['uout']) if ci==len(curves)-1 else np.dot(curves[ci+1]['PI']-c['PI'],c['uout'])
        return Dp,Dn
    def avail(ci):
        Dp,Dn=Dside(ci)
        if ci>0: Dp-=Tlen(curves[ci-1])
        if ci+1<len(curves): Dn-=Tlen(curves[ci+1])
        return Dp,Dn
    # ---- optimizacion de tangentes virtuales (barridos de descenso por coordenadas) ----
    vidx=[(ci,ci+1) for ci in range(len(curves)-1) if seq[curves[ci]['j']+1][1]['virtual']]
    def pair_cost(ci):
        """coste del par (ci,ci+1) con la tangente virtual actual: SSE ajustada + penalizacion de factibilidad"""
        c1,c2=curves[ci],curves[ci+1]; refresh(c1); refresh(c2)
        if c1['PI'] is None or c2['PI'] is None or abs(c1['delta'])<1e-4 or abs(c2['delta'])<1e-4: return 1e12,None,None
        R1,s1=fit_R(c1['PI'],c1['uin'],c1['uout'],c1['delta'],c1['Q']); R2,s2=fit_R(c2['PI'],c2['uin'],c2['uout'],c2['delta'],c2['Q'])
        D=np.dot(c2['PI']-c1['PI'],c1['uout'])
        if D<=0: return 1e12,None,None
        T1=R1*math.tan(abs(c1['delta'])/2); T2=R2*math.tan(abs(c2['delta'])/2)
        over=max(0.0,T1+T2-D)
        if over>0:  # encoger para que quepa y recalcular coste real
            f=D/(T1+T2)*0.999; R1=max(R1*f,prm['R_ABS']); R2=max(R2*f,prm['R_ABS'])
            T1=R1*math.tan(abs(c1['delta'])/2); T2=R2*math.tan(abs(c2['delta'])/2); pen_over=max(0.0,T1+T2-D)
            s1=float((dist_circ(c1['Q'],c1['PI'],c1['uin'],c1['uout'],c1['delta'],R1)**2).mean()); s2=float((dist_circ(c2['Q'],c2['PI'],c2['uin'],c2['uout'],c2['delta'],R2)**2).mean())
        # factibilidad con vecinos exteriores (fijos)
        pen=(pen_over**2 if over>0 else 0.0)
        Dp,_=Dside(ci); 
        if ci>0: Dp-=Tlen(curves[ci-1])
        _,Dn=Dside(ci+1)
        if ci+2<len(curves): Dn-=Tlen(curves[ci+2])
        pen+=max(0.0,T1-Dp)**2+max(0.0,T2-Dn)**2
        m1=float(dist_circ(c1['Q'],c1['PI'],c1['uin'],c1['uout'],c1['delta'],R1).max()); m2=float(dist_circ(c2['Q'],c2['PI'],c2['uin'],c2['uout'],c2['delta'],R2).max())
        return s1*len(c1['Q'])+s2*len(c2['Q'])+0.3*(len(c1['Q'])*m1*m1+len(c2['Q'])*m2*m2)+50*pen, R1, R2
    def optimize_pairs(pairs, nsweeps, steps=((3.0,2.0),(1.5,1.0),(0.75,0.5),(0.35,0.25),(0.15,0.12))):
        for sweep in range(nsweeps):
            for ci,cj in pairs:
                tj=seq[curves[ci]['j']+1][1]; base_p=tj['p'].copy(); base_u=tj['u'].copy(); nrm=rot90(base_u)
                best,R1,R2=pair_cost(ci)
                if R1 is None: continue
                phi=0.0; off=0.0
                for dphi,doff in steps:
                    improved=True
                    while improved:
                        improved=False
                        for dp,do in [(dphi,0),(-dphi,0),(0,doff),(0,-doff)]:
                            p2=phi+dp; o2=off+do; a=math.radians(p2); ca,sa=math.cos(a),math.sin(a)
                            tj['u']=np.array([ca*base_u[0]-sa*base_u[1], sa*base_u[0]+ca*base_u[1]]); tj['p']=base_p+nrm*o2
                            cst,r1,r2=pair_cost(ci)
                            if cst<best-1e-9: best,R1,R2,phi,off=cst,r1,r2,p2,o2; improved=True
                            else:
                                a=math.radians(phi); ca,sa=math.cos(a),math.sin(a)
                                tj['u']=np.array([ca*base_u[0]-sa*base_u[1], sa*base_u[0]+ca*base_u[1]]); tj['p']=base_p+nrm*off
                refresh(curves[ci]); refresh(curves[cj]); curves[ci]['R']=R1; curves[cj]['R']=R2
                if ci>0: refresh(curves[ci-1])
                if cj+1<len(curves): refresh(curves[cj+1])
    optimize_pairs(vidx, prm['SWEEPS'])
    allidx=[(ci,ci+1) for ci in range(len(curves)-1)]
    optimize_pairs(allidx, prm['SWEEPS_REAL'], steps=((0.6,0.6),(0.3,0.3),(0.15,0.15)))
    # particion posterior de curvas con mal ajuste (compuestas) y reoptimizacion local
    for c in curves: refresh(c)
    splits=[]
    for c in curves:
        if c['kind']!='curva' or c['i1']-c['i0']<30 or c['PI'] is None: continue
        d=dist_circ(c['Q'],c['PI'],c['uin'],c['uout'],c['delta'],c['R'])
        if d.max()>prm['TOL_SPLIT']:
            im=c['qa']+int(np.argmax(d)); im=min(max(im,c['i0']+10),min(c['i1'],n-1)-10); splits.append((c['j'],im))
    if splits:
        for j,im in sorted(splits,reverse=True):
            c=seq[j][1]; seq[j:j+1]=[('C',dict(i0=c['i0'],i1=im,sign=c['sign'],kind='curva')),('T',virtual_at(im)),('C',dict(i0=im,i1=c['i1'],sign=c['sign'],kind='curva'))]
        oldR={}
        for c in curves: oldR[(c['i0'],c['i1'])]=c['R']
        curves=build_curves()
        log(f'  particion posterior de {len(splits)} curvas; reoptimizacion local')
        js=set(j for j,_ in splits)
        local=set()
        for ci,c in enumerate(curves):
            if any(abs(c['j']-j)<=4 for j in js):
                for k in (ci-2,ci-1,ci,ci+1):
                    if 0<=k<len(curves)-1: local.add((k,k+1))
        optimize_pairs(sorted(local), 4)
    for c in curves: refresh(c); c['Rfit']=c['R']
    log(f'  ajuste base {time.time()-t0:.1f}s')
    # ---- factibilidad global ----
    def feasibility(maxit=80):
        for it in range(maxit):
            bad=0
            for ci,c in enumerate(curves):
                Dp,Dn=avail(ci); T=Tlen(c); lim=min(Dp,Dn)
                if T>lim+1e-6:
                    bad+=1
                    if lim<=0.3:
                        c['R']=max(c['R']*0.9,prm['R_ABS'])
                        if ci>0 and Dp<=Dn: curves[ci-1]['R']=max(curves[ci-1]['R']*0.9,prm['R_ABS'])
                        if ci+1<len(curves) and Dn<Dp: curves[ci+1]['R']=max(curves[ci+1]['R']*0.9,prm['R_ABS'])
                    else: c['R']=max(c['R']*(lim/T),prm['R_ABS'])
            if bad==0: return True
        return False
    ok=feasibility()
    if not ok:
        bad=[]
        for ci in range(len(curves)-1):
            D=np.dot(curves[ci+1]['PI']-curves[ci]['PI'],curves[ci]['uout'])
            if Tlen(curves[ci])+Tlen(curves[ci+1])>D+1e-6: bad.append((ci,ci+1)); seq[curves[ci]['j']+1][1]['virtual']=True
        log(f'  tangentes infactibles: {len(bad)} -> se reoptimizan como virtuales')
        optimize_pairs(bad,2)
        for c in curves: refresh(c)
        ok=feasibility()
        if not ok:
            for ci in range(len(curves)-1):
                D=np.dot(curves[ci+1]['PI']-curves[ci]['PI'],curves[ci]['uout']); T1=Tlen(curves[ci]); T2=Tlen(curves[ci+1])
                if T1+T2>D+1e-6:
                    f=D/(T1+T2)
                    for c in (curves[ci],curves[ci+1]): c['R']=max(c['R']*f,prm['R_ABS']); c['forced']=True
            log('  AVISO: radios forzados por debajo del minimo de volteo en algun punto (revisar)')
    # ---- subir radios al minimo normativo ----
    for ci,c in enumerate(curves):
        if c['R']<prm['RMIN_NORM']-1e-6:
            Dp,Dn=avail(ci); td=math.tan(abs(c['delta'])/2); Rmax=min(Dp,Dn)/td if td>1e-9 else 1e9
            Rup=min(prm['RMIN_NORM'],Rmax)
            if Rup>c['R']+0.05:
                d=dist_circ(c['Q'],c['PI'],c['uin'],c['uout'],c['delta'],Rup)
                if d.max()<=prm['TOL_UP']: c['R']=Rup; c['raised']=True
    for c in curves:
        R=c['R']; m=5 if R<100 else 10 if R<500 else 50; Rr=math.floor(R/m+1e-9)*m
        c['R']=Rr if (Rr>=prm['R_FLOOR'] and (R-Rr<0.4*m or Rr>=prm['RMIN_NORM'])) else round(R,1)
        if c['R']<prm['R_FLOOR']: c['volteo_bajo']=True
    if not feasibility(40):
        for ci in range(len(curves)-1):
            D=np.dot(curves[ci+1]['PI']-curves[ci]['PI'],curves[ci]['uout']); T1=Tlen(curves[ci]); T2=Tlen(curves[ci+1])
            if T1+T2>D+1e-6:
                f=D/(T1+T2)
                for c in (curves[ci],curves[ci+1]): c['R']=max(c['R']*f,prm['R_ABS']); c['forced']=True
    if spirals:
        for ci,c in enumerate(curves):
            R=c['R']
            if R>=prm['R_NO_SPIRAL'] or R<prm['LS_MIN']: continue
            Ls=prm['LS_NORM'] if R>=prm['LS_NORM'] else prm['LS_MIN']
            if Ls>R: continue
            g=scs_geom(c['PI'],c['uin'],c['uout'],c['delta'],R,Ls)
            if g is None or g['Larc']<prm['V']/3.6: c['spiral_fail']='arco insuficiente'; continue
            c['Ls']=Ls; Dp,Dn=avail(ci)
            if g['T']>min(Dp,Dn)+1e-6: c['Ls']=0.0; c['spiral_fail']='no cabe'
    for c in curves:
        g=scs_geom(c['PI'],c['uin'],c['uout'],c['delta'],c['R'],c['Ls']); c['g']=g
        d=dist_pts_poly(c['Q'],sample_scs(g)) if c['Ls']>0 else dist_circ(c['Q'],c['PI'],c['uin'],c['uout'],c['delta'],c['R'])
        c['dmax']=float(d.max()); c['drms']=float(np.sqrt((d**2).mean()))
        c['Avirtual']=seq[c['j']-1][1]['virtual']; c['Bvirtual']=seq[c['j']+1][1]['virtual']
    for ci in range(len(curves)-1):
        D=np.dot(curves[ci+1]['PI']-curves[ci]['PI'],curves[ci]['uout']); T1=Tlen(curves[ci]); T2=Tlen(curves[ci+1])
        if T1+T2>D+1e-3: log(f"  NEG: C{ci+1}-C{ci+2} s={s[curves[ci]['i0']]:.0f} D={D:.1f} T1={T1:.1f} T2={T2:.1f} R1={curves[ci]['R']:.1f} R2={curves[ci+1]['R']:.1f} d1={math.degrees(curves[ci]['delta']):.0f} d2={math.degrees(curves[ci+1]['delta']):.0f} virt={seq[curves[ci]['j']+1][1]['virtual']}")
    m=Model(); m.s,m.x,m.y,m.th,m.k,m.curves,m.start,m.end,m.seq=s,x,y,th,k,curves,start,end,seq
    log(f'  total {time.time()-t0:.1f}s')
    return m

def assemble(m):
    curves=m.curves; els=[]; sta=0.0
    c0=curves[0]; pos=c0['PI']-c0['uin']*np.dot(c0['PI']-m.start,c0['uin'])
    for ci,c in enumerate(curves):
        g=c['g']; L=float(np.dot(g['TS']-pos,c['uin']))
        els.append(dict(type='Line',sta=sta,L=L,A=pos.copy(),B=g['TS'].copy(),u=c['uin'])); sta+=L
        if g['Ls']>0: els.append(dict(type='Spiral',sta=sta,L=g['Ls'],A=g['TS'],B=g['SC'],R=g['R'],left=g['left'],g=g,entry=True,ci=ci)); sta+=g['Ls']
        els.append(dict(type='Curve',sta=sta,L=g['Larc'],A=g['SC'],B=g['CS'],C=g['C'],R=g['R'],left=g['left'],g=g,ci=ci)); sta+=g['Larc']
        if g['Ls']>0: els.append(dict(type='Spiral',sta=sta,L=g['Ls'],A=g['CS'],B=g['ST'],R=g['R'],left=g['left'],g=g,entry=False,ci=ci)); sta+=g['Ls']
        pos=g['ST'].copy()
    cl=curves[-1]; endp=cl['PI']+cl['uout']*np.dot(m.end-cl['PI'],cl['uout']); L=float(np.dot(endp-pos,cl['uout']))
    els.append(dict(type='Line',sta=sta,L=L,A=pos,B=endp,u=cl['uout'])); sta+=L
    pts=[]
    for e in els:
        if e['type']=='Line': pts.append(np.array([e['A'],e['B']]))
        elif e['type']=='Curve':
            a0=ang(e['A']-e['C']); nn=max(int(e['L'])+2,3); sgn=1 if e['left'] else -1
            aa=a0+sgn*np.linspace(0,e['L']/e['R'],nn); pts.append(np.stack([e['C'][0]+e['R']*np.cos(aa),e['C'][1]+e['R']*np.sin(aa)],1))
        else:
            g=e['g']; xs,ys=clothoid_xy(g['Ls'],g['R'])
            if e['entry']: pts.append(g['TS'][None,:]+xs[:,None]*g['uin'][None,:]+ys[:,None]*rot90(g['uin'],g['left'])[None,:])
            else: q=g['ST'][None,:]-xs[:,None]*g['uout'][None,:]+ys[:,None]*rot90(g['uout'],g['left'])[None,:]; pts.append(q[::-1])
    return els, sta, np.vstack(pts)

def report(m, els, Ltot, poly, sp):
    Q=np.stack([m.x,m.y],1); d=dist_pts_poly(Q,poly); cs=m.curves
    print(f"curvas {len(cs)} | tangentes reales {sum(1 for e in m.seq if e[0]=='T' and not e[1]['virtual'])} virtuales {sum(1 for e in m.seq if e[0]=='T' and e[1]['virtual'])}")
    print(f"longitud eje {Ltot:.1f} m (trazo {m.s[-1]:.1f}); desvio lateral trazo->eje: max {d.max():.2f} med {d.mean():.2f} p95 {np.percentile(d,95):.2f}; >1.5m: {(d>1.5).sum()} m >2.5m: {(d>2.5).sum()} m >4m: {(d>4).sum()} m")
    R=np.array([c['R'] for c in cs])
    print('R>=45:',(R>=45).sum(),' 25-45:',((R>=25)&(R<45)).sum(),' <25:',(R<25).sum(),' minR',R.min(),' subidos',sum(1 for c in cs if c.get('raised')), ' kinds',{k:sum(1 for c in cs if c['kind']==k) for k in set(c['kind'] for c in cs)})
    LL=np.array([e['L'] for e in els if e['type']=='Line'])
    print('tangentes:',len(LL),' <1m:',(LL<1).sum(),' 1-20:',((LL>=1)&(LL<20)).sum(),' 20-56:',((LL>=20)&(LL<56)).sum(),' >=56:',(LL>=56).sum(),' negativas:',(LL<-0.01).sum(),' min',LL.min().round(3))
    if sp: print('con espiral:',sum(1 for c in cs if c['Ls']>0),' sin (no cabe/arco):',sum(1 for c in cs if c.get('spiral_fail')))
    print('peores curvas:')
    for c in sorted(cs,key=lambda c:-c['dmax'])[:8]:
        print(f"  s={m.s[c['i0']]:.0f}-{m.s[min(c['i1'],len(m.s)-1)]:.0f} kind={c['kind']} R={c['R']:.1f} Rfit={c['Rfit']:.1f} d={math.degrees(c['delta']):.1f} dmax={c['dmax']:.2f} A={'v' if c['Avirtual'] else 'r'} B={'v' if c['Bvirtual'] else 'r'}")
    return d

if __name__=='__main__':
    P=np.load('pts.npy')[:,[1,0]]; sp='--spirals' in sys.argv
    m=build(P, spirals=sp); els,Ltot,poly=assemble(m); d=report(m,els,Ltot,poly,sp)
    pickle.dump(dict(els=els,Ltot=Ltot,poly=poly,curves=[{k:v for k,v in c.items() if k not in('Q',)} for c in m.curves],d=d,s=m.s,x=m.x,y=m.y,prm=PRM),open('model_sp.pkl' if sp else 'model.pkl','wb'))
