import sys, math, xml.etree.ElementTree as ET
ns='{http://www.landxml.org/schema/LandXML-1.2}'
r=ET.parse(sys.argv[1]).getroot()
al=r.find(f'{ns}Alignments/{ns}Alignment'); print('name',al.get('name'),'length',al.get('length'),'staStart',al.get('staStart'))
for e in al: 
    if e.tag!=ns+'CoordGeom': print(e.tag.split('}')[1], e.attrib, [(c.tag.split('}')[1],c.attrib,(c.text or '')[:60]) for c in e])
cg=al.find(ns+'CoordGeom'); pts=[]
for el in cg:
    assert el.tag==ns+'Line', el.tag
    s=el.find(ns+'Start').text.split(); e=el.find(ns+'End').text.split()
    s=(float(s[0]),float(s[1])); e=(float(e[0]),float(e[1]))  # LandXML: Northing Easting
    if not pts: pts.append(s)
    else:
        d=math.hypot(pts[-1][0]-s[0],pts[-1][1]-s[1])
        if d>1e-6: print('GAP',len(pts),d)
    pts.append(e)
print('vertices',len(pts))
import numpy as np
P=np.array(pts)  # N,E
seg=np.diff(P,axis=0); L=np.hypot(seg[:,0],seg[:,1]); hd=np.degrees(np.arctan2(seg[:,1],seg[:,0]))  # azimuth from north (N,E)
dfl=(np.diff(hd)+180)%360-180
print('total length',L.sum(),'min seg',L.min(),'max seg',L.max(),'mean',L.mean())
print('N range',P[:,0].min(),P[:,0].max(),'E range',P[:,1].min(),P[:,1].max())
print('deflection abs: >90:',(abs(dfl)>90).sum(),' 45-90:',((abs(dfl)>45)&(abs(dfl)<=90)).sum(),' 20-45:',((abs(dfl)>20)&(abs(dfl)<=45)).sum(),' 5-20:',((abs(dfl)>5)&(abs(dfl)<=20)).sum(),' <=5:',(abs(dfl)<=5).sum())
# cumulative station of vertices
sta=np.concatenate([[0],np.cumsum(L)])
# print big deflections with station
big=[(round(sta[i+1],1),round(dfl[i],1),round(L[i],1),round(L[i+1],1)) for i in range(len(dfl)) if abs(dfl[i])>40]
print('big deflections (sta, dfl, Lprev, Lnext):'); print(big)
# heading change over 100 m windows to find switchbacks
cum=np.concatenate([[0],np.cumsum(dfl)])
sw=[]
for i in range(len(sta)-1):
    j=np.searchsorted(sta,sta[i]+120)
    if j<len(cum) and abs(cum[min(j,len(cum)-1)]-cum[i])>140: sw.append((round(sta[i]),round(cum[min(j,len(cum)-1)]-cum[i])))
print('switchback-like windows (sta start, heading change over 120 m):',len(sw)); print(sw[:80])
np.save('pts.npy',P)
