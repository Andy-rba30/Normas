import pickle, numpy as np, math, sys
from PIL import Image, ImageDraw
m=pickle.load(open(sys.argv[1],'rb')); s=m['s']; x=m['x']; y=m['y']; els=m['els']; cs=m['curves']; poly=m['poly']
s0=float(sys.argv[2]); s1=float(sys.argv[3]); out=sys.argv[4]
i0=int(s0); i1=int(s1); X=x[i0:i1+1]; Y=y[i0:i1+1]
pad=25; xmin,xmax,ymin,ymax=X.min()-pad,X.max()+pad,Y.min()-pad,Y.max()+pad
W=1100; sc=W/(xmax-xmin); H=int((ymax-ymin)*sc)+1
img=Image.new('RGB',(W,H),'white'); dr=ImageDraw.Draw(img)
def T(px,py): return ((px-xmin)*sc, (ymax-py)*sc)
# grid 10 m
for gx in np.arange(math.floor(xmin/10)*10, xmax, 10): dr.line([T(gx,ymin),T(gx,ymax)],fill=(235,235,235))
for gy in np.arange(math.floor(ymin/10)*10, ymax, 10): dr.line([T(xmin,gy),T(xmax,gy)],fill=(235,235,235))
# trazo
pts=[T(a,b) for a,b in zip(x[max(i0-40,0):i1+40],y[max(i0-40,0):i1+40])]; dr.line(pts,fill=(140,140,140),width=3)
for k in range(max(i0-40,0),i1+40,10):
    if k<len(x): dr.ellipse([T(x[k],y[k])[0]-2,T(x[k],y[k])[1]-2,T(x[k],y[k])[0]+2,T(x[k],y[k])[1]+2],fill=(90,90,90)); 
    if k<len(x) and k%50==0: dr.text((T(x[k],y[k])[0]+4,T(x[k],y[k])[1]),f'{k}',fill=(60,60,60))
# eje
pp=[T(a,b) for a,b in poly if xmin-50<a<xmax+50 and ymin-50<b<ymax+50]
# dibujar por elementos para colorear
for e in els:
    if e['sta']+e['L']<s0-60 or e['sta']>s1+60: continue
    if e['type']=='Line': dr.line([T(*e['A']),T(*e['B'])],fill=(21,101,192),width=3)
    elif e['type']=='Curve':
        a0=math.atan2(e['A'][1]-e['C'][1],e['A'][0]-e['C'][0]); sgn=1 if e['left'] else -1; n=max(int(e['L'])+2,3)
        aa=a0+sgn*np.linspace(0,e['L']/e['R'],n); q=[T(e['C'][0]+e['R']*math.cos(a),e['C'][1]+e['R']*math.sin(a)) for a in aa]
        R=e['R']; col=(27,158,58) if R>=45 else (255,152,0) if R>=25 else (211,47,47)
        dr.line(q,fill=col,width=4)
        c=cs[e['ci']]; g=c['g']; P=T(*g['PI']); dr.ellipse([P[0]-4,P[1]-4,P[0]+4,P[1]+4],outline=col,width=2)
        dr.text((P[0]+5,P[1]-12),f"C{e['ci']+1} R{R:.1f} d{math.degrees(c['delta']):.0f}{'v' if c['Avirtual'] else 'r'}{'v' if c['Bvirtual'] else 'r'}",fill=col)
        # tangentes in/out como lineas finas
        for u,sg in ((g['uin'],-1),(g['uout'],1)):
            A=g['PI']+u*sg*0; B=g['PI']+u*sg*40; dr.line([T(*A),T(*B)],fill=(200,200,255),width=1)
    else:
        q=[T(a,b) for a,b in poly]  # simplificado
dr.text((10,10),f's={s0:.0f}-{s1:.0f}  (gris: trazo; azul: tangentes; verde/naranja/rojo: curvas por radio; cuadricula 10 m)',fill=(0,0,0))
img.save(out); print('saved',out,img.size)
