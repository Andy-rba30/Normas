---
title: "Memoria de diseño geométrico en planta"
subtitle: "Eje EJE DG2018 V40 CIRCULAR, ajustado al trazo existente según el Manual de Carreteras: Diseño Geométrico DG-2018"
date: "16/10/2026"
lang: es
---

# 1. Objeto y alcance

Este documento describe el eje en planta contenido en el archivo `EJE_DG2018_circular.xml` (LandXML 1.2, alineamiento "EJE DG2018 V40 CIRCULAR", longitud 11,468.09 m), obtenido a partir de la poligonal del trazo existente `PROCESAMIENTO DISEÑO GEOMETRICO` (11,491.71 m, 1181 vértices, UTM WGS84 zona 17 Sur), y contrasta cada parámetro adoptado con lo que exige el Manual de Carreteras: Diseño Geométrico DG-2018 (MTC, revisada y corregida a enero de 2018).

Premisas del proyecto: carretera de Segunda Clase, velocidad de diseño 40 km/h, tramos en zona poblada donde se busca la mínima expropiación. Por ello el eje se ajustó al trazo actual y solo se regularizó la geometría (tangentes rectas y curvas circulares), aceptando radios excepcionales y curvas de vuelta donde el terreno y las edificaciones no permiten el radio normativo.

# 2. Parámetros de diseño adoptados y contraste con la DG-2018

| Parámetro | Valor adoptado | Lo que indica la DG-2018 (cita) | Referencia | Situación en el eje |
|------------|-----------|------------------------------------------|---------|------------------------|
| Clasificación por demanda | Carretera de Segunda Clase | "Son carreteras con IMDA entre 2 000 y 400 veh/día, con una calzada de dos carriles de 3.30 m de ancho como mínimo (...) La superficie de rodadura de estas carreteras debe ser pavimentada." | Tópico 101.04 | Dato del proyecto. |
| Clasificación por orografía | Terreno escarpado (tipo 4) | "Tiene pendientes transversales al eje de la vía superiores al 100% y sus pendientes longitudinales excepcionales son superiores al 8%, exigiendo el máximo de movimiento de tierras." | Tópico 102.04 | Adoptado porque es la única orografía en la que la Tabla 204.01 admite 40 km/h para Segunda Clase (en terreno accidentado el rango es 50 a 80 km/h). |
| Velocidad de diseño | 40 km/h | Tabla 204.01: Carretera de Segunda Clase, escarpado, rango 40 a 70 km/h. | Tabla 204.01 | Cumple (límite inferior del rango). |
| Velocidad específica en elementos puntuales | 30 km/h en curvas excepcionales | "La velocidad máxima con que sería abordado cada elemento geométrico, es la Velocidad Específica con la que se debe diseñar (...) La condición deseable es que a la mayoría de los elementos geométricos que integran el tramo homogéneo se les pueda asignar como Velocidad Específica, el valor de la Velocidad de Diseño del tramo." | Tópico 204.03 | Las curvas con 25 m ≤ R < 45 m se diseñan con Ve = 30 km/h y requieren señalización de velocidad. |
| Peralte máximo | 12 % absoluto (8 % normal) | Tabla 304.05: "Zona rural (T. Accidentado o Escarpado): 12.0 absoluto, 8.0 % normal". | Tabla 304.05 | El radio mínimo se calcula con 12 %. |
| Fricción transversal máxima | 0.17 | Tabla 302.02: f máx = 0.17 para 30 y 40 km/h. | Tabla 302.02 | - |
| Radio mínimo normativo | 45 m | Tabla 302.02, área rural accidentada o escarpada: "40 km/h, p máx 12.00 %, f máx 0.17, radio calculado 43.4 m, radio redondeado 45 m". | Tabla 302.02 | 175 curvas de 324 (54 %) tienen R ≥ 45 m. |
| Radio mínimo con peralte normal 8 % | 50 m | Tabla 302.02, área rural plana u ondulada: "40 km/h, 8.00 %, 0.17, 50.4 m, 50 m". | Tabla 302.02 | 83 curvas (26 %) tienen R ≥ 50 m y pueden peraltarse con 8 %. |
| Radio excepcional | 25 m ≤ R < 45 m | La DG-2018 no define un radio mínimo excepcional para carreteras de Segunda Clase. Se adopta el radio mínimo de la fila de 30 km/h de la Tabla 302.02: "30 km/h, 12.00 %, 0.17, 24.4 m, 25 m", es decir, la curva se diseña con velocidad específica de 30 km/h. | Tabla 302.02 y Tópico 204.03 | 58 curvas (18 %). Listado en el capítulo 6.2. |
| Curvas de vuelta | Radio interior Ri ≥ 8 m (normal) o 6 m (absoluto); Re según Tabla 302.12 | "Son aquellas curvas que se proyectan sobre una ladera, en terrenos accidentados, con el propósito de obtener o alcanzar una cota mayor (...) Este tipo de curvas no se emplearán en autopistas, en tanto que en carreteras de Primera Clase podrán utilizarse en casos excepcionales (...) El radio interior de 8 m, representa un mínimo normal. El radio interior de 6 m, representa un mínimo absoluto y sólo podrá ser usado en forma excepcional." | Tópico 302.07 y Tabla 302.12 | 91 curvas con R de eje < 25 m (28 %): 43 con Ri ≥ 8 m, 13 con 6 ≤ Ri < 8 m y 35 con Ri < 6 m (no cumplen ni el mínimo absoluto). Capítulo 6.3. |
| Radio a partir del cual no se requiere peralte | 3 500 m (V = 40 km/h) | Tabla 304.04: "Velocidad 40 km/h: radio 3 500 m". | Tabla 304.04 | Ninguna curva del eje supera 3 500 m; todas se peraltan. |
| Peralte mínimo | 2 % para 2 500 ≤ R < 3 500 m | Tabla 304.06: "40 ≤ V < 100: 2 500 ≤ R < 3 500". | Tabla 304.06 | - |
| Transición del peralte | ipmáx = 1.8 − 0.01 V = 1.4 %; Lmín = (pf − pi)/ipmáx · B | "ipmáx = 1.8 − 0.01 V (...) Lmín = (pf − pi)/ipmáx · B". | Tópico 302.08 | Para Civil 3D se entrega el archivo de criterios DG2018_Corregido_2.xml (tablas "DG2018 _PMax 12%" y método "DG2018 METRICO"). |
| Longitud mínima de tangentes | 56 m entre curvas en S; 111 m entre curvas del mismo sentido; máx. deseable 668 m | Tabla 302.01: "40 km/h: L mín.s 56, L mín.o 111, L máx 668". | Tabla 302.01 | Solo 4 de 323 tangentes intermedias cumplen. Limitación propia del trazo existente (capítulo 6.4). |
| Longitud mínima de curva | 3V = 120 m; para Δ ≤ 5°: L > 30(10 − Δ); nunca Δ < 59′ | "La longitud mínima de curva (L) será: carreteras de dos carriles 3V (...) En el caso de ángulos de deflexión Δ pequeños, iguales o inferiores a 5º (...) L > 30(10 − Δ) (...) No se usará nunca ángulos de deflexión menores de 59' (minutos)." | Tópico 302.02 | Ninguna curva alcanza 120 m (la mayor tiene 120 m). 21 curvas tienen Δ < 5°; ninguna tiene Δ < 59′. |
| Curvas de transición (clotoides) | No incluidas en esta variante | Tabla 302.11A: para 40 km/h se puede prescindir de la transición si R ≥ 150 m. Tabla 302.10: longitud mínima de transición 40 m a 40 km/h; "En ningún caso se adoptarán longitudes de transición menores a 30 m". Tópico 302.05.06: R/3 ≤ A ≤ R. | Tópicos 302.05.06 y 302.05.07, Tablas 302.10 y 302.11A | 320 curvas tienen R < 150 m y requerirían clotoide; con Le = 40 m solo cabe en 5 (variante EJE_DG2018_clotoides.xml) porque las tangentes disponibles son demasiado cortas. |
| Relación entre radios consecutivos | Tabla 302.08 (grupo 2) | "cuando se enlacen curvas circulares consecutivas sin tangente intermedia, así como mediante tangente de longitud menor o igual a 200 m, la relación de radios (...) no sobrepasará los valores (...) Grupo 2: Carreteras de Segunda y Tercera Clase." | Tópico 302.04.05 y Tabla 302.08 | 43 de 323 pares cumplen. |
| Sobreancho | Sa = n(R − √(R² − L²)) + V/(10 √R); mínimo 0.40 m; vehículo B2 con L = 8.25 + 2.30 = 10.55 m | "Sa = n (R − √(R² − L²)) + V/(10√R) (...) Se considera apropiado un valor mínimo de 0.40 m de sobreancho para justificar su adopción." Tabla 202.01: ómnibus de dos ejes B2, separación de ejes 8.25 m, vuelo delantero 2.30 m. | Tópico 302.09.03, Tabla 202.01 | Valor por curva en el Anexo A. En curvas de vuelta el ancho se toma de la Tabla 302.12. |
| Ancho de calzada | 6.00 m | Tabla 304.01: Carretera de Segunda Clase, orografía 4, 40 km/h: 6.60 / 6.60 / 6.60 / 6.00 m según orografía 1 a 4. | Tabla 304.01 | 6.00 m en escarpado (6.60 m si el tramo se clasifica como accidentado). |
| Ancho de bermas | 0.50 m | Tabla 304.02: Segunda Clase, 40 km/h: 1.20 / 1.20 / 0.90 / 0.50 m según orografía. | Tabla 304.02 | 0.50 m en escarpado. |
| Bombeo | 2.0 a 2.5 % | Tabla 304.03: pavimento asfáltico o de concreto, 2.0 % (< 500 mm/año) o 2.5 % (> 500 mm/año). | Tabla 304.03 | Según precipitación de la zona. |
| Visibilidad de parada y de paso | Dp = 50 m; Da = 270 m | Tabla 205.01: "40 km/h: 50 m". Tabla 205.03: "40 km/h: 270 m". | Tablas 205.01 y 205.03 | Verificar banquetas de visibilidad (Tópico 302.10.01) en las curvas de radio menor a 60 m en corte. |

# 3. Metodología de obtención del eje

1. La poligonal original se remuestreó cada metro y se calculó el rumbo y la curvatura a lo largo del trazo.
2. Los tramos con radio de curvatura mayor a 250 m se trataron como rectos y se les ajustó una tangente por mínimos cuadrados; cuando algún punto se separaba más de 0.8 m de la recta, la tangente se partió en dos.
3. Cada tramo de curvatura continua del mismo sentido se convirtió en una curva circular, con el PI en la intersección de las tangentes vecinas y el radio ajustado por mínimos cuadrados a los puntos del trazo. Las deflexiones menores de 8° cuya supresión desplaza el eje menos de 0.5 m se absorbieron en la tangente.
4. Entre curvas consecutivas sin recta intermedia (curvas en S o compuestas) la tangente común se optimizó para minimizar la separación respecto al trazo manteniendo la tangencia.
5. Donde el radio ajustado resultó menor de 45 m, se subió hasta 45 m siempre que la separación respecto al trazo no superara 2.0 m (131 curvas). Los radios se redondearon a múltiplos de 5 m (10 m por encima de 100 m).
6. Las curvas de más de 170° (volteos) se representan con dos arcos consecutivos del mismo radio, porque Civil 3D no admite una curva simple de 180° o más.

# 4. Resultados globales

| Indicador | Valor |
|----------------------------|------------|
| Longitud del trazo original / del eje corregido | 11,491.71 m / 11,468.09 m |
| Número de curvas / tangentes | 324 / 325 |
| Curvas con R ≥ 50 m (cumple con peralte 8 %) | 83 (26 %) |
| Curvas con 45 ≤ R < 50 m (cumple con peralte 12 %) | 92 (28 %) |
| Curvas excepcionales, 25 ≤ R < 45 m (Ve = 30 km/h) | 58 (18 %) |
| Curvas de vuelta, R < 25 m | 91 (28 %) |
| Curvas llevadas al radio mínimo normativo (R = 45 m) | 90 |
| Separación lateral del trazo actual respecto al eje: promedio / percentil 95 / máxima | 0.33 m / 1.13 m / 5.22 m |
| Longitud de trazo con separación mayor a 1.5 m / 2.5 m / 4.0 m | 358 m / 146 m / 25 m |
| Tangentes intermedias que cumplen la Tabla 302.01 | 4 de 323 |
| Pares de curvas consecutivas que cumplen la Tabla 302.08 | 43 de 323 |
| Curvas con longitud ≥ 3V = 120 m | 0 de 324 |

# 5. Interpretación

El 54 % de las curvas cumple el radio mínimo de la DG-2018 para 40 km/h. El 18 % queda entre 25 y 45 m y debe tratarse como curva excepcional con velocidad específica de 30 km/h y señalización preventiva y reglamentaria. El 28 % restante corresponde a curvas de vuelta y esquinas urbanas con radios de eje entre 6 y 25 m, que es lo que impone la geometría existente; en 35 de ellas el radio interior resultante es menor de 6 m, de modo que para cumplir siquiera el mínimo absoluto habría que ampliar la plataforma o expropiar.

Las longitudes mínimas de tangente, la longitud mínima de curva de 120 m, las clotoides y la relación de radios consecutivos no se cumplen en la mayor parte del eje. No es un defecto del ajuste sino de la premisa de seguir el trazo existente: con curvas cada 35 m en promedio no hay espacio para tangentes de 56 a 111 m ni para espirales de 40 m. Si el proyecto exige cumplir esos parámetros, habrá que rediseñar tramos completos con expropiación.

# 6. Inventario de curvas por tipo

## 6.1 Curvas en el radio mínimo normativo (R = 45 m)

90 curvas quedan exactamente en el radio mínimo de la Tabla 302.02; de ellas 71 fueron llevadas a 45 m desde un radio ajustado menor (separación admitida ≤ 2.0 m). Deben peraltarse con el máximo de 12 %.

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | Lc (m) | Sep. máx. trazo (m) | Origen |
|------|---------|---------|---------|------|----|-----|-----|------|----------|
| C-4 | 0+099.00 | 9472189.807 | 612980.759 | 31.5 | D | 44.97 | 24.7 | 1.89 | subido al mínimo |
| C-12 | 0+277.49 | 9472316.394 | 613017.482 | 5.5 | I | 45.00 | 4.3 | 0.91 | subido al mínimo |
| C-16 | 0+361.43 | 9472347.907 | 612981.130 | 10.9 | D | 45.00 | 8.6 | 0.22 | subido al mínimo |
| C-17 | 0+382.41 | 9472351.893 | 612960.508 | 8.8 | D | 45.00 | 6.9 | 0.09 | subido al mínimo |
| C-20 | 0+478.22 | 9472384.202 | 612870.599 | 46.7 | D | 45.00 | 36.7 | 1.55 | subido al mínimo |
| C-21 | 0+521.80 | 9472424.822 | 612849.548 | 22.8 | I | 45.00 | 17.9 | 0.29 | ajuste al trazo |
| C-24 | 0+693.55 | 9472567.487 | 612812.812 | 40.5 | D | 45.00 | 31.8 | 0.70 | subido al mínimo |
| C-29 | 0+885.74 | 9472672.597 | 612728.598 | 84.0 | D | 45.00 | 66.0 | 1.56 | ajuste al trazo |
| C-32 | 1+013.66 | 9472810.529 | 612756.323 | 41.3 | I | 44.95 | 32.4 | 0.86 | subido al mínimo |
| C-34 | 1+074.09 | 9472804.918 | 612716.138 | 19.3 | D | 45.00 | 15.2 | 0.33 | subido al mínimo |
| C-36 | 1+124.91 | 9472772.919 | 612676.667 | 14.7 | D | 45.00 | 11.6 | 0.34 | subido al mínimo |
| C-39 | 1+352.69 | 9472719.756 | 612471.344 | 74.3 | D | 45.00 | 58.3 | 0.93 | ajuste al trazo |
| C-40 | 1+415.80 | 9472791.596 | 612458.780 | 30.4 | I | 45.00 | 23.9 | 1.18 | subido al mínimo |
| C-45 | 1+615.28 | 9472827.619 | 612299.230 | 22.3 | D | 45.00 | 17.5 | 0.51 | subido al mínimo |
| C-50 | 1+812.33 | 9472784.335 | 612148.461 | 7.1 | D | 45.00 | 5.6 | 0.22 | subido al mínimo |
| C-53 | 1+928.55 | 9472694.509 | 612081.130 | 11.8 | I | 45.00 | 9.3 | 0.17 | subido al mínimo |
| C-54 | 1+952.81 | 9472679.553 | 612061.984 | 19.2 | D | 45.00 | 15.1 | 0.16 | ajuste al trazo |
| C-57 | 2+015.77 | 9472686.709 | 612008.290 | 27.4 | D | 45.00 | 21.5 | 0.76 | subido al mínimo |
| C-62 | 2+153.21 | 9472744.752 | 611933.459 | 32.0 | I | 45.00 | 25.1 | 0.60 | subido al mínimo |
| C-64 | 2+242.78 | 9472759.983 | 611860.454 | 40.8 | I | 45.00 | 32.1 | 0.51 | ajuste al trazo |
| C-65 | 2+276.24 | 9472763.607 | 611825.759 | 7.7 | I | 45.00 | 6.0 | 0.62 | subido al mínimo |
| C-68 | 2+388.15 | 9472704.516 | 611756.000 | 16.2 | I | 45.00 | 12.7 | 0.57 | ajuste al trazo |
| C-75 | 2+657.32 | 9472577.483 | 611564.659 | 30.8 | I | 45.00 | 24.2 | 0.74 | subido al mínimo |
| C-76 | 2+691.77 | 9472583.502 | 611530.134 | 25.8 | D | 45.00 | 20.2 | 0.95 | subido al mínimo |
| C-79 | 2+825.63 | 9472619.144 | 611414.752 | 17.3 | I | 45.00 | 13.6 | 0.31 | ajuste al trazo |
| C-83 | 3+036.40 | 9472624.270 | 611232.394 | 8.8 | D | 45.00 | 6.9 | 0.21 | subido al mínimo |
| C-84 | 3+059.08 | 9472645.335 | 611223.944 | 8.1 | D | 45.00 | 6.4 | 0.12 | subido al mínimo |
| C-87 | 3+176.10 | 9472715.476 | 611163.313 | 30.6 | I | 45.00 | 24.1 | 0.58 | subido al mínimo |
| C-89 | 3+255.08 | 9472661.808 | 611105.823 | 21.6 | I | 45.00 | 16.9 | 0.32 | ajuste al trazo |
| C-94 | 3+409.78 | 9472653.181 | 611030.052 | 10.5 | D | 45.00 | 8.3 | 0.25 | subido al mínimo |
| C-104 | 3+722.23 | 9472479.485 | 610955.759 | 27.8 | I | 45.00 | 21.8 | 1.14 | subido al mínimo |
| C-106 | 3+832.86 | 9472502.060 | 610850.676 | 5.5 | D | 45.00 | 4.4 | 0.43 | subido al mínimo |
| C-107 | 3+842.51 | 9472507.189 | 610842.495 | 8.4 | I | 45.00 | 6.6 | 0.12 | subido al mínimo |
| C-108 | 3+851.51 | 9472510.808 | 610834.241 | 3.9 | I | 45.00 | 3.0 | 0.07 | subido al mínimo |
| C-112 | 3+964.83 | 9472553.981 | 610730.567 | 9.1 | D | 45.00 | 7.2 | 0.24 | subido al mínimo |
| C-115 | 4+073.62 | 9472562.537 | 610623.126 | 12.5 | D | 45.00 | 9.8 | 0.31 | subido al mínimo |
| C-118 | 4+217.46 | 9472560.856 | 610482.581 | 28.2 | I | 45.00 | 22.1 | 0.51 | subido al mínimo |
| C-124 | 4+414.59 | 9472551.328 | 610326.692 | 35.6 | I | 45.00 | 28.0 | 0.49 | subido al mínimo |
| C-126 | 4+480.72 | 9472546.514 | 610260.006 | 4.1 | I | 45.00 | 3.2 | 0.17 | subido al mínimo |
| C-130 | 4+552.04 | 9472519.929 | 610197.194 | 25.5 | D | 45.00 | 20.0 | 1.27 | subido al mínimo |
| C-137 | 4+682.14 | 9472463.422 | 610081.749 | 18.4 | I | 45.00 | 14.4 | 0.13 | ajuste al trazo |
| C-139 | 4+745.10 | 9472448.886 | 610029.585 | 21.3 | I | 45.00 | 16.7 | 0.22 | ajuste al trazo |
| C-140 | 4+795.10 | 9472438.535 | 609980.467 | 44.2 | D | 45.00 | 34.7 | 1.65 | subido al mínimo |
| C-144 | 4+890.95 | 9472425.917 | 609906.797 | 10.4 | D | 45.00 | 8.2 | 0.13 | ajuste al trazo |
| C-149 | 5+074.35 | 9472346.474 | 609762.633 | 8.9 | D | 45.00 | 7.0 | 0.27 | subido al mínimo |
| C-150 | 5+142.06 | 9472315.710 | 609702.299 | 5.1 | D | 45.00 | 4.0 | 0.47 | subido al mínimo |
| C-152 | 5+205.94 | 9472300.221 | 609640.768 | 18.3 | I | 45.00 | 14.4 | 0.87 | subido al mínimo |
| C-155 | 5+322.51 | 9472263.851 | 609530.347 | 8.8 | D | 45.00 | 6.9 | 0.23 | subido al mínimo |
| C-156 | 5+351.53 | 9472257.218 | 609502.075 | 13.6 | I | 45.00 | 10.7 | 0.29 | subido al mínimo |
| C-157 | 5+374.93 | 9472246.628 | 609481.152 | 5.9 | D | 45.00 | 4.6 | 0.21 | subido al mínimo |
| C-158 | 5+438.41 | 9472223.926 | 609421.873 | 4.4 | D | 45.00 | 3.5 | 0.25 | subido al mínimo |
| C-159 | 5+492.79 | 9472208.438 | 609369.745 | 17.6 | I | 45.00 | 13.8 | 0.68 | subido al mínimo |
| C-164 | 5+799.18 | 9472283.459 | 609143.685 | 14.3 | D | 45.00 | 11.3 | 0.48 | subido al mínimo |
| C-167 | 5+955.77 | 9472154.202 | 609085.475 | 8.5 | D | 45.00 | 6.7 | 0.22 | subido al mínimo |
| C-168 | 5+999.89 | 9472115.767 | 609063.786 | 6.7 | D | 45.00 | 5.3 | 0.22 | subido al mínimo |
| C-169 | 6+017.87 | 9472101.253 | 609053.171 | 5.4 | D | 45.00 | 4.2 | 0.26 | subido al mínimo |
| C-171 | 6+093.41 | 9472040.854 | 609008.598 | 7.2 | I | 45.00 | 5.7 | 0.60 | subido al mínimo |
| C-173 | 6+237.94 | 9471930.530 | 608927.705 | 23.8 | I | 45.00 | 18.7 | 0.59 | subido al mínimo |
| C-174 | 6+272.65 | 9471905.424 | 608903.335 | 8.9 | D | 45.00 | 7.0 | 0.26 | subido al mínimo |
| C-175 | 6+321.82 | 9471875.881 | 608864.013 | 11.8 | D | 45.00 | 9.3 | 0.32 | subido al mínimo |
| C-178 | 6+459.63 | 9471809.087 | 608744.190 | 77.1 | D | 45.00 | 60.6 | 1.93 | subido al mínimo |
| C-185 | 6+658.48 | 9471914.358 | 608657.337 | 25.0 | D | 45.00 | 19.7 | 0.39 | subido al mínimo |
| C-209 | 7+476.13 | 9471612.913 | 608386.663 | 28.3 | I | 45.00 | 22.2 | 0.31 | subido al mínimo |
| C-228 | 7+985.60 | 9471436.095 | 608307.908 | 9.5 | I | 45.00 | 7.5 | 0.15 | subido al mínimo |
| C-229 | 7+997.65 | 9471435.790 | 608295.844 | 2.0 | D | 45.00 | 1.6 | 0.02 | subido al mínimo |
| C-230 | 8+003.12 | 9471435.842 | 608290.369 | 0.2 | I | 45.00 | 0.2 | 0.02 | subido al mínimo |
| C-231 | 8+009.54 | 9471435.876 | 608283.952 | 1.4 | I | 45.00 | 1.1 | 0.02 | subido al mínimo |
| C-232 | 8+020.51 | 9471435.665 | 608272.986 | 1.5 | I | 45.00 | 1.2 | 0.01 | subido al mínimo |
| C-234 | 8+100.51 | 9471424.264 | 608193.881 | 15.9 | D | 45.00 | 12.5 | 0.64 | subido al mínimo |
| C-238 | 8+235.25 | 9471529.574 | 608141.225 | 11.8 | D | 45.00 | 9.3 | 0.30 | ajuste al trazo |
| C-240 | 8+273.83 | 9471557.242 | 608115.098 | 27.5 | D | 45.00 | 21.6 | 0.21 | ajuste al trazo |
| C-241 | 8+306.68 | 9471586.912 | 608100.043 | 10.1 | D | 45.00 | 7.9 | 0.23 | subido al mínimo |
| C-242 | 8+323.09 | 9471602.642 | 608095.298 | 10.0 | I | 45.00 | 7.8 | 0.27 | subido al mínimo |
| C-243 | 8+348.57 | 9471625.412 | 608083.821 | 4.3 | I | 45.00 | 3.4 | 0.30 | subido al mínimo |
| C-248 | 8+569.89 | 9471807.256 | 607991.071 | 29.3 | D | 45.00 | 23.0 | 0.45 | ajuste al trazo |
| C-252 | 8+748.23 | 9471953.791 | 607928.689 | 32.0 | D | 45.00 | 25.1 | 0.78 | subido al mínimo |
| C-260 | 9+081.12 | 9471911.350 | 607807.368 | 67.8 | D | 45.00 | 53.2 | 0.94 | ajuste al trazo |
| C-269 | 9+329.23 | 9471804.341 | 607813.043 | 23.8 | D | 45.00 | 18.7 | 0.42 | subido al mínimo |
| C-270 | 9+352.93 | 9471780.365 | 607813.290 | 25.0 | I | 45.00 | 19.6 | 0.21 | ajuste al trazo |
| C-273 | 9+441.97 | 9471767.309 | 607787.435 | 43.5 | D | 44.98 | 34.1 | 1.25 | subido al mínimo |
| C-277 | 9+613.87 | 9471808.389 | 607657.950 | 48.0 | D | 45.00 | 37.7 | 0.81 | ajuste al trazo |
| C-280 | 9+714.61 | 9471866.802 | 607582.823 | 13.5 | D | 45.00 | 10.6 | 0.41 | subido al mínimo |
| C-286 | 9+996.15 | 9471727.071 | 607566.691 | 68.8 | I | 45.00 | 54.1 | 0.90 | ajuste al trazo |
| C-287 | 10+052.60 | 9471721.732 | 607630.515 | 13.4 | I | 45.00 | 10.6 | 0.28 | subido al mínimo |
| C-299 | 10+449.92 | 9471698.310 | 607607.115 | 53.0 | I | 45.00 | 41.6 | 2.00 | subido al mínimo |
| C-302 | 10+670.48 | 9471763.099 | 607449.956 | 28.0 | I | 45.00 | 22.0 | 0.52 | ajuste al trazo |
| C-306 | 10+852.97 | 9471920.322 | 607428.954 | 13.4 | I | 45.00 | 10.6 | 0.33 | subido al mínimo |
| C-309 | 10+975.98 | 9472003.071 | 607514.411 | 18.5 | D | 45.00 | 14.5 | 0.61 | subido al mínimo |
| C-313 | 11+064.68 | 9472068.942 | 607520.665 | 9.9 | I | 45.00 | 7.8 | 0.17 | subido al mínimo |
| C-314 | 11+093.16 | 9472059.305 | 607493.835 | 37.4 | D | 45.00 | 29.4 | 0.96 | subido al mínimo |

## 6.2 Curvas excepcionales (25 m ≤ R < 45 m)

58 curvas. La velocidad específica se calcula con Ve = √(127 · R · (0.12 + 0.17)), que reproduce los radios de la Tabla 302.02 para 30 y 40 km/h (25 m → 30 km/h, 45 m → 41 km/h). Todas requieren peralte 12 %, sobreancho y señalización de velocidad máxima 30 km/h.

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | Ve (km/h) | Sa (m) | Lc (m) | Sep. máx. trazo (m) |
|------|---------|---------|---------|------|----|-----|------|-----|-----|------|
| C-1 | 0+037.84 | 9472166.454 | 613022.231 | 44.7 | I | 38.78 | 38 | 3.57 | 30.2 | 1.16 |
| C-7 | 0+169.11 | 9472248.915 | 612948.678 | 36.4 | D | 25.00 | 30 | 5.47 | 15.9 | 0.43 |
| C-15 | 0+325.02 | 9472347.878 | 613017.986 | 28.7 | I | 40.97 | 39 | 3.39 | 20.5 | 0.21 |
| C-22 | 0+613.01 | 9472483.412 | 612779.332 | 77.8 | D | 39.90 | 38 | 3.47 | 54.2 | 1.74 |
| C-27 | 0+765.84 | 9472618.128 | 612836.504 | 45.9 | I | 29.88 | 33 | 4.58 | 24.0 | 0.97 |
| C-28 | 0+781.46 | 9472622.422 | 612820.063 | 14.1 | D | 35.00 | 36 | 3.93 | 8.6 | 0.39 |
| C-30 | 0+926.77 | 9472724.322 | 612750.290 | 31.9 | I | 43.60 | 40 | 3.20 | 24.3 | 1.38 |
| C-42 | 1+496.58 | 9472779.312 | 612398.742 | 60.8 | D | 40.48 | 39 | 3.43 | 43.0 | 0.76 |
| C-44 | 1+587.02 | 9472824.333 | 612331.803 | 66.4 | I | 29.90 | 33 | 4.58 | 34.6 | 0.61 |
| C-46 | 1+643.65 | 9472841.054 | 612273.997 | 35.4 | I | 38.90 | 38 | 3.56 | 24.1 | 1.21 |
| C-47 | 1+666.67 | 9472837.985 | 612250.375 | 32.3 | D | 39.31 | 38 | 3.52 | 22.2 | 0.38 |
| C-55 | 1+984.31 | 9472669.378 | 612032.020 | 27.0 | D | 43.90 | 40 | 3.18 | 20.7 | 0.17 |
| C-59 | 2+063.69 | 9472732.887 | 611995.109 | 37.0 | D | 37.28 | 37 | 3.70 | 24.1 | 0.65 |
| C-63 | 2+195.40 | 9472717.221 | 611900.604 | 86.8 | D | 30.00 | 33 | 4.56 | 45.4 | 1.24 |
| C-71 | 2+573.36 | 9472606.735 | 611624.722 | 71.4 | I | 29.40 | 33 | 4.65 | 36.6 | 0.37 |
| C-72 | 2+611.86 | 9472567.615 | 611604.346 | 38.9 | D | 37.30 | 37 | 3.70 | 25.4 | 1.18 |
| C-78 | 2+786.53 | 9472638.826 | 611452.769 | 62.6 | I | 30.00 | 33 | 4.56 | 32.8 | 1.66 |
| C-82 | 3+000.40 | 9472588.315 | 611253.691 | 75.6 | D | 25.00 | 30 | 5.47 | 33.0 | 0.57 |
| C-85 | 3+123.31 | 9472707.739 | 611208.700 | 22.5 | I | 43.10 | 40 | 3.23 | 16.9 | 0.35 |
| C-93 | 3+379.61 | 9472683.873 | 611029.183 | 32.2 | I | 35.01 | 36 | 3.93 | 19.7 | 1.18 |
| C-98 | 3+562.18 | 9472511.901 | 611065.550 | 36.1 | D | 30.00 | 33 | 4.56 | 18.9 | 5.17 |
| C-101 | 3+641.85 | 9472449.657 | 611030.786 | 43.7 | D | 35.00 | 36 | 3.93 | 26.7 | 5.84 |
| C-102 | 3+666.81 | 9472453.707 | 611004.763 | 37.7 | D | 32.50 | 35 | 4.22 | 21.4 | 4.64 |
| C-119 | 4+239.21 | 9472556.841 | 610460.744 | 22.9 | D | 44.89 | 41 | 3.11 | 17.9 | 0.25 |
| C-122 | 4+313.75 | 9472505.989 | 610421.844 | 75.2 | D | 30.00 | 33 | 4.56 | 39.4 | 0.80 |
| C-163 | 5+752.32 | 9472297.505 | 609198.596 | 80.4 | I | 34.20 | 35 | 4.02 | 48.0 | 0.42 |
| C-186 | 6+702.86 | 9471869.912 | 608662.043 | 32.1 | I | 30.00 | 33 | 4.56 | 16.8 | 0.66 |
| C-187 | 6+719.09 | 9471856.784 | 608672.342 | 27.4 | D | 33.14 | 35 | 4.14 | 15.8 | 0.21 |
| C-192 | 6+884.43 | 9471803.158 | 608604.034 | 19.0 | I | 34.00 | 35 | 4.04 | 11.3 | 0.25 |
| C-193 | 6+928.53 | 9471765.017 | 608581.692 | 45.2 | I | 34.50 | 36 | 3.99 | 27.2 | 0.47 |
| C-197 | 7+116.15 | 9471643.281 | 608471.076 | 90.7 | D | 40.00 | 38 | 3.47 | 63.3 | 1.02 |
| C-203 | 7+251.05 | 9471666.658 | 608430.695 | 19.2 | I | 42.46 | 40 | 3.28 | 14.2 | 0.62 |
| C-210 | 7+536.52 | 9471556.942 | 608362.774 | 86.9 | D | 40.00 | 38 | 3.47 | 60.6 | 0.51 |
| C-217 | 7+706.76 | 9471559.037 | 608419.344 | 20.1 | D | 39.20 | 38 | 3.53 | 13.7 | 0.13 |
| C-220 | 7+800.71 | 9471472.167 | 608452.241 | 28.5 | D | 27.30 | 32 | 5.01 | 13.6 | 0.30 |
| C-227 | 7+963.19 | 9471432.294 | 608334.781 | 71.2 | D | 25.00 | 30 | 5.47 | 31.1 | 0.40 |
| C-237 | 8+186.60 | 9471492.268 | 608176.443 | 56.5 | I | 30.00 | 33 | 4.56 | 29.6 | 0.47 |
| C-239 | 8+253.94 | 9471545.530 | 608131.436 | 22.8 | I | 40.00 | 38 | 3.47 | 15.9 | 0.53 |
| C-245 | 8+425.42 | 9471697.937 | 608064.124 | 59.2 | I | 29.10 | 33 | 4.70 | 30.1 | 0.47 |
| C-246 | 8+498.22 | 9471732.769 | 607996.813 | 63.8 | D | 30.00 | 33 | 4.56 | 33.4 | 0.55 |
| C-247 | 8+550.99 | 9471789.463 | 607997.954 | 22.3 | I | 35.00 | 36 | 3.93 | 13.6 | 0.42 |
| C-256 | 8+902.81 | 9471873.080 | 607898.972 | 62.6 | I | 39.59 | 38 | 3.50 | 43.2 | 0.73 |
| C-258 | 8+977.95 | 9471866.233 | 607877.279 | 50.7 | D | 29.40 | 33 | 4.65 | 26.0 | 0.90 |
| C-261 | 9+109.92 | 9471946.258 | 607798.526 | 7.7 | I | 38.90 | 38 | 3.56 | 5.2 | 0.53 |
| C-263 | 9+128.90 | 9471951.915 | 607783.540 | 18.5 | I | 26.02 | 31 | 5.25 | 8.4 | 0.69 |
| C-265 | 9+200.70 | 9471891.124 | 607753.031 | 93.0 | I | 39.72 | 38 | 3.49 | 64.4 | 0.65 |
| C-266 | 9+238.73 | 9471882.177 | 607809.566 | 15.9 | D | 38.90 | 38 | 3.56 | 10.8 | 0.24 |
| C-268 | 9+297.65 | 9471836.954 | 607798.225 | 63.9 | I | 32.20 | 34 | 4.26 | 35.9 | 0.40 |
| C-278 | 9+635.25 | 9471828.331 | 607645.055 | 9.6 | D | 37.90 | 37 | 3.65 | 6.4 | 0.10 |
| C-279 | 9+665.70 | 9471856.323 | 607633.025 | 55.0 | I | 29.30 | 33 | 4.67 | 28.1 | 0.66 |
| C-283 | 9+836.54 | 9471878.523 | 607515.210 | 82.7 | I | 25.00 | 30 | 5.47 | 36.1 | 0.47 |
| C-284 | 9+869.92 | 9471853.443 | 607548.005 | 50.6 | D | 38.40 | 38 | 3.60 | 33.9 | 0.32 |
| C-290 | 10+104.72 | 9471715.102 | 607677.255 | 54.4 | D | 28.02 | 32 | 4.88 | 26.6 | 1.59 |
| C-291 | 10+120.19 | 9471697.708 | 607674.164 | 12.9 | I | 28.83 | 33 | 4.74 | 6.5 | 1.99 |
| C-300 | 10+473.46 | 9471683.547 | 607584.758 | 11.9 | D | 41.61 | 39 | 3.34 | 8.7 | 0.28 |
| C-311 | 11+031.17 | 9472051.466 | 607540.695 | 25.6 | I | 39.10 | 38 | 3.54 | 17.5 | 0.89 |
| C-321 | 11+456.58 | 9472275.701 | 607215.356 | 0.7 | D | 27.90 | 32 | 4.90 | 0.3 | 0.05 |
| C-323 | 11+459.00 | 9472277.067 | 607213.357 | 0.7 | D | 40.50 | 39 | 3.43 | 0.5 | 0.01 |

## 6.3 Curvas de vuelta (R < 25 m)

91 curvas. El radio interior Ri se obtiene de Ri + ancho/2 = R, con el ancho de calzada en curva de vuelta (Re − Ri) de la Tabla 302.12 para la maniobra C2 (camión de dos ejes cruzándose con un vehículo ligero), que considera calzada de 6 m en tangente. Criterio: Ri ≥ 8 m cumple el mínimo normal; 6 ≤ Ri < 8 m es el mínimo absoluto de uso excepcional; Ri < 6 m no cumple.

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R eje (m) | Ri (m) | Re (m) | Ancho (m) | Evaluación DG-2018 | Sep. máx. trazo (m) |
|------|---------|---------|---------|------|----|-----|-----|-----|-----|-------------|------|
| C-2 | 0+056.50 | 9472186.685 | 613023.879 | 72.0 | I | 6.00 | 1.1 | 10.9 | 9.75 | no cumple (Ri < 6 m) | 0.96 |
| C-3 | 0+064.01 | 9472190.036 | 613015.866 | 23.1 | I | 21.22 | 17.1 | 25.3 | 8.14 | cumple (Ri ≥ 8 m) | 1.08 |
| C-5 | 0+121.27 | 9472201.640 | 612961.140 | 48.6 | D | 22.70 | 18.7 | 26.7 | 8.07 | cumple (Ri ≥ 8 m) | 1.76 |
| C-8 | 0+186.17 | 9472266.013 | 612952.910 | 42.2 | I | 10.75 | 5.9 | 15.6 | 9.75 | no cumple (Ri < 6 m) | 0.36 |
| C-9 | 0+195.14 | 9472274.247 | 612948.468 | 81.8 | D | 6.00 | 1.1 | 10.9 | 9.75 | no cumple (Ri < 6 m) | 1.15 |
| C-10 | 0+208.11 | 9472283.050 | 612960.368 | 35.0 | I | 23.80 | 19.8 | 27.8 | 8.01 | cumple (Ri ≥ 8 m) | 0.45 |
| C-11 | 0+222.93 | 9472297.545 | 612965.224 | 51.6 | D | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 2.11 |
| C-13 | 0+288.44 | 9472321.075 | 613027.388 | 18.3 | I | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.25 |
| C-14 | 0+308.29 | 9472334.796 | 613041.805 | 107.6 | I | 12.20 | 7.5 | 16.9 | 9.37 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.59 |
| C-19 | 0+437.09 | 9472372.920 | 612910.184 | 16.4 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.15 |
| C-23 | 0+635.66 | 9472512.525 | 612794.601 | 9.3 | I | 8.07 | 3.2 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.74 |
| C-25 | 0+730.56 | 9472587.366 | 612845.663 | 6.5 | I | 17.37 | 13.2 | 21.6 | 8.40 | cumple (Ri ≥ 8 m) | 0.45 |
| C-26 | 0+737.78 | 9472591.784 | 612851.375 | 81.7 | I | 7.20 | 2.3 | 12.1 | 9.75 | no cumple (Ri < 6 m) | 0.69 |
| C-33 | 1+042.19 | 9472836.729 | 612741.678 | 112.0 | I | 8.80 | 3.9 | 13.7 | 9.75 | no cumple (Ri < 6 m) | 0.65 |
| C-41 | 1+460.18 | 9472825.871 | 612429.694 | 106.1 | I | 24.20 | 20.2 | 28.2 | 8.00 | cumple (Ri ≥ 8 m) | 0.98 |
| C-43 | 1+545.97 | 9472783.479 | 612344.963 | 67.7 | D | 11.70 | 6.9 | 16.5 | 9.51 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.49 |
| C-49 | 1+789.36 | 9472806.914 | 612152.660 | 1.3 | I | 11.60 | 6.8 | 16.4 | 9.54 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.05 |
| C-56 | 1+998.16 | 9472671.422 | 612017.929 | 49.5 | D | 8.01 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.27 |
| C-58 | 2+028.94 | 9472700.257 | 612007.144 | 15.4 | I | 19.40 | 15.3 | 23.5 | 8.24 | cumple (Ri ≥ 8 m) | 0.17 |
| C-60 | 2+102.78 | 9472771.151 | 612006.630 | 135.3 | I | 11.30 | 6.5 | 16.1 | 9.63 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.39 |
| C-66 | 2+331.58 | 9472761.933 | 611770.429 | 88.4 | I | 9.10 | 4.2 | 14.0 | 9.75 | no cumple (Ri < 6 m) | 0.94 |
| C-73 | 2+630.64 | 9472559.705 | 611586.193 | 60.6 | D | 11.32 | 6.5 | 16.1 | 9.62 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.35 |
| C-86 | 3+147.26 | 9472727.226 | 611194.407 | 74.4 | I | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.37 |
| C-90 | 3+287.68 | 9472636.120 | 611085.416 | 89.0 | D | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.91 |
| C-92 | 3+376.47 | 9472717.578 | 611049.115 | 147.0 | I | 8.60 | 3.7 | 13.5 | 9.75 | no cumple (Ri < 6 m) | 0.39 |
| C-97 | 3+547.00 | 9472520.056 | 611052.384 | 35.5 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 2.64 |
| C-99 | 3+581.41 | 9472493.487 | 611073.043 | 53.0 | D | 17.70 | 13.5 | 21.9 | 8.37 | cumple (Ri ≥ 8 m) | 4.60 |
| C-103 | 3+679.27 | 9472463.336 | 610995.637 | 24.5 | I | 10.02 | 5.1 | 14.9 | 9.75 | no cumple (Ri < 6 m) | 1.50 |
| C-111 | 3+944.04 | 9472551.225 | 610751.467 | 31.7 | I | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.60 |
| C-120 | 4+261.17 | 9472561.633 | 610439.068 | 93.2 | I | 12.40 | 7.7 | 17.1 | 9.31 | mínimo absoluto (6 ≤ Ri < 8 m) | 1.46 |
| C-129 | 4+522.71 | 9472540.972 | 610218.570 | 45.4 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.19 |
| C-131 | 4+606.08 | 9472502.142 | 610145.809 | 4.3 | I | 11.40 | 6.6 | 16.2 | 9.60 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.44 |
| C-133 | 4+611.93 | 9472500.023 | 610140.360 | 7.0 | I | 6.31 | 1.4 | 11.2 | 9.75 | no cumple (Ri < 6 m) | 0.33 |
| C-134 | 4+612.75 | 9472499.660 | 610139.619 | 8.4 | D | 6.00 | 1.1 | 10.9 | 9.75 | no cumple (Ri < 6 m) | 0.11 |
| C-135 | 4+613.87 | 9472499.320 | 610138.552 | 3.2 | D | 24.06 | 20.1 | 28.1 | 8.00 | cumple (Ri ≥ 8 m) | 0.13 |
| C-138 | 4+705.94 | 9472442.070 | 610070.965 | 72.6 | D | 13.80 | 9.3 | 18.3 | 8.91 | cumple (Ri ≥ 8 m) | 0.46 |
| C-141 | 4+825.98 | 9472456.007 | 609952.809 | 80.8 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 1.23 |
| C-142 | 4+839.96 | 9472442.261 | 609940.648 | 22.4 | I | 19.70 | 15.6 | 23.8 | 8.22 | cumple (Ri ≥ 8 m) | 0.27 |
| C-143 | 4+877.93 | 9472406.297 | 609928.172 | 113.4 | D | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 1.09 |
| C-145 | 4+914.17 | 9472444.464 | 609892.798 | 90.1 | I | 8.00 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.26 |
| C-161 | 5+612.31 | 9472172.908 | 609260.939 | 30.0 | D | 12.91 | 8.3 | 17.5 | 9.17 | cumple (Ri ≥ 8 m) | 0.28 |
| C-165 | 5+830.61 | 9472283.454 | 609112.203 | 82.6 | I | 24.00 | 20.0 | 28.0 | 8.00 | cumple (Ri ≥ 8 m) | 1.09 |
| C-182 | 6+615.79 | 9471953.327 | 608663.664 | 97.7 | I | 11.03 | 6.2 | 15.9 | 9.70 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.34 |
| C-183 | 6+631.54 | 9471940.939 | 608645.255 | 71.0 | I | 13.35 | 8.8 | 17.9 | 9.04 | cumple (Ri ≥ 8 m) | 0.52 |
| C-184 | 6+641.16 | 9471929.222 | 608648.383 | 16.1 | I | 18.40 | 14.2 | 22.6 | 8.31 | cumple (Ri ≥ 8 m) | 0.15 |
| C-188 | 6+786.90 | 9471789.864 | 608685.060 | 41.9 | D | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.72 |
| C-189 | 6+805.44 | 9471773.408 | 608675.123 | 107.5 | D | 8.48 | 3.6 | 13.4 | 9.75 | no cumple (Ri < 6 m) | 0.44 |
| C-191 | 6+872.44 | 9471811.787 | 608614.087 | 56.8 | I | 13.97 | 9.5 | 18.4 | 8.87 | cumple (Ri ≥ 8 m) | 0.71 |
| C-198 | 7+168.53 | 9471709.489 | 608448.163 | 45.7 | D | 6.00 | 1.1 | 10.9 | 9.75 | no cumple (Ri < 6 m) | 1.08 |
| C-199 | 7+176.22 | 9471716.611 | 608451.725 | 71.7 | I | 7.52 | 2.6 | 12.4 | 9.75 | no cumple (Ri < 6 m) | 5.24 |
| C-200 | 7+194.59 | 9471730.601 | 608437.667 | 112.4 | I | 9.40 | 4.5 | 14.3 | 9.75 | no cumple (Ri < 6 m) | 5.64 |
| C-202 | 7+242.98 | 9471674.476 | 608428.671 | 6.9 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 2.86 |
| C-204 | 7+338.47 | 9471593.808 | 608479.262 | 17.1 | I | 8.00 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 2.08 |
| C-205 | 7+372.93 | 9471572.038 | 608505.994 | 151.7 | D | 7.97 | 3.1 | 12.8 | 9.75 | no cumple (Ri < 6 m) | 0.56 |
| C-206 | 7+371.47 | 9471579.670 | 608466.114 | 42.9 | D | 23.00 | 19.0 | 27.0 | 8.05 | cumple (Ri ≥ 8 m) | 0.43 |
| C-208 | 7+448.57 | 9471631.255 | 608409.634 | 63.3 | I | 14.34 | 10.0 | 18.7 | 8.76 | cumple (Ri ≥ 8 m) | 0.15 |
| C-211 | 7+565.84 | 9471572.115 | 608321.039 | 19.3 | I | 8.89 | 4.0 | 13.8 | 9.75 | no cumple (Ri < 6 m) | 0.63 |
| C-212 | 7+585.75 | 9471572.337 | 608301.096 | 133.6 | I | 7.90 | 3.0 | 12.8 | 9.75 | no cumple (Ri < 6 m) | 0.52 |
| C-213 | 7+592.54 | 9471553.874 | 608318.287 | 36.7 | I | 20.48 | 16.4 | 24.6 | 8.18 | cumple (Ri ≥ 8 m) | 0.33 |
| C-215 | 7+678.92 | 9471568.379 | 608398.272 | 12.3 | D | 22.99 | 19.0 | 27.0 | 8.05 | cumple (Ri ≥ 8 m) | 0.26 |
| C-216 | 7+693.47 | 9471576.001 | 608410.694 | 94.5 | D | 11.19 | 6.4 | 16.0 | 9.66 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.37 |
| C-221 | 7+826.73 | 9471445.917 | 608454.063 | 115.8 | D | 12.15 | 7.5 | 16.8 | 9.39 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.45 |
| C-222 | 7+832.57 | 9471453.375 | 608435.469 | 5.0 | D | 15.10 | 10.8 | 19.4 | 8.65 | cumple (Ri ≥ 8 m) | 0.32 |
| C-223 | 7+834.66 | 9471454.320 | 608433.604 | 10.5 | I | 10.80 | 5.9 | 15.7 | 9.75 | no cumple (Ri < 6 m) | 0.32 |
| C-224 | 7+836.29 | 9471454.780 | 608432.037 | 9.1 | D | 8.02 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.23 |
| C-226 | 7+913.35 | 9471482.198 | 608360.027 | 83.8 | I | 18.30 | 14.1 | 22.5 | 8.32 | cumple (Ri ≥ 8 m) | 1.02 |
| C-235 | 8+126.76 | 9471427.040 | 608167.698 | 82.8 | D | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.73 |
| C-249 | 8+615.01 | 9471852.429 | 607997.510 | 56.2 | I | 24.10 | 20.1 | 28.1 | 8.00 | cumple (Ri ≥ 8 m) | 1.04 |
| C-251 | 8+717.41 | 9471946.138 | 607961.163 | 69.0 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.64 |
| C-253 | 8+797.00 | 9471988.888 | 607893.859 | 138.0 | I | 8.60 | 3.7 | 13.5 | 9.75 | no cumple (Ri < 6 m) | 1.14 |
| C-254 | 8+803.37 | 9471958.469 | 607895.335 | 36.7 | I | 24.30 | 20.3 | 28.3 | 8.00 | cumple (Ri ≥ 8 m) | 0.64 |
| C-255 | 8+850.89 | 9471921.340 | 607925.882 | 68.6 | D | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.48 |
| C-257 | 9+007.18 | 9471781.884 | 607959.128 | 169.3 | D | 8.00 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 1.04 |
| C-259 | 9+011.03 | 9471900.924 | 607881.254 | 88.5 | I | 11.20 | 6.4 | 16.0 | 9.66 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.65 |
| C-262 | 9+120.11 | 9471955.720 | 607794.723 | 86.9 | I | 8.01 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.56 |
| C-264 | 9+155.23 | 9471935.932 | 607762.515 | 40.8 | I | 10.70 | 5.8 | 15.6 | 9.75 | no cumple (Ri < 6 m) | 0.47 |
| C-267 | 9+259.27 | 9471873.488 | 607828.259 | 104.5 | D | 11.75 | 7.0 | 16.5 | 9.50 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.55 |
| C-272 | 9+421.25 | 9471717.373 | 607840.435 | 154.9 | D | 8.30 | 3.4 | 13.2 | 9.75 | no cumple (Ri < 6 m) | 1.68 |
| C-274 | 9+461.53 | 9471788.571 | 607786.239 | 27.9 | I | 13.50 | 9.0 | 18.0 | 9.00 | cumple (Ri ≥ 8 m) | 0.38 |
| C-275 | 9+511.94 | 9471831.834 | 607760.094 | 96.0 | I | 14.70 | 10.3 | 19.1 | 8.71 | cumple (Ri ≥ 8 m) | 1.34 |
| C-281 | 9+746.83 | 9471880.585 | 607553.646 | 61.2 | D | 23.60 | 19.6 | 27.6 | 8.02 | cumple (Ri ≥ 8 m) | 0.71 |
| C-282 | 9+802.39 | 9471938.742 | 607550.086 | 146.4 | I | 8.70 | 3.8 | 13.6 | 9.75 | no cumple (Ri < 6 m) | 0.76 |
| C-288 | 10+080.86 | 9471725.993 | 607658.496 | 19.2 | I | 7.51 | 2.6 | 12.4 | 9.75 | no cumple (Ri < 6 m) | 0.96 |
| C-289 | 10+086.89 | 9471728.828 | 607663.850 | 73.6 | D | 6.40 | 1.5 | 11.3 | 9.75 | no cumple (Ri < 6 m) | 1.87 |
| C-292 | 10+181.32 | 9471636.629 | 607677.205 | 21.7 | D | 10.10 | 5.2 | 15.0 | 9.75 | no cumple (Ri < 6 m) | 0.60 |
| C-294 | 10+254.53 | 9471570.989 | 607695.578 | 39.6 | D | 10.60 | 5.7 | 15.5 | 9.75 | no cumple (Ri < 6 m) | 1.25 |
| C-295 | 10+276.41 | 9471549.058 | 607698.960 | 132.3 | D | 7.70 | 2.8 | 12.6 | 9.75 | no cumple (Ri < 6 m) | 0.82 |
| C-298 | 10+416.18 | 9471686.112 | 607641.417 | 74.0 | I | 12.40 | 7.7 | 17.1 | 9.31 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.51 |
| C-308 | 10+956.02 | 9471983.138 | 607508.918 | 44.7 | I | 17.00 | 12.8 | 21.2 | 8.43 | cumple (Ri ≥ 8 m) | 0.18 |
| C-312 | 11+051.62 | 9472072.165 | 607539.252 | 95.8 | I | 10.72 | 5.8 | 15.6 | 9.75 | no cumple (Ri < 6 m) | 0.70 |
| C-324 | 11+460.33 | 9472277.832 | 607212.267 | 8.5 | D | 14.54 | 10.2 | 18.9 | 8.73 | cumple (Ri ≥ 8 m) | 0.03 |

Agrupación en zonas (curvas de vuelta consecutivas):

| Zona | Prog. inicio | Prog. fin | Curvas | R mín. eje (m) | Ri mín. (m) | Evaluación |
|-----|--------|--------|------------|------|------|-------------|
| V-1 | 0+052.15 | 0+068.22 | C-2, C-3 | 6.0 | 1.1 | no cumple |
| V-2 | 0+111.03 | 0+130.27 | C-5 | 22.7 | 18.7 | cumple |
| V-3 | 0+182.01 | 0+229.19 | C-8, C-9, C-10, C-11 | 6.0 | 1.1 | no cumple |
| V-4 | 0+285.22 | 0+314.52 | C-13, C-14 | 12.2 | 7.5 | mínimo absoluto |
| V-5 | 0+434.92 | 0+439.23 | C-19 | 15.0 | 10.7 | cumple |
| V-6 | 0+635.00 | 0+636.31 | C-23 | 8.1 | 3.2 | no cumple |
| V-7 | 0+729.57 | 0+741.82 | C-25, C-26 | 7.2 | 2.3 | no cumple |
| V-8 | 1+029.14 | 1+046.35 | C-33 | 8.8 | 3.9 | no cumple |
| V-9 | 1+428.02 | 1+472.82 | C-41 | 24.2 | 20.2 | cumple |
| V-10 | 1+538.12 | 1+551.95 | C-43 | 11.7 | 6.9 | mínimo absoluto |
| V-11 | 1+789.23 | 1+789.49 | C-49 | 11.6 | 6.8 | mínimo absoluto |
| V-12 | 1+994.46 | 2+001.39 | C-56 | 8.0 | 3.1 | no cumple |
| V-13 | 2+026.32 | 2+031.54 | C-58 | 19.4 | 15.3 | cumple |
| V-14 | 2+075.29 | 2+101.98 | C-60 | 11.3 | 6.5 | mínimo absoluto |
| V-15 | 2+322.72 | 2+336.77 | C-66 | 9.1 | 4.2 | no cumple |
| V-16 | 2+624.03 | 2+636.00 | C-73 | 11.3 | 6.5 | mínimo absoluto |
| V-17 | 3+132.06 | 3+158.05 | C-86 | 20.0 | 15.9 | cumple |
| V-18 | 3+272.95 | 3+296.24 | C-90 | 15.0 | 10.7 | cumple |
| V-19 | 3+347.43 | 3+369.50 | C-92 | 8.6 | 3.7 | no cumple |
| V-20 | 3+542.20 | 3+551.50 | C-97 | 15.0 | 10.7 | cumple |
| V-21 | 3+572.59 | 3+588.96 | C-99 | 17.7 | 13.5 | cumple |
| V-22 | 3+677.10 | 3+681.38 | C-103 | 10.0 | 5.1 | no cumple |
| V-23 | 3+938.37 | 3+949.42 | C-111 | 20.0 | 15.9 | cumple |
| V-24 | 4+248.05 | 4+268.22 | C-120 | 12.4 | 7.7 | mínimo absoluto |
| V-25 | 4+516.44 | 4+528.32 | C-129 | 15.0 | 10.7 | cumple |
| V-26 | 4+605.65 | 4+606.51 | C-131 | 11.4 | 6.6 | mínimo absoluto |
| V-27 | 4+611.54 | 4+614.55 | C-133, C-134, C-135 | 6.0 | 1.1 | no cumple |
| V-28 | 4+695.81 | 4+713.29 | C-138 | 13.8 | 9.3 | cumple |
| V-29 | 4+813.22 | 4+884.78 | C-141, C-142, C-143 | 15.0 | 10.7 | cumple |
| V-30 | 4+906.15 | 4+918.73 | C-145 | 8.0 | 3.1 | no cumple |
| V-31 | 5+608.85 | 5+615.60 | C-161 | 12.9 | 8.3 | cumple |
| V-32 | 5+809.52 | 5+844.12 | C-165 | 24.0 | 20.0 | cumple |
| V-33 | 6+603.16 | 6+643.74 | C-182, C-183, C-184 | 11.0 | 6.2 | mínimo absoluto |
| V-34 | 6+779.25 | 6+809.79 | C-188, C-189 | 8.5 | 3.6 | no cumple |
| V-35 | 6+864.88 | 6+878.74 | C-191 | 14.0 | 9.5 | cumple |
| V-36 | 7+166.00 | 7+198.99 | C-198, C-199, C-200 | 6.0 | 1.1 | no cumple |
| V-37 | 7+242.07 | 7+243.88 | C-202 | 15.0 | 10.7 | cumple |
| V-38 | 7+337.26 | 7+379.65 | C-204, C-205, C-206 | 8.0 | 3.1 | no cumple |
| V-39 | 7+439.74 | 7+455.57 | C-208 | 14.3 | 10.0 | cumple |
| V-40 | 7+564.32 | 7+598.87 | C-211, C-212, C-213 | 7.9 | 3.0 | no cumple |
| V-41 | 7+676.45 | 7+699.82 | C-215, C-216 | 11.2 | 6.4 | mínimo absoluto |
| V-42 | 7+807.36 | 7+836.93 | C-221, C-222, C-223, C-224 | 8.0 | 3.1 | no cumple |
| V-43 | 7+896.92 | 7+923.70 | C-226 | 18.3 | 14.1 | cumple |
| V-44 | 8+109.11 | 8+138.03 | C-235 | 20.0 | 15.9 | cumple |
| V-45 | 8+602.15 | 8+625.77 | C-249 | 24.1 | 20.1 | cumple |
| V-46 | 8+707.11 | 8+725.17 | C-251 | 15.0 | 10.7 | cumple |
| V-47 | 8+774.60 | 8+861.19 | C-253, C-254, C-255 | 8.6 | 3.7 | no cumple |
| V-48 | 8+921.98 | 8+945.62 | C-257 | 8.0 | 3.1 | no cumple |
| V-49 | 9+000.11 | 9+017.42 | C-259 | 11.2 | 6.4 | mínimo absoluto |
| V-50 | 9+112.52 | 9+124.67 | C-262 | 8.0 | 3.1 | no cumple |
| V-51 | 9+151.25 | 9+158.87 | C-264 | 10.7 | 5.8 | no cumple |
| V-52 | 9+244.10 | 9+265.52 | C-267 | 11.7 | 7.0 | mínimo absoluto |
| V-53 | 9+383.98 | 9+406.42 | C-272 | 8.3 | 3.4 | no cumple |
| V-54 | 9+458.17 | 9+520.25 | C-274, C-275 | 13.5 | 9.0 | cumple |
| V-55 | 9+732.87 | 9+795.79 | C-281, C-282 | 8.7 | 3.8 | no cumple |
| V-56 | 10+079.58 | 10+090.32 | C-288, C-289 | 6.4 | 1.5 | no cumple |
| V-57 | 10+179.38 | 10+183.21 | C-292 | 10.1 | 5.2 | no cumple |
| V-58 | 10+250.71 | 10+276.78 | C-294, C-295 | 7.7 | 2.8 | no cumple |
| V-59 | 10+406.84 | 10+422.85 | C-298 | 12.4 | 7.7 | mínimo absoluto |
| V-60 | 10+949.03 | 10+962.30 | C-308 | 17.0 | 12.8 | cumple |
| V-61 | 11+039.75 | 11+057.68 | C-312 | 10.7 | 5.8 | no cumple |
| V-62 | 11+459.25 | 11+461.41 | C-324 | 14.5 | 10.2 | cumple |

## 6.4 Tangentes

| Longitud de la tangente intermedia | Cantidad |
|------------------------|------|
| 0 (curvas enlazadas) | 57 |
| 0 a 20 m | 181 |
| 20 a 56 m | 74 |
| 56 a 111 m | 11 |
| más de 111 m | 0 |

Las 4 tangentes que cumplen la Tabla 302.01 son:

| Entre curvas | Longitud (m) | Mínimo exigido (m) | Tipo |
|---------|------|------|------|
| C-76 y C-77 | 62.5 | 56 | curvas en S |
| C-162 y C-163 | 84.4 | 56 | curvas en S |
| C-165 y C-166 | 63.6 | 56 | curvas en S |
| C-171 y C-172 | 56.6 | 56 | curvas en S |

## 6.5 Sitios donde el eje se separa más de 2.5 m del trazo actual

Son los puntos a revisar en campo o en Civil 3D antes de aprobar el eje, por su posible afectación a edificaciones.

| Curva | Prog. PC | Prog. PT | Norte PI | Este PI | R (m) | Separación máx. (m) | Comentario |
|------|--------|--------|---------|---------|-----|------|----------------|
| C-97 | 3+542.20 | 3+551.50 | 9472520.056 | 611052.384 | 15.0 | 2.64 | cadena de curvas de radio variable en el trazo |
| C-98 | 3+552.41 | 3+571.30 | 9472511.901 | 611065.550 | 30.0 | 5.17 | cadena de curvas de radio variable en el trazo |
| C-99 | 3+572.59 | 3+588.96 | 9472493.487 | 611073.043 | 17.7 | 4.60 | cadena de curvas de radio variable en el trazo |
| C-100 | 3+590.49 | 3+626.52 | 9472468.891 | 611058.366 | 85.0 | 3.29 | cadena de curvas de radio variable en el trazo |
| C-101 | 3+627.81 | 3+654.52 | 9472449.657 | 611030.786 | 35.0 | 5.84 | cadena de curvas de radio variable en el trazo |
| C-102 | 3+655.72 | 3+677.10 | 9472453.707 | 611004.763 | 32.5 | 4.64 | cadena de curvas de radio variable en el trazo |
| C-199 | 7+170.78 | 7+180.20 | 9471716.611 | 608451.725 | 7.5 | 5.24 | cadena de curvas de radio variable en el trazo |
| C-200 | 7+180.55 | 7+198.99 | 9471730.601 | 608437.667 | 9.4 | 5.64 | cadena de curvas de radio variable en el trazo |
| C-201 | 7+200.13 | 7+234.25 | 9471700.434 | 608425.197 | 65.0 | 2.84 | cadena de curvas de radio variable en el trazo |
| C-202 | 7+242.07 | 7+243.88 | 9471674.476 | 608428.671 | 15.0 | 2.86 | cadena de curvas de radio variable en el trazo |
| C-301 | 10+506.62 | 10+626.52 | 9471641.793 | 607478.766 | 70.0 | 2.92 | cadena de curvas de radio variable en el trazo |

# 7. Conclusiones y recomendaciones

1. El eje cumple el radio mínimo de la DG-2018 (45 m a 40 km/h, peralte 12 %) en 175 de 324 curvas. En 58 curvas se adopta radio excepcional con velocidad específica de 30 km/h y en 91 se trata de curvas de vuelta o esquinas urbanas.
2. Las 35 curvas con radio interior menor de 6 m (zonas V-1, V-3 y otras indicadas en 6.3) no admiten justificación con la DG-2018. Se recomienda ampliar la plataforma en esos puntos o aceptar expropiaciones puntuales.
3. Los primeros 230 m (zona urbana de inicio) tienen geometría de calles, con radios de 6 a 22 m. Conviene tratar ese tramo como vía urbana con velocidad de 20 a 30 km/h.
4. Las clotoides, las tangentes mínimas y la longitud mínima de curva no se cumplen por la premisa de seguir el trazo existente. Debe dejarse constancia en el expediente, con la señalización vertical y horizontal correspondiente al Manual de Dispositivos de Control de Tránsito.
5. En Civil 3D, asociar al eje el archivo de criterios DG2018_Corregido_2.xml con velocidad 40 km/h; los triángulos de advertencia que queden marcan exactamente las curvas de los capítulos 6.2 y 6.3.
6. Verificar la visibilidad de parada (50 m) con banquetas en las curvas de radio menor a 60 m ubicadas en corte, según el Tópico 302.10.01.

# Anexo A. Tabla completa de curvas

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | T (m) | Lc (m) | E (m) | Prog. PC | Prog. PT | Sa (m) | Tang. sig. (m) | Sep. (m) | Clase |
|-----|--------|---------|---------|-----|---|-----|-----|-----|----|--------|--------|----|-----|----|---------|
| C-1 | 0+037.84 | 9472166.45 | 613022.23 | 44.7 | I | 38.78 | 15.9 | 30.2 | 3.15 | 0+021.90 | 0+052.15 | 3.57 | 0.0 | 1.16 | Excepcional |
| C-2 | 0+056.50 | 9472186.69 | 613023.88 | 72.0 | I | 6.00 | 4.4 | 7.5 | 1.41 | 0+052.15 | 0+059.68 | - | 0.0 | 0.96 | Vuelta |
| C-3 | 0+064.01 | 9472190.04 | 613015.87 | 23.1 | I | 21.22 | 4.3 | 8.5 | 0.44 | 0+059.68 | 0+068.22 | 6.49 | 18.1 | 1.08 | Vuelta |
| C-4 | 0+099.00 | 9472189.81 | 612980.76 | 31.5 | D | 44.97 | 12.7 | 24.7 | 1.75 | 0+086.33 | 0+111.03 | 3.11 | 0.0 | 1.89 | Normativa 12% |
| C-5 | 0+121.27 | 9472201.64 | 612961.14 | 48.6 | D | 22.70 | 10.2 | 19.2 | 2.20 | 0+111.03 | 0+130.27 | 6.04 | 11.9 | 1.76 | Vuelta |
| C-6 | 0+151.29 | 9472232.39 | 612955.53 | 12.2 | I | 85.00 | 9.1 | 18.1 | 0.48 | 0+142.22 | 0+160.29 | 1.75 | 0.6 | 0.21 | Normativa 8% |
| C-7 | 0+169.11 | 9472248.92 | 612948.68 | 36.4 | D | 25.00 | 8.2 | 15.9 | 1.32 | 0+160.88 | 0+176.78 | 5.47 | 5.2 | 0.43 | Excepcional |
| C-8 | 0+186.17 | 9472266.01 | 612952.91 | 42.2 | I | 10.75 | 4.2 | 7.9 | 0.77 | 0+182.01 | 0+189.94 | 18.57 | 0.0 | 0.36 | Vuelta |
| C-9 | 0+195.14 | 9472274.25 | 612948.47 | 81.8 | D | 6.00 | 5.2 | 8.6 | 1.94 | 0+189.94 | 0+198.51 | - | 2.1 | 1.15 | Vuelta |
| C-10 | 0+208.11 | 9472283.05 | 612960.37 | 35.0 | I | 23.80 | 7.5 | 14.5 | 1.15 | 0+200.61 | 0+215.14 | 5.75 | 0.5 | 0.45 | Vuelta |
| C-11 | 0+222.93 | 9472297.54 | 612965.22 | 51.6 | D | 15.00 | 7.3 | 13.5 | 1.66 | 0+215.67 | 0+229.19 | 9.71 | 46.2 | 2.11 | Vuelta |
| C-12 | 0+277.49 | 9472316.39 | 613017.48 | 5.5 | I | 45.00 | 2.1 | 4.3 | 0.05 | 0+275.34 | 0+279.63 | 3.10 | 5.6 | 0.91 | Normativa 12% |
| C-13 | 0+288.44 | 9472321.07 | 613027.39 | 18.3 | I | 20.00 | 3.2 | 6.4 | 0.26 | 0+285.22 | 0+291.60 | 6.91 | -0.0 | 0.25 | Vuelta |
| C-14 | 0+308.29 | 9472334.80 | 613041.80 | 107.6 | I | 12.20 | 16.7 | 22.9 | 8.47 | 0+291.60 | 0+314.52 | 13.29 | 0.0 | 0.59 | Vuelta |
| C-15 | 0+325.02 | 9472347.88 | 613017.99 | 28.7 | I | 40.97 | 10.5 | 20.5 | 1.32 | 0+314.52 | 0+335.07 | 3.39 | 22.1 | 0.21 | Excepcional |
| C-16 | 0+361.43 | 9472347.91 | 612981.13 | 10.9 | D | 45.00 | 4.3 | 8.6 | 0.20 | 0+357.14 | 0+365.70 | 3.10 | 13.2 | 0.22 | Normativa 12% |
| C-17 | 0+382.41 | 9472351.89 | 612960.51 | 8.8 | D | 45.00 | 3.5 | 6.9 | 0.13 | 0+378.94 | 0+385.86 | 3.10 | 28.6 | 0.09 | Normativa 12% |
| C-18 | 0+424.43 | 9472366.10 | 612920.95 | 12.6 | D | 90.00 | 9.9 | 19.8 | 0.55 | 0+414.50 | 0+434.28 | 1.66 | 0.6 | 0.17 | Normativa 8% |
| C-19 | 0+437.09 | 9472372.92 | 612910.18 | 16.4 | I | 15.00 | 2.2 | 4.3 | 0.16 | 0+434.92 | 0+439.23 | 9.71 | 19.6 | 0.15 | Vuelta |
| C-20 | 0+478.22 | 9472384.20 | 612870.60 | 46.7 | D | 45.00 | 19.4 | 36.7 | 4.01 | 0+458.80 | 0+495.47 | 3.10 | 17.3 | 1.55 | Normativa 12% |
| C-21 | 0+521.80 | 9472424.82 | 612849.55 | 22.8 | I | 45.00 | 9.1 | 17.9 | 0.90 | 0+512.74 | 0+530.62 | 3.10 | 50.2 | 0.29 | Normativa 12% |
| C-22 | 0+613.01 | 9472483.41 | 612779.33 | 77.8 | D | 39.90 | 32.2 | 54.2 | 11.38 | 0+580.80 | 0+635.00 | 3.47 | -0.0 | 1.74 | Excepcional |
| C-23 | 0+635.66 | 9472512.53 | 612794.60 | 9.3 | I | 8.07 | 0.7 | 1.3 | 0.03 | 0+635.00 | 0+636.31 | - | 40.6 | 0.74 | Vuelta |
| C-24 | 0+693.55 | 9472567.49 | 612812.81 | 40.5 | D | 45.00 | 16.6 | 31.8 | 2.96 | 0+676.96 | 0+708.76 | 3.10 | 20.8 | 0.70 | Normativa 12% |
| C-25 | 0+730.56 | 9472587.37 | 612845.66 | 6.5 | I | 17.37 | 1.0 | 2.0 | 0.03 | 0+729.57 | 0+731.55 | 8.10 | 0.0 | 0.45 | Vuelta |
| C-26 | 0+737.78 | 9472591.78 | 612851.37 | 81.7 | I | 7.20 | 6.2 | 10.3 | 2.32 | 0+731.55 | 0+741.82 | - | 11.4 | 0.69 | Vuelta |
| C-27 | 0+765.84 | 9472618.13 | 612836.50 | 45.9 | I | 29.88 | 12.7 | 24.0 | 2.57 | 0+753.18 | 0+777.13 | 4.58 | 0.0 | 0.97 | Excepcional |
| C-28 | 0+781.46 | 9472622.42 | 612820.06 | 14.1 | D | 35.00 | 4.3 | 8.6 | 0.27 | 0+777.13 | 0+785.75 | 3.93 | 59.5 | 0.39 | Excepcional |
| C-29 | 0+885.74 | 9472672.60 | 612728.60 | 84.0 | D | 45.00 | 40.5 | 66.0 | 15.55 | 0+845.22 | 0+911.20 | 3.10 | 3.1 | 1.56 | Normativa 12% |
| C-30 | 0+926.77 | 9472724.32 | 612750.29 | 31.9 | I | 43.60 | 12.5 | 24.3 | 1.75 | 0+914.30 | 0+938.59 | 3.20 | 8.0 | 1.38 | Excepcional |
| C-31 | 0+959.77 | 9472757.55 | 612744.92 | 21.3 | D | 70.00 | 13.2 | 26.0 | 1.23 | 0+946.60 | 0+972.64 | 2.08 | 24.1 | 0.33 | Normativa 8% |
| C-32 | 1+013.66 | 9472810.53 | 612756.32 | 41.3 | I | 44.95 | 17.0 | 32.4 | 3.09 | 0+996.71 | 1+029.14 | 3.11 | -0.0 | 0.86 | Normativa 12% |
| C-33 | 1+042.19 | 9472836.73 | 612741.68 | 112.0 | I | 8.80 | 13.1 | 17.2 | 6.94 | 1+029.14 | 1+046.35 | - | 20.1 | 0.65 | Vuelta |
| C-34 | 1+074.09 | 9472804.92 | 612716.14 | 19.3 | D | 45.00 | 7.7 | 15.2 | 0.65 | 1+066.42 | 1+081.61 | 3.10 | 2.1 | 0.33 | Normativa 12% |
| C-35 | 1+091.22 | 9472795.79 | 612701.47 | 10.8 | I | 80.00 | 7.6 | 15.1 | 0.36 | 1+083.67 | 1+098.73 | 1.84 | 20.4 | 0.07 | Normativa 8% |
| C-36 | 1+124.91 | 9472772.92 | 612676.67 | 14.7 | D | 45.00 | 5.8 | 11.6 | 0.37 | 1+119.10 | 1+130.66 | 3.10 | 9.1 | 0.34 | Normativa 12% |
| C-37 | 1+151.38 | 9472760.47 | 612653.23 | 21.9 | I | 60.00 | 11.6 | 22.9 | 1.11 | 1+139.79 | 1+162.70 | 2.39 | 20.2 | 0.25 | Normativa 8% |
| C-38 | 1+222.45 | 9472705.95 | 612607.21 | 55.6 | D | 75.00 | 39.6 | 72.8 | 9.80 | 1+182.87 | 1+255.70 | 1.95 | 62.9 | 0.53 | Normativa 8% |
| C-39 | 1+352.69 | 9472719.76 | 612471.34 | 74.3 | D | 45.00 | 34.1 | 58.3 | 11.45 | 1+318.61 | 1+376.95 | 3.10 | 26.6 | 0.93 | Normativa 12% |
| C-40 | 1+415.80 | 9472791.60 | 612458.78 | 30.4 | I | 45.00 | 12.2 | 23.9 | 1.63 | 1+403.57 | 1+427.45 | 3.10 | 0.6 | 1.18 | Normativa 12% |
| C-41 | 1+460.18 | 9472825.87 | 612429.69 | 106.1 | I | 24.20 | 32.2 | 44.8 | 16.04 | 1+428.02 | 1+472.82 | 5.65 | 0.0 | 0.98 | Vuelta |
| C-42 | 1+496.58 | 9472779.31 | 612398.74 | 60.8 | D | 40.48 | 23.8 | 43.0 | 6.46 | 1+472.82 | 1+515.79 | 3.43 | 22.3 | 0.76 | Excepcional |
| C-43 | 1+545.97 | 9472783.48 | 612344.96 | 67.7 | D | 11.70 | 7.8 | 13.8 | 2.39 | 1+538.12 | 1+551.95 | 14.45 | 15.5 | 0.49 | Vuelta |
| C-44 | 1+587.02 | 9472824.33 | 612331.80 | 66.4 | I | 29.90 | 19.6 | 34.6 | 5.83 | 1+567.46 | 1+602.10 | 4.58 | 4.3 | 0.61 | Excepcional |
| C-45 | 1+615.28 | 9472827.62 | 612299.23 | 22.3 | D | 45.00 | 8.9 | 17.5 | 0.86 | 1+606.43 | 1+623.92 | 3.10 | 7.3 | 0.51 | Normativa 12% |
| C-46 | 1+643.65 | 9472841.05 | 612274.00 | 35.4 | I | 38.90 | 12.4 | 24.1 | 1.94 | 1+631.22 | 1+655.28 | 3.56 | -0.0 | 1.21 | Excepcional |
| C-47 | 1+666.67 | 9472837.98 | 612250.37 | 32.3 | D | 39.31 | 11.4 | 22.2 | 1.62 | 1+655.28 | 1+677.45 | 3.52 | 11.0 | 0.38 | Excepcional |
| C-48 | 1+757.70 | 9472876.60 | 612167.27 | 103.1 | I | 55.00 | 69.2 | 99.0 | 33.43 | 1+688.45 | 1+787.41 | 2.58 | 1.8 | 1.57 | Normativa 8% |
| C-49 | 1+789.36 | 9472806.91 | 612152.66 | 1.3 | I | 11.60 | 0.1 | 0.3 | 0.00 | 1+789.23 | 1+789.49 | 14.73 | 20.0 | 0.05 | Vuelta |
| C-50 | 1+812.33 | 9472784.34 | 612148.46 | 7.1 | D | 45.00 | 2.8 | 5.6 | 0.09 | 1+809.54 | 1+815.11 | 3.10 | 18.9 | 0.22 | Normativa 12% |
| C-51 | 1+844.33 | 9472753.83 | 612138.77 | 16.8 | D | 70.00 | 10.4 | 20.6 | 0.76 | 1+833.96 | 1+854.55 | 2.08 | 28.0 | 0.43 | Normativa 8% |
| C-52 | 1+900.90 | 9472707.07 | 612106.66 | 29.3 | D | 70.00 | 18.3 | 35.8 | 2.36 | 1+882.58 | 1+918.42 | 2.08 | 5.5 | 0.43 | Normativa 8% |
| C-53 | 1+928.55 | 9472694.51 | 612081.13 | 11.8 | I | 45.00 | 4.7 | 9.3 | 0.24 | 1+923.90 | 1+933.17 | 3.10 | 12.0 | 0.17 | Normativa 12% |
| C-54 | 1+952.81 | 9472679.55 | 612061.98 | 19.2 | D | 45.00 | 7.6 | 15.1 | 0.64 | 1+945.18 | 1+960.30 | 3.10 | 13.5 | 0.16 | Normativa 12% |
| C-55 | 1+984.31 | 9472669.38 | 612032.02 | 27.0 | D | 43.90 | 10.5 | 20.7 | 1.25 | 1+973.77 | 1+994.46 | 3.18 | 0.0 | 0.17 | Excepcional |
| C-56 | 1+998.16 | 9472671.42 | 612017.93 | 49.5 | D | 8.01 | 3.7 | 6.9 | 0.81 | 1+994.46 | 2+001.39 | - | 3.4 | 0.27 | Vuelta |
| C-57 | 2+015.77 | 9472686.71 | 612008.29 | 27.4 | D | 45.00 | 11.0 | 21.5 | 1.32 | 2+004.79 | 2+026.32 | 3.10 | -0.0 | 0.76 | Normativa 12% |
| C-58 | 2+028.94 | 9472700.26 | 612007.14 | 15.4 | I | 19.40 | 2.6 | 5.2 | 0.18 | 2+026.32 | 2+031.54 | 7.15 | 19.7 | 0.17 | Vuelta |
| C-59 | 2+063.69 | 9472732.89 | 611995.11 | 37.0 | D | 37.28 | 12.5 | 24.1 | 2.03 | 2+051.21 | 2+075.29 | 3.70 | -0.0 | 0.65 | Excepcional |
| C-60 | 2+102.78 | 9472771.15 | 612006.63 | 135.3 | I | 11.30 | 27.5 | 26.7 | 18.42 | 2+075.29 | 2+101.98 | 15.69 | 3.5 | 0.39 | Vuelta |
| C-61 | 2+120.03 | 9472749.39 | 611966.63 | 20.6 | D | 80.00 | 14.5 | 28.7 | 1.31 | 2+105.51 | 2+134.24 | 1.84 | 6.1 | 0.24 | Normativa 8% |
| C-62 | 2+153.21 | 9472744.75 | 611933.46 | 32.0 | I | 45.00 | 12.9 | 25.1 | 1.81 | 2+140.31 | 2+165.44 | 3.10 | 1.6 | 0.60 | Normativa 12% |
| C-63 | 2+195.40 | 9472717.22 | 611900.60 | 86.8 | D | 30.00 | 28.4 | 45.4 | 11.28 | 2+167.05 | 2+212.48 | 4.56 | 13.6 | 1.24 | Excepcional |
| C-64 | 2+242.78 | 9472759.98 | 611860.45 | 40.8 | I | 45.00 | 16.8 | 32.1 | 3.02 | 2+226.03 | 2+258.10 | 3.10 | 15.1 | 0.51 | Normativa 12% |
| C-65 | 2+276.24 | 9472763.61 | 611825.76 | 7.7 | I | 45.00 | 3.0 | 6.0 | 0.10 | 2+273.21 | 2+279.25 | 3.10 | 43.5 | 0.62 | Normativa 12% |
| C-66 | 2+331.58 | 9472761.93 | 611770.43 | 88.4 | I | 9.10 | 8.9 | 14.0 | 3.60 | 2+322.72 | 2+336.77 | - | 0.4 | 0.94 | Vuelta |
| C-67 | 2+359.65 | 9472730.20 | 611770.53 | 29.7 | D | 85.00 | 22.5 | 44.0 | 2.93 | 2+337.13 | 2+381.17 | 1.75 | 0.6 | 0.34 | Normativa 8% |
| C-68 | 2+388.15 | 9472704.52 | 611756.00 | 16.2 | I | 45.00 | 6.4 | 12.7 | 0.45 | 2+381.74 | 2+394.47 | 3.10 | 18.6 | 0.57 | Normativa 12% |
| C-69 | 2+444.72 | 9472649.38 | 611742.96 | 43.2 | D | 80.00 | 31.7 | 60.3 | 6.05 | 2+413.03 | 2+473.37 | 1.84 | 36.6 | 0.54 | Normativa 8% |
| C-70 | 2+531.30 | 9472599.94 | 611668.21 | 42.4 | D | 55.00 | 21.3 | 40.7 | 3.98 | 2+510.00 | 2+550.65 | 2.58 | 1.6 | 0.45 | Normativa 8% |
| C-71 | 2+573.36 | 9472606.73 | 611624.72 | 71.4 | I | 29.40 | 21.1 | 36.6 | 6.79 | 2+552.25 | 2+588.87 | 4.65 | 9.8 | 0.37 | Excepcional |
| C-72 | 2+611.86 | 9472567.61 | 611604.35 | 38.9 | D | 37.30 | 13.2 | 25.4 | 2.26 | 2+598.68 | 2+624.03 | 3.70 | 0.0 | 1.18 | Excepcional |
| C-73 | 2+630.64 | 9472559.70 | 611586.19 | 60.6 | D | 11.32 | 6.6 | 12.0 | 1.79 | 2+624.03 | 2+636.00 | 15.62 | -0.0 | 0.35 | Vuelta |
| C-74 | 2+637.96 | 9472564.87 | 611579.35 | 3.6 | D | 62.14 | 2.0 | 3.9 | 0.03 | 2+636.00 | 2+639.91 | 2.31 | 5.0 | 0.12 | Normativa 8% |
| C-75 | 2+657.32 | 9472577.48 | 611564.66 | 30.8 | I | 45.00 | 12.4 | 24.2 | 1.67 | 2+644.94 | 2+669.10 | 3.10 | 12.4 | 0.74 | Normativa 12% |
| C-76 | 2+691.77 | 9472583.50 | 611530.13 | 25.8 | D | 45.00 | 10.3 | 20.2 | 1.16 | 2+681.48 | 2+701.71 | 3.10 | 62.5 | 0.95 | Normativa 12% |
| C-77 | 2+765.81 | 9472626.87 | 611469.69 | 0.4 | I | 450.00 | 1.6 | 3.2 | 0.00 | 2+764.23 | 2+767.40 | 0.44 | 0.9 | 0.58 | Normativa 8% |
| C-78 | 2+786.53 | 9472638.83 | 611452.77 | 62.6 | I | 30.00 | 18.2 | 32.8 | 5.11 | 2+768.28 | 2+801.07 | 4.56 | 17.7 | 1.66 | Excepcional |
| C-79 | 2+825.63 | 9472619.14 | 611414.75 | 17.3 | I | 45.00 | 6.8 | 13.6 | 0.52 | 2+818.79 | 2+832.38 | 3.10 | 12.6 | 0.31 | Normativa 12% |
| C-80 | 2+883.11 | 9472578.66 | 611373.81 | 69.5 | D | 55.00 | 38.2 | 66.7 | 11.95 | 2+844.94 | 2+911.68 | 2.58 | 6.4 | 1.02 | Normativa 8% |
| C-81 | 2+938.66 | 9472606.04 | 611314.68 | 41.1 | I | 55.00 | 20.6 | 39.4 | 3.73 | 2+918.07 | 2+957.48 | 2.58 | 23.5 | 0.40 | Normativa 8% |
| C-82 | 3+000.40 | 9472588.32 | 611253.69 | 75.6 | D | 25.00 | 19.4 | 33.0 | 6.63 | 2+981.02 | 3+013.99 | 5.47 | 19.0 | 0.57 | Excepcional |
| C-83 | 3+036.40 | 9472624.27 | 611232.39 | 8.8 | D | 45.00 | 3.5 | 6.9 | 0.13 | 3+032.94 | 3+039.84 | 3.10 | 16.0 | 0.21 | Normativa 12% |
| C-84 | 3+059.08 | 9472645.33 | 611223.94 | 8.1 | D | 45.00 | 3.2 | 6.4 | 0.11 | 3+055.89 | 3+062.27 | 3.10 | 52.5 | 0.12 | Normativa 12% |
| C-85 | 3+123.31 | 9472707.74 | 611208.70 | 22.5 | I | 43.10 | 8.6 | 16.9 | 0.85 | 3+114.73 | 3+131.68 | 3.23 | 0.4 | 0.35 | Excepcional |
| C-86 | 3+147.26 | 9472727.23 | 611194.41 | 74.4 | I | 20.00 | 15.2 | 26.0 | 5.12 | 3+132.06 | 3+158.05 | 6.91 | 5.7 | 0.37 | Vuelta |
| C-87 | 3+176.10 | 9472715.48 | 611163.31 | 30.6 | I | 45.00 | 12.3 | 24.1 | 1.66 | 3+163.77 | 3+187.83 | 3.10 | 19.5 | 0.58 | Normativa 12% |
| C-88 | 3+224.27 | 9472677.40 | 611132.85 | 21.4 | D | 90.00 | 17.0 | 33.6 | 1.59 | 3+207.29 | 3+240.85 | 1.66 | 5.7 | 0.15 | Normativa 8% |
| C-89 | 3+255.08 | 9472661.81 | 611105.82 | 21.6 | I | 45.00 | 8.6 | 16.9 | 0.81 | 3+246.51 | 3+263.44 | 3.10 | 9.5 | 0.32 | Normativa 12% |
| C-90 | 3+287.68 | 9472636.12 | 611085.42 | 89.0 | D | 15.00 | 14.7 | 23.3 | 6.02 | 3+272.95 | 3+296.24 | 9.71 | 2.3 | 0.91 | Vuelta |
| C-91 | 3+324.31 | 9472662.12 | 611051.43 | 50.2 | D | 55.00 | 25.8 | 48.2 | 5.73 | 3+298.55 | 3+346.73 | 2.58 | 0.7 | 0.61 | Normativa 8% |
| C-92 | 3+376.47 | 9472717.58 | 611049.12 | 147.0 | I | 8.60 | 29.0 | 22.1 | 21.69 | 3+347.43 | 3+369.50 | - | -0.0 | 0.39 | Vuelta |
| C-93 | 3+379.61 | 9472683.87 | 611029.18 | 32.2 | I | 35.01 | 10.1 | 19.7 | 1.43 | 3+369.50 | 3+389.18 | 3.93 | 16.4 | 1.18 | Excepcional |
| C-94 | 3+409.78 | 9472653.18 | 611030.05 | 10.5 | D | 45.00 | 4.2 | 8.3 | 0.19 | 3+405.63 | 3+413.90 | 3.10 | 0.8 | 0.25 | Normativa 12% |
| C-95 | 3+420.91 | 9472642.16 | 611028.32 | 10.1 | I | 70.00 | 6.2 | 12.4 | 0.27 | 3+414.71 | 3+427.08 | 2.08 | 39.1 | 0.36 | Normativa 8% |
| C-96 | 3+488.95 | 9472574.10 | 611029.76 | 21.5 | I | 120.00 | 22.8 | 45.0 | 2.15 | 3+466.16 | 3+511.21 | 1.29 | 31.0 | 0.22 | Normativa 8% |
| C-97 | 3+547.00 | 9472520.06 | 611052.38 | 35.5 | I | 15.00 | 4.8 | 9.3 | 0.75 | 3+542.20 | 3+551.50 | 9.71 | 0.9 | 2.64 | Vuelta |
| C-98 | 3+562.18 | 9472511.90 | 611065.55 | 36.1 | D | 30.00 | 9.8 | 18.9 | 1.55 | 3+552.41 | 3+571.30 | 4.56 | 1.3 | 5.17 | Excepcional |
| C-99 | 3+581.41 | 9472493.49 | 611073.04 | 53.0 | D | 17.70 | 8.8 | 16.4 | 2.08 | 3+572.59 | 3+588.96 | 7.93 | 1.5 | 4.60 | Vuelta |
| C-100 | 3+608.78 | 9472468.89 | 611058.37 | 24.3 | D | 85.00 | 18.3 | 36.0 | 1.94 | 3+590.49 | 3+626.52 | 1.75 | 1.3 | 3.29 | Normativa 8% |
| C-101 | 3+641.85 | 9472449.66 | 611030.79 | 43.7 | D | 35.00 | 14.0 | 26.7 | 2.71 | 3+627.81 | 3+654.52 | 3.93 | 1.2 | 5.84 | Excepcional |
| C-102 | 3+666.81 | 9472453.71 | 611004.76 | 37.7 | D | 32.50 | 11.1 | 21.4 | 1.84 | 3+655.72 | 3+677.10 | 4.22 | 0.0 | 4.64 | Excepcional |
| C-103 | 3+679.27 | 9472463.34 | 610995.64 | 24.5 | I | 10.02 | 2.2 | 4.3 | 0.23 | 3+677.10 | 3+681.38 | - | 29.7 | 1.50 | Vuelta |
| C-104 | 3+722.23 | 9472479.48 | 610955.76 | 27.8 | I | 45.00 | 11.1 | 21.8 | 1.35 | 3+711.12 | 3+732.91 | 3.10 | 24.6 | 1.14 | Normativa 12% |
| C-105 | 3+771.94 | 9472474.50 | 610905.86 | 32.2 | D | 50.00 | 14.5 | 28.1 | 2.05 | 3+757.49 | 3+785.63 | 2.82 | 45.1 | 0.36 | Normativa 8% |
| C-106 | 3+832.86 | 9472502.06 | 610850.68 | 5.5 | D | 45.00 | 2.2 | 4.4 | 0.05 | 3+830.68 | 3+835.04 | 3.10 | 4.2 | 0.43 | Normativa 12% |
| C-107 | 3+842.51 | 9472507.19 | 610842.49 | 8.4 | I | 45.00 | 3.3 | 6.6 | 0.12 | 3+839.20 | 3+845.81 | 3.10 | 4.2 | 0.12 | Normativa 12% |
| C-108 | 3+851.51 | 9472510.81 | 610834.24 | 3.9 | I | 45.00 | 1.5 | 3.0 | 0.03 | 3+850.00 | 3+853.03 | 3.10 | 11.4 | 0.07 | Normativa 12% |
| C-109 | 3+867.59 | 9472516.26 | 610819.12 | 4.6 | D | 80.00 | 3.2 | 6.4 | 0.06 | 3+864.39 | 3+870.78 | 1.84 | 49.0 | 0.14 | Normativa 8% |
| C-110 | 3+928.83 | 9472541.55 | 610763.34 | 14.8 | D | 70.00 | 9.1 | 18.0 | 0.59 | 3+919.76 | 3+937.80 | 2.08 | 0.6 | 0.27 | Normativa 8% |
| C-111 | 3+944.04 | 9472551.22 | 610751.47 | 31.7 | I | 20.00 | 5.7 | 11.0 | 0.79 | 3+938.37 | 3+949.42 | 6.91 | 11.8 | 0.60 | Vuelta |
| C-112 | 3+964.83 | 9472553.98 | 610730.57 | 9.1 | D | 45.00 | 3.6 | 7.2 | 0.14 | 3+961.25 | 3+968.41 | 3.10 | 17.1 | 0.24 | Normativa 12% |
| C-113 | 4+003.78 | 9472565.13 | 610693.24 | 24.2 | I | 85.00 | 18.2 | 35.9 | 1.93 | 3+985.55 | 4+021.46 | 1.75 | 3.1 | 0.23 | Normativa 8% |
| C-114 | 4+037.62 | 9472560.59 | 610659.16 | 10.7 | D | 140.00 | 13.1 | 26.1 | 0.61 | 4+024.55 | 4+050.61 | 1.13 | 18.1 | 0.36 | Normativa 8% |
| C-115 | 4+073.62 | 9472562.54 | 610623.13 | 12.5 | D | 45.00 | 4.9 | 9.8 | 0.27 | 4+068.68 | 4+078.52 | 3.10 | 9.2 | 0.31 | Normativa 12% |
| C-116 | 4+104.87 | 9472570.96 | 610592.99 | 29.6 | I | 65.00 | 17.2 | 33.6 | 2.23 | 4+087.68 | 4+121.29 | 2.22 | 45.2 | 0.37 | Normativa 8% |
| C-117 | 4+186.39 | 9472551.05 | 610513.15 | 31.8 | D | 70.00 | 19.9 | 38.8 | 2.78 | 4+166.47 | 4+205.29 | 2.08 | 0.9 | 0.66 | Normativa 8% |
| C-118 | 4+217.46 | 9472560.86 | 610482.58 | 28.2 | I | 45.00 | 11.3 | 22.1 | 1.40 | 4+206.16 | 4+228.31 | 3.10 | 1.8 | 0.51 | Normativa 12% |
| C-119 | 4+239.21 | 9472556.84 | 610460.74 | 22.9 | D | 44.89 | 9.1 | 17.9 | 0.91 | 4+230.12 | 4+248.05 | 3.11 | 0.0 | 0.25 | Excepcional |
| C-120 | 4+261.17 | 9472561.63 | 610439.07 | 93.2 | I | 12.40 | 13.1 | 20.2 | 5.65 | 4+248.05 | 4+268.22 | 12.90 | 6.4 | 1.46 | Vuelta |
| C-121 | 4+281.60 | 9472535.49 | 610434.81 | 14.5 | D | 55.00 | 7.0 | 13.9 | 0.44 | 4+274.62 | 4+288.51 | 2.58 | 2.1 | 0.30 | Normativa 8% |
| C-122 | 4+313.75 | 9472505.99 | 610421.84 | 75.2 | D | 30.00 | 23.1 | 39.4 | 7.87 | 4+290.63 | 4+330.02 | 4.56 | 1.2 | 0.80 | Excepcional |
| C-123 | 4+351.04 | 9472512.85 | 610378.25 | 27.8 | D | 80.00 | 19.8 | 38.8 | 2.41 | 4+331.25 | 4+370.05 | 1.84 | 30.1 | 0.38 | Normativa 8% |
| C-124 | 4+414.59 | 9472551.33 | 610326.69 | 35.6 | I | 45.00 | 14.5 | 28.0 | 2.27 | 4+400.13 | 4+428.12 | 3.10 | 8.9 | 0.49 | Normativa 12% |
| C-125 | 4+444.63 | 9472551.92 | 610295.72 | 9.7 | I | 90.00 | 7.6 | 15.3 | 0.32 | 4+436.98 | 4+452.24 | 1.66 | 26.9 | 0.13 | Normativa 8% |
| C-126 | 4+480.72 | 9472546.51 | 610260.01 | 4.1 | I | 45.00 | 1.6 | 3.2 | 0.03 | 4+479.10 | 4+482.33 | 3.10 | 13.9 | 0.17 | Normativa 12% |
| C-127 | 4+500.03 | 9472542.26 | 610241.17 | 4.3 | D | 100.00 | 3.8 | 7.6 | 0.07 | 4+496.25 | 4+503.80 | 1.52 | 0.6 | 0.06 | Normativa 8% |
| C-128 | 4+510.08 | 9472540.79 | 610231.22 | 9.2 | D | 70.00 | 5.7 | 11.3 | 0.23 | 4+504.42 | 4+515.71 | 2.08 | 0.7 | 0.09 | Normativa 8% |
| C-129 | 4+522.71 | 9472540.97 | 610218.57 | 45.4 | I | 15.00 | 6.3 | 11.9 | 1.26 | 4+516.44 | 4+528.32 | 9.71 | 13.6 | 0.19 | Vuelta |
| C-130 | 4+552.04 | 9472519.93 | 610197.19 | 25.5 | D | 45.00 | 10.2 | 20.0 | 1.13 | 4+541.88 | 4+561.87 | 3.10 | 43.8 | 1.27 | Normativa 12% |
| C-131 | 4+606.08 | 9472502.14 | 610145.81 | 4.3 | I | 11.40 | 0.4 | 0.9 | 0.01 | 4+605.65 | 4+606.51 | 15.35 | -0.0 | 0.44 | Vuelta |
| C-132 | 4+608.98 | 9472500.99 | 610143.15 | 4.3 | D | 65.41 | 2.5 | 4.9 | 0.05 | 4+606.51 | 4+611.44 | 2.21 | 0.1 | 0.15 | Normativa 8% |
| C-133 | 4+611.93 | 9472500.02 | 610140.36 | 7.0 | I | 6.31 | 0.4 | 0.8 | 0.01 | 4+611.54 | 4+612.31 | - | 0.0 | 0.33 | Vuelta |
| C-134 | 4+612.75 | 9472499.66 | 610139.62 | 8.4 | D | 6.00 | 0.4 | 0.9 | 0.02 | 4+612.31 | 4+613.19 | - | 0.0 | 0.11 | Vuelta |
| C-135 | 4+613.87 | 9472499.32 | 610138.55 | 3.2 | D | 24.06 | 0.7 | 1.4 | 0.01 | 4+613.19 | 4+614.55 | 5.69 | 1.0 | 0.13 | Vuelta |
| C-136 | 4+642.71 | 9472492.11 | 610110.63 | 30.3 | I | 100.00 | 27.1 | 53.0 | 3.61 | 4+615.60 | 4+668.55 | 1.52 | 6.3 | 0.31 | Normativa 8% |
| C-137 | 4+682.14 | 9472463.42 | 610081.75 | 18.4 | I | 45.00 | 7.3 | 14.4 | 0.59 | 4+674.86 | 4+689.30 | 3.10 | 6.5 | 0.13 | Normativa 12% |
| C-138 | 4+705.94 | 9472442.07 | 610070.96 | 72.6 | D | 13.80 | 10.1 | 17.5 | 3.32 | 4+695.81 | 4+713.29 | 10.88 | 23.4 | 0.46 | Vuelta |
| C-139 | 4+745.10 | 9472448.89 | 610029.59 | 21.3 | I | 45.00 | 8.4 | 16.7 | 0.79 | 4+736.65 | 4+753.34 | 3.10 | 23.5 | 0.22 | Normativa 12% |
| C-140 | 4+795.10 | 9472438.54 | 609980.47 | 44.2 | D | 45.00 | 18.3 | 34.7 | 3.57 | 4+776.83 | 4+811.53 | 3.10 | 1.7 | 1.65 | Normativa 12% |
| C-141 | 4+825.98 | 9472456.01 | 609952.81 | 80.8 | I | 15.00 | 12.8 | 21.1 | 4.69 | 4+813.22 | 4+834.37 | 9.71 | 1.7 | 1.23 | Vuelta |
| C-142 | 4+839.96 | 9472442.26 | 609940.65 | 22.4 | I | 19.70 | 3.9 | 7.7 | 0.38 | 4+836.07 | 4+843.76 | 7.03 | 11.3 | 0.27 | Vuelta |
| C-143 | 4+877.93 | 9472406.30 | 609928.17 | 113.4 | D | 15.00 | 22.8 | 29.7 | 12.33 | 4+855.09 | 4+884.78 | 9.71 | 2.1 | 1.09 | Vuelta |
| C-144 | 4+890.95 | 9472425.92 | 609906.80 | 10.4 | D | 45.00 | 4.1 | 8.2 | 0.19 | 4+886.85 | 4+895.03 | 3.10 | 11.1 | 0.13 | Normativa 12% |
| C-145 | 4+914.17 | 9472444.46 | 609892.80 | 90.1 | I | 8.00 | 8.0 | 12.6 | 3.32 | 4+906.15 | 4+918.73 | - | 11.3 | 0.26 | Vuelta |
| C-146 | 4+936.22 | 9472429.06 | 609872.47 | 8.3 | D | 85.00 | 6.2 | 12.3 | 0.22 | 4+930.04 | 4+942.38 | 1.75 | 24.4 | 0.18 | Normativa 8% |
| C-147 | 4+975.16 | 9472410.27 | 609838.34 | 17.4 | I | 55.00 | 8.4 | 16.7 | 0.64 | 4+966.73 | 4+983.46 | 2.58 | 19.1 | 0.19 | Normativa 8% |
| C-148 | 5+015.19 | 9472381.26 | 609810.57 | 10.3 | D | 140.00 | 12.6 | 25.2 | 0.57 | 5+002.58 | 5+027.73 | 1.13 | 43.1 | 0.12 | Normativa 8% |
| C-149 | 5+074.35 | 9472346.47 | 609762.63 | 8.9 | D | 45.00 | 3.5 | 7.0 | 0.14 | 5+070.83 | 5+077.86 | 3.10 | 62.2 | 0.27 | Normativa 12% |
| C-150 | 5+142.06 | 9472315.71 | 609702.30 | 5.1 | D | 45.00 | 2.0 | 4.0 | 0.04 | 5+140.08 | 5+144.05 | 3.10 | 17.7 | 0.47 | Normativa 12% |
| C-151 | 5+173.09 | 9472304.10 | 609673.52 | 15.2 | D | 85.00 | 11.3 | 22.6 | 0.75 | 5+161.74 | 5+184.30 | 1.75 | 14.4 | 0.30 | Normativa 8% |
| C-152 | 5+205.94 | 9472300.22 | 609640.77 | 18.3 | I | 45.00 | 7.3 | 14.4 | 0.58 | 5+198.68 | 5+213.08 | 3.10 | 15.0 | 0.87 | Normativa 12% |
| C-153 | 5+241.45 | 9472285.11 | 609608.50 | 12.7 | D | 120.00 | 13.3 | 26.6 | 0.74 | 5+228.11 | 5+254.68 | 1.29 | 31.5 | 0.24 | Normativa 8% |
| C-154 | 5+298.73 | 9472272.78 | 609552.45 | 9.6 | I | 150.00 | 12.6 | 25.1 | 0.53 | 5+286.14 | 5+311.25 | 1.07 | 7.8 | 0.17 | Normativa 8% |
| C-155 | 5+322.51 | 9472263.85 | 609530.35 | 8.8 | D | 45.00 | 3.5 | 6.9 | 0.13 | 5+319.05 | 5+325.95 | 3.10 | 20.2 | 0.23 | Normativa 12% |
| C-156 | 5+351.53 | 9472257.22 | 609502.07 | 13.6 | I | 45.00 | 5.4 | 10.7 | 0.32 | 5+346.15 | 5+356.87 | 3.10 | 15.8 | 0.29 | Normativa 12% |
| C-157 | 5+374.93 | 9472246.63 | 609481.15 | 5.9 | D | 45.00 | 2.3 | 4.6 | 0.06 | 5+372.62 | 5+377.24 | 3.10 | 59.4 | 0.21 | Normativa 12% |
| C-158 | 5+438.41 | 9472223.93 | 609421.87 | 4.4 | D | 45.00 | 1.7 | 3.5 | 0.03 | 5+436.67 | 5+440.14 | 3.10 | 45.7 | 0.25 | Normativa 12% |
| C-159 | 5+492.79 | 9472208.44 | 609369.74 | 17.6 | I | 45.00 | 7.0 | 13.8 | 0.53 | 5+485.83 | 5+499.63 | 3.10 | 36.8 | 0.68 | Normativa 12% |
| C-160 | 5+575.01 | 9472162.25 | 609301.59 | 48.8 | D | 85.00 | 38.6 | 72.4 | 8.34 | 5+536.43 | 5+608.85 | 1.75 | 0.0 | 0.63 | Normativa 8% |
| C-161 | 5+612.31 | 9472172.91 | 609260.94 | 30.0 | D | 12.91 | 3.5 | 6.7 | 0.45 | 5+608.85 | 5+615.60 | 12.05 | 4.7 | 0.28 | Vuelta |
| C-162 | 5+629.74 | 9472185.27 | 609248.42 | 21.4 | D | 50.00 | 9.5 | 18.7 | 0.89 | 5+620.29 | 5+638.97 | 2.82 | 84.4 | 0.21 | Normativa 8% |
| C-163 | 5+752.32 | 9472297.51 | 609198.60 | 80.4 | I | 34.20 | 28.9 | 48.0 | 10.58 | 5+723.41 | 5+771.41 | 4.02 | 22.1 | 0.42 | Excepcional |
| C-164 | 5+799.18 | 9472283.46 | 609143.68 | 14.3 | D | 45.00 | 5.7 | 11.3 | 0.35 | 5+793.52 | 5+804.78 | 3.10 | 4.7 | 0.48 | Normativa 12% |
| C-165 | 5+830.61 | 9472283.45 | 609112.20 | 82.6 | I | 24.00 | 21.1 | 34.6 | 7.94 | 5+809.52 | 5+844.12 | 5.70 | 63.6 | 1.09 | Vuelta |
| C-166 | 5+913.70 | 9472193.54 | 609100.53 | 13.5 | D | 50.00 | 5.9 | 11.8 | 0.35 | 5+907.77 | 5+919.58 | 2.82 | 32.8 | 0.47 | Normativa 8% |
| C-167 | 5+955.77 | 9472154.20 | 609085.48 | 8.5 | D | 45.00 | 3.3 | 6.7 | 0.12 | 5+952.43 | 5+959.10 | 3.10 | 38.1 | 0.22 | Normativa 12% |
| C-168 | 5+999.89 | 9472115.77 | 609063.79 | 6.7 | D | 45.00 | 2.7 | 5.3 | 0.08 | 5+997.24 | 6+002.54 | 3.10 | 13.2 | 0.22 | Normativa 12% |
| C-169 | 6+017.87 | 9472101.25 | 609053.17 | 5.4 | D | 45.00 | 2.1 | 4.2 | 0.05 | 6+015.75 | 6+019.98 | 3.10 | 38.5 | 0.26 | Normativa 12% |
| C-170 | 6+067.74 | 9472063.94 | 609020.08 | 15.1 | I | 70.00 | 9.3 | 18.5 | 0.61 | 6+058.45 | 6+076.91 | 2.08 | 13.7 | 0.13 | Normativa 8% |
| C-171 | 6+093.41 | 9472040.85 | 609008.60 | 7.2 | I | 45.00 | 2.8 | 5.7 | 0.09 | 6+090.57 | 6+096.25 | 3.10 | 56.6 | 0.60 | Normativa 12% |
| C-172 | 6+189.10 | 9471950.49 | 608977.09 | 48.8 | D | 80.00 | 36.3 | 68.1 | 7.84 | 6+152.84 | 6+220.94 | 1.84 | 7.5 | 0.88 | Normativa 8% |
| C-173 | 6+237.94 | 9471930.53 | 608927.71 | 23.8 | I | 45.00 | 9.5 | 18.7 | 0.99 | 6+228.43 | 6+247.17 | 3.10 | 22.0 | 0.59 | Normativa 12% |
| C-174 | 6+272.65 | 9471905.42 | 608903.34 | 8.9 | D | 45.00 | 3.5 | 7.0 | 0.14 | 6+269.14 | 6+276.15 | 3.10 | 41.0 | 0.26 | Normativa 12% |
| C-175 | 6+321.82 | 9471875.88 | 608864.01 | 11.8 | D | 45.00 | 4.7 | 9.3 | 0.24 | 6+317.16 | 6+326.45 | 3.10 | 0.8 | 0.32 | Normativa 12% |
| C-176 | 6+341.14 | 9471867.67 | 608846.49 | 14.4 | I | 110.00 | 13.9 | 27.6 | 0.87 | 6+327.28 | 6+354.86 | 1.40 | 18.3 | 0.26 | Normativa 8% |
| C-177 | 6+380.09 | 9471842.83 | 608816.30 | 14.4 | D | 55.00 | 6.9 | 13.8 | 0.44 | 6+373.15 | 6+386.95 | 2.58 | 36.8 | 0.54 | Normativa 8% |
| C-178 | 6+459.63 | 9471809.09 | 608744.19 | 77.1 | D | 45.00 | 35.9 | 60.6 | 12.56 | 6+423.74 | 6+484.33 | 3.10 | 32.7 | 1.93 | Normativa 12% |
| C-179 | 6+537.16 | 9471879.06 | 608689.65 | 17.6 | D | 130.00 | 20.1 | 39.8 | 1.54 | 6+517.08 | 6+556.93 | 1.21 | 12.8 | 0.15 | Normativa 8% |
| C-180 | 6+576.19 | 9471915.94 | 608675.96 | 9.3 | D | 80.00 | 6.5 | 12.9 | 0.26 | 6+569.71 | 6+582.64 | 1.84 | 8.6 | 0.08 | Normativa 8% |
| C-181 | 6+597.23 | 9471936.61 | 608671.90 | 15.1 | I | 45.26 | 6.0 | 11.9 | 0.40 | 6+591.22 | 6+603.16 | 3.09 | 0.0 | 0.29 | Normativa 12% |
| C-182 | 6+615.79 | 9471953.33 | 608663.66 | 97.7 | I | 11.03 | 12.6 | 18.8 | 5.74 | 6+603.16 | 6+621.98 | 16.81 | 0.0 | 0.34 | Vuelta |
| C-183 | 6+631.54 | 9471940.94 | 608645.26 | 71.0 | I | 13.35 | 9.5 | 16.5 | 3.05 | 6+622.02 | 6+638.56 | 11.44 | 0.0 | 0.52 | Vuelta |
| C-184 | 6+641.16 | 9471929.22 | 608648.38 | 16.1 | I | 18.40 | 2.6 | 5.2 | 0.18 | 6+638.56 | 6+643.74 | 7.58 | 4.8 | 0.15 | Vuelta |
| C-185 | 6+658.48 | 9471914.36 | 608657.34 | 25.0 | D | 45.00 | 10.0 | 19.7 | 1.09 | 6+648.50 | 6+668.15 | 3.10 | 26.1 | 0.39 | Normativa 12% |
| C-186 | 6+702.86 | 9471869.91 | 608662.04 | 32.1 | I | 30.00 | 8.6 | 16.8 | 1.21 | 6+694.24 | 6+711.03 | 4.56 | 0.0 | 0.66 | Excepcional |
| C-187 | 6+719.09 | 9471856.78 | 608672.34 | 27.4 | D | 33.14 | 8.1 | 15.8 | 0.97 | 6+711.03 | 6+726.85 | 4.14 | 52.4 | 0.21 | Excepcional |
| C-188 | 6+786.90 | 9471789.86 | 608685.06 | 41.9 | D | 20.00 | 7.7 | 14.6 | 1.41 | 6+779.25 | 6+793.87 | 6.91 | 0.0 | 0.72 | Vuelta |
| C-189 | 6+805.44 | 9471773.41 | 608675.12 | 107.5 | D | 8.48 | 11.6 | 15.9 | 5.86 | 6+793.87 | 6+809.79 | - | 9.4 | 0.44 | Vuelta |
| C-190 | 6+835.21 | 9471801.16 | 608650.67 | 32.4 | I | 55.00 | 16.0 | 31.1 | 2.28 | 6+819.22 | 6+850.34 | 2.58 | 14.5 | 0.42 | Normativa 8% |
| C-191 | 6+872.44 | 9471811.79 | 608614.09 | 56.8 | I | 13.97 | 7.6 | 13.9 | 1.91 | 6+864.88 | 6+878.74 | 10.69 | -0.0 | 0.71 | Vuelta |
| C-192 | 6+884.43 | 9471803.16 | 608604.03 | 19.0 | I | 34.00 | 5.7 | 11.3 | 0.47 | 6+878.74 | 6+890.01 | 4.04 | 24.1 | 0.25 | Excepcional |
| C-193 | 6+928.53 | 9471765.02 | 608581.69 | 45.2 | I | 34.50 | 14.4 | 27.2 | 2.87 | 6+914.15 | 6+941.39 | 3.99 | 1.0 | 0.47 | Excepcional |
| C-194 | 6+971.04 | 9471722.48 | 608592.99 | 55.1 | D | 55.00 | 28.7 | 52.9 | 7.03 | 6+942.36 | 6+995.23 | 2.58 | 19.2 | 0.50 | Normativa 8% |
| C-195 | 7+020.74 | 9471681.08 | 608558.02 | 10.3 | D | 70.00 | 6.3 | 12.6 | 0.29 | 7+014.42 | 7+027.04 | 2.08 | 0.5 | 0.28 | Normativa 8% |
| C-196 | 7+038.79 | 9471669.58 | 608544.06 | 19.7 | D | 65.00 | 11.3 | 22.3 | 0.97 | 7+027.53 | 7+049.83 | 2.22 | 25.8 | 0.40 | Normativa 8% |
| C-197 | 7+116.15 | 9471643.28 | 608471.08 | 90.7 | D | 40.00 | 40.5 | 63.3 | 16.93 | 7+075.64 | 7+138.98 | 3.47 | 27.0 | 1.02 | Excepcional |
| C-198 | 7+168.53 | 9471709.49 | 608448.16 | 45.7 | D | 6.00 | 2.5 | 4.8 | 0.51 | 7+166.00 | 7+170.78 | - | 0.0 | 1.08 | Vuelta |
| C-199 | 7+176.22 | 9471716.61 | 608451.72 | 71.7 | I | 7.52 | 5.4 | 9.4 | 1.76 | 7+170.78 | 7+180.20 | - | 0.4 | 5.24 | Vuelta |
| C-200 | 7+194.59 | 9471730.60 | 608437.67 | 112.4 | I | 9.40 | 14.0 | 18.4 | 7.50 | 7+180.55 | 7+198.99 | - | 1.1 | 5.64 | Vuelta |
| C-201 | 7+217.59 | 9471700.43 | 608425.20 | 30.1 | I | 65.00 | 17.5 | 34.1 | 2.31 | 7+200.13 | 7+234.25 | 2.22 | 7.8 | 2.84 | Normativa 8% |
| C-202 | 7+242.98 | 9471674.48 | 608428.67 | 6.9 | I | 15.00 | 0.9 | 1.8 | 0.03 | 7+242.07 | 7+243.88 | 9.71 | 0.0 | 2.86 | Vuelta |
| C-203 | 7+251.05 | 9471666.66 | 608430.70 | 19.2 | I | 42.46 | 7.2 | 14.2 | 0.60 | 7+243.88 | 7+258.09 | 3.28 | 79.2 | 0.62 | Excepcional |
| C-204 | 7+338.47 | 9471593.81 | 608479.26 | 17.1 | I | 8.00 | 1.2 | 2.4 | 0.09 | 7+337.26 | 7+339.66 | - | 1.7 | 2.08 | Vuelta |
| C-205 | 7+372.93 | 9471572.04 | 608505.99 | 151.7 | D | 7.97 | 31.6 | 21.1 | 24.60 | 7+341.35 | 7+362.44 | - | 0.0 | 0.56 | Vuelta |
| C-206 | 7+371.47 | 9471579.67 | 608466.11 | 42.9 | D | 23.00 | 9.0 | 17.2 | 1.71 | 7+362.44 | 7+379.65 | 5.96 | 17.0 | 0.43 | Vuelta |
| C-207 | 7+418.67 | 9471618.39 | 608437.67 | 29.0 | I | 85.00 | 22.0 | 43.1 | 2.80 | 7+396.65 | 7+439.74 | 1.75 | 0.0 | 0.38 | Normativa 8% |
| C-208 | 7+448.57 | 9471631.25 | 608409.63 | 63.3 | I | 14.34 | 8.8 | 15.8 | 2.50 | 7+439.74 | 7+455.57 | 10.31 | 9.2 | 0.15 | Vuelta |
| C-209 | 7+476.13 | 9471612.91 | 608386.66 | 28.3 | I | 45.00 | 11.3 | 22.2 | 1.41 | 7+464.79 | 7+487.00 | 3.10 | 11.7 | 0.31 | Normativa 12% |
| C-210 | 7+536.52 | 9471556.94 | 608362.77 | 86.9 | D | 40.00 | 37.9 | 60.6 | 15.08 | 7+498.65 | 7+559.30 | 3.47 | 5.0 | 0.51 | Excepcional |
| C-211 | 7+565.84 | 9471572.11 | 608321.04 | 19.3 | I | 8.89 | 1.5 | 3.0 | 0.13 | 7+564.32 | 7+567.32 | - | 0.0 | 0.63 | Vuelta |
| C-212 | 7+585.75 | 9471572.34 | 608301.10 | 133.6 | I | 7.90 | 18.4 | 18.4 | 12.15 | 7+567.32 | 7+585.74 | - | 0.0 | 0.52 | Vuelta |
| C-213 | 7+592.54 | 9471553.87 | 608318.29 | 36.7 | I | 20.48 | 6.8 | 13.1 | 1.10 | 7+585.74 | 7+598.87 | 6.74 | 23.1 | 0.33 | Vuelta |
| C-214 | 7+647.48 | 9471543.95 | 608372.80 | 54.1 | I | 50.00 | 25.5 | 47.2 | 6.15 | 7+621.94 | 7+669.16 | 2.82 | 7.3 | 0.94 | Normativa 8% |
| C-215 | 7+678.92 | 9471568.38 | 608398.27 | 12.3 | D | 22.99 | 2.5 | 4.9 | 0.13 | 7+676.45 | 7+681.37 | 5.96 | -0.0 | 0.26 | Vuelta |
| C-216 | 7+693.47 | 9471576.00 | 608410.69 | 94.5 | D | 11.19 | 12.1 | 18.5 | 5.30 | 7+681.37 | 7+699.82 | 16.13 | 0.0 | 0.37 | Vuelta |
| C-217 | 7+706.76 | 9471559.04 | 608419.34 | 20.1 | D | 39.20 | 6.9 | 13.7 | 0.61 | 7+699.82 | 7+713.55 | 3.53 | 7.5 | 0.13 | Excepcional |
| C-218 | 7+733.48 | 9471532.36 | 608422.59 | 14.2 | I | 100.00 | 12.5 | 24.8 | 0.77 | 7+721.01 | 7+745.83 | 1.52 | 12.9 | 0.19 | Normativa 8% |
| C-219 | 7+770.68 | 9471497.55 | 608436.07 | 11.3 | I | 120.00 | 11.9 | 23.7 | 0.59 | 7+758.77 | 7+782.51 | 1.29 | 11.3 | 0.12 | Normativa 8% |
| C-220 | 7+800.71 | 9471472.17 | 608452.24 | 28.5 | D | 27.30 | 6.9 | 13.6 | 0.87 | 7+793.77 | 7+807.36 | 5.01 | -0.0 | 0.30 | Excepcional |
| C-221 | 7+826.73 | 9471445.92 | 608454.06 | 115.8 | D | 12.15 | 19.4 | 24.6 | 10.72 | 7+807.36 | 7+831.91 | 13.40 | 0.0 | 0.45 | Vuelta |
| C-222 | 7+832.57 | 9471453.37 | 608435.47 | 5.0 | D | 15.10 | 0.7 | 1.3 | 0.01 | 7+831.91 | 7+833.23 | 9.62 | 0.4 | 0.32 | Vuelta |
| C-223 | 7+834.66 | 9471454.32 | 608433.60 | 10.5 | I | 10.80 | 1.0 | 2.0 | 0.05 | 7+833.67 | 7+835.65 | 18.20 | -0.0 | 0.32 | Vuelta |
| C-224 | 7+836.29 | 9471454.78 | 608432.04 | 9.1 | D | 8.02 | 0.6 | 1.3 | 0.03 | 7+835.65 | 7+836.93 | - | -0.0 | 0.23 | Vuelta |
| C-225 | 7+838.96 | 9471455.93 | 608429.63 | 4.8 | I | 48.12 | 2.0 | 4.1 | 0.04 | 7+836.93 | 7+840.99 | 2.92 | 55.9 | 1.00 | Normativa 12% |
| C-226 | 7+913.35 | 9471482.20 | 608360.03 | 83.8 | I | 18.30 | 16.4 | 26.8 | 6.29 | 7+896.92 | 7+923.70 | 7.63 | 21.6 | 1.02 | Vuelta |
| C-227 | 7+963.19 | 9471432.29 | 608334.78 | 71.2 | D | 25.00 | 17.9 | 31.1 | 5.75 | 7+945.29 | 7+976.36 | 5.47 | 5.5 | 0.40 | Excepcional |
| C-228 | 7+985.60 | 9471436.09 | 608307.91 | 9.5 | I | 45.00 | 3.7 | 7.5 | 0.15 | 7+981.86 | 7+989.32 | 3.10 | 7.5 | 0.15 | Normativa 12% |
| C-229 | 7+997.65 | 9471435.79 | 608295.84 | 2.0 | D | 45.00 | 0.8 | 1.6 | 0.01 | 7+996.87 | 7+998.43 | 3.10 | 4.6 | 0.02 | Normativa 12% |
| C-230 | 8+003.12 | 9471435.84 | 608290.37 | 0.2 | I | 45.00 | 0.1 | 0.2 | 0.00 | 8+003.03 | 8+003.22 | 3.10 | 5.8 | 0.02 | Normativa 12% |
| C-231 | 8+009.54 | 9471435.88 | 608283.95 | 1.4 | I | 45.00 | 0.6 | 1.1 | 0.00 | 8+008.99 | 8+010.09 | 3.10 | 9.8 | 0.02 | Normativa 12% |
| C-232 | 8+020.51 | 9471435.67 | 608272.99 | 1.5 | I | 45.00 | 0.6 | 1.2 | 0.00 | 8+019.91 | 8+021.11 | 3.10 | 4.8 | 0.01 | Normativa 12% |
| C-233 | 8+038.44 | 9471434.85 | 608255.07 | 7.2 | I | 200.00 | 12.6 | 25.1 | 0.39 | 8+025.88 | 8+050.98 | 0.84 | 43.3 | 0.12 | Normativa 8% |
| C-234 | 8+100.51 | 9471424.26 | 608193.88 | 15.9 | D | 45.00 | 6.3 | 12.5 | 0.43 | 8+094.24 | 8+106.70 | 3.10 | 2.4 | 0.64 | Normativa 12% |
| C-235 | 8+126.76 | 9471427.04 | 608167.70 | 82.8 | D | 20.00 | 17.6 | 28.9 | 6.67 | 8+109.11 | 8+138.03 | 6.91 | 0.4 | 0.73 | Vuelta |
| C-236 | 8+145.95 | 9471452.60 | 608167.20 | 14.2 | D | 60.00 | 7.5 | 14.9 | 0.46 | 8+138.46 | 8+153.35 | 2.39 | 17.1 | 0.20 | Normativa 8% |
| C-237 | 8+186.60 | 9471492.27 | 608176.44 | 56.5 | I | 30.00 | 16.1 | 29.6 | 4.05 | 8+170.50 | 8+200.06 | 4.56 | 30.5 | 0.47 | Excepcional |
| C-238 | 8+235.25 | 9471529.57 | 608141.23 | 11.8 | D | 45.00 | 4.7 | 9.3 | 0.24 | 8+230.60 | 8+239.88 | 3.10 | 6.0 | 0.30 | Normativa 12% |
| C-239 | 8+253.94 | 9471545.53 | 608131.44 | 22.8 | I | 40.00 | 8.1 | 15.9 | 0.81 | 8+245.86 | 8+261.80 | 3.47 | 1.0 | 0.53 | Excepcional |
| C-240 | 8+273.83 | 9471557.24 | 608115.10 | 27.5 | D | 45.00 | 11.0 | 21.6 | 1.32 | 8+262.83 | 8+284.40 | 3.10 | 18.3 | 0.21 | Normativa 12% |
| C-241 | 8+306.68 | 9471586.91 | 608100.04 | 10.1 | D | 45.00 | 4.0 | 7.9 | 0.18 | 8+302.69 | 8+310.64 | 3.10 | 8.5 | 0.23 | Normativa 12% |
| C-242 | 8+323.09 | 9471602.64 | 608095.30 | 10.0 | I | 45.00 | 3.9 | 7.8 | 0.17 | 8+319.17 | 8+326.99 | 3.10 | 19.9 | 0.27 | Normativa 12% |
| C-243 | 8+348.57 | 9471625.41 | 608083.82 | 4.3 | I | 45.00 | 1.7 | 3.4 | 0.03 | 8+346.87 | 8+350.26 | 3.10 | 19.0 | 0.30 | Normativa 12% |
| C-244 | 8+381.53 | 9471653.65 | 608066.81 | 27.6 | D | 50.00 | 12.3 | 24.1 | 1.49 | 8+369.25 | 8+393.33 | 2.82 | 15.6 | 0.28 | Normativa 8% |
| C-245 | 8+425.42 | 9471697.94 | 608064.12 | 59.2 | I | 29.10 | 16.5 | 30.1 | 4.36 | 8+408.90 | 8+438.95 | 4.70 | 40.6 | 0.47 | Excepcional |
| C-246 | 8+498.22 | 9471732.77 | 607996.81 | 63.8 | D | 30.00 | 18.7 | 33.4 | 5.34 | 8+479.55 | 8+512.95 | 4.56 | 31.1 | 0.55 | Excepcional |
| C-247 | 8+550.99 | 9471789.46 | 607997.95 | 22.3 | I | 35.00 | 6.9 | 13.6 | 0.67 | 8+544.09 | 8+557.71 | 3.93 | 0.4 | 0.42 | Excepcional |
| C-248 | 8+569.89 | 9471807.26 | 607991.07 | 29.3 | D | 45.00 | 11.7 | 23.0 | 1.51 | 8+558.14 | 8+581.13 | 3.10 | 21.0 | 0.45 | Normativa 12% |
| C-249 | 8+615.01 | 9471852.43 | 607997.51 | 56.2 | I | 24.10 | 12.9 | 23.6 | 3.21 | 8+602.15 | 8+625.77 | 5.68 | 1.3 | 1.04 | Vuelta |
| C-250 | 8+649.04 | 9471876.58 | 607970.65 | 40.3 | D | 60.00 | 22.0 | 42.2 | 3.91 | 8+627.04 | 8+669.21 | 2.39 | 37.9 | 0.72 | Normativa 8% |
| C-251 | 8+717.41 | 9471946.14 | 607961.16 | 69.0 | I | 15.00 | 10.3 | 18.1 | 3.20 | 8+707.11 | 8+725.17 | 9.71 | 10.2 | 0.64 | Vuelta |
| C-252 | 8+748.23 | 9471953.79 | 607928.69 | 32.0 | D | 45.00 | 12.9 | 25.1 | 1.81 | 8+735.34 | 8+760.44 | 3.10 | 14.2 | 0.78 | Normativa 12% |
| C-253 | 8+797.00 | 9471988.89 | 607893.86 | 138.0 | I | 8.60 | 22.4 | 20.7 | 15.40 | 8+774.60 | 8+795.31 | - | 0.0 | 1.14 | Vuelta |
| C-254 | 8+803.37 | 9471958.47 | 607895.33 | 36.7 | I | 24.30 | 8.1 | 15.6 | 1.30 | 8+795.31 | 8+810.87 | 5.63 | 26.4 | 0.64 | Vuelta |
| C-255 | 8+850.89 | 9471921.34 | 607925.88 | 68.6 | D | 20.00 | 13.6 | 23.9 | 4.21 | 8+837.25 | 8+861.19 | 6.91 | 17.6 | 0.48 | Vuelta |
| C-256 | 8+902.81 | 9471873.08 | 607898.97 | 62.6 | I | 39.59 | 24.0 | 43.2 | 6.73 | 8+878.76 | 8+921.98 | 3.50 | 0.0 | 0.73 | Excepcional |
| C-257 | 9+007.18 | 9471781.88 | 607959.13 | 169.3 | D | 8.00 | 85.2 | 23.6 | 77.58 | 8+921.98 | 8+945.62 | - | 18.4 | 1.04 | Vuelta |
| C-258 | 8+977.95 | 9471866.23 | 607877.28 | 50.7 | D | 29.40 | 13.9 | 26.0 | 3.13 | 8+964.03 | 8+990.03 | 4.65 | 10.1 | 0.90 | Excepcional |
| C-259 | 9+011.03 | 9471900.92 | 607881.25 | 88.5 | I | 11.20 | 10.9 | 17.3 | 4.44 | 9+000.11 | 9+017.42 | 16.08 | 33.5 | 0.65 | Vuelta |
| C-260 | 9+081.12 | 9471911.35 | 607807.37 | 67.8 | D | 45.00 | 30.2 | 53.2 | 9.20 | 9+050.91 | 9+104.12 | 3.10 | 3.2 | 0.94 | Normativa 12% |
| C-261 | 9+109.92 | 9471946.26 | 607798.53 | 7.7 | I | 38.90 | 2.6 | 5.2 | 0.09 | 9+107.31 | 9+112.52 | 3.56 | 0.0 | 0.53 | Excepcional |
| C-262 | 9+120.11 | 9471955.72 | 607794.72 | 86.9 | I | 8.01 | 7.6 | 12.1 | 3.02 | 9+112.52 | 9+124.67 | - | -0.0 | 0.56 | Vuelta |
| C-263 | 9+128.90 | 9471951.91 | 607783.54 | 18.5 | I | 26.02 | 4.2 | 8.4 | 0.34 | 9+124.67 | 9+133.05 | 5.25 | 18.2 | 0.69 | Excepcional |
| C-264 | 9+155.23 | 9471935.93 | 607762.51 | 40.8 | I | 10.70 | 4.0 | 7.6 | 0.72 | 9+151.25 | 9+158.87 | 19.05 | 0.0 | 0.47 | Vuelta |
| C-265 | 9+200.70 | 9471891.12 | 607753.03 | 93.0 | I | 39.72 | 41.8 | 64.4 | 17.96 | 9+158.87 | 9+223.31 | 3.49 | 10.0 | 0.65 | Excepcional |
| C-266 | 9+238.73 | 9471882.18 | 607809.57 | 15.9 | D | 38.90 | 5.4 | 10.8 | 0.38 | 9+233.28 | 9+244.10 | 3.56 | 0.0 | 0.24 | Excepcional |
| C-267 | 9+259.27 | 9471873.49 | 607828.26 | 104.5 | D | 11.75 | 15.2 | 21.4 | 7.44 | 9+244.10 | 9+265.52 | 14.33 | 12.1 | 0.55 | Vuelta |
| C-268 | 9+297.65 | 9471836.95 | 607798.23 | 63.9 | I | 32.20 | 20.1 | 35.9 | 5.74 | 9+277.59 | 9+313.47 | 4.26 | 6.3 | 0.40 | Excepcional |
| C-269 | 9+329.23 | 9471804.34 | 607813.04 | 23.8 | D | 45.00 | 9.5 | 18.7 | 0.99 | 9+319.73 | 9+338.45 | 3.10 | 4.5 | 0.42 | Normativa 12% |
| C-270 | 9+352.93 | 9471780.36 | 607813.29 | 25.0 | I | 45.00 | 10.0 | 19.6 | 1.09 | 9+342.96 | 9+362.59 | 3.10 | 17.7 | 0.21 | Normativa 12% |
| C-271 | 9+382.12 | 9471753.76 | 607826.04 | 4.0 | D | 53.35 | 1.9 | 3.7 | 0.03 | 9+380.25 | 9+383.98 | 2.65 | 0.0 | 0.14 | Normativa 8% |
| C-272 | 9+421.25 | 9471717.37 | 607840.44 | 154.9 | D | 8.30 | 37.3 | 22.4 | 29.88 | 9+383.98 | 9+406.42 | - | 17.6 | 1.68 | Vuelta |
| C-273 | 9+441.97 | 9471767.31 | 607787.43 | 43.5 | D | 44.98 | 17.9 | 34.1 | 3.45 | 9+424.03 | 9+458.17 | 3.11 | 0.0 | 1.25 | Normativa 12% |
| C-274 | 9+461.53 | 9471788.57 | 607786.24 | 27.9 | I | 13.50 | 3.4 | 6.6 | 0.41 | 9+458.17 | 9+464.75 | 11.24 | 30.9 | 0.38 | Vuelta |
| C-275 | 9+511.94 | 9471831.83 | 607760.09 | 96.0 | I | 14.70 | 16.3 | 24.6 | 7.27 | 9+495.61 | 9+520.25 | 9.97 | 1.8 | 1.34 | Vuelta |
| C-276 | 9+558.33 | 9471798.96 | 607716.73 | 46.3 | D | 85.00 | 36.3 | 68.7 | 7.44 | 9+522.00 | 9+590.67 | 1.75 | 3.2 | 1.00 | Normativa 8% |
| C-277 | 9+613.87 | 9471808.39 | 607657.95 | 48.0 | D | 45.00 | 20.0 | 37.7 | 4.26 | 9+593.84 | 9+631.53 | 3.10 | 0.5 | 0.81 | Normativa 12% |
| C-278 | 9+635.25 | 9471828.33 | 607645.06 | 9.6 | D | 37.90 | 3.2 | 6.4 | 0.13 | 9+632.05 | 9+638.42 | 3.65 | 12.0 | 0.10 | Excepcional |
| C-279 | 9+665.70 | 9471856.32 | 607633.02 | 55.0 | I | 29.30 | 15.2 | 28.1 | 3.73 | 9+650.46 | 9+678.56 | 4.67 | 30.7 | 0.66 | Excepcional |
| C-280 | 9+714.61 | 9471866.80 | 607582.82 | 13.5 | D | 45.00 | 5.3 | 10.6 | 0.31 | 9+709.29 | 9+719.88 | 3.10 | 13.0 | 0.41 | Normativa 12% |
| C-281 | 9+746.83 | 9471880.59 | 607553.65 | 61.2 | D | 23.60 | 14.0 | 25.2 | 3.82 | 9+732.87 | 9+758.08 | 5.80 | 15.5 | 0.71 | Vuelta |
| C-282 | 9+802.39 | 9471938.74 | 607550.09 | 146.4 | I | 8.70 | 28.8 | 22.2 | 21.42 | 9+773.55 | 9+795.79 | - | 18.8 | 0.76 | Vuelta |
| C-283 | 9+836.54 | 9471878.52 | 607515.21 | 82.7 | I | 25.00 | 22.0 | 36.1 | 8.30 | 9+814.55 | 9+850.62 | 5.47 | 1.1 | 0.47 | Excepcional |
| C-284 | 9+869.92 | 9471853.44 | 607548.00 | 50.6 | D | 38.40 | 18.2 | 33.9 | 4.08 | 9+851.75 | 9+885.69 | 3.60 | 40.9 | 0.32 | Excepcional |
| C-285 | 9+938.67 | 9471782.33 | 607550.43 | 14.4 | I | 95.00 | 12.0 | 24.0 | 0.76 | 9+926.63 | 9+950.58 | 1.59 | 14.7 | 0.20 | Normativa 8% |
| C-286 | 9+996.15 | 9471727.07 | 607566.69 | 68.8 | I | 45.00 | 30.8 | 54.1 | 9.54 | 9+965.33 | 10+019.38 | 3.10 | 27.9 | 0.90 | Normativa 12% |
| C-287 | 10+052.60 | 9471721.73 | 607630.51 | 13.4 | I | 45.00 | 5.3 | 10.6 | 0.31 | 10+047.30 | 10+057.85 | 3.10 | 21.7 | 0.28 | Normativa 12% |
| C-288 | 10+080.86 | 9471725.99 | 607658.50 | 19.2 | I | 7.51 | 1.3 | 2.5 | 0.11 | 10+079.58 | 10+082.10 | - | -0.0 | 0.96 | Vuelta |
| C-289 | 10+086.89 | 9471728.83 | 607663.85 | 73.6 | D | 6.40 | 4.8 | 8.2 | 1.59 | 10+082.10 | 10+090.32 | - | -0.0 | 1.87 | Vuelta |
| C-290 | 10+104.72 | 9471715.10 | 607677.25 | 54.4 | D | 28.02 | 14.4 | 26.6 | 3.48 | 10+090.32 | 10+116.93 | 4.88 | -0.0 | 1.59 | Excepcional |
| C-291 | 10+120.19 | 9471697.71 | 607674.16 | 12.9 | I | 28.83 | 3.3 | 6.5 | 0.18 | 10+116.93 | 10+123.43 | 4.74 | 56.0 | 1.99 | Excepcional |
| C-292 | 10+181.32 | 9471636.63 | 607677.21 | 21.7 | D | 10.10 | 1.9 | 3.8 | 0.18 | 10+179.38 | 10+183.21 | - | 1.5 | 0.60 | Vuelta |
| C-293 | 10+221.26 | 9471598.79 | 607664.28 | 67.2 | I | 55.00 | 36.6 | 64.6 | 11.05 | 10+184.68 | 10+249.24 | 2.58 | 1.5 | 1.54 | Normativa 8% |
| C-294 | 10+254.53 | 9471570.99 | 607695.58 | 39.6 | D | 10.60 | 3.8 | 7.3 | 0.67 | 10+250.71 | 10+258.04 | 20.37 | 1.0 | 1.25 | Vuelta |
| C-295 | 10+276.41 | 9471549.06 | 607698.96 | 132.3 | D | 7.70 | 17.4 | 17.8 | 11.33 | 10+259.01 | 10+276.78 | - | 0.6 | 0.82 | Vuelta |
| C-296 | 10+299.00 | 9471570.91 | 607665.92 | 39.6 | D | 60.00 | 21.6 | 41.5 | 3.77 | 10+277.41 | 10+318.87 | 2.39 | 57.0 | 0.80 | Normativa 8% |
| C-297 | 10+387.60 | 9471657.34 | 607639.62 | 20.5 | D | 65.00 | 11.7 | 23.2 | 1.05 | 10+375.85 | 10+399.10 | 2.22 | 7.7 | 0.33 | Normativa 8% |
| C-298 | 10+416.18 | 9471686.11 | 607641.42 | 74.0 | I | 12.40 | 9.3 | 16.0 | 3.13 | 10+406.84 | 10+422.85 | 12.90 | 4.6 | 0.51 | Vuelta |
| C-299 | 10+449.92 | 9471698.31 | 607607.12 | 53.0 | I | 45.00 | 22.4 | 41.6 | 5.29 | 10+427.48 | 10+469.11 | 3.10 | -0.0 | 2.00 | Normativa 12% |
| C-300 | 10+473.46 | 9471683.55 | 607584.76 | 11.9 | D | 41.61 | 4.3 | 8.7 | 0.23 | 10+469.11 | 10+477.78 | 3.34 | 28.8 | 0.28 | Excepcional |
| C-301 | 10+587.35 | 9471641.79 | 607478.77 | 98.1 | D | 70.00 | 80.7 | 119.9 | 36.85 | 10+506.62 | 10+626.52 | 2.08 | 32.7 | 2.92 | Normativa 8% |
| C-302 | 10+670.48 | 9471763.10 | 607449.96 | 28.0 | I | 45.00 | 11.2 | 22.0 | 1.37 | 10+659.27 | 10+681.24 | 3.10 | 33.1 | 0.52 | Normativa 12% |
| C-303 | 10+730.97 | 9471808.86 | 607409.71 | 28.6 | D | 65.00 | 16.6 | 32.5 | 2.08 | 10+714.39 | 10+746.87 | 2.22 | 12.0 | 0.31 | Normativa 8% |
| C-304 | 10+765.44 | 9471843.17 | 607401.98 | 10.0 | D | 75.00 | 6.6 | 13.1 | 0.29 | 10+758.89 | 10+771.96 | 1.95 | 21.6 | 0.15 | Normativa 8% |
| C-305 | 10+819.04 | 9471896.74 | 607399.45 | 54.1 | D | 50.00 | 25.5 | 47.2 | 6.14 | 10+793.52 | 10+840.71 | 2.82 | 7.0 | 0.48 | Normativa 8% |
| C-306 | 10+852.97 | 9471920.32 | 607428.95 | 13.4 | I | 45.00 | 5.3 | 10.6 | 0.31 | 10+847.66 | 10+858.23 | 3.10 | 17.7 | 0.33 | Normativa 12% |
| C-307 | 10+891.59 | 9471950.83 | 607452.72 | 22.2 | D | 80.00 | 15.7 | 31.0 | 1.52 | 10+875.90 | 10+906.88 | 1.84 | 42.2 | 0.31 | Normativa 8% |
| C-308 | 10+956.02 | 9471983.14 | 607508.92 | 44.7 | I | 17.00 | 7.0 | 13.3 | 1.38 | 10+949.03 | 10+962.30 | 8.31 | 6.4 | 0.18 | Vuelta |
| C-309 | 10+975.98 | 9472003.07 | 607514.41 | 18.5 | D | 45.00 | 7.3 | 14.5 | 0.59 | 10+968.65 | 10+983.18 | 3.10 | 14.6 | 0.61 | Normativa 12% |
| C-310 | 11+006.93 | 9472028.86 | 607531.74 | 12.3 | I | 85.00 | 9.2 | 18.3 | 0.49 | 10+997.76 | 11+016.02 | 1.75 | 6.3 | 0.22 | Normativa 8% |
| C-311 | 11+031.17 | 9472051.47 | 607540.70 | 25.6 | I | 39.10 | 8.9 | 17.5 | 1.00 | 11+022.29 | 11+039.75 | 3.54 | 0.0 | 0.89 | Excepcional |
| C-312 | 11+051.62 | 9472072.17 | 607539.25 | 95.8 | I | 10.72 | 11.9 | 17.9 | 5.28 | 11+039.75 | 11+057.68 | 18.90 | 3.1 | 0.70 | Vuelta |
| C-313 | 11+064.68 | 9472068.94 | 607520.66 | 9.9 | I | 45.00 | 3.9 | 7.8 | 0.17 | 11+060.77 | 11+068.56 | 3.10 | 9.4 | 0.17 | Normativa 12% |
| C-314 | 11+093.16 | 9472059.31 | 607493.84 | 37.4 | D | 45.00 | 15.2 | 29.4 | 2.51 | 11+077.94 | 11+107.30 | 3.10 | 70.2 | 0.96 | Normativa 12% |
| C-315 | 11+212.58 | 9472095.79 | 607378.98 | 56.7 | D | 65.00 | 35.1 | 64.3 | 8.86 | 11+177.50 | 11+241.84 | 2.22 | 1.8 | 0.48 | Normativa 8% |
| C-316 | 11+260.55 | 9472147.58 | 607364.46 | 34.1 | I | 55.00 | 16.9 | 32.8 | 2.53 | 11+243.66 | 11+276.43 | 2.58 | 38.2 | 0.70 | Normativa 8% |
| C-317 | 11+325.25 | 9472189.99 | 607314.27 | 11.0 | D | 110.00 | 10.6 | 21.1 | 0.51 | 11+314.66 | 11+335.77 | 1.40 | 1.0 | 0.17 | Normativa 8% |
| C-318 | 11+351.53 | 9472210.52 | 607297.76 | 14.1 | I | 120.00 | 14.8 | 29.5 | 0.91 | 11+336.72 | 11+366.18 | 1.29 | 39.5 | 0.47 | Normativa 8% |
| C-319 | 11+408.17 | 9472244.80 | 607252.48 | 5.8 | D | 50.00 | 2.5 | 5.0 | 0.06 | 11+405.66 | 11+410.68 | 2.82 | 21.5 | 0.41 | Normativa 8% |
| C-320 | 11+440.32 | 9472266.68 | 607228.93 | 9.3 | I | 100.00 | 8.1 | 16.2 | 0.33 | 11+432.19 | 11+448.40 | 1.52 | 8.0 | 0.11 | Normativa 8% |
| C-321 | 11+456.58 | 9472275.70 | 607215.36 | 0.7 | D | 27.90 | 0.2 | 0.3 | 0.00 | 11+456.41 | 11+456.74 | 4.90 | -0.0 | 0.05 | Excepcional |
| C-322 | 11+457.03 | 9472275.96 | 607214.98 | 0.1 | D | 412.99 | 0.3 | 0.6 | 0.00 | 11+456.74 | 11+457.32 | 0.47 | 1.4 | 0.00 | Normativa 8% |
| C-323 | 11+459.00 | 9472277.07 | 607213.36 | 0.7 | D | 40.50 | 0.2 | 0.5 | 0.00 | 11+458.75 | 11+459.25 | 3.43 | -0.0 | 0.01 | Excepcional |
| C-324 | 11+460.33 | 9472277.83 | 607212.27 | 8.5 | D | 14.54 | 1.1 | 2.2 | 0.04 | 11+459.25 | 11+461.41 | 10.12 | 6.7 | 0.03 | Vuelta |

# Anexo B. Archivos entregados

- `EJE_DG2018_circular.xml`: eje en LandXML 1.2 para importar en Civil 3D (IMPORTLANDXML).
- `EJE_DG2018_circular_curvas.csv`: tabla de curvas con observaciones detalladas por curva.
- `EJE_DG2018_circular_PI_PNEZD.csv` y `EJE_DG2018_circular_PI_polilinea.scr`: PIs como puntos y como polilínea de AutoCAD.
- `EJE_DG2018_circular_planta.svg` y `.png`: croquis de planta con el trazo actual y el eje coloreado por clase de curva.
- `DG2018_Corregido_2.xml`: archivo de criterios de diseño DG-2018 para Civil 3D.
- `EJE_DG2018_clotoides.xml`: variante con clotoides de 40 m en las 5 curvas donde caben.
