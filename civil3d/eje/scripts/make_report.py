import sys, os, math, datetime, numpy as np
sys.path.insert(0,'/tmp/claude-0/-home-user-Normas/1d8bfce3-3294-5b1e-ace9-ad5fa4f1a13c/scratchpad/aln')
os.chdir('/tmp/claude-0/-home-user-Normas/1d8bfce3-3294-5b1e-ace9-ad5fa4f1a13c/scratchpad/aln')
import write_outputs as W
m=W.load('model.pkl'); rows=W.curve_rows(m); cs=m['curves']; d=m['d']; n=len(rows)
V=40.0
def sta(s): return W.sta_fmt(s)
def ve(R): return math.sqrt(127*R*(0.12+0.17))   # velocidad especifica con p=12%, f=0.17 (Tabla 302.02, 30-40 km/h)
R=np.array([r['R'] for r in rows])
cum50=(R>=50-0.06).sum(); cum45=((R>=45-0.06)&(R<50-0.06)).sum(); exc=((R>=25)&(R<45-0.06)).sum(); vol=(R<25).sum()
raised=[r for r,c in zip(rows,cs) if c.get('raised')]
at45=[r for r in rows if abs(r['R']-45)<0.07]
excs=[r for r in rows if 25<=r['R']<45-0.06]
vols=[r for r in rows if r['R']<25]
ri=[(r,W.ri_volteo(r['R'])) for r in vols]
ri8=sum(1 for _,x in ri if x>=8); ri6=sum(1 for _,x in ri if 6<=x<8); ri0=sum(1 for _,x in ri if x<6)
tn=[r['tan_next'] for r in rows[:-1]]
same=[(rows[i]['sentido']==rows[i+1]['sentido']) for i in range(n-1)]
tan_ok=sum(1 for t,s in zip(tn,same) if t>=(111 if s else 56))
tan_cls={'0 (curvas enlazadas)':sum(1 for t in tn if t<0.05),'0 a 20 m':sum(1 for t in tn if 0.05<=t<20),'20 a 56 m':sum(1 for t in tn if 20<=t<56),'56 a 111 m':sum(1 for t in tn if 56<=t<111),'más de 111 m':sum(1 for t in tn if t>=111)}
small=[r for r in rows if r['delta']<5]
ratio_ok=sum(1 for r in rows[:-1] if 'relacion de radios' not in r['obs'])
hot=[r for r in rows if r['dmax']>2.5]
Ltot=m['Ltot']; L0=m['s'][-1]
# zonas de volteo
grp=[]; cur=[]
for r in rows:
    if r['R']<25: cur.append(r)
    elif cur: grp.append(cur); cur=[]
if cur: grp.append(cur)

L=[]; A=L.append
A('---'); A('title: "Memoria de diseño geométrico en planta"'); A('subtitle: "Eje EJE DG2018 V40 CIRCULAR, ajustado al trazo existente según el Manual de Carreteras: Diseño Geométrico DG-2018"'); A(f'date: "{datetime.date.today().strftime("%d/%m/%Y")}"'); A('lang: es'); A('---'); A('')
A('# 1. Objeto y alcance'); A('')
A(f'Este documento describe el eje en planta contenido en el archivo `EJE_DG2018_circular.xml` (LandXML 1.2, alineamiento "EJE DG2018 V40 CIRCULAR", longitud {Ltot:,.2f} m), obtenido a partir de la poligonal del trazo existente `PROCESAMIENTO DISEÑO GEOMETRICO` ({L0:,.2f} m, {1181} vértices, UTM WGS84 zona 17 Sur), y contrasta cada parámetro adoptado con lo que exige el Manual de Carreteras: Diseño Geométrico DG-2018 (MTC, revisada y corregida a enero de 2018).')
A('')
A('Premisas del proyecto: carretera de Segunda Clase, velocidad de diseño 40 km/h, tramos en zona poblada donde se busca la mínima expropiación. Por ello el eje se ajustó al trazo actual y solo se regularizó la geometría (tangentes rectas y curvas circulares), aceptando radios excepcionales y curvas de vuelta donde el terreno y las edificaciones no permiten el radio normativo.')
A('')
A('# 2. Parámetros de diseño adoptados y contraste con la DG-2018'); A('')
A('| Parámetro | Valor adoptado | Lo que indica la DG-2018 (cita) | Referencia | Situación en el eje |')
A('|------------|-----------|------------------------------------------|---------|------------------------|')
A('| Clasificación por demanda | Carretera de Segunda Clase | "Son carreteras con IMDA entre 2 000 y 400 veh/día, con una calzada de dos carriles de 3.30 m de ancho como mínimo (...) La superficie de rodadura de estas carreteras debe ser pavimentada." | Tópico 101.04 | Dato del proyecto. |')
A('| Clasificación por orografía | Terreno escarpado (tipo 4) | "Tiene pendientes transversales al eje de la vía superiores al 100% y sus pendientes longitudinales excepcionales son superiores al 8%, exigiendo el máximo de movimiento de tierras." | Tópico 102.04 | Adoptado porque es la única orografía en la que la Tabla 204.01 admite 40 km/h para Segunda Clase (en terreno accidentado el rango es 50 a 80 km/h). |')
A('| Velocidad de diseño | 40 km/h | Tabla 204.01: Carretera de Segunda Clase, escarpado, rango 40 a 70 km/h. | Tabla 204.01 | Cumple (límite inferior del rango). |')
A('| Velocidad específica en elementos puntuales | 30 km/h en curvas excepcionales | "La velocidad máxima con que sería abordado cada elemento geométrico, es la Velocidad Específica con la que se debe diseñar (...) La condición deseable es que a la mayoría de los elementos geométricos que integran el tramo homogéneo se les pueda asignar como Velocidad Específica, el valor de la Velocidad de Diseño del tramo." | Tópico 204.03 | Las curvas con 25 m ≤ R < 45 m se diseñan con Ve = 30 km/h y requieren señalización de velocidad. |')
A('| Peralte máximo | 12 % absoluto (8 % normal) | Tabla 304.05: "Zona rural (T. Accidentado o Escarpado): 12.0 absoluto, 8.0 % normal". | Tabla 304.05 | El radio mínimo se calcula con 12 %. |')
A('| Fricción transversal máxima | 0.17 | Tabla 302.02: f máx = 0.17 para 30 y 40 km/h. | Tabla 302.02 | - |')
A(f'| Radio mínimo normativo | 45 m | Tabla 302.02, área rural accidentada o escarpada: "40 km/h, p máx 12.00 %, f máx 0.17, radio calculado 43.4 m, radio redondeado 45 m". | Tabla 302.02 | {cum50+cum45} curvas de {n} ({100*(cum50+cum45)/n:.0f} %) tienen R ≥ 45 m. |')
A(f'| Radio mínimo con peralte normal 8 % | 50 m | Tabla 302.02, área rural plana u ondulada: "40 km/h, 8.00 %, 0.17, 50.4 m, 50 m". | Tabla 302.02 | {cum50} curvas ({100*cum50/n:.0f} %) tienen R ≥ 50 m y pueden peraltarse con 8 %. |')
A(f'| Radio excepcional | 25 m ≤ R < 45 m | La DG-2018 no define un radio mínimo excepcional para carreteras de Segunda Clase. Se adopta el radio mínimo de la fila de 30 km/h de la Tabla 302.02: "30 km/h, 12.00 %, 0.17, 24.4 m, 25 m", es decir, la curva se diseña con velocidad específica de 30 km/h. | Tabla 302.02 y Tópico 204.03 | {exc} curvas ({100*exc/n:.0f} %). Listado en el capítulo 6.2. |')
A(f'| Curvas de vuelta | Radio interior Ri ≥ 8 m (normal) o 6 m (absoluto); Re según Tabla 302.12 | "Son aquellas curvas que se proyectan sobre una ladera, en terrenos accidentados, con el propósito de obtener o alcanzar una cota mayor (...) Este tipo de curvas no se emplearán en autopistas, en tanto que en carreteras de Primera Clase podrán utilizarse en casos excepcionales (...) El radio interior de 8 m, representa un mínimo normal. El radio interior de 6 m, representa un mínimo absoluto y sólo podrá ser usado en forma excepcional." | Tópico 302.07 y Tabla 302.12 | {vol} curvas con R de eje < 25 m ({100*vol/n:.0f} %): {ri8} con Ri ≥ 8 m, {ri6} con 6 ≤ Ri < 8 m y {ri0} con Ri < 6 m (no cumplen ni el mínimo absoluto). Capítulo 6.3. |')
A('| Radio a partir del cual no se requiere peralte | 3 500 m (V = 40 km/h) | Tabla 304.04: "Velocidad 40 km/h: radio 3 500 m". | Tabla 304.04 | Ninguna curva del eje supera 3 500 m; todas se peraltan. |')
A('| Peralte mínimo | 2 % para 2 500 ≤ R < 3 500 m | Tabla 304.06: "40 ≤ V < 100: 2 500 ≤ R < 3 500". | Tabla 304.06 | - |')
A('| Transición del peralte | ipmáx = 1.8 − 0.01 V = 1.4 %; Lmín = (pf − pi)/ipmáx · B | "ipmáx = 1.8 − 0.01 V (...) Lmín = (pf − pi)/ipmáx · B". | Tópico 302.08 | Para Civil 3D se entrega el archivo de criterios DG2018_Corregido_2.xml (tablas "DG2018 _PMax 12%" y método "DG2018 METRICO"). |')
A(f'| Longitud mínima de tangentes | 56 m entre curvas en S; 111 m entre curvas del mismo sentido; máx. deseable 668 m | Tabla 302.01: "40 km/h: L mín.s 56, L mín.o 111, L máx 668". | Tabla 302.01 | Solo {tan_ok} de {n-1} tangentes intermedias cumplen. Limitación propia del trazo existente (capítulo 6.4). |')
A(f'| Longitud mínima de curva | 3V = 120 m; para Δ ≤ 5°: L > 30(10 − Δ); nunca Δ < 59′ | "La longitud mínima de curva (L) será: carreteras de dos carriles 3V (...) En el caso de ángulos de deflexión Δ pequeños, iguales o inferiores a 5º (...) L > 30(10 − Δ) (...) No se usará nunca ángulos de deflexión menores de 59\' (minutos)." | Tópico 302.02 | Ninguna curva alcanza 120 m (la mayor tiene {max(r["Ltot"] for r in rows):.0f} m). {len(small)} curvas tienen Δ < 5°; ninguna tiene Δ < 59′. |')
A(f'| Curvas de transición (clotoides) | No incluidas en esta variante | Tabla 302.11A: para 40 km/h se puede prescindir de la transición si R ≥ 150 m. Tabla 302.10: longitud mínima de transición 40 m a 40 km/h; "En ningún caso se adoptarán longitudes de transición menores a 30 m". Tópico 302.05.06: R/3 ≤ A ≤ R. | Tópicos 302.05.06 y 302.05.07, Tablas 302.10 y 302.11A | {sum(1 for r in rows if r["R"]<150)} curvas tienen R < 150 m y requerirían clotoide; con Le = 40 m solo cabe en 5 (variante EJE_DG2018_clotoides.xml) porque las tangentes disponibles son demasiado cortas. |')
A(f'| Relación entre radios consecutivos | Tabla 302.08 (grupo 2) | "cuando se enlacen curvas circulares consecutivas sin tangente intermedia, así como mediante tangente de longitud menor o igual a 200 m, la relación de radios (...) no sobrepasará los valores (...) Grupo 2: Carreteras de Segunda y Tercera Clase." | Tópico 302.04.05 y Tabla 302.08 | {ratio_ok} de {n-1} pares cumplen. |')
A('| Sobreancho | Sa = n(R − √(R² − L²)) + V/(10 √R); mínimo 0.40 m; vehículo B2 con L = 8.25 + 2.30 = 10.55 m | "Sa = n (R − √(R² − L²)) + V/(10√R) (...) Se considera apropiado un valor mínimo de 0.40 m de sobreancho para justificar su adopción." Tabla 202.01: ómnibus de dos ejes B2, separación de ejes 8.25 m, vuelo delantero 2.30 m. | Tópico 302.09.03, Tabla 202.01 | Valor por curva en el Anexo A. En curvas de vuelta el ancho se toma de la Tabla 302.12. |')
A('| Ancho de calzada | 6.00 m | Tabla 304.01: Carretera de Segunda Clase, orografía 4, 40 km/h: 6.60 / 6.60 / 6.60 / 6.00 m según orografía 1 a 4. | Tabla 304.01 | 6.00 m en escarpado (6.60 m si el tramo se clasifica como accidentado). |')
A('| Ancho de bermas | 0.50 m | Tabla 304.02: Segunda Clase, 40 km/h: 1.20 / 1.20 / 0.90 / 0.50 m según orografía. | Tabla 304.02 | 0.50 m en escarpado. |')
A('| Bombeo | 2.0 a 2.5 % | Tabla 304.03: pavimento asfáltico o de concreto, 2.0 % (< 500 mm/año) o 2.5 % (> 500 mm/año). | Tabla 304.03 | Según precipitación de la zona. |')
A('| Visibilidad de parada y de paso | Dp = 50 m; Da = 270 m | Tabla 205.01: "40 km/h: 50 m". Tabla 205.03: "40 km/h: 270 m". | Tablas 205.01 y 205.03 | Verificar banquetas de visibilidad (Tópico 302.10.01) en las curvas de radio menor a 60 m en corte. |')
A('')
A('# 3. Metodología de obtención del eje'); A('')
A('1. La poligonal original se remuestreó cada metro y se calculó el rumbo y la curvatura a lo largo del trazo.')
A('2. Los tramos con radio de curvatura mayor a 250 m se trataron como rectos y se les ajustó una tangente por mínimos cuadrados; cuando algún punto se separaba más de 0.8 m de la recta, la tangente se partió en dos.')
A('3. Cada tramo de curvatura continua del mismo sentido se convirtió en una curva circular, con el PI en la intersección de las tangentes vecinas y el radio ajustado por mínimos cuadrados a los puntos del trazo. Las deflexiones menores de 8° cuya supresión desplaza el eje menos de 0.5 m se absorbieron en la tangente.')
A('4. Entre curvas consecutivas sin recta intermedia (curvas en S o compuestas) la tangente común se optimizó para minimizar la separación respecto al trazo manteniendo la tangencia.')
A(f'5. Donde el radio ajustado resultó menor de 45 m, se subió hasta 45 m siempre que la separación respecto al trazo no superara 2.0 m ({len(raised)} curvas). Los radios se redondearon a múltiplos de 5 m (10 m por encima de 100 m).')
A('6. Las curvas de más de 170° (volteos) se representan con dos arcos consecutivos del mismo radio, porque Civil 3D no admite una curva simple de 180° o más.')
A('')
A('# 4. Resultados globales'); A('')
A('| Indicador | Valor |'); A('|----------------------------|------------|')
A(f'| Longitud del trazo original / del eje corregido | {L0:,.2f} m / {Ltot:,.2f} m |')
A(f'| Número de curvas / tangentes | {n} / {n+1} |')
A(f'| Curvas con R ≥ 50 m (cumple con peralte 8 %) | {cum50} ({100*cum50/n:.0f} %) |')
A(f'| Curvas con 45 ≤ R < 50 m (cumple con peralte 12 %) | {cum45} ({100*cum45/n:.0f} %) |')
A(f'| Curvas excepcionales, 25 ≤ R < 45 m (Ve = 30 km/h) | {exc} ({100*exc/n:.0f} %) |')
A(f'| Curvas de vuelta, R < 25 m | {vol} ({100*vol/n:.0f} %) |')
A(f'| Curvas llevadas al radio mínimo normativo (R = 45 m) | {len(at45)} |')
A(f'| Separación lateral del trazo actual respecto al eje: promedio / percentil 95 / máxima | {d.mean():.2f} m / {np.percentile(d,95):.2f} m / {d.max():.2f} m |')
A(f'| Longitud de trazo con separación mayor a 1.5 m / 2.5 m / 4.0 m | {(d>1.5).sum()} m / {(d>2.5).sum()} m / {(d>4).sum()} m |')
A(f'| Tangentes intermedias que cumplen la Tabla 302.01 | {tan_ok} de {n-1} |')
A(f'| Pares de curvas consecutivas que cumplen la Tabla 302.08 | {ratio_ok} de {n-1} |')
A(f'| Curvas con longitud ≥ 3V = 120 m | 0 de {n} |')
A('')
A('# 5. Interpretación'); A('')
A(f'El {100*(cum50+cum45)/n:.0f} % de las curvas cumple el radio mínimo de la DG-2018 para 40 km/h. El {100*exc/n:.0f} % queda entre 25 y 45 m y debe tratarse como curva excepcional con velocidad específica de 30 km/h y señalización preventiva y reglamentaria. El {100*vol/n:.0f} % restante corresponde a curvas de vuelta y esquinas urbanas con radios de eje entre 6 y 25 m, que es lo que impone la geometría existente; en {ri0} de ellas el radio interior resultante es menor de 6 m, de modo que para cumplir siquiera el mínimo absoluto habría que ampliar la plataforma o expropiar.')
A('')
A('Las longitudes mínimas de tangente, la longitud mínima de curva de 120 m, las clotoides y la relación de radios consecutivos no se cumplen en la mayor parte del eje. No es un defecto del ajuste sino de la premisa de seguir el trazo existente: con curvas cada 35 m en promedio no hay espacio para tangentes de 56 a 111 m ni para espirales de 40 m. Si el proyecto exige cumplir esos parámetros, habrá que rediseñar tramos completos con expropiación.')
A('')
A('# 6. Inventario de curvas por tipo'); A('')
A('## 6.1 Curvas en el radio mínimo normativo (R = 45 m)'); A('')
A(f'{len(at45)} curvas quedan exactamente en el radio mínimo de la Tabla 302.02; de ellas {sum(1 for r,c in zip(rows,cs) if abs(r["R"]-45)<0.07 and c.get("raised"))} fueron llevadas a 45 m desde un radio ajustado menor (separación admitida ≤ 2.0 m). Deben peraltarse con el máximo de 12 %.'); A('')
A('| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | Lc (m) | Sep. máx. trazo (m) | Origen |')
A('|------|---------|---------|---------|------|----|-----|-----|------|----------|')
for r,c in zip(rows,cs):
    if abs(r['R']-45)<0.07: A(f"| C-{r['n']} | {sta(r['sta_PI'])} | {r['PI_N']:.3f} | {r['PI_E']:.3f} | {r['delta']:.1f} | {r['sentido']} | {r['R']:.2f} | {r['Lc']:.1f} | {r['dmax']:.2f} | {'subido al mínimo' if c.get('raised') else 'ajuste al trazo'} |")
A('')
A('## 6.2 Curvas excepcionales (25 m ≤ R < 45 m)'); A('')
A(f'{len(excs)} curvas. La velocidad específica se calcula con Ve = √(127 · R · (0.12 + 0.17)), que reproduce los radios de la Tabla 302.02 para 30 y 40 km/h (25 m → 30 km/h, 45 m → 41 km/h). Todas requieren peralte 12 %, sobreancho y señalización de velocidad máxima 30 km/h.'); A('')
A('| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | Ve (km/h) | Sa (m) | Lc (m) | Sep. máx. trazo (m) |')
A('|------|---------|---------|---------|------|----|-----|------|-----|-----|------|')
for r in excs: A(f"| C-{r['n']} | {sta(r['sta_PI'])} | {r['PI_N']:.3f} | {r['PI_E']:.3f} | {r['delta']:.1f} | {r['sentido']} | {r['R']:.2f} | {ve(r['R']):.0f} | {r['Sa']:.2f} | {r['Lc']:.1f} | {r['dmax']:.2f} |")
A('')
A('## 6.3 Curvas de vuelta (R < 25 m)'); A('')
A(f'{len(vols)} curvas. El radio interior Ri se obtiene de Ri + ancho/2 = R, con el ancho de calzada en curva de vuelta (Re − Ri) de la Tabla 302.12 para la maniobra C2 (camión de dos ejes cruzándose con un vehículo ligero), que considera calzada de 6 m en tangente. Criterio: Ri ≥ 8 m cumple el mínimo normal; 6 ≤ Ri < 8 m es el mínimo absoluto de uso excepcional; Ri < 6 m no cumple.'); A('')
A('| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R eje (m) | Ri (m) | Re (m) | Ancho (m) | Evaluación DG-2018 | Sep. máx. trazo (m) |')
A('|------|---------|---------|---------|------|----|-----|-----|-----|-----|-------------|------|')
for r,x in ri:
    w=W.ancho_volteo(x); ev='cumple (Ri ≥ 8 m)' if x>=8 else 'mínimo absoluto (6 ≤ Ri < 8 m)' if x>=6 else 'no cumple (Ri < 6 m)'
    A(f"| C-{r['n']} | {sta(r['sta_PI'])} | {r['PI_N']:.3f} | {r['PI_E']:.3f} | {r['delta']:.1f} | {r['sentido']} | {r['R']:.2f} | {x:.1f} | {x+w:.1f} | {w:.2f} | {ev} | {r['dmax']:.2f} |")
A('')
A('Agrupación en zonas (curvas de vuelta consecutivas):'); A('')
A('| Zona | Prog. inicio | Prog. fin | Curvas | R mín. eje (m) | Ri mín. (m) | Evaluación |'); A('|-----|--------|--------|------------|------|------|-------------|')
for i,g in enumerate(grp):
    rmin=min(r['R'] for r in g); x=W.ri_volteo(rmin); ev='cumple' if x>=8 else 'mínimo absoluto' if x>=6 else 'no cumple'
    A(f"| V-{i+1} | {sta(g[0]['sta_PC'])} | {sta(g[-1]['sta_PT'])} | {', '.join('C-'+str(r['n']) for r in g)} | {rmin:.1f} | {x:.1f} | {ev} |")
A('')
A('## 6.4 Tangentes'); A('')
A('| Longitud de la tangente intermedia | Cantidad |'); A('|------------------------|------|')
for k_,v_ in tan_cls.items(): A(f'| {k_} | {v_} |')
A(''); A(f'Las {tan_ok} tangentes que cumplen la Tabla 302.01 son:'); A('')
A('| Entre curvas | Longitud (m) | Mínimo exigido (m) | Tipo |'); A('|---------|------|------|------|')
for i,(t,s_) in enumerate(zip(tn,same)):
    need=111 if s_ else 56
    if t>=need: A(f"| C-{i+1} y C-{i+2} | {t:.1f} | {need} | {'mismo sentido' if s_ else 'curvas en S'} |")
A('')
A('## 6.5 Sitios donde el eje se separa más de 2.5 m del trazo actual'); A('')
A('Son los puntos a revisar en campo o en Civil 3D antes de aprobar el eje, por su posible afectación a edificaciones.'); A('')
A('| Curva | Prog. PC | Prog. PT | Norte PI | Este PI | R (m) | Separación máx. (m) | Comentario |'); A('|------|--------|--------|---------|---------|-----|------|----------------|')
for r in hot: A(f"| C-{r['n']} | {sta(r['sta_PC'])} | {sta(r['sta_PT'])} | {r['PI_N']:.3f} | {r['PI_E']:.3f} | {r['R']:.1f} | {r['dmax']:.2f} | {'radio subido al mínimo normativo' if 'subido' in r['obs'] else 'cadena de curvas de radio variable en el trazo'} |")
A('')
A('# 7. Conclusiones y recomendaciones'); A('')
A(f'1. El eje cumple el radio mínimo de la DG-2018 (45 m a 40 km/h, peralte 12 %) en {cum50+cum45} de {n} curvas. En {exc} curvas se adopta radio excepcional con velocidad específica de 30 km/h y en {vol} se trata de curvas de vuelta o esquinas urbanas.')
A(f'2. Las {ri0} curvas con radio interior menor de 6 m (zonas V-1, V-3 y otras indicadas en 6.3) no admiten justificación con la DG-2018. Se recomienda ampliar la plataforma en esos puntos o aceptar expropiaciones puntuales.')
A('3. Los primeros 230 m (zona urbana de inicio) tienen geometría de calles, con radios de 6 a 22 m. Conviene tratar ese tramo como vía urbana con velocidad de 20 a 30 km/h.')
A('4. Las clotoides, las tangentes mínimas y la longitud mínima de curva no se cumplen por la premisa de seguir el trazo existente. Debe dejarse constancia en el expediente, con la señalización vertical y horizontal correspondiente al Manual de Dispositivos de Control de Tránsito.')
A('5. En Civil 3D, asociar al eje el archivo de criterios DG2018_Corregido_2.xml con velocidad 40 km/h; los triángulos de advertencia que queden marcan exactamente las curvas de los capítulos 6.2 y 6.3.')
A('6. Verificar la visibilidad de parada (50 m) con banquetas en las curvas de radio menor a 60 m ubicadas en corte, según el Tópico 302.10.01.')
A('')
A('# Anexo A. Tabla completa de curvas'); A('')
A('| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | T (m) | Lc (m) | E (m) | Prog. PC | Prog. PT | Sa (m) | Tang. sig. (m) | Sep. (m) | Clase |')
A('|-----|--------|---------|---------|-----|---|-----|-----|-----|----|--------|--------|----|-----|----|---------|')
for r in rows:
    cl='Normativa 8%' if r['R']>=50-0.06 else 'Normativa 12%' if r['R']>=45-0.06 else 'Excepcional' if r['R']>=25 else 'Vuelta'
    sa='-' if math.isnan(r['Sa']) else f"{r['Sa']:.2f}"
    A(f"| C-{r['n']} | {sta(r['sta_PI'])} | {r['PI_N']:.2f} | {r['PI_E']:.2f} | {r['delta']:.1f} | {r['sentido']} | {r['R']:.2f} | {r['T']:.1f} | {r['Lc']:.1f} | {r['E']:.2f} | {sta(r['sta_PC'])} | {sta(r['sta_PT'])} | {sa} | {r['tan_next']:.1f} | {r['dmax']:.2f} | {cl} |")
A('')
A('# Anexo B. Archivos entregados'); A('')
A('- `EJE_DG2018_circular.xml`: eje en LandXML 1.2 para importar en Civil 3D (IMPORTLANDXML).')
A('- `EJE_DG2018_circular_curvas.csv`: tabla de curvas con observaciones detalladas por curva.')
A('- `EJE_DG2018_circular_PI_PNEZD.csv` y `EJE_DG2018_circular_PI_polilinea.scr`: PIs como puntos y como polilínea de AutoCAD.')
A('- `EJE_DG2018_circular_planta.svg` y `.png`: croquis de planta con el trazo actual y el eje coloreado por clase de curva.')
A('- `DG2018_Corregido_2.xml`: archivo de criterios de diseño DG-2018 para Civil 3D.')
A('- `EJE_DG2018_clotoides.xml`: variante con clotoides de 40 m en las 5 curvas donde caben.')
out='/tmp/claude-0/-home-user-Normas/1d8bfce3-3294-5b1e-ace9-ad5fa4f1a13c/scratchpad/rep/memoria.md'
open(out,'w',encoding='utf-8').write('\n'.join(L)+'\n'); print('md ok', len(L), 'lineas;', 'at45',len(at45),'exc',len(excs),'vol',len(vols),'ri',ri8,ri6,ri0,'tan_ok',tan_ok,'hot',len(hot),'small',len(small))
