import re, math, pickle, numpy as np, sys
svg=open(sys.argv[1]).read(); m=pickle.load(open(sys.argv[2],'rb'))
vb=re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"',svg); W=float(vb.group(1)); H=float(vb.group(2))
poly=m['poly']; x=m['x']; y=m['y']
x0=min(poly[:,0].min(),x.min())-60; y1=max(poly[:,1].max(),y.max())+60
paths=re.findall(r'<path d="M ([\d.\-]+) ([\d.\-]+) A ([\d.]+) [\d.]+ 0 ([01]) ([01]) ([\d.\-]+) ([\d.\-]+)"',svg)
curves=[e for e in m['els'] if e['type']=='Curve']
assert len(paths)==len(curves), (len(paths),len(curves))
bad=0; worst=0
for (sx,sy,r,fa,fs,ex,ey),e in zip(paths,curves):
    x1,y1_,x2,y2=float(sx),float(sy),float(ex),float(ey); r=float(r); fa=int(fa); fs=int(fs)
    # centro implicito segun SVG (F.6.5), sin rotacion y rx=ry=r
    dx=(x1-x2)/2; dy=(y1_-y2)/2; num=r*r*r*r-r*r*dy*dy-r*r*dx*dx; den=r*r*dy*dy+r*r*dx*dx
    coef=math.sqrt(max(num/den,0)); 
    if fa==fs: coef=-coef
    cxp=coef*(r*dy/r); cyp=coef*(-r*dx/r)
    cx=cxp+(x1+x2)/2; cy=cyp+(y1_+y2)/2
    Cx=e['C'][0]-x0; Cy=y1-e['C'][1]
    d=math.hypot(cx-Cx,cy-Cy); worst=max(worst,d)
    if d>0.5: bad+=1
print('arcos',len(paths),'centros inconsistentes',bad,'max error centro (m)',round(worst,3))
