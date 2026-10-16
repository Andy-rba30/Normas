"""Planta general del eje corregido vs trazo actual, en PNG (PIL)."""
import pickle, numpy as np, math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont
m=pickle.load(open(sys.argv[1],'rb')); out=sys.argv[2]; title=sys.argv[3] if len(sys.argv)>3 else ''
x=m['x']; y=m['y']; els=m['els']; cs=m['curves']; d=m['d']
pad=80; xmin,xmax,ymin,ymax=x.min()-pad,x.max()+pad,y.min()-pad,y.max()+pad
W=4200; sc=W/(xmax-xmin); H=int((ymax-ymin)*sc)+160
img=Image.new('RGB',(W,H),'white'); dr=ImageDraw.Draw(img)
try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22); fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',30); fs=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)
except Exception: f=fb=fs=ImageFont.load_default()
def T(px,py): return ((px-xmin)*sc, (ymax-py)*sc+120)
# cuadricula 500 m
for gx in np.arange(math.floor(xmin/500)*500, xmax, 500):
    dr.line([T(gx,ymin),T(gx,ymax)],fill=(225,225,225)); dr.text((T(gx,ymax)[0]+3,T(gx,ymax)[1]+2),f'E {gx:.0f}',fill=(120,120,120),font=fs)
for gy in np.arange(math.floor(ymin/500)*500, ymax, 500):
    dr.line([T(xmin,gy),T(xmax,gy)],fill=(225,225,225)); dr.text((T(xmin,gy)[0]+3,T(xmin,gy)[1]-16),f'N {gy:.0f}',fill=(120,120,120),font=fs)
dr.line([T(a,b) for a,b in zip(x,y)],fill=(150,150,150),width=3)
for e in els:
    if e['type']=='Line': dr.line([T(*e['A']),T(*e['B'])],fill=(21,101,192),width=3)
    elif e['type']=='Curve':
        a0=math.atan2(e['A'][1]-e['C'][1],e['A'][0]-e['C'][0]); sgn=1 if e['left'] else -1; n=max(int(e['L'])+2,3)
        aa=a0+sgn*np.linspace(0,e['L']/e['R'],n); q=[T(e['C'][0]+e['R']*math.cos(a),e['C'][1]+e['R']*math.sin(a)) for a in aa]
        R=e['R']; col=(27,158,58) if R>=45 else (255,152,0) if R>=25 else (211,47,47); dr.line(q,fill=col,width=5)
    else:
        g=e['g']; from fit_axis import clothoid_xy, rot90
        xs,ys=clothoid_xy(g['Ls'],g['R'],30)
        pts=(g['TS'][None,:]+xs[:,None]*g['uin'][None,:]+ys[:,None]*rot90(g['uin'],g['left'])[None,:]) if e['entry'] else (g['ST'][None,:]-xs[:,None]*g['uout'][None,:]+ys[:,None]*rot90(g['uout'],g['left'])[None,:])
        dr.line([T(a,b) for a,b in pts],fill=(142,36,170),width=5)
# progresivas cada 500 m
sta=0.0
for e in els:
    for k in range(int(sta//500)+1, int((sta+e['L'])//500)+1):
        t=(k*500-sta)/max(e['L'],1e-9)
        if e['type']=='Curve':
            a0=math.atan2(e['A'][1]-e['C'][1],e['A'][0]-e['C'][0]); sgn=1 if e['left'] else -1; a=a0+sgn*(e['L']/e['R'])*t; p=(e['C'][0]+e['R']*math.cos(a),e['C'][1]+e['R']*math.sin(a))
        else: p=e['A']+(e['B']-e['A'])*t
        P=T(*p); dr.ellipse([P[0]-6,P[1]-6,P[0]+6,P[1]+6],fill=(0,0,0)); dr.text((P[0]+8,P[1]-10),f'{k*0.5:.1f}',fill=(0,0,0),font=f)
    sta+=e['L']
# zonas con desvio > 2.5 m marcadas en magenta sobre el trazo
for i in np.where(d>2.5)[0][::2]:
    P=T(x[i],y[i]); dr.ellipse([P[0]-3,P[1]-3,P[0]+3,P[1]+3],fill=(255,0,200))
dr.text((20,15),title or 'Eje corregido DG-2018 (V = 40 km/h) sobre el trazo actual',fill=(0,0,0),font=fb)
leg=[((150,150,150),'Trazo actual'),((21,101,192),'Tangentes'),((27,158,58),'Curvas R >= 45 m (cumple)'),((255,152,0),'Curvas 25-45 m (excepcional, Ve 30 km/h)'),((211,47,47),'Curvas R < 25 m (curva de vuelta)'),((142,36,170),'Clotoides'),((255,0,200),'Desvio trazo-eje > 2.5 m'),((0,0,0),'Progresiva (km)')]
xx=20
for col,t in leg:
    dr.line([(xx,70),(xx+40,70)],fill=col,width=6); dr.text((xx+48,58),t,fill=(0,0,0),font=f); xx+=48+f.getlength(t)+30
img.save(out); print('saved',out,img.size)
