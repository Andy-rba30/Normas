"""Verifica continuidad (posicion y direccion) de un alineamiento LandXML con Line/Curve/Spiral."""
import sys, math, xml.etree.ElementTree as ET, numpy as np
ns='{http://www.landxml.org/schema/LandXML-1.2}'
r=ET.parse(sys.argv[1]).getroot(); al=r.find(f'{ns}Alignments/{ns}Alignment'); cg=al.find(ns+'CoordGeom')
def pt(e,tag): t=e.find(ns+tag).text.split(); return np.array([float(t[1]),float(t[0])])  # (E,N)
els=[]
for e in cg:
    tag=e.tag.split('}')[1]
    if tag=='Line': A=pt(e,'Start'); B=pt(e,'End'); u=(B-A)/np.linalg.norm(B-A); els.append((tag,A,B,u,u,np.linalg.norm(B-A)))
    elif tag=='Curve':
        A=pt(e,'Start'); B=pt(e,'End'); C=pt(e,'Center'); R=float(e.get('radius')); left=e.get('rot')=='ccw'
        def tang(P):
            v=P-C; t=np.array([-v[1],v[0]]) if left else np.array([v[1],-v[0]]); return t/np.linalg.norm(t)
        rA=np.linalg.norm(A-C); rB=np.linalg.norm(B-C)
        if abs(rA-R)>1e-3 or abs(rB-R)>1e-3: print('RADIO INCONSISTENTE', R, rA, rB)
        els.append((tag,A,B,tang(A),tang(B),float(e.get('length'))))
    elif tag=='Spiral':
        A=pt(e,'Start'); B=pt(e,'End'); P=pt(e,'PI'); uA=(P-A)/np.linalg.norm(P-A); uB=(B-P)/np.linalg.norm(B-P)
        els.append((tag,A,B,uA,uB,float(e.get('length'))))
gap=0; ang=0; worst=None
for (t1,A1,B1,u1a,u1b,L1),(t2,A2,B2,u2a,u2b,L2) in zip(els[:-1],els[1:]):
    g=np.linalg.norm(B1-A2); a=math.degrees(math.acos(max(-1,min(1,float(np.dot(u1b,u2a))))))
    if g>gap: gap=g
    if a>ang: ang=a; worst=(t1,t2,A2)
Ls=np.array([e[5] for e in els]); n_tiny=(Ls<0.05).sum()
print(f'elementos {len(els)}: lineas {sum(1 for e in els if e[0]=="Line")} curvas {sum(1 for e in els if e[0]=="Curve")} espirales {sum(1 for e in els if e[0]=="Spiral")}')
print(f'max salto de posicion entre elementos {gap*1000:.3f} mm; max quiebre de direccion {ang:.4f} grados {worst if ang>0.01 else ""}; elementos < 5 cm: {n_tiny}; longitud total {Ls.sum():.3f} vs atributo {al.get("length")}')
