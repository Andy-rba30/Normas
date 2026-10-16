---
title: "Memoria de diseño geométrico en planta"
subtitle: "Eje EJE DG2018 V40 CIRCULAR, ajustado al trazo existente según el Manual de Carreteras: Diseño Geométrico DG-2018"
date: "16/10/2026"
lang: es
---

# 1. Objeto y alcance

Este documento describe el eje en planta contenido en el archivo `EJE_DG2018_circular.xml` (LandXML 1.2, alineamiento "EJE DG2018 V40 CIRCULAR", longitud 11,472.98 m), obtenido a partir de la poligonal del trazo existente `PROCESAMIENTO DISEÑO GEOMETRICO` (11,491.71 m, 1181 vértices, UTM WGS84 zona 17 Sur), y contrasta cada parámetro adoptado con lo que exige el Manual de Carreteras: Diseño Geométrico DG-2018 (MTC, revisada y corregida a enero de 2018).

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
| Radio mínimo normativo | 45 m | Tabla 302.02, área rural accidentada o escarpada: "40 km/h, p máx 12.00 %, f máx 0.17, radio calculado 43.4 m, radio redondeado 45 m". | Tabla 302.02 | 146 curvas de 282 (52 %) tienen R ≥ 45 m. |
| Radio mínimo con peralte normal 8 % | 50 m | Tabla 302.02, área rural plana u ondulada: "40 km/h, 8.00 %, 0.17, 50.4 m, 50 m". | Tabla 302.02 | 88 curvas (31 %) tienen R ≥ 50 m y pueden peraltarse con 8 %. |
| Radio excepcional | 25 m ≤ R < 45 m | La DG-2018 no define un radio mínimo excepcional para carreteras de Segunda Clase. Se adopta el radio mínimo de la fila de 30 km/h de la Tabla 302.02: "30 km/h, 12.00 %, 0.17, 24.4 m, 25 m", es decir, la curva se diseña con velocidad específica de 30 km/h. | Tabla 302.02 y Tópico 204.03 | 52 curvas (18 %). Listado en el capítulo 6.2. |
| Curvas de vuelta | Radio interior Ri ≥ 8 m (normal) o 6 m (absoluto); Re según Tabla 302.12 | "Son aquellas curvas que se proyectan sobre una ladera, en terrenos accidentados, con el propósito de obtener o alcanzar una cota mayor (...) Este tipo de curvas no se emplearán en autopistas, en tanto que en carreteras de Primera Clase podrán utilizarse en casos excepcionales (...) El radio interior de 8 m, representa un mínimo normal. El radio interior de 6 m, representa un mínimo absoluto y sólo podrá ser usado en forma excepcional." | Tópico 302.07 y Tabla 302.12 | 84 curvas con R de eje < 25 m (30 %): 40 con Ri ≥ 8 m, 11 con 6 ≤ Ri < 8 m y 33 con Ri < 6 m (no cumplen ni el mínimo absoluto). Capítulo 6.3. |
| Radio a partir del cual no se requiere peralte | 3 500 m (V = 40 km/h) | Tabla 304.04: "Velocidad 40 km/h: radio 3 500 m". | Tabla 304.04 | Ninguna curva del eje supera 3 500 m; todas se peraltan. |
| Peralte mínimo | 2 % para 2 500 ≤ R < 3 500 m | Tabla 304.06: "40 ≤ V < 100: 2 500 ≤ R < 3 500". | Tabla 304.06 | - |
| Transición del peralte | ipmáx = 1.8 − 0.01 V = 1.4 %; Lmín = (pf − pi)/ipmáx · B | "ipmáx = 1.8 − 0.01 V (...) Lmín = (pf − pi)/ipmáx · B". | Tópico 302.08 | Para Civil 3D se entrega el archivo de criterios DG2018_Corregido_2.xml (tablas "DG2018 _PMax 12%" y método "DG2018 METRICO"). |
| Longitud mínima de tangentes | 56 m entre curvas en S; 111 m entre curvas del mismo sentido; máx. deseable 668 m | Tabla 302.01: "40 km/h: L mín.s 56, L mín.o 111, L máx 668". | Tabla 302.01 | 7 de 281 tangentes intermedias cumplen; además 50 pares del mismo sentido se resolvieron como curva compuesta sin tangente (Tópico 302.06.03). El resto es limitación del trazo existente (capítulo 6.4 y capítulo 7). |
| Curvas vecinas del mismo sentido | Fundidas en una sola curva o en compuesta cuando la tangente intermedia era corta | "En general se evitará el empleo de curvas del mismo sentido, cuando estén separadas por un tramo en tangente de una longitud menor a 400 m, en longitudes menores excepcionalmente puede utilizarse una curva policéntrica." | Tópico 302.06.03 | Ver capítulo 7 (pasada de tangentes). |
| Longitud mínima de curva | 3V = 120 m; para Δ ≤ 5°: L > 30(10 − Δ); nunca Δ < 59′ | "La longitud mínima de curva (L) será: carreteras de dos carriles 3V (...) En el caso de ángulos de deflexión Δ pequeños, iguales o inferiores a 5º (...) L > 30(10 − Δ) (...) No se usará nunca ángulos de deflexión menores de 59' (minutos)." | Tópico 302.02 | Ninguna curva alcanza 120 m (la mayor tiene 122 m). 10 curvas tienen Δ < 5°; ninguna tiene Δ < 59′. |
| Curvas de transición (clotoides) | No incluidas en esta variante | Tabla 302.11A: para 40 km/h se puede prescindir de la transición si R ≥ 150 m. Tabla 302.10: longitud mínima de transición 40 m a 40 km/h; "En ningún caso se adoptarán longitudes de transición menores a 30 m". Tópico 302.05.06: R/3 ≤ A ≤ R. | Tópicos 302.05.06 y 302.05.07, Tablas 302.10 y 302.11A | 269 curvas tienen R < 150 m y requerirían clotoide; con Le = 40 m solo cabe en 5 (variante EJE_DG2018_clotoides.xml) porque las tangentes disponibles son demasiado cortas. |
| Relación entre radios consecutivos | Tabla 302.08 (grupo 2) | "cuando se enlacen curvas circulares consecutivas sin tangente intermedia, así como mediante tangente de longitud menor o igual a 200 m, la relación de radios (...) no sobrepasará los valores (...) Grupo 2: Carreteras de Segunda y Tercera Clase." | Tópico 302.04.05 y Tabla 302.08 | 39 de 281 pares cumplen. |
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
5. Donde el radio ajustado resultó menor de 45 m, se subió hasta 45 m siempre que la separación respecto al trazo no superara 2.0 m (97 curvas). Los radios se redondearon a múltiplos de 5 m (10 m por encima de 100 m).
6. Las curvas de más de 170° (volteos) se representan con dos arcos consecutivos del mismo radio, porque Civil 3D no admite una curva simple de 180° o más.

# 4. Resultados globales

| Indicador | Valor |
|----------------------------|------------|
| Longitud del trazo original / del eje corregido | 11,491.71 m / 11,472.98 m |
| Número de curvas / tangentes | 282 / 283 |
| Curvas con R ≥ 50 m (cumple con peralte 8 %) | 88 (31 %) |
| Curvas con 45 ≤ R < 50 m (cumple con peralte 12 %) | 58 (21 %) |
| Curvas excepcionales, 25 ≤ R < 45 m (Ve = 30 km/h) | 52 (18 %) |
| Curvas de vuelta, R < 25 m | 84 (30 %) |
| Curvas llevadas al radio mínimo normativo (R = 45 m) | 57 |
| Separación lateral del trazo actual respecto al eje: promedio / percentil 95 / máxima | 0.39 m / 1.25 m / 5.22 m |
| Longitud de trazo con separación mayor a 1.5 m / 2.5 m / 4.0 m | 355 m / 146 m / 25 m |
| Tangentes intermedias que cumplen la Tabla 302.01 | 7 de 281 |
| Pares de curvas consecutivas que cumplen la Tabla 302.08 | 39 de 281 |
| Curvas con longitud ≥ 3V = 120 m | 0 de 282 |

# 5. Interpretación

El 52 % de las curvas cumple el radio mínimo de la DG-2018 para 40 km/h. El 18 % queda entre 25 y 45 m y debe tratarse como curva excepcional con velocidad específica de 30 km/h y señalización preventiva y reglamentaria. El 30 % restante corresponde a curvas de vuelta y esquinas urbanas con radios de eje entre 6 y 25 m, que es lo que impone la geometría existente; en 33 de ellas el radio interior resultante es menor de 6 m, de modo que para cumplir siquiera el mínimo absoluto habría que ampliar la plataforma o expropiar.

Las longitudes mínimas de tangente, la longitud mínima de curva de 120 m, las clotoides y la relación de radios consecutivos no se cumplen en la mayor parte del eje. No es un defecto del ajuste sino de la premisa de seguir el trazo existente: con curvas cada 35 m en promedio no hay espacio para tangentes de 56 a 111 m ni para espirales de 40 m. Si el proyecto exige cumplir esos parámetros, habrá que rediseñar tramos completos con expropiación.

# 6. Inventario de curvas por tipo

## 6.1 Curvas en el radio mínimo normativo (R = 45 m)

57 curvas quedan exactamente en el radio mínimo de la Tabla 302.02; de ellas 41 fueron llevadas a 45 m desde un radio ajustado menor (separación admitida ≤ 2.0 m). Deben peraltarse con el máximo de 12 %.

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | Lc (m) | Sep. máx. trazo (m) | Origen |
|------|---------|---------|---------|------|----|-----|-----|------|----------|
| C-3 | 0+099.58 | 9472189.807 | 612980.759 | 31.5 | D | 44.97 | 24.7 | 1.89 | subido al mínimo |
| C-16 | 0+479.75 | 9472384.202 | 612870.599 | 46.7 | D | 45.00 | 36.7 | 1.55 | subido al mínimo |
| C-17 | 0+523.33 | 9472424.822 | 612849.548 | 22.8 | I | 45.00 | 17.9 | 0.29 | ajuste al trazo |
| C-20 | 0+695.09 | 9472567.487 | 612812.812 | 40.5 | D | 45.00 | 31.8 | 0.70 | subido al mínimo |
| C-25 | 0+887.28 | 9472672.597 | 612728.598 | 84.0 | D | 45.00 | 66.0 | 1.56 | ajuste al trazo |
| C-28 | 1+015.20 | 9472810.529 | 612756.323 | 41.3 | I | 44.95 | 32.4 | 0.86 | subido al mínimo |
| C-30 | 1+075.62 | 9472804.918 | 612716.138 | 19.3 | D | 45.00 | 15.2 | 0.33 | subido al mínimo |
| C-32 | 1+126.44 | 9472772.919 | 612676.667 | 14.7 | D | 45.00 | 11.6 | 0.34 | subido al mínimo |
| C-35 | 1+354.23 | 9472719.756 | 612471.344 | 74.3 | D | 45.00 | 58.3 | 0.93 | ajuste al trazo |
| C-36 | 1+417.33 | 9472791.596 | 612458.780 | 30.4 | I | 45.00 | 23.9 | 1.18 | subido al mínimo |
| C-41 | 1+616.52 | 9472827.619 | 612299.230 | 22.3 | D | 45.00 | 17.5 | 0.51 | subido al mínimo |
| C-48 | 1+929.98 | 9472694.509 | 612081.130 | 11.8 | I | 45.00 | 9.3 | 0.17 | subido al mínimo |
| C-52 | 2+016.51 | 9472686.709 | 612008.290 | 27.4 | D | 45.00 | 21.5 | 0.76 | subido al mínimo |
| C-57 | 2+153.96 | 9472744.752 | 611933.459 | 32.0 | I | 45.00 | 25.1 | 0.60 | subido al mínimo |
| C-62 | 2+389.39 | 9472704.516 | 611756.000 | 16.2 | I | 45.00 | 12.7 | 0.57 | ajuste al trazo |
| C-68 | 2+658.61 | 9472577.483 | 611564.659 | 30.8 | I | 45.00 | 24.2 | 0.74 | subido al mínimo |
| C-69 | 2+693.06 | 9472583.502 | 611530.134 | 25.8 | D | 45.00 | 20.2 | 0.95 | subido al mínimo |
| C-71 | 2+827.71 | 9472619.144 | 611414.752 | 17.3 | I | 45.00 | 13.6 | 0.31 | ajuste al trazo |
| C-79 | 3+257.60 | 9472661.808 | 611105.823 | 21.6 | I | 45.00 | 16.9 | 0.32 | ajuste al trazo |
| C-84 | 3+411.16 | 9472653.181 | 611030.052 | 10.5 | D | 45.00 | 8.3 | 0.25 | subido al mínimo |
| C-94 | 3+723.62 | 9472479.485 | 610955.759 | 27.8 | I | 45.00 | 21.8 | 1.14 | subido al mínimo |
| C-101 | 3+966.11 | 9472553.981 | 610730.567 | 9.1 | D | 45.00 | 7.2 | 0.24 | subido al mínimo |
| C-104 | 4+106.41 | 9472570.961 | 610592.995 | 29.6 | I | 45.00 | 23.3 | 0.83 | ajuste al trazo |
| C-105 | 4+188.17 | 9472551.054 | 610513.146 | 31.8 | D | 45.00 | 25.0 | 0.94 | ajuste al trazo |
| C-106 | 4+219.61 | 9472560.856 | 610482.581 | 28.2 | I | 45.00 | 22.1 | 0.51 | subido al mínimo |
| C-115 | 4+554.75 | 9472519.929 | 610197.194 | 25.5 | D | 45.00 | 20.0 | 1.27 | subido al mínimo |
| C-124 | 4+747.64 | 9472448.886 | 610029.585 | 21.3 | I | 45.00 | 16.7 | 0.22 | ajuste al trazo |
| C-125 | 4+797.64 | 9472438.535 | 609980.467 | 44.2 | D | 45.00 | 34.7 | 1.65 | subido al mínimo |
| C-132 | 5+078.60 | 9472346.474 | 609762.633 | 8.9 | D | 45.00 | 7.0 | 0.27 | subido al mínimo |
| C-134 | 5+210.31 | 9472300.221 | 609640.768 | 18.3 | I | 45.00 | 14.4 | 0.87 | subido al mínimo |
| C-137 | 5+326.88 | 9472263.851 | 609530.347 | 8.8 | D | 45.00 | 6.9 | 0.23 | subido al mínimo |
| C-138 | 5+355.91 | 9472257.218 | 609502.075 | 13.6 | I | 45.00 | 10.7 | 0.29 | subido al mínimo |
| C-139 | 5+379.31 | 9472246.628 | 609481.152 | 5.9 | D | 45.00 | 4.6 | 0.21 | subido al mínimo |
| C-141 | 5+497.10 | 9472208.438 | 609369.745 | 17.6 | I | 45.00 | 13.8 | 0.68 | subido al mínimo |
| C-146 | 5+803.28 | 9472283.459 | 609143.685 | 14.3 | D | 45.00 | 11.3 | 0.48 | subido al mínimo |
| C-153 | 6+242.01 | 9471930.530 | 608927.705 | 23.8 | I | 45.00 | 18.7 | 0.59 | subido al mínimo |
| C-154 | 6+276.72 | 9471905.424 | 608903.335 | 8.9 | D | 45.00 | 7.0 | 0.26 | subido al mínimo |
| C-155 | 6+325.89 | 9471875.881 | 608864.013 | 11.8 | D | 45.00 | 9.3 | 0.32 | subido al mínimo |
| C-158 | 6+463.70 | 9471809.087 | 608744.190 | 77.1 | D | 45.00 | 60.6 | 1.93 | subido al mínimo |
| C-163 | 6+660.78 | 9471914.358 | 608657.337 | 25.0 | D | 45.00 | 19.7 | 0.39 | subido al mínimo |
| C-201 | 7+989.78 | 9471436.095 | 608307.908 | 9.5 | I | 45.00 | 7.5 | 0.15 | subido al mínimo |
| C-202 | 8+001.83 | 9471435.790 | 608295.844 | 2.0 | D | 45.00 | 1.6 | 0.02 | subido al mínimo |
| C-204 | 8+104.77 | 9471424.264 | 608193.881 | 15.9 | D | 45.00 | 12.5 | 0.64 | subido al mínimo |
| C-207 | 8+239.02 | 9471529.574 | 608141.225 | 11.8 | D | 45.00 | 9.3 | 0.30 | ajuste al trazo |
| C-209 | 8+277.59 | 9471557.242 | 608115.098 | 27.5 | D | 45.00 | 21.6 | 0.21 | ajuste al trazo |
| C-216 | 8+573.73 | 9471807.256 | 607991.071 | 29.3 | D | 45.00 | 23.0 | 0.45 | ajuste al trazo |
| C-220 | 8+752.06 | 9471953.791 | 607928.689 | 32.0 | D | 45.00 | 25.1 | 0.78 | subido al mínimo |
| C-228 | 9+084.96 | 9471911.350 | 607807.368 | 67.8 | D | 45.00 | 53.2 | 0.94 | ajuste al trazo |
| C-234 | 9+334.66 | 9471804.341 | 607813.043 | 23.8 | D | 45.00 | 18.7 | 0.42 | subido al mínimo |
| C-235 | 9+358.36 | 9471780.365 | 607813.290 | 25.0 | I | 45.00 | 19.6 | 0.21 | ajuste al trazo |
| C-238 | 9+447.40 | 9471767.309 | 607787.435 | 43.5 | D | 44.98 | 34.1 | 1.25 | subido al mínimo |
| C-250 | 10+000.99 | 9471727.071 | 607566.691 | 68.8 | I | 45.00 | 54.1 | 0.90 | ajuste al trazo |
| C-263 | 10+453.60 | 9471698.310 | 607607.115 | 53.0 | I | 45.00 | 41.6 | 2.00 | subido al mínimo |
| C-266 | 10+674.17 | 9471763.099 | 607449.956 | 28.0 | I | 45.00 | 22.0 | 0.52 | ajuste al trazo |
| C-269 | 10+856.98 | 9471920.322 | 607428.954 | 13.4 | I | 45.00 | 10.6 | 0.33 | subido al mínimo |
| C-272 | 10+979.99 | 9472003.071 | 607514.411 | 18.5 | D | 45.00 | 14.5 | 0.61 | subido al mínimo |
| C-275 | 11+098.06 | 9472059.305 | 607493.835 | 37.4 | D | 45.00 | 29.4 | 0.96 | subido al mínimo |

## 6.2 Curvas excepcionales (25 m ≤ R < 45 m)

52 curvas. La velocidad específica se calcula con Ve = √(127 · R · (0.12 + 0.17)), que reproduce los radios de la Tabla 302.02 para 30 y 40 km/h (25 m → 30 km/h, 45 m → 41 km/h). Todas requieren peralte 12 %, sobreancho y señalización de velocidad máxima 30 km/h.

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | Ve (km/h) | Sa (m) | Lc (m) | Sep. máx. trazo (m) |
|------|---------|---------|---------|------|----|-----|------|-----|-----|------|
| C-1 | 0+037.84 | 9472166.454 | 613022.231 | 44.7 | I | 38.78 | 38 | 3.57 | 30.2 | 1.16 |
| C-6 | 0+169.69 | 9472248.915 | 612948.678 | 36.4 | D | 25.00 | 30 | 5.47 | 15.9 | 0.43 |
| C-12 | 0+326.44 | 9472347.878 | 613017.986 | 28.7 | I | 40.00 | 38 | 3.47 | 20.1 | 0.21 |
| C-18 | 0+614.54 | 9472483.412 | 612779.332 | 77.8 | D | 39.90 | 38 | 3.47 | 54.2 | 1.74 |
| C-23 | 0+767.37 | 9472618.128 | 612836.504 | 45.9 | I | 29.88 | 33 | 4.58 | 24.0 | 0.97 |
| C-24 | 0+783.00 | 9472622.422 | 612820.063 | 14.1 | D | 35.00 | 36 | 3.93 | 8.6 | 0.39 |
| C-26 | 0+928.30 | 9472724.322 | 612750.290 | 31.9 | I | 43.60 | 40 | 3.20 | 24.3 | 1.38 |
| C-38 | 1+497.76 | 9472779.312 | 612398.742 | 60.8 | D | 40.00 | 38 | 3.47 | 42.5 | 0.76 |
| C-40 | 1+588.26 | 9472824.333 | 612331.803 | 66.4 | I | 29.90 | 33 | 4.58 | 34.6 | 0.61 |
| C-42 | 1+644.88 | 9472841.054 | 612273.997 | 35.4 | I | 38.90 | 38 | 3.56 | 24.1 | 1.21 |
| C-43 | 1+667.90 | 9472837.985 | 612250.375 | 32.3 | D | 39.31 | 38 | 3.52 | 22.2 | 0.38 |
| C-50 | 1+985.49 | 9472669.378 | 612032.020 | 27.0 | D | 43.90 | 40 | 3.18 | 20.7 | 0.17 |
| C-54 | 2+064.44 | 9472732.887 | 611995.109 | 37.0 | D | 37.28 | 37 | 3.70 | 24.1 | 0.65 |
| C-58 | 2+196.15 | 9472717.221 | 611900.604 | 86.8 | D | 30.00 | 33 | 4.56 | 45.4 | 1.24 |
| C-65 | 2+574.61 | 9472606.735 | 611624.722 | 71.4 | I | 29.40 | 33 | 4.65 | 36.6 | 0.37 |
| C-66 | 2+613.11 | 9472567.615 | 611604.346 | 38.9 | D | 37.30 | 37 | 3.70 | 25.4 | 1.18 |
| C-74 | 3+002.48 | 9472588.315 | 611253.691 | 75.6 | D | 25.00 | 30 | 5.47 | 33.0 | 0.57 |
| C-83 | 3+380.99 | 9472683.873 | 611029.183 | 32.2 | I | 34.50 | 36 | 3.99 | 19.4 | 1.18 |
| C-88 | 3+563.57 | 9472511.901 | 611065.550 | 36.1 | D | 30.00 | 33 | 4.56 | 18.9 | 5.17 |
| C-91 | 3+643.24 | 9472449.657 | 611030.786 | 43.7 | D | 35.00 | 36 | 3.93 | 26.7 | 5.84 |
| C-92 | 3+668.20 | 9472453.707 | 611004.763 | 37.7 | D | 32.50 | 35 | 4.22 | 21.4 | 4.64 |
| C-107 | 4+241.35 | 9472556.841 | 610460.744 | 22.9 | D | 44.89 | 41 | 3.11 | 17.9 | 0.25 |
| C-109 | 4+314.90 | 9472504.737 | 610429.794 | 89.7 | D | 32.60 | 35 | 4.21 | 51.0 | 0.90 |
| C-143 | 5+616.62 | 9472172.908 | 609260.939 | 30.0 | D | 30.42 | 33 | 4.50 | 15.9 | 0.88 |
| C-145 | 5+756.42 | 9472297.505 | 609198.596 | 80.4 | I | 34.20 | 35 | 4.02 | 48.0 | 0.42 |
| C-160 | 6+601.50 | 9471936.611 | 608671.898 | 15.1 | I | 44.69 | 41 | 3.12 | 11.8 | 0.29 |
| C-164 | 6+705.15 | 9471869.912 | 608662.043 | 32.1 | I | 30.00 | 33 | 4.56 | 16.8 | 0.66 |
| C-165 | 6+721.39 | 9471856.784 | 608672.342 | 27.4 | D | 33.14 | 35 | 4.14 | 15.8 | 0.21 |
| C-170 | 6+886.72 | 9471803.158 | 608604.034 | 19.0 | I | 34.00 | 35 | 4.04 | 11.3 | 0.25 |
| C-171 | 6+930.82 | 9471765.017 | 608581.692 | 45.2 | I | 34.50 | 36 | 3.99 | 27.2 | 0.47 |
| C-174 | 7+118.48 | 9471643.281 | 608471.076 | 90.7 | D | 40.00 | 38 | 3.47 | 63.3 | 1.02 |
| C-180 | 7+253.38 | 9471666.658 | 608430.695 | 19.2 | I | 42.46 | 40 | 3.28 | 14.2 | 0.62 |
| C-187 | 7+538.47 | 9471556.942 | 608362.774 | 86.9 | D | 40.00 | 38 | 3.47 | 60.6 | 0.51 |
| C-193 | 7+708.73 | 9471559.037 | 608419.344 | 20.1 | D | 39.20 | 38 | 3.53 | 13.7 | 0.13 |
| C-200 | 7+967.37 | 9471432.294 | 608334.781 | 71.2 | D | 25.00 | 30 | 5.47 | 31.1 | 0.40 |
| C-206 | 8+190.37 | 9471492.268 | 608176.443 | 56.5 | I | 30.00 | 33 | 4.56 | 29.6 | 0.47 |
| C-208 | 8+257.71 | 9471545.530 | 608131.436 | 22.8 | I | 40.00 | 38 | 3.47 | 15.9 | 0.53 |
| C-213 | 8+429.26 | 9471697.937 | 608064.124 | 59.2 | I | 29.10 | 33 | 4.70 | 30.1 | 0.47 |
| C-214 | 8+502.06 | 9471732.769 | 607996.813 | 63.8 | D | 30.00 | 33 | 4.56 | 33.4 | 0.55 |
| C-215 | 8+554.83 | 9471789.463 | 607997.954 | 22.3 | I | 35.00 | 36 | 3.93 | 13.6 | 0.42 |
| C-224 | 8+906.65 | 9471873.080 | 607898.972 | 62.6 | I | 39.59 | 38 | 3.50 | 43.2 | 0.73 |
| C-226 | 8+981.79 | 9471866.233 | 607877.279 | 50.7 | D | 29.40 | 33 | 4.65 | 26.0 | 0.90 |
| C-231 | 9+205.30 | 9471891.124 | 607753.031 | 93.0 | I | 39.70 | 38 | 3.49 | 64.4 | 0.65 |
| C-233 | 9+303.08 | 9471836.954 | 607798.225 | 63.9 | I | 32.20 | 34 | 4.26 | 35.9 | 0.40 |
| C-242 | 9+623.58 | 9471809.135 | 607653.305 | 57.6 | D | 43.80 | 40 | 3.18 | 44.1 | 0.79 |
| C-243 | 9+670.81 | 9471856.323 | 607633.025 | 55.0 | I | 29.30 | 33 | 4.67 | 28.1 | 0.66 |
| C-247 | 9+841.54 | 9471878.523 | 607515.210 | 82.7 | I | 25.00 | 30 | 5.47 | 36.1 | 0.47 |
| C-248 | 9+874.91 | 9471853.443 | 607548.005 | 50.6 | D | 38.40 | 38 | 3.60 | 33.9 | 0.32 |
| C-254 | 10+109.36 | 9471715.102 | 607677.255 | 54.4 | D | 28.02 | 32 | 4.88 | 26.6 | 1.59 |
| C-255 | 10+124.83 | 9471697.708 | 607674.164 | 12.9 | I | 28.83 | 33 | 4.74 | 6.5 | 1.99 |
| C-264 | 10+477.15 | 9471683.547 | 607584.758 | 11.9 | D | 41.61 | 39 | 3.34 | 8.7 | 0.28 |
| C-282 | 11+464.85 | 9472277.571 | 607212.541 | 10.0 | D | 40.00 | 38 | 3.47 | 7.0 | 0.12 |

## 6.3 Curvas de vuelta (R < 25 m)

84 curvas. El radio interior Ri se obtiene de Ri + ancho/2 = R, con el ancho de calzada en curva de vuelta (Re − Ri) de la Tabla 302.12 para la maniobra C2 (camión de dos ejes cruzándose con un vehículo ligero), que considera calzada de 6 m en tangente. Criterio: Ri ≥ 8 m cumple el mínimo normal; 6 ≤ Ri < 8 m es el mínimo absoluto de uso excepcional; Ri < 6 m no cumple.

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R eje (m) | Ri (m) | Re (m) | Ancho (m) | Evaluación DG-2018 | Sep. máx. trazo (m) |
|------|---------|---------|---------|------|----|-----|-----|-----|-----|-------------|------|
| C-2 | 0+059.92 | 9472190.090 | 613024.156 | 95.0 | I | 7.12 | 2.2 | 12.0 | 9.75 | no cumple (Ri < 6 m) | 1.08 |
| C-4 | 0+121.85 | 9472201.640 | 612961.140 | 48.6 | D | 22.70 | 18.7 | 26.7 | 8.07 | cumple (Ri ≥ 8 m) | 1.76 |
| C-7 | 0+186.74 | 9472266.013 | 612952.910 | 42.2 | I | 10.75 | 5.9 | 15.6 | 9.75 | no cumple (Ri < 6 m) | 0.36 |
| C-8 | 0+195.72 | 9472274.247 | 612948.468 | 81.8 | D | 6.00 | 1.1 | 10.9 | 9.75 | no cumple (Ri < 6 m) | 1.15 |
| C-9 | 0+208.69 | 9472283.050 | 612960.368 | 35.0 | I | 23.80 | 19.8 | 27.8 | 8.01 | cumple (Ri ≥ 8 m) | 0.45 |
| C-10 | 0+223.50 | 9472297.545 | 612965.224 | 51.6 | D | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 2.11 |
| C-11 | 0+315.17 | 9472328.984 | 613052.387 | 131.4 | I | 13.10 | 8.5 | 17.7 | 9.11 | cumple (Ri ≥ 8 m) | 1.18 |
| C-15 | 0+438.62 | 9472372.920 | 612910.184 | 16.4 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.15 |
| C-19 | 0+637.19 | 9472512.525 | 612794.601 | 9.3 | I | 8.07 | 3.2 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.74 |
| C-21 | 0+732.09 | 9472587.366 | 612845.663 | 6.5 | I | 17.37 | 13.2 | 21.6 | 8.40 | cumple (Ri ≥ 8 m) | 0.45 |
| C-22 | 0+739.31 | 9472591.784 | 612851.375 | 81.7 | I | 7.20 | 2.3 | 12.1 | 9.75 | no cumple (Ri < 6 m) | 0.69 |
| C-29 | 1+043.73 | 9472836.729 | 612741.678 | 112.0 | I | 8.80 | 3.9 | 13.7 | 9.75 | no cumple (Ri < 6 m) | 0.65 |
| C-37 | 1+461.71 | 9472825.871 | 612429.694 | 106.1 | I | 24.63 | 20.6 | 28.6 | 8.00 | cumple (Ri ≥ 8 m) | 1.24 |
| C-39 | 1+547.21 | 9472783.479 | 612344.963 | 67.7 | D | 11.70 | 6.9 | 16.5 | 9.51 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.49 |
| C-51 | 1+999.33 | 9472671.422 | 612017.929 | 49.5 | D | 15.40 | 11.1 | 19.7 | 8.61 | cumple (Ri ≥ 8 m) | 0.96 |
| C-53 | 2+029.69 | 9472700.257 | 612007.144 | 15.4 | I | 19.40 | 15.3 | 23.5 | 8.24 | cumple (Ri ≥ 8 m) | 0.17 |
| C-55 | 2+103.52 | 9472771.151 | 612006.630 | 135.3 | I | 11.30 | 6.5 | 16.1 | 9.63 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.39 |
| C-60 | 2+332.83 | 9472761.933 | 611770.429 | 88.4 | I | 9.10 | 4.2 | 14.0 | 9.75 | no cumple (Ri < 6 m) | 0.94 |
| C-67 | 2+632.49 | 9472559.465 | 611585.644 | 64.2 | D | 11.50 | 6.7 | 16.3 | 9.57 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.37 |
| C-70 | 2+787.74 | 9472638.901 | 611452.915 | 63.0 | I | 23.80 | 19.8 | 27.8 | 8.01 | cumple (Ri ≥ 8 m) | 0.63 |
| C-76 | 3+148.63 | 9472730.524 | 611203.135 | 97.0 | I | 21.70 | 17.6 | 25.8 | 8.12 | cumple (Ri ≥ 8 m) | 1.29 |
| C-80 | 3+290.21 | 9472636.120 | 611085.416 | 89.0 | D | 17.35 | 13.1 | 21.5 | 8.40 | cumple (Ri ≥ 8 m) | 0.43 |
| C-82 | 3+378.03 | 9472717.578 | 611049.115 | 147.0 | I | 8.64 | 3.8 | 13.5 | 9.75 | no cumple (Ri < 6 m) | 0.46 |
| C-87 | 3+548.39 | 9472520.056 | 611052.384 | 35.5 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 2.64 |
| C-89 | 3+582.80 | 9472493.487 | 611073.043 | 53.0 | D | 17.70 | 13.5 | 21.9 | 8.37 | cumple (Ri ≥ 8 m) | 4.60 |
| C-93 | 3+680.66 | 9472463.336 | 610995.637 | 24.5 | I | 10.02 | 5.1 | 14.9 | 9.75 | no cumple (Ri < 6 m) | 1.50 |
| C-100 | 3+945.32 | 9472551.225 | 610751.467 | 31.7 | I | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.60 |
| C-108 | 4+263.31 | 9472561.633 | 610439.068 | 93.2 | I | 12.40 | 7.7 | 17.1 | 9.31 | mínimo absoluto (6 ≤ Ri < 8 m) | 1.46 |
| C-114 | 4+525.42 | 9472540.972 | 610218.570 | 45.4 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.19 |
| C-116 | 4+608.79 | 9472502.142 | 610145.809 | 4.3 | I | 11.40 | 6.6 | 16.2 | 9.60 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.44 |
| C-118 | 4+614.64 | 9472500.023 | 610140.360 | 7.0 | I | 6.31 | 1.4 | 11.2 | 9.75 | no cumple (Ri < 6 m) | 0.33 |
| C-119 | 4+615.46 | 9472499.660 | 610139.619 | 8.4 | D | 6.00 | 1.1 | 10.9 | 9.75 | no cumple (Ri < 6 m) | 0.11 |
| C-120 | 4+616.58 | 9472499.320 | 610138.552 | 3.2 | D | 24.06 | 20.1 | 28.1 | 8.00 | cumple (Ri ≥ 8 m) | 0.13 |
| C-123 | 4+708.54 | 9472442.070 | 610070.965 | 72.6 | D | 14.07 | 9.7 | 18.5 | 8.84 | cumple (Ri ≥ 8 m) | 0.46 |
| C-126 | 4+835.70 | 9472459.837 | 609946.745 | 103.1 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.99 |
| C-127 | 4+887.87 | 9472400.337 | 609926.104 | 123.8 | D | 15.60 | 11.3 | 19.9 | 8.59 | cumple (Ri ≥ 8 m) | 1.31 |
| C-128 | 4+918.41 | 9472444.464 | 609892.798 | 90.1 | I | 8.00 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.26 |
| C-147 | 5+834.71 | 9472283.454 | 609112.203 | 82.6 | I | 24.00 | 20.0 | 28.0 | 8.00 | cumple (Ri ≥ 8 m) | 1.09 |
| C-161 | 6+727.32 | 9472049.546 | 608616.265 | 168.7 | I | 12.04 | 7.3 | 16.7 | 9.42 | mínimo absoluto (6 ≤ Ri < 8 m) | 1.46 |
| C-162 | 6+643.46 | 9471929.222 | 608648.383 | 16.1 | I | 18.40 | 14.2 | 22.6 | 8.31 | cumple (Ri ≥ 8 m) | 0.15 |
| C-166 | 6+789.20 | 9471789.864 | 608685.060 | 41.9 | D | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.72 |
| C-167 | 6+807.73 | 9471773.408 | 608675.123 | 107.5 | D | 8.48 | 3.6 | 13.4 | 9.75 | no cumple (Ri < 6 m) | 0.51 |
| C-169 | 6+874.74 | 9471811.787 | 608614.087 | 56.8 | I | 13.97 | 9.5 | 18.4 | 8.87 | cumple (Ri ≥ 8 m) | 0.71 |
| C-175 | 7+170.85 | 9471709.489 | 608448.163 | 45.7 | D | 6.00 | 1.1 | 10.9 | 9.75 | no cumple (Ri < 6 m) | 1.08 |
| C-176 | 7+178.55 | 9471716.611 | 608451.725 | 71.7 | I | 7.52 | 2.6 | 12.4 | 9.75 | no cumple (Ri < 6 m) | 5.24 |
| C-177 | 7+196.92 | 9471730.601 | 608437.667 | 112.4 | I | 9.40 | 4.5 | 14.3 | 9.75 | no cumple (Ri < 6 m) | 5.64 |
| C-179 | 7+245.30 | 9471674.476 | 608428.671 | 6.9 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 2.86 |
| C-181 | 7+340.80 | 9471593.808 | 608479.262 | 17.1 | I | 8.00 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 2.08 |
| C-182 | 7+375.25 | 9471572.038 | 608505.994 | 151.7 | D | 7.97 | 3.1 | 12.8 | 9.75 | no cumple (Ri < 6 m) | 0.56 |
| C-183 | 7+373.80 | 9471579.670 | 608466.114 | 42.9 | D | 23.00 | 19.0 | 27.0 | 8.05 | cumple (Ri ≥ 8 m) | 0.43 |
| C-185 | 7+450.89 | 9471631.255 | 608409.634 | 63.3 | I | 14.34 | 10.0 | 18.7 | 8.76 | cumple (Ri ≥ 8 m) | 0.21 |
| C-188 | 7+567.79 | 9471572.115 | 608321.039 | 19.3 | I | 8.89 | 4.0 | 13.8 | 9.75 | no cumple (Ri < 6 m) | 0.63 |
| C-189 | 7+587.70 | 9471572.337 | 608301.096 | 133.6 | I | 7.97 | 3.1 | 12.8 | 9.75 | no cumple (Ri < 6 m) | 0.57 |
| C-190 | 7+594.33 | 9471553.874 | 608318.287 | 36.7 | I | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.33 |
| C-192 | 7+695.89 | 9471578.882 | 608409.225 | 106.8 | D | 11.40 | 6.6 | 16.2 | 9.60 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.27 |
| C-195 | 7+850.67 | 9471431.884 | 608477.901 | 149.4 | D | 13.10 | 8.5 | 17.7 | 9.11 | cumple (Ri ≥ 8 m) | 1.48 |
| C-196 | 7+838.84 | 9471454.320 | 608433.604 | 10.5 | I | 10.80 | 5.9 | 15.7 | 9.75 | no cumple (Ri < 6 m) | 0.32 |
| C-197 | 7+840.47 | 9471454.780 | 608432.037 | 9.1 | D | 8.02 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.23 |
| C-199 | 7+917.53 | 9471482.198 | 608360.027 | 83.8 | I | 18.30 | 14.1 | 22.5 | 8.32 | cumple (Ri ≥ 8 m) | 1.02 |
| C-205 | 8+137.35 | 9471427.707 | 608161.406 | 97.1 | D | 23.32 | 19.3 | 27.3 | 8.03 | cumple (Ri ≥ 8 m) | 1.22 |
| C-211 | 8+334.54 | 9471610.093 | 608093.050 | 14.3 | I | 15.47 | 11.2 | 19.8 | 8.60 | cumple (Ri ≥ 8 m) | 1.34 |
| C-217 | 8+618.85 | 9471852.429 | 607997.510 | 56.2 | I | 24.10 | 20.1 | 28.1 | 8.00 | cumple (Ri ≥ 8 m) | 1.04 |
| C-219 | 8+721.25 | 9471946.138 | 607961.163 | 69.0 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.64 |
| C-221 | 8+800.84 | 9471988.888 | 607893.859 | 138.0 | I | 8.60 | 3.7 | 13.5 | 9.75 | no cumple (Ri < 6 m) | 1.14 |
| C-222 | 8+807.20 | 9471958.469 | 607895.335 | 36.7 | I | 24.30 | 20.3 | 28.3 | 8.00 | cumple (Ri ≥ 8 m) | 0.64 |
| C-223 | 8+854.73 | 9471921.340 | 607925.882 | 68.6 | D | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.48 |
| C-225 | 9+011.02 | 9471781.884 | 607959.128 | 169.3 | D | 8.00 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 1.04 |
| C-227 | 9+014.86 | 9471900.924 | 607881.254 | 88.5 | I | 11.20 | 6.4 | 16.0 | 9.66 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.65 |
| C-229 | 9+128.51 | 9471960.554 | 607794.904 | 113.0 | I | 8.90 | 4.0 | 13.8 | 9.75 | no cumple (Ri < 6 m) | 0.76 |
| C-230 | 9+159.84 | 9471935.932 | 607762.515 | 40.8 | I | 10.74 | 5.9 | 15.6 | 9.75 | no cumple (Ri < 6 m) | 0.47 |
| C-232 | 9+266.49 | 9471878.559 | 607832.428 | 120.4 | D | 12.40 | 7.7 | 17.1 | 9.31 | mínimo absoluto (6 ≤ Ri < 8 m) | 1.13 |
| C-237 | 9+426.68 | 9471717.373 | 607840.435 | 154.9 | D | 8.30 | 3.4 | 13.2 | 9.75 | no cumple (Ri < 6 m) | 1.68 |
| C-239 | 9+466.96 | 9471788.571 | 607786.239 | 27.9 | I | 13.50 | 9.0 | 18.0 | 9.00 | cumple (Ri ≥ 8 m) | 0.38 |
| C-240 | 9+517.37 | 9471831.834 | 607760.094 | 96.0 | I | 14.70 | 10.3 | 19.1 | 8.71 | cumple (Ri ≥ 8 m) | 1.34 |
| C-245 | 9+751.83 | 9471880.585 | 607553.646 | 61.2 | D | 23.60 | 19.6 | 27.6 | 8.02 | cumple (Ri ≥ 8 m) | 0.71 |
| C-246 | 9+807.38 | 9471938.742 | 607550.086 | 146.4 | I | 8.70 | 3.8 | 13.6 | 9.75 | no cumple (Ri < 6 m) | 0.76 |
| C-252 | 10+085.50 | 9471725.993 | 607658.496 | 19.2 | I | 7.51 | 2.6 | 12.4 | 9.75 | no cumple (Ri < 6 m) | 0.96 |
| C-253 | 10+091.53 | 9471728.828 | 607663.850 | 73.6 | D | 6.40 | 1.5 | 11.3 | 9.75 | no cumple (Ri < 6 m) | 1.87 |
| C-256 | 10+185.96 | 9471636.629 | 607677.205 | 21.7 | D | 10.10 | 5.2 | 15.0 | 9.75 | no cumple (Ri < 6 m) | 0.60 |
| C-258 | 10+259.16 | 9471570.989 | 607695.578 | 39.6 | D | 10.60 | 5.7 | 15.5 | 9.75 | no cumple (Ri < 6 m) | 1.25 |
| C-259 | 10+281.05 | 9471549.058 | 607698.960 | 132.3 | D | 8.13 | 3.3 | 13.0 | 9.75 | no cumple (Ri < 6 m) | 0.82 |
| C-262 | 10+419.87 | 9471686.112 | 607641.417 | 74.0 | I | 12.40 | 7.7 | 17.1 | 9.31 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.51 |
| C-271 | 10+960.04 | 9471983.138 | 607508.918 | 44.7 | I | 17.00 | 12.8 | 21.2 | 8.43 | cumple (Ri ≥ 8 m) | 0.18 |
| C-274 | 11+059.34 | 9472075.534 | 607539.017 | 105.8 | I | 11.65 | 6.9 | 16.4 | 9.53 | mínimo absoluto (6 ≤ Ri < 8 m) | 1.00 |

Agrupación en zonas (curvas de vuelta consecutivas):

| Zona | Prog. inicio | Prog. fin | Curvas | R mín. eje (m) | Ri mín. (m) | Evaluación |
|-----|--------|--------|------------|------|------|-------------|
| V-1 | 0+052.15 | 0+063.95 | C-2 | 7.1 | 2.2 | no cumple |
| V-2 | 0+111.61 | 0+130.85 | C-4 | 22.7 | 18.7 | cumple |
| V-3 | 0+182.59 | 0+316.20 | C-7, C-8, C-9, C-10, C-11 | 6.0 | 1.1 | no cumple |
| V-4 | 0+436.45 | 0+440.76 | C-15 | 15.0 | 10.7 | cumple |
| V-5 | 0+636.53 | 0+637.84 | C-19 | 8.1 | 3.2 | no cumple |
| V-6 | 0+731.10 | 0+743.35 | C-21, C-22 | 7.2 | 2.3 | no cumple |
| V-7 | 1+030.67 | 1+047.88 | C-29 | 8.8 | 3.9 | no cumple |
| V-8 | 1+428.98 | 1+474.58 | C-37 | 24.6 | 20.6 | cumple |
| V-9 | 1+539.36 | 1+553.19 | C-39 | 11.7 | 6.9 | mínimo absoluto |
| V-10 | 1+992.23 | 2+005.54 | C-51 | 15.4 | 11.1 | cumple |
| V-11 | 2+027.06 | 2+032.28 | C-53 | 19.4 | 15.3 | cumple |
| V-12 | 2+076.04 | 2+102.72 | C-55 | 11.3 | 6.5 | mínimo absoluto |
| V-13 | 2+323.97 | 2+338.02 | C-60 | 9.1 | 4.2 | no cumple |
| V-14 | 2+625.28 | 2+638.16 | C-67 | 11.5 | 6.7 | mínimo absoluto |
| V-15 | 2+773.15 | 2+799.33 | C-70 | 23.8 | 19.8 | cumple |
| V-16 | 3+124.12 | 3+160.84 | C-76 | 21.7 | 17.6 | cumple |
| V-17 | 3+273.18 | 3+300.11 | C-80 | 17.3 | 13.1 | cumple |
| V-18 | 3+348.84 | 3+371.02 | C-82 | 8.6 | 3.8 | no cumple |
| V-19 | 3+543.59 | 3+552.88 | C-87 | 15.0 | 10.7 | cumple |
| V-20 | 3+573.98 | 3+590.34 | C-89 | 17.7 | 13.5 | cumple |
| V-21 | 3+678.49 | 3+682.77 | C-93 | 10.0 | 5.1 | no cumple |
| V-22 | 3+939.65 | 3+950.70 | C-100 | 20.0 | 15.9 | cumple |
| V-23 | 4+250.19 | 4+270.36 | C-108 | 12.4 | 7.7 | mínimo absoluto |
| V-24 | 4+519.15 | 4+531.03 | C-114 | 15.0 | 10.7 | cumple |
| V-25 | 4+608.36 | 4+609.22 | C-116 | 11.4 | 6.6 | mínimo absoluto |
| V-26 | 4+614.25 | 4+617.26 | C-118, C-119, C-120 | 6.0 | 1.1 | no cumple |
| V-27 | 4+698.21 | 4+716.04 | C-123 | 14.1 | 9.7 | cumple |
| V-28 | 4+816.80 | 4+922.98 | C-126, C-127, C-128 | 8.0 | 3.1 | no cumple |
| V-29 | 5+813.62 | 5+848.22 | C-147 | 24.0 | 20.0 | cumple |
| V-30 | 6+605.39 | 6+646.03 | C-161, C-162 | 12.0 | 7.3 | mínimo absoluto |
| V-31 | 6+781.54 | 6+812.08 | C-166, C-167 | 8.5 | 3.6 | no cumple |
| V-32 | 6+867.18 | 6+881.04 | C-169 | 14.0 | 9.5 | cumple |
| V-33 | 7+168.33 | 7+201.32 | C-175, C-176, C-177 | 6.0 | 1.1 | no cumple |
| V-34 | 7+244.40 | 7+246.20 | C-179 | 15.0 | 10.7 | cumple |
| V-35 | 7+339.59 | 7+381.98 | C-181, C-182, C-183 | 8.0 | 3.1 | no cumple |
| V-36 | 7+442.06 | 7+457.89 | C-185 | 14.3 | 10.0 | cumple |
| V-37 | 7+566.27 | 7+600.51 | C-188, C-189, C-190 | 8.0 | 3.1 | no cumple |
| V-38 | 7+680.55 | 7+701.79 | C-192 | 11.4 | 6.6 | mínimo absoluto |
| V-39 | 7+802.86 | 7+841.11 | C-195, C-196, C-197 | 8.0 | 3.1 | no cumple |
| V-40 | 7+901.09 | 7+927.87 | C-199 | 18.3 | 14.1 | cumple |
| V-41 | 8+110.96 | 8+150.47 | C-205 | 23.3 | 19.3 | cumple |
| V-42 | 8+332.60 | 8+336.46 | C-211 | 15.5 | 11.2 | cumple |
| V-43 | 8+605.99 | 8+629.61 | C-217 | 24.1 | 20.1 | cumple |
| V-44 | 8+710.95 | 8+729.01 | C-219 | 15.0 | 10.7 | cumple |
| V-45 | 8+778.44 | 8+865.03 | C-221, C-222, C-223 | 8.6 | 3.7 | no cumple |
| V-46 | 8+925.82 | 8+949.45 | C-225 | 8.0 | 3.1 | no cumple |
| V-47 | 9+003.95 | 9+021.25 | C-227 | 11.2 | 6.4 | mínimo absoluto |
| V-48 | 9+115.05 | 9+163.50 | C-229, C-230 | 8.9 | 4.0 | no cumple |
| V-49 | 9+244.82 | 9+270.89 | C-232 | 12.4 | 7.7 | mínimo absoluto |
| V-50 | 9+389.41 | 9+411.85 | C-237 | 8.3 | 3.4 | no cumple |
| V-51 | 9+463.60 | 9+525.68 | C-239, C-240 | 13.5 | 9.0 | cumple |
| V-52 | 9+737.87 | 9+800.78 | C-245, C-246 | 8.7 | 3.8 | no cumple |
| V-53 | 10+084.22 | 10+094.96 | C-252, C-253 | 6.4 | 1.5 | no cumple |
| V-54 | 10+184.02 | 10+187.85 | C-256 | 10.1 | 5.2 | no cumple |
| V-55 | 10+255.35 | 10+281.44 | C-258, C-259 | 8.1 | 3.3 | no cumple |
| V-56 | 10+410.53 | 10+426.54 | C-262 | 12.4 | 7.7 | mínimo absoluto |
| V-57 | 10+953.05 | 10+966.31 | C-271 | 17.0 | 12.8 | cumple |
| V-58 | 11+043.94 | 11+065.45 | C-274 | 11.7 | 6.9 | mínimo absoluto |

## 6.4 Tangentes

| Longitud de la tangente intermedia | Cantidad |
|------------------------|------|
| 0 (curvas enlazadas) | 78 |
| 0 a 20 m | 119 |
| 20 a 56 m | 71 |
| 56 a 111 m | 13 |
| más de 111 m | 0 |

Las 7 tangentes que cumplen la Tabla 302.01 son:

| Entre curvas | Longitud (m) | Mínimo exigido (m) | Tipo |
|---------|------|------|------|
| C-10 y C-11 | 56.4 | 56 | curvas en S |
| C-69 y C-70 | 70.2 | 56 | curvas en S |
| C-104 y C-105 | 57.6 | 56 | curvas en S |
| C-144 y C-145 | 84.4 | 56 | curvas en S |
| C-147 y C-148 | 63.6 | 56 | curvas en S |
| C-151 y C-152 | 59.3 | 56 | curvas en S |
| C-203 y C-204 | 56.4 | 56 | curvas en S |

## 6.5 Sitios donde el eje se separa más de 2.5 m del trazo actual

Son los puntos a revisar en campo o en Civil 3D antes de aprobar el eje, por su posible afectación a edificaciones.

| Curva | Prog. PC | Prog. PT | Norte PI | Este PI | R (m) | Separación máx. (m) | Comentario |
|------|--------|--------|---------|---------|-----|------|----------------|
| C-87 | 3+543.59 | 3+552.88 | 9472520.056 | 611052.384 | 15.0 | 2.64 | cadena de curvas de radio variable en el trazo |
| C-88 | 3+553.80 | 3+572.69 | 9472511.901 | 611065.550 | 30.0 | 5.17 | cadena de curvas de radio variable en el trazo |
| C-89 | 3+573.98 | 3+590.34 | 9472493.487 | 611073.043 | 17.7 | 4.60 | cadena de curvas de radio variable en el trazo |
| C-90 | 3+591.88 | 3+627.90 | 9472468.891 | 611058.366 | 85.0 | 3.29 | cadena de curvas de radio variable en el trazo |
| C-91 | 3+629.19 | 3+655.91 | 9472449.657 | 611030.786 | 35.0 | 5.84 | cadena de curvas de radio variable en el trazo |
| C-92 | 3+657.11 | 3+678.49 | 9472453.707 | 611004.763 | 32.5 | 4.64 | cadena de curvas de radio variable en el trazo |
| C-176 | 7+173.11 | 7+182.52 | 9471716.611 | 608451.725 | 7.5 | 5.24 | cadena de curvas de radio variable en el trazo |
| C-177 | 7+182.88 | 7+201.32 | 9471730.601 | 608437.667 | 9.4 | 5.64 | cadena de curvas de radio variable en el trazo |
| C-178 | 7+202.45 | 7+236.58 | 9471700.434 | 608425.197 | 65.0 | 2.84 | cadena de curvas de radio variable en el trazo |
| C-179 | 7+244.40 | 7+246.20 | 9471674.476 | 608428.671 | 15.0 | 2.86 | cadena de curvas de radio variable en el trazo |
| C-265 | 10+510.31 | 10+630.21 | 9471641.793 | 607478.766 | 70.0 | 2.92 | cadena de curvas de radio variable en el trazo |

# 7. Pasada de tangentes (Tabla 302.01 y Tópico 302.06.03)

Sobre el eje ajustado al trazo se aplicó una pasada para respetar las longitudes de tangente donde fuera posible, con una separación máxima adicional respecto al trazo de 1.5 m. Reglas aplicadas:

1. Curvas consecutivas del mismo sentido separadas por una tangente menor de 111 m: se reemplazan por una sola curva circular si cabe dentro de la tolerancia; si no, se convierten en curva compuesta (policéntrica) elevando el radio de una de ellas hasta eliminar la tangente intermedia, solución que el Tópico 302.06.03 admite excepcionalmente. Nunca se recorta una tangente vecina entre curvas en S.
2. Curvas en S con tangente menor de 56 m: se reducen los radios de ambas curvas, sin bajar de 45 m, hasta abrir la tangente a 56 m, siempre que la separación respecto al trazo no supere la tolerancia.
3. Las deflexiones menores de 12° cuya supresión desplaza el eje menos de 1.0 m se absorbieron en la tangente desde el ajuste base, lo que alarga las tangentes y reduce el número de curvas.

| Indicador | Antes de la pasada | Después |
|------------------------------|---------|---------|
| Número de curvas | 324 | 282 |
| Pares del mismo sentido con tangente corta (0 < L < 111 m) | 125 | 45 |
| Pares del mismo sentido resueltos como curva compuesta (sin tangente) | 11 | 49 |
| Pares del mismo sentido con tangente ≥ 111 m | 0 | 0 |
| Pares en S con tangente ≥ 56 m | 4 | 7 |
| Pares en S con tangente entre 20 y 56 m | 46 | 47 |
| Pares en S con tangente menor de 20 m (incluye 0) | 137 | 133 |

Resultado de la pasada: 42 fusiones en una sola curva, 42 pares convertidos en curva compuesta, 45 pares del mismo sentido que no admiten ninguna de las dos soluciones dentro de la tolerancia, 2 tangentes en S abiertas a 56 m y 171 que no pueden abrirse sin bajar de 45 m de radio o sin salirse del trazo más de 1.5 m.

Las tangentes en S son el incumplimiento que queda. Para abrir 56 m entre dos curvas de 45 m de radio y 40° de deflexión los PIs deben distar unos 90 m, y en este trazo distan típicamente de 30 a 80 m. Solo se puede corregir saliéndose del trazo existente, es decir, con expropiación, o reduciendo la velocidad específica del sector.

# 8. Conclusiones y recomendaciones

1. El eje cumple el radio mínimo de la DG-2018 (45 m a 40 km/h, peralte 12 %) en 146 de 282 curvas. En 52 curvas se adopta radio excepcional con velocidad específica de 30 km/h y en 84 se trata de curvas de vuelta o esquinas urbanas.
2. Las 33 curvas con radio interior menor de 6 m (zonas V-1, V-3 y otras indicadas en 6.3) no admiten justificación con la DG-2018. Se recomienda ampliar la plataforma en esos puntos o aceptar expropiaciones puntuales.
3. Los primeros 230 m (zona urbana de inicio) tienen geometría de calles, con radios de 6 a 22 m. Conviene tratar ese tramo como vía urbana con velocidad de 20 a 30 km/h.
4. Las clotoides, las tangentes mínimas y la longitud mínima de curva no se cumplen por la premisa de seguir el trazo existente. Debe dejarse constancia en el expediente, con la señalización vertical y horizontal correspondiente al Manual de Dispositivos de Control de Tránsito.
7. Las tangentes en S que siguen por debajo de 56 m deben señalizarse como sector de curvas sucesivas; su corrección geométrica exige expropiación.
5. En Civil 3D, asociar al eje el archivo de criterios DG2018_Corregido_2.xml con velocidad 40 km/h; los triángulos de advertencia que queden marcan exactamente las curvas de los capítulos 6.2 y 6.3.
6. Verificar la visibilidad de parada (50 m) con banquetas en las curvas de radio menor a 60 m ubicadas en corte, según el Tópico 302.10.01.

# Anexo A. Tabla completa de curvas

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | T (m) | Lc (m) | E (m) | Prog. PC | Prog. PT | Sa (m) | Tang. sig. (m) | Sep. (m) | Clase |
|-----|--------|---------|---------|-----|---|-----|-----|-----|----|--------|--------|----|-----|----|---------|
| C-1 | 0+037.84 | 9472166.45 | 613022.23 | 44.7 | I | 38.78 | 15.9 | 30.2 | 3.15 | 0+021.90 | 0+052.15 | 3.57 | 0.0 | 1.16 | Excepcional |
| C-2 | 0+059.92 | 9472190.09 | 613024.16 | 95.0 | I | 7.12 | 7.8 | 11.8 | 3.42 | 0+052.15 | 0+063.95 | - | 23.0 | 1.08 | Vuelta |
| C-3 | 0+099.58 | 9472189.81 | 612980.76 | 31.5 | D | 44.97 | 12.7 | 24.7 | 1.75 | 0+086.91 | 0+111.61 | 3.11 | 0.0 | 1.89 | Normativa 12% |
| C-4 | 0+121.85 | 9472201.64 | 612961.14 | 48.6 | D | 22.70 | 10.2 | 19.2 | 2.20 | 0+111.61 | 0+130.85 | 6.04 | 11.9 | 1.76 | Vuelta |
| C-5 | 0+151.86 | 9472232.39 | 612955.53 | 12.2 | I | 85.00 | 9.1 | 18.1 | 0.48 | 0+142.79 | 0+160.87 | 1.75 | 0.6 | 0.21 | Normativa 8% |
| C-6 | 0+169.69 | 9472248.92 | 612948.68 | 36.4 | D | 25.00 | 8.2 | 15.9 | 1.32 | 0+161.46 | 0+177.35 | 5.47 | 5.2 | 0.43 | Excepcional |
| C-7 | 0+186.74 | 9472266.01 | 612952.91 | 42.2 | I | 10.75 | 4.2 | 7.9 | 0.77 | 0+182.59 | 0+190.52 | 18.57 | 0.0 | 0.36 | Vuelta |
| C-8 | 0+195.72 | 9472274.25 | 612948.47 | 81.8 | D | 6.00 | 5.2 | 8.6 | 1.94 | 0+190.52 | 0+199.09 | - | 2.1 | 1.15 | Vuelta |
| C-9 | 0+208.69 | 9472283.05 | 612960.37 | 35.0 | I | 23.80 | 7.5 | 14.5 | 1.15 | 0+201.19 | 0+215.72 | 5.75 | 0.5 | 0.45 | Vuelta |
| C-10 | 0+223.50 | 9472297.54 | 612965.22 | 51.6 | D | 15.00 | 7.3 | 13.5 | 1.66 | 0+216.25 | 0+229.77 | 9.71 | 56.4 | 2.11 | Vuelta |
| C-11 | 0+315.17 | 9472328.98 | 613052.39 | 131.4 | I | 13.10 | 29.0 | 30.0 | 18.73 | 0+286.16 | 0+316.20 | 11.77 | -0.0 | 1.18 | Vuelta |
| C-12 | 0+326.44 | 9472347.88 | 613017.99 | 28.7 | I | 40.00 | 10.2 | 20.1 | 1.29 | 0+316.20 | 0+336.26 | 3.47 | 23.1 | 0.21 | Excepcional |
| C-13 | 0+372.41 | 9472347.91 | 612971.58 | 19.7 | D | 75.00 | 13.0 | 25.8 | 1.12 | 0+359.38 | 0+385.19 | 1.95 | 30.8 | 0.69 | Normativa 8% |
| C-14 | 0+425.96 | 9472366.10 | 612920.95 | 12.6 | D | 90.00 | 9.9 | 19.8 | 0.55 | 0+416.03 | 0+435.81 | 1.66 | 0.6 | 0.17 | Normativa 8% |
| C-15 | 0+438.62 | 9472372.92 | 612910.18 | 16.4 | I | 15.00 | 2.2 | 4.3 | 0.16 | 0+436.45 | 0+440.76 | 9.71 | 19.6 | 0.15 | Vuelta |
| C-16 | 0+479.75 | 9472384.20 | 612870.60 | 46.7 | D | 45.00 | 19.4 | 36.7 | 4.01 | 0+460.33 | 0+497.00 | 3.10 | 17.3 | 1.55 | Normativa 12% |
| C-17 | 0+523.33 | 9472424.82 | 612849.55 | 22.8 | I | 45.00 | 9.1 | 17.9 | 0.90 | 0+514.27 | 0+532.15 | 3.10 | 50.2 | 0.29 | Normativa 12% |
| C-18 | 0+614.54 | 9472483.41 | 612779.33 | 77.8 | D | 39.90 | 32.2 | 54.2 | 11.38 | 0+582.33 | 0+636.53 | 3.47 | -0.0 | 1.74 | Excepcional |
| C-19 | 0+637.19 | 9472512.53 | 612794.60 | 9.3 | I | 8.07 | 0.7 | 1.3 | 0.03 | 0+636.53 | 0+637.84 | - | 40.6 | 0.74 | Vuelta |
| C-20 | 0+695.09 | 9472567.49 | 612812.81 | 40.5 | D | 45.00 | 16.6 | 31.8 | 2.96 | 0+678.49 | 0+710.29 | 3.10 | 20.8 | 0.70 | Normativa 12% |
| C-21 | 0+732.09 | 9472587.37 | 612845.66 | 6.5 | I | 17.37 | 1.0 | 2.0 | 0.03 | 0+731.10 | 0+733.08 | 8.10 | 0.0 | 0.45 | Vuelta |
| C-22 | 0+739.31 | 9472591.78 | 612851.37 | 81.7 | I | 7.20 | 6.2 | 10.3 | 2.32 | 0+733.08 | 0+743.35 | - | 11.4 | 0.69 | Vuelta |
| C-23 | 0+767.37 | 9472618.13 | 612836.50 | 45.9 | I | 29.88 | 12.7 | 24.0 | 2.57 | 0+754.71 | 0+778.66 | 4.58 | 0.0 | 0.97 | Excepcional |
| C-24 | 0+783.00 | 9472622.42 | 612820.06 | 14.1 | D | 35.00 | 4.3 | 8.6 | 0.27 | 0+778.66 | 0+787.28 | 3.93 | 59.5 | 0.39 | Excepcional |
| C-25 | 0+887.28 | 9472672.60 | 612728.60 | 84.0 | D | 45.00 | 40.5 | 66.0 | 15.55 | 0+846.75 | 0+912.73 | 3.10 | 3.1 | 1.56 | Normativa 12% |
| C-26 | 0+928.30 | 9472724.32 | 612750.29 | 31.9 | I | 43.60 | 12.5 | 24.3 | 1.75 | 0+915.83 | 0+940.12 | 3.20 | 8.0 | 1.38 | Excepcional |
| C-27 | 0+961.30 | 9472757.55 | 612744.92 | 21.3 | D | 70.00 | 13.2 | 26.0 | 1.23 | 0+948.13 | 0+974.17 | 2.08 | 24.1 | 0.33 | Normativa 8% |
| C-28 | 1+015.20 | 9472810.53 | 612756.32 | 41.3 | I | 44.95 | 17.0 | 32.4 | 3.09 | 0+998.24 | 1+030.67 | 3.11 | -0.0 | 0.86 | Normativa 12% |
| C-29 | 1+043.73 | 9472836.73 | 612741.68 | 112.0 | I | 8.80 | 13.1 | 17.2 | 6.94 | 1+030.67 | 1+047.88 | - | 20.1 | 0.65 | Vuelta |
| C-30 | 1+075.62 | 9472804.92 | 612716.14 | 19.3 | D | 45.00 | 7.7 | 15.2 | 0.65 | 1+067.95 | 1+083.14 | 3.10 | 2.1 | 0.33 | Normativa 12% |
| C-31 | 1+092.75 | 9472795.79 | 612701.47 | 10.8 | I | 80.00 | 7.6 | 15.1 | 0.36 | 1+085.20 | 1+100.26 | 1.84 | 20.4 | 0.07 | Normativa 8% |
| C-32 | 1+126.44 | 9472772.92 | 612676.67 | 14.7 | D | 45.00 | 5.8 | 11.6 | 0.37 | 1+120.63 | 1+132.19 | 3.10 | 9.1 | 0.34 | Normativa 12% |
| C-33 | 1+152.92 | 9472760.47 | 612653.23 | 21.9 | I | 60.00 | 11.6 | 22.9 | 1.11 | 1+141.32 | 1+164.23 | 2.39 | 20.2 | 0.25 | Normativa 8% |
| C-34 | 1+223.98 | 9472705.95 | 612607.21 | 55.6 | D | 75.00 | 39.6 | 72.8 | 9.80 | 1+184.40 | 1+257.24 | 1.95 | 62.9 | 0.53 | Normativa 8% |
| C-35 | 1+354.23 | 9472719.76 | 612471.34 | 74.3 | D | 45.00 | 34.1 | 58.3 | 11.45 | 1+320.15 | 1+378.48 | 3.10 | 26.6 | 0.93 | Normativa 12% |
| C-36 | 1+417.33 | 9472791.60 | 612458.78 | 30.4 | I | 45.00 | 12.2 | 23.9 | 1.63 | 1+405.11 | 1+428.98 | 3.10 | -0.0 | 1.18 | Normativa 12% |
| C-37 | 1+461.71 | 9472825.87 | 612429.69 | 106.1 | I | 24.63 | 32.7 | 45.6 | 16.33 | 1+428.98 | 1+474.58 | 5.55 | -0.3 | 1.24 | Vuelta |
| C-38 | 1+497.76 | 9472779.31 | 612398.74 | 60.8 | D | 40.00 | 23.5 | 42.5 | 6.38 | 1+474.29 | 1+516.74 | 3.47 | 22.6 | 0.76 | Excepcional |
| C-39 | 1+547.21 | 9472783.48 | 612344.96 | 67.7 | D | 11.70 | 7.8 | 13.8 | 2.39 | 1+539.36 | 1+553.19 | 14.45 | 15.5 | 0.49 | Vuelta |
| C-40 | 1+588.26 | 9472824.33 | 612331.80 | 66.4 | I | 29.90 | 19.6 | 34.6 | 5.83 | 1+568.70 | 1+603.34 | 4.58 | 4.3 | 0.61 | Excepcional |
| C-41 | 1+616.52 | 9472827.62 | 612299.23 | 22.3 | D | 45.00 | 8.9 | 17.5 | 0.86 | 1+607.66 | 1+625.15 | 3.10 | 7.3 | 0.51 | Normativa 12% |
| C-42 | 1+644.88 | 9472841.05 | 612274.00 | 35.4 | I | 38.90 | 12.4 | 24.1 | 1.94 | 1+632.45 | 1+656.51 | 3.56 | -0.0 | 1.21 | Excepcional |
| C-43 | 1+667.90 | 9472837.98 | 612250.37 | 32.3 | D | 39.31 | 11.4 | 22.2 | 1.62 | 1+656.51 | 1+678.69 | 3.52 | 11.0 | 0.38 | Excepcional |
| C-44 | 1+758.94 | 9472876.60 | 612167.27 | 103.1 | I | 55.00 | 69.2 | 99.0 | 33.43 | 1+689.69 | 1+788.64 | 2.58 | -0.0 | 1.57 | Normativa 8% |
| C-45 | 1+790.60 | 9472806.91 | 612152.66 | 1.3 | I | 171.82 | 2.0 | 3.9 | 0.01 | 1+788.64 | 1+792.55 | 0.95 | 24.8 | 0.05 | Normativa 8% |
| C-46 | 1+836.43 | 9472761.86 | 612144.28 | 23.9 | D | 90.00 | 19.1 | 37.6 | 2.00 | 1+817.35 | 1+854.95 | 1.66 | 29.1 | 1.03 | Normativa 8% |
| C-47 | 1+902.33 | 9472707.07 | 612106.66 | 29.3 | D | 70.00 | 18.3 | 35.8 | 2.36 | 1+884.01 | 1+919.85 | 2.08 | 5.5 | 0.43 | Normativa 8% |
| C-48 | 1+929.98 | 9472694.51 | 612081.13 | 11.8 | I | 45.00 | 4.7 | 9.3 | 0.24 | 1+925.33 | 1+934.60 | 3.10 | -1.5 | 0.17 | Normativa 12% |
| C-49 | 1+954.24 | 9472679.55 | 612061.98 | 19.2 | D | 124.49 | 21.1 | 41.8 | 1.78 | 1+933.14 | 1+974.95 | 1.25 | 0.0 | 1.27 | Normativa 8% |
| C-50 | 1+985.49 | 9472669.38 | 612032.02 | 27.0 | D | 43.90 | 10.5 | 20.7 | 1.25 | 1+974.95 | 1+995.64 | 3.18 | -3.4 | 0.17 | Excepcional |
| C-51 | 1+999.33 | 9472671.42 | 612017.93 | 49.5 | D | 15.40 | 7.1 | 13.3 | 1.56 | 1+992.23 | 2+005.54 | 9.38 | 0.0 | 0.96 | Vuelta |
| C-52 | 2+016.51 | 9472686.71 | 612008.29 | 27.4 | D | 45.00 | 11.0 | 21.5 | 1.32 | 2+005.54 | 2+027.06 | 3.10 | -0.0 | 0.76 | Normativa 12% |
| C-53 | 2+029.69 | 9472700.26 | 612007.14 | 15.4 | I | 19.40 | 2.6 | 5.2 | 0.18 | 2+027.06 | 2+032.28 | 7.15 | 19.7 | 0.17 | Vuelta |
| C-54 | 2+064.44 | 9472732.89 | 611995.11 | 37.0 | D | 37.28 | 12.5 | 24.1 | 2.03 | 2+051.96 | 2+076.04 | 3.70 | -0.0 | 0.65 | Excepcional |
| C-55 | 2+103.52 | 9472771.15 | 612006.63 | 135.3 | I | 11.30 | 27.5 | 26.7 | 18.42 | 2+076.04 | 2+102.72 | 15.69 | 3.5 | 0.39 | Vuelta |
| C-56 | 2+120.78 | 9472749.39 | 611966.63 | 20.6 | D | 80.00 | 14.5 | 28.7 | 1.31 | 2+106.25 | 2+134.99 | 1.84 | 6.1 | 0.24 | Normativa 8% |
| C-57 | 2+153.96 | 9472744.75 | 611933.46 | 32.0 | I | 45.00 | 12.9 | 25.1 | 1.81 | 2+141.05 | 2+166.18 | 3.10 | 1.6 | 0.60 | Normativa 12% |
| C-58 | 2+196.15 | 9472717.22 | 611900.60 | 86.8 | D | 30.00 | 28.4 | 45.4 | 11.28 | 2+167.79 | 2+213.22 | 4.56 | 14.0 | 1.24 | Excepcional |
| C-59 | 2+249.76 | 9472764.53 | 611856.19 | 48.5 | I | 50.00 | 22.5 | 42.4 | 4.85 | 2+227.22 | 2+269.58 | 2.82 | 54.4 | 1.33 | Normativa 8% |
| C-60 | 2+332.83 | 9472761.93 | 611770.43 | 88.4 | I | 9.10 | 8.9 | 14.0 | 3.60 | 2+323.97 | 2+338.02 | - | 0.4 | 0.94 | Vuelta |
| C-61 | 2+360.90 | 9472730.20 | 611770.53 | 29.7 | D | 85.00 | 22.5 | 44.0 | 2.93 | 2+338.37 | 2+382.41 | 1.75 | 0.6 | 0.34 | Normativa 8% |
| C-62 | 2+389.39 | 9472704.52 | 611756.00 | 16.2 | I | 45.00 | 6.4 | 12.7 | 0.45 | 2+382.99 | 2+395.71 | 3.10 | 18.6 | 0.57 | Normativa 12% |
| C-63 | 2+445.96 | 9472649.38 | 611742.96 | 43.2 | D | 80.00 | 31.7 | 60.3 | 6.05 | 2+414.27 | 2+474.62 | 1.84 | 36.6 | 0.54 | Normativa 8% |
| C-64 | 2+532.55 | 9472599.94 | 611668.21 | 42.4 | D | 55.00 | 21.3 | 40.7 | 3.98 | 2+511.24 | 2+551.90 | 2.58 | 1.6 | 0.45 | Normativa 8% |
| C-65 | 2+574.61 | 9472606.73 | 611624.72 | 71.4 | I | 29.40 | 21.1 | 36.6 | 6.79 | 2+553.50 | 2+590.12 | 4.65 | 9.8 | 0.37 | Excepcional |
| C-66 | 2+613.11 | 9472567.61 | 611604.35 | 38.9 | D | 37.30 | 13.2 | 25.4 | 2.26 | 2+599.93 | 2+625.28 | 3.70 | -0.0 | 1.18 | Excepcional |
| C-67 | 2+632.49 | 9472559.47 | 611585.64 | 64.2 | D | 11.50 | 7.2 | 12.9 | 2.07 | 2+625.28 | 2+638.16 | 15.03 | 8.1 | 0.37 | Vuelta |
| C-68 | 2+658.61 | 9472577.48 | 611564.66 | 30.8 | I | 45.00 | 12.4 | 24.2 | 1.67 | 2+646.23 | 2+670.39 | 3.10 | 12.4 | 0.74 | Normativa 12% |
| C-69 | 2+693.06 | 9472583.50 | 611530.13 | 25.8 | D | 45.00 | 10.3 | 20.2 | 1.16 | 2+682.76 | 2+703.00 | 3.10 | 70.2 | 0.95 | Normativa 12% |
| C-70 | 2+787.74 | 9472638.90 | 611452.91 | 63.0 | I | 23.80 | 14.6 | 26.2 | 4.12 | 2+773.15 | 2+799.33 | 5.75 | 21.5 | 0.63 | Vuelta |
| C-71 | 2+827.71 | 9472619.14 | 611414.75 | 17.3 | I | 45.00 | 6.8 | 13.6 | 0.52 | 2+820.87 | 2+834.46 | 3.10 | 12.6 | 0.31 | Normativa 12% |
| C-72 | 2+885.19 | 9472578.66 | 611373.81 | 69.5 | D | 55.00 | 38.2 | 66.7 | 11.95 | 2+847.02 | 2+913.76 | 2.58 | 6.4 | 1.02 | Normativa 8% |
| C-73 | 2+940.74 | 9472606.04 | 611314.68 | 41.1 | I | 55.00 | 20.6 | 39.4 | 3.73 | 2+920.15 | 2+959.56 | 2.58 | 23.5 | 0.40 | Normativa 8% |
| C-74 | 3+002.48 | 9472588.32 | 611253.69 | 75.6 | D | 25.00 | 19.4 | 33.0 | 6.63 | 2+983.10 | 3+016.07 | 5.47 | 0.0 | 0.57 | Excepcional |
| C-75 | 3+049.51 | 9472633.76 | 611226.77 | 16.9 | D | 224.94 | 33.4 | 66.4 | 2.47 | 3+016.07 | 3+082.47 | 0.76 | 41.6 | 1.19 | Normativa 8% |
| C-76 | 3+148.63 | 9472730.52 | 611203.13 | 97.0 | I | 21.70 | 24.5 | 36.7 | 11.04 | 3+124.12 | 3+160.84 | 6.33 | 0.0 | 1.29 | Vuelta |
| C-77 | 3+178.90 | 9472715.48 | 611163.31 | 30.6 | I | 65.90 | 18.1 | 35.2 | 2.43 | 3+160.84 | 3+196.09 | 2.19 | 13.7 | 1.31 | Normativa 8% |
| C-78 | 3+226.80 | 9472677.40 | 611132.85 | 21.4 | D | 90.00 | 17.0 | 33.6 | 1.59 | 3+209.82 | 3+243.38 | 1.66 | 5.7 | 0.15 | Normativa 8% |
| C-79 | 3+257.60 | 9472661.81 | 611105.82 | 21.6 | I | 45.00 | 8.6 | 16.9 | 0.81 | 3+249.04 | 3+265.97 | 3.10 | 7.2 | 0.32 | Normativa 12% |
| C-80 | 3+290.21 | 9472636.12 | 611085.42 | 89.0 | D | 17.35 | 17.0 | 26.9 | 6.96 | 3+273.18 | 3+300.11 | 8.11 | 0.0 | 0.43 | Vuelta |
| C-81 | 3+325.87 | 9472662.12 | 611051.43 | 50.2 | D | 55.00 | 25.8 | 48.2 | 5.73 | 3+300.11 | 3+348.29 | 2.58 | 0.6 | 0.61 | Normativa 8% |
| C-82 | 3+378.03 | 9472717.58 | 611049.12 | 147.0 | I | 8.64 | 29.2 | 22.2 | 21.80 | 3+348.84 | 3+371.02 | - | -0.0 | 0.46 | Vuelta |
| C-83 | 3+380.99 | 9472683.87 | 611029.18 | 32.2 | I | 34.50 | 10.0 | 19.4 | 1.41 | 3+371.02 | 3+390.42 | 3.99 | 16.6 | 1.18 | Excepcional |
| C-84 | 3+411.16 | 9472653.18 | 611030.05 | 10.5 | D | 45.00 | 4.2 | 8.3 | 0.19 | 3+407.01 | 3+415.29 | 3.10 | 0.8 | 0.25 | Normativa 12% |
| C-85 | 3+422.30 | 9472642.16 | 611028.32 | 10.1 | I | 70.00 | 6.2 | 12.4 | 0.27 | 3+416.09 | 3+428.47 | 2.08 | 39.1 | 0.36 | Normativa 8% |
| C-86 | 3+490.34 | 9472574.10 | 611029.76 | 21.5 | I | 120.00 | 22.8 | 45.0 | 2.15 | 3+467.55 | 3+512.59 | 1.29 | 31.0 | 0.22 | Normativa 8% |
| C-87 | 3+548.39 | 9472520.06 | 611052.38 | 35.5 | I | 15.00 | 4.8 | 9.3 | 0.75 | 3+543.59 | 3+552.88 | 9.71 | 0.9 | 2.64 | Vuelta |
| C-88 | 3+563.57 | 9472511.90 | 611065.55 | 36.1 | D | 30.00 | 9.8 | 18.9 | 1.55 | 3+553.80 | 3+572.69 | 4.56 | 1.3 | 5.17 | Excepcional |
| C-89 | 3+582.80 | 9472493.49 | 611073.04 | 53.0 | D | 17.70 | 8.8 | 16.4 | 2.08 | 3+573.98 | 3+590.34 | 7.93 | 1.5 | 4.60 | Vuelta |
| C-90 | 3+610.17 | 9472468.89 | 611058.37 | 24.3 | D | 85.00 | 18.3 | 36.0 | 1.94 | 3+591.88 | 3+627.90 | 1.75 | 1.3 | 3.29 | Normativa 8% |
| C-91 | 3+643.24 | 9472449.66 | 611030.79 | 43.7 | D | 35.00 | 14.0 | 26.7 | 2.71 | 3+629.19 | 3+655.91 | 3.93 | 1.2 | 5.84 | Excepcional |
| C-92 | 3+668.20 | 9472453.71 | 611004.76 | 37.7 | D | 32.50 | 11.1 | 21.4 | 1.84 | 3+657.11 | 3+678.49 | 4.22 | 0.0 | 4.64 | Excepcional |
| C-93 | 3+680.66 | 9472463.34 | 610995.64 | 24.5 | I | 10.02 | 2.2 | 4.3 | 0.23 | 3+678.49 | 3+682.77 | - | 29.7 | 1.50 | Vuelta |
| C-94 | 3+723.62 | 9472479.48 | 610955.76 | 27.8 | I | 45.00 | 11.1 | 21.8 | 1.35 | 3+712.50 | 3+734.30 | 3.10 | 24.6 | 1.14 | Normativa 12% |
| C-95 | 3+773.33 | 9472474.50 | 610905.86 | 32.2 | D | 50.00 | 14.5 | 28.1 | 2.05 | 3+758.87 | 3+787.01 | 2.82 | 0.0 | 0.36 | Normativa 8% |
| C-96 | 3+834.25 | 9472502.06 | 610850.68 | 5.5 | D | 974.90 | 47.2 | 94.4 | 1.14 | 3+787.01 | 3+881.40 | 0.24 | -40.6 | 1.37 | Normativa 8% |
| C-97 | 3+846.68 | 9472508.71 | 610840.08 | 12.3 | I | 55.00 | 5.9 | 11.8 | 0.32 | 3+840.77 | 3+852.55 | 2.58 | -35.8 | 0.14 | Normativa 8% |
| C-98 | 3+868.92 | 9472516.26 | 610819.12 | 4.6 | D | 1304.58 | 52.2 | 104.3 | 1.04 | 3+816.74 | 3+921.03 | 0.20 | 0.0 | 1.01 | Normativa 8% |
| C-99 | 3+930.10 | 9472541.55 | 610763.34 | 14.8 | D | 70.00 | 9.1 | 18.0 | 0.59 | 3+921.03 | 3+939.07 | 2.08 | 0.6 | 0.27 | Normativa 8% |
| C-100 | 3+945.32 | 9472551.22 | 610751.47 | 31.7 | I | 20.00 | 5.7 | 11.0 | 0.79 | 3+939.65 | 3+950.70 | 6.91 | 11.8 | 0.60 | Vuelta |
| C-101 | 3+966.11 | 9472553.98 | 610730.57 | 9.1 | D | 45.00 | 3.6 | 7.2 | 0.14 | 3+962.52 | 3+969.68 | 3.10 | 17.1 | 0.24 | Normativa 12% |
| C-102 | 4+005.05 | 9472565.13 | 610693.24 | 24.2 | I | 85.00 | 18.2 | 35.9 | 1.93 | 3+986.82 | 4+022.74 | 1.75 | 14.1 | 0.23 | Normativa 8% |
| C-103 | 4+058.77 | 9472557.97 | 610639.45 | 23.2 | D | 106.70 | 21.9 | 43.2 | 2.22 | 4+036.87 | 4+080.07 | 1.43 | 14.4 | 1.44 | Normativa 8% |
| C-104 | 4+106.41 | 9472570.96 | 610592.99 | 29.6 | I | 45.00 | 11.9 | 23.3 | 1.55 | 4+094.51 | 4+117.77 | 3.10 | 57.6 | 0.83 | Normativa 12% |
| C-105 | 4+188.17 | 9472551.05 | 610513.15 | 31.8 | D | 45.00 | 12.8 | 25.0 | 1.79 | 4+175.36 | 4+200.32 | 3.10 | 8.0 | 0.94 | Normativa 12% |
| C-106 | 4+219.61 | 9472560.86 | 610482.58 | 28.2 | I | 45.00 | 11.3 | 22.1 | 1.40 | 4+208.30 | 4+230.45 | 3.10 | 1.8 | 0.51 | Normativa 12% |
| C-107 | 4+241.35 | 9472556.84 | 610460.74 | 22.9 | D | 44.89 | 9.1 | 17.9 | 0.91 | 4+232.26 | 4+250.19 | 3.11 | 0.0 | 0.25 | Excepcional |
| C-108 | 4+263.31 | 9472561.63 | 610439.07 | 93.2 | I | 12.40 | 13.1 | 20.2 | 5.65 | 4+250.19 | 4+270.36 | 12.90 | 12.1 | 1.46 | Vuelta |
| C-109 | 4+314.90 | 9472504.74 | 610429.79 | 89.7 | D | 32.60 | 32.4 | 51.0 | 13.38 | 4+282.47 | 4+333.50 | 4.21 | -0.0 | 0.90 | Excepcional |
| C-110 | 4+353.26 | 9472512.85 | 610378.25 | 27.8 | D | 80.00 | 19.8 | 38.8 | 2.41 | 4+333.47 | 4+372.27 | 1.84 | 31.0 | 0.38 | Normativa 8% |
| C-111 | 4+424.16 | 9472555.72 | 610320.80 | 45.3 | I | 50.00 | 20.9 | 39.6 | 4.19 | 4+403.27 | 4+442.84 | 2.82 | 0.0 | 1.48 | Normativa 8% |
| C-112 | 4+483.45 | 9472546.51 | 610260.01 | 4.1 | I | 1128.60 | 40.6 | 81.2 | 0.73 | 4+442.84 | 4+524.02 | 0.22 | -22.7 | 0.76 | Normativa 8% |
| C-113 | 4+509.61 | 9472540.74 | 610234.46 | 13.6 | D | 70.00 | 8.3 | 16.6 | 0.49 | 4+501.28 | 4+517.86 | 2.08 | 1.3 | 0.16 | Normativa 8% |
| C-114 | 4+525.42 | 9472540.97 | 610218.57 | 45.4 | I | 15.00 | 6.3 | 11.9 | 1.26 | 4+519.15 | 4+531.03 | 9.71 | 13.6 | 0.19 | Vuelta |
| C-115 | 4+554.75 | 9472519.93 | 610197.19 | 25.5 | D | 45.00 | 10.2 | 20.0 | 1.13 | 4+544.59 | 4+564.58 | 3.10 | 43.8 | 1.27 | Normativa 12% |
| C-116 | 4+608.79 | 9472502.14 | 610145.81 | 4.3 | I | 11.40 | 0.4 | 0.9 | 0.01 | 4+608.36 | 4+609.22 | 15.35 | -0.0 | 0.44 | Vuelta |
| C-117 | 4+611.69 | 9472500.99 | 610143.15 | 4.3 | D | 65.41 | 2.5 | 4.9 | 0.05 | 4+609.22 | 4+614.15 | 2.21 | 0.1 | 0.15 | Normativa 8% |
| C-118 | 4+614.64 | 9472500.02 | 610140.36 | 7.0 | I | 6.31 | 0.4 | 0.8 | 0.01 | 4+614.25 | 4+615.02 | - | 0.0 | 0.33 | Vuelta |
| C-119 | 4+615.46 | 9472499.66 | 610139.62 | 8.4 | D | 6.00 | 0.4 | 0.9 | 0.02 | 4+615.02 | 4+615.90 | - | 0.0 | 0.11 | Vuelta |
| C-120 | 4+616.58 | 9472499.32 | 610138.55 | 3.2 | D | 24.06 | 0.7 | 1.4 | 0.01 | 4+615.90 | 4+617.26 | 5.69 | 1.0 | 0.13 | Vuelta |
| C-121 | 4+645.42 | 9472492.11 | 610110.63 | 30.3 | I | 100.00 | 27.1 | 53.0 | 3.61 | 4+618.31 | 4+671.26 | 1.52 | -0.0 | 0.31 | Normativa 8% |
| C-122 | 4+684.86 | 9472463.42 | 610081.75 | 18.4 | I | 83.96 | 13.6 | 26.9 | 1.09 | 4+671.26 | 4+698.21 | 1.77 | 0.0 | 0.56 | Normativa 8% |
| C-123 | 4+708.54 | 9472442.07 | 610070.96 | 72.6 | D | 14.07 | 10.3 | 17.8 | 3.38 | 4+698.21 | 4+716.04 | 10.58 | 23.2 | 0.46 | Vuelta |
| C-124 | 4+747.64 | 9472448.89 | 610029.59 | 21.3 | I | 45.00 | 8.4 | 16.7 | 0.79 | 4+739.20 | 4+755.89 | 3.10 | 23.5 | 0.22 | Normativa 12% |
| C-125 | 4+797.64 | 9472438.54 | 609980.47 | 44.2 | D | 45.00 | 18.3 | 34.7 | 3.57 | 4+779.38 | 4+814.08 | 3.10 | 2.7 | 1.65 | Normativa 12% |
| C-126 | 4+835.70 | 9472459.84 | 609946.75 | 103.1 | I | 15.00 | 18.9 | 27.0 | 9.14 | 4+816.80 | 4+843.80 | 9.71 | 14.8 | 0.99 | Vuelta |
| C-127 | 4+887.87 | 9472400.34 | 609926.10 | 123.8 | D | 15.60 | 29.2 | 33.7 | 17.53 | 4+858.64 | 4+892.35 | 9.23 | 18.0 | 1.31 | Vuelta |
| C-128 | 4+918.41 | 9472444.46 | 609892.80 | 90.1 | I | 8.00 | 8.0 | 12.6 | 3.32 | 4+910.40 | 4+922.98 | - | 11.3 | 0.26 | Vuelta |
| C-129 | 4+940.46 | 9472429.06 | 609872.47 | 8.3 | D | 85.00 | 6.2 | 12.3 | 0.22 | 4+934.29 | 4+946.62 | 1.75 | 24.4 | 0.18 | Normativa 8% |
| C-130 | 4+979.40 | 9472410.27 | 609838.34 | 17.4 | I | 55.00 | 8.4 | 16.7 | 0.64 | 4+970.98 | 4+987.70 | 2.58 | 19.1 | 0.19 | Normativa 8% |
| C-131 | 5+019.43 | 9472381.26 | 609810.57 | 10.3 | D | 140.00 | 12.6 | 25.2 | 0.57 | 5+006.82 | 5+031.97 | 1.13 | 43.1 | 0.12 | Normativa 8% |
| C-132 | 5+078.60 | 9472346.47 | 609762.63 | 8.9 | D | 45.00 | 3.5 | 7.0 | 0.14 | 5+075.08 | 5+082.10 | 3.10 | 69.8 | 0.27 | Normativa 12% |
| C-133 | 5+169.81 | 9472305.03 | 609681.36 | 20.3 | D | 100.00 | 17.9 | 35.4 | 1.58 | 5+151.95 | 5+187.31 | 1.52 | 15.7 | 1.16 | Normativa 8% |
| C-134 | 5+210.31 | 9472300.22 | 609640.77 | 18.3 | I | 45.00 | 7.3 | 14.4 | 0.58 | 5+203.05 | 5+217.45 | 3.10 | 15.0 | 0.87 | Normativa 12% |
| C-135 | 5+245.82 | 9472285.11 | 609608.50 | 12.7 | D | 120.00 | 13.3 | 26.6 | 0.74 | 5+232.48 | 5+259.06 | 1.29 | 31.5 | 0.24 | Normativa 8% |
| C-136 | 5+303.10 | 9472272.78 | 609552.45 | 9.6 | I | 150.00 | 12.6 | 25.1 | 0.53 | 5+290.52 | 5+315.62 | 1.07 | 7.8 | 0.17 | Normativa 8% |
| C-137 | 5+326.88 | 9472263.85 | 609530.35 | 8.8 | D | 45.00 | 3.5 | 6.9 | 0.13 | 5+323.42 | 5+330.33 | 3.10 | 20.2 | 0.23 | Normativa 12% |
| C-138 | 5+355.91 | 9472257.22 | 609502.07 | 13.6 | I | 45.00 | 5.4 | 10.7 | 0.32 | 5+350.52 | 5+361.24 | 3.10 | 15.8 | 0.29 | Normativa 12% |
| C-139 | 5+379.31 | 9472246.63 | 609481.15 | 5.9 | D | 45.00 | 2.3 | 4.6 | 0.06 | 5+376.99 | 5+381.62 | 3.10 | -0.0 | 0.21 | Normativa 12% |
| C-140 | 5+442.78 | 9472223.93 | 609421.87 | 4.4 | D | 1589.09 | 61.2 | 122.3 | 1.18 | 5+381.62 | 5+503.88 | 0.17 | -13.7 | 1.29 | Normativa 8% |
| C-141 | 5+497.10 | 9472208.44 | 609369.74 | 17.6 | I | 45.00 | 7.0 | 13.8 | 0.53 | 5+490.14 | 5+503.95 | 3.10 | 36.8 | 0.68 | Normativa 12% |
| C-142 | 5+579.32 | 9472162.25 | 609301.59 | 48.8 | D | 85.00 | 38.6 | 72.4 | 8.34 | 5+540.75 | 5+613.17 | 1.75 | -4.7 | 0.63 | Normativa 8% |
| C-143 | 5+616.62 | 9472172.91 | 609260.94 | 30.0 | D | 30.42 | 8.1 | 15.9 | 1.07 | 5+608.48 | 5+624.39 | 4.50 | 0.0 | 0.88 | Excepcional |
| C-144 | 5+633.84 | 9472185.27 | 609248.42 | 21.4 | D | 50.00 | 9.5 | 18.7 | 0.89 | 5+624.39 | 5+643.07 | 2.82 | 84.4 | 0.21 | Normativa 8% |
| C-145 | 5+756.42 | 9472297.51 | 609198.60 | 80.4 | I | 34.20 | 28.9 | 48.0 | 10.58 | 5+727.51 | 5+775.51 | 4.02 | 22.1 | 0.42 | Excepcional |
| C-146 | 5+803.28 | 9472283.46 | 609143.68 | 14.3 | D | 45.00 | 5.7 | 11.3 | 0.35 | 5+797.62 | 5+808.88 | 3.10 | 4.7 | 0.48 | Normativa 12% |
| C-147 | 5+834.71 | 9472283.45 | 609112.20 | 82.6 | I | 24.00 | 21.1 | 34.6 | 7.94 | 5+813.62 | 5+848.22 | 5.70 | 63.6 | 1.09 | Vuelta |
| C-148 | 5+917.80 | 9472193.54 | 609100.53 | 13.5 | D | 50.00 | 5.9 | 11.8 | 0.35 | 5+911.87 | 5+923.69 | 2.82 | -0.0 | 0.47 | Normativa 8% |
| C-149 | 5+959.87 | 9472154.20 | 609085.48 | 8.5 | D | 487.28 | 36.2 | 72.2 | 1.34 | 5+923.69 | 5+995.93 | 0.41 | -0.0 | 1.36 | Normativa 8% |
| C-150 | 6+011.90 | 9472108.78 | 609059.84 | 12.1 | D | 150.34 | 16.0 | 31.8 | 0.85 | 5+995.93 | 6+027.75 | 1.07 | 34.7 | 0.32 | Normativa 8% |
| C-151 | 6+080.24 | 9472057.55 | 609014.42 | 22.3 | I | 90.00 | 17.8 | 35.1 | 1.74 | 6+062.47 | 6+097.56 | 1.66 | 59.3 | 0.70 | Normativa 8% |
| C-152 | 6+193.17 | 9471950.49 | 608977.09 | 48.8 | D | 80.00 | 36.3 | 68.1 | 7.84 | 6+156.90 | 6+225.01 | 1.84 | 7.5 | 0.88 | Normativa 8% |
| C-153 | 6+242.01 | 9471930.53 | 608927.71 | 23.8 | I | 45.00 | 9.5 | 18.7 | 0.99 | 6+232.50 | 6+251.23 | 3.10 | 22.0 | 0.59 | Normativa 12% |
| C-154 | 6+276.72 | 9471905.42 | 608903.34 | 8.9 | D | 45.00 | 3.5 | 7.0 | 0.14 | 6+273.20 | 6+280.22 | 3.10 | 41.0 | 0.26 | Normativa 12% |
| C-155 | 6+325.89 | 9471875.88 | 608864.01 | 11.8 | D | 45.00 | 4.7 | 9.3 | 0.24 | 6+321.23 | 6+330.52 | 3.10 | 0.8 | 0.32 | Normativa 12% |
| C-156 | 6+345.21 | 9471867.67 | 608846.49 | 14.4 | I | 110.00 | 13.9 | 27.6 | 0.87 | 6+331.35 | 6+358.92 | 1.40 | 18.3 | 0.26 | Normativa 8% |
| C-157 | 6+384.16 | 9471842.83 | 608816.30 | 14.4 | D | 55.00 | 6.9 | 13.8 | 0.44 | 6+377.22 | 6+391.02 | 2.58 | 36.8 | 0.54 | Normativa 8% |
| C-158 | 6+463.70 | 9471809.09 | 608744.19 | 77.1 | D | 45.00 | 35.9 | 60.6 | 12.56 | 6+427.81 | 6+488.40 | 3.10 | 35.9 | 1.93 | Normativa 12% |
| C-159 | 6+555.26 | 9471890.13 | 608681.03 | 26.8 | D | 130.00 | 31.0 | 60.9 | 3.64 | 6+524.27 | 6+585.13 | 1.21 | 10.4 | 0.94 | Normativa 8% |
| C-160 | 6+601.50 | 9471936.61 | 608671.90 | 15.1 | I | 44.69 | 5.9 | 11.8 | 0.39 | 6+595.57 | 6+607.36 | 3.12 | -2.0 | 0.29 | Excepcional |
| C-161 | 6+727.32 | 9472049.55 | 608616.27 | 168.7 | I | 12.04 | 121.9 | 35.5 | 110.48 | 6+605.39 | 6+640.85 | 13.63 | 0.0 | 1.46 | Vuelta |
| C-162 | 6+643.46 | 9471929.22 | 608648.38 | 16.1 | I | 18.40 | 2.6 | 5.2 | 0.18 | 6+640.85 | 6+646.03 | 7.58 | 4.8 | 0.15 | Vuelta |
| C-163 | 6+660.78 | 9471914.36 | 608657.34 | 25.0 | D | 45.00 | 10.0 | 19.7 | 1.09 | 6+650.79 | 6+670.44 | 3.10 | 26.1 | 0.39 | Normativa 12% |
| C-164 | 6+705.15 | 9471869.91 | 608662.04 | 32.1 | I | 30.00 | 8.6 | 16.8 | 1.21 | 6+696.53 | 6+713.32 | 4.56 | 0.0 | 0.66 | Excepcional |
| C-165 | 6+721.39 | 9471856.78 | 608672.34 | 27.4 | D | 33.14 | 8.1 | 15.8 | 0.97 | 6+713.32 | 6+729.14 | 4.14 | 52.4 | 0.21 | Excepcional |
| C-166 | 6+789.20 | 9471789.86 | 608685.06 | 41.9 | D | 20.00 | 7.7 | 14.6 | 1.41 | 6+781.54 | 6+796.16 | 6.91 | 0.0 | 0.72 | Vuelta |
| C-167 | 6+807.73 | 9471773.41 | 608675.12 | 107.5 | D | 8.48 | 11.6 | 15.9 | 5.86 | 6+796.16 | 6+812.08 | - | 9.4 | 0.51 | Vuelta |
| C-168 | 6+837.50 | 9471801.16 | 608650.67 | 32.4 | I | 55.00 | 16.0 | 31.1 | 2.28 | 6+821.51 | 6+852.63 | 2.58 | 14.5 | 0.42 | Normativa 8% |
| C-169 | 6+874.74 | 9471811.79 | 608614.09 | 56.8 | I | 13.97 | 7.6 | 13.9 | 1.91 | 6+867.18 | 6+881.04 | 10.69 | -0.0 | 0.71 | Vuelta |
| C-170 | 6+886.72 | 9471803.16 | 608604.03 | 19.0 | I | 34.00 | 5.7 | 11.3 | 0.47 | 6+881.04 | 6+892.31 | 4.04 | 24.1 | 0.25 | Excepcional |
| C-171 | 6+930.82 | 9471765.02 | 608581.69 | 45.2 | I | 34.50 | 14.4 | 27.2 | 2.87 | 6+916.45 | 6+943.69 | 3.99 | 1.0 | 0.47 | Excepcional |
| C-172 | 6+973.33 | 9471722.48 | 608592.99 | 55.1 | D | 55.00 | 28.7 | 52.9 | 7.03 | 6+944.66 | 6+997.52 | 2.58 | 20.3 | 0.50 | Normativa 8% |
| C-173 | 7+035.21 | 9471671.78 | 608550.16 | 30.0 | D | 65.00 | 17.4 | 34.0 | 2.29 | 7+017.80 | 7+051.82 | 2.22 | 26.1 | 0.40 | Normativa 8% |
| C-174 | 7+118.48 | 9471643.28 | 608471.08 | 90.7 | D | 40.00 | 40.5 | 63.3 | 16.93 | 7+077.96 | 7+141.31 | 3.47 | 27.0 | 1.02 | Excepcional |
| C-175 | 7+170.85 | 9471709.49 | 608448.16 | 45.7 | D | 6.00 | 2.5 | 4.8 | 0.51 | 7+168.33 | 7+173.11 | - | 0.0 | 1.08 | Vuelta |
| C-176 | 7+178.55 | 9471716.61 | 608451.72 | 71.7 | I | 7.52 | 5.4 | 9.4 | 1.76 | 7+173.11 | 7+182.52 | - | 0.4 | 5.24 | Vuelta |
| C-177 | 7+196.92 | 9471730.60 | 608437.67 | 112.4 | I | 9.40 | 14.0 | 18.4 | 7.50 | 7+182.88 | 7+201.32 | - | 1.1 | 5.64 | Vuelta |
| C-178 | 7+219.92 | 9471700.43 | 608425.20 | 30.1 | I | 65.00 | 17.5 | 34.1 | 2.31 | 7+202.45 | 7+236.58 | 2.22 | 7.8 | 2.84 | Normativa 8% |
| C-179 | 7+245.30 | 9471674.48 | 608428.67 | 6.9 | I | 15.00 | 0.9 | 1.8 | 0.03 | 7+244.40 | 7+246.20 | 9.71 | 0.0 | 2.86 | Vuelta |
| C-180 | 7+253.38 | 9471666.66 | 608430.70 | 19.2 | I | 42.46 | 7.2 | 14.2 | 0.60 | 7+246.20 | 7+260.42 | 3.28 | 79.2 | 0.62 | Excepcional |
| C-181 | 7+340.80 | 9471593.81 | 608479.26 | 17.1 | I | 8.00 | 1.2 | 2.4 | 0.09 | 7+339.59 | 7+341.99 | - | 1.7 | 2.08 | Vuelta |
| C-182 | 7+375.25 | 9471572.04 | 608505.99 | 151.7 | D | 7.97 | 31.6 | 21.1 | 24.60 | 7+343.68 | 7+364.77 | - | 0.0 | 0.56 | Vuelta |
| C-183 | 7+373.80 | 9471579.67 | 608466.11 | 42.9 | D | 23.00 | 9.0 | 17.2 | 1.71 | 7+364.77 | 7+381.98 | 5.96 | 17.0 | 0.43 | Vuelta |
| C-184 | 7+420.99 | 9471618.39 | 608437.67 | 29.0 | I | 85.00 | 22.0 | 43.1 | 2.80 | 7+398.98 | 7+442.06 | 1.75 | 0.0 | 0.38 | Normativa 8% |
| C-185 | 7+450.89 | 9471631.25 | 608409.63 | 63.3 | I | 14.34 | 8.8 | 15.8 | 2.50 | 7+442.06 | 7+457.89 | 10.31 | 0.0 | 0.21 | Vuelta |
| C-186 | 7+478.46 | 9471612.91 | 608386.66 | 28.3 | I | 81.63 | 20.6 | 40.3 | 2.55 | 7+457.89 | 7+498.18 | 1.81 | 2.4 | 1.19 | Normativa 8% |
| C-187 | 7+538.47 | 9471556.94 | 608362.77 | 86.9 | D | 40.00 | 37.9 | 60.6 | 15.08 | 7+500.60 | 7+561.25 | 3.47 | 5.0 | 0.51 | Excepcional |
| C-188 | 7+567.79 | 9471572.11 | 608321.04 | 19.3 | I | 8.89 | 1.5 | 3.0 | 0.13 | 7+566.27 | 7+569.27 | - | -0.2 | 0.63 | Vuelta |
| C-189 | 7+587.70 | 9471572.34 | 608301.10 | 133.6 | I | 7.97 | 18.6 | 18.6 | 12.26 | 7+569.11 | 7+587.69 | - | 0.0 | 0.57 | Vuelta |
| C-190 | 7+594.33 | 9471553.87 | 608318.29 | 36.7 | I | 20.00 | 6.6 | 12.8 | 1.07 | 7+587.69 | 7+600.51 | 6.91 | 23.2 | 0.33 | Vuelta |
| C-191 | 7+649.28 | 9471543.95 | 608372.80 | 54.1 | I | 50.00 | 25.5 | 47.2 | 6.15 | 7+623.74 | 7+670.97 | 2.82 | 9.6 | 0.94 | Normativa 8% |
| C-192 | 7+695.89 | 9471578.88 | 608409.22 | 106.8 | D | 11.40 | 15.3 | 21.2 | 7.72 | 7+680.55 | 7+701.79 | 15.35 | -0.0 | 0.27 | Vuelta |
| C-193 | 7+708.73 | 9471559.04 | 608419.34 | 20.1 | D | 39.20 | 6.9 | 13.7 | 0.61 | 7+701.79 | 7+715.52 | 3.53 | 9.7 | 0.13 | Excepcional |
| C-194 | 7+752.46 | 9471515.48 | 608424.65 | 25.6 | I | 120.00 | 27.2 | 53.5 | 3.05 | 7+725.25 | 7+778.77 | 1.29 | 24.1 | 0.99 | Normativa 8% |
| C-195 | 7+850.67 | 9471431.88 | 608477.90 | 149.4 | D | 13.10 | 47.8 | 34.1 | 36.48 | 7+802.86 | 7+837.00 | 11.77 | 0.8 | 1.48 | Vuelta |
| C-196 | 7+838.84 | 9471454.32 | 608433.60 | 10.5 | I | 10.80 | 1.0 | 2.0 | 0.05 | 7+837.85 | 7+839.83 | 18.20 | -0.0 | 0.32 | Vuelta |
| C-197 | 7+840.47 | 9471454.78 | 608432.04 | 9.1 | D | 8.02 | 0.6 | 1.3 | 0.03 | 7+839.83 | 7+841.11 | - | -0.0 | 0.23 | Vuelta |
| C-198 | 7+843.14 | 9471455.93 | 608429.63 | 4.8 | I | 48.12 | 2.0 | 4.1 | 0.04 | 7+841.11 | 7+845.17 | 2.92 | 55.9 | 1.00 | Normativa 12% |
| C-199 | 7+917.53 | 9471482.20 | 608360.03 | 83.8 | I | 18.30 | 16.4 | 26.8 | 6.29 | 7+901.09 | 7+927.87 | 7.63 | 21.6 | 1.02 | Vuelta |
| C-200 | 7+967.37 | 9471432.29 | 608334.78 | 71.2 | D | 25.00 | 17.9 | 31.1 | 5.75 | 7+949.46 | 7+980.54 | 5.47 | 5.5 | 0.40 | Excepcional |
| C-201 | 7+989.78 | 9471436.09 | 608307.91 | 9.5 | I | 45.00 | 3.7 | 7.5 | 0.15 | 7+986.04 | 7+993.50 | 3.10 | 7.5 | 0.15 | Normativa 12% |
| C-202 | 8+001.83 | 9471435.79 | 608295.84 | 2.0 | D | 45.00 | 0.8 | 1.6 | 0.01 | 8+001.05 | 8+002.61 | 3.10 | 25.9 | 0.02 | Normativa 12% |
| C-203 | 8+035.31 | 9471436.11 | 608262.36 | 10.4 | I | 75.00 | 6.8 | 13.6 | 0.31 | 8+028.51 | 8+042.06 | 1.95 | 56.4 | 0.67 | Normativa 8% |
| C-204 | 8+104.77 | 9471424.26 | 608193.88 | 15.9 | D | 45.00 | 6.3 | 12.5 | 0.43 | 8+098.50 | 8+110.96 | 3.10 | 0.0 | 0.64 | Normativa 12% |
| C-205 | 8+137.35 | 9471427.71 | 608161.41 | 97.1 | D | 23.32 | 26.4 | 39.5 | 11.90 | 8+110.96 | 8+150.47 | 5.87 | 23.8 | 1.22 | Vuelta |
| C-206 | 8+190.37 | 9471492.27 | 608176.44 | 56.5 | I | 30.00 | 16.1 | 29.6 | 4.05 | 8+174.26 | 8+203.82 | 4.56 | 30.5 | 0.47 | Excepcional |
| C-207 | 8+239.02 | 9471529.57 | 608141.23 | 11.8 | D | 45.00 | 4.7 | 9.3 | 0.24 | 8+234.36 | 8+243.64 | 3.10 | 6.0 | 0.30 | Normativa 12% |
| C-208 | 8+257.71 | 9471545.53 | 608131.44 | 22.8 | I | 40.00 | 8.1 | 15.9 | 0.81 | 8+249.63 | 8+265.57 | 3.47 | 1.0 | 0.53 | Excepcional |
| C-209 | 8+277.59 | 9471557.24 | 608115.10 | 27.5 | D | 45.00 | 11.0 | 21.6 | 1.32 | 8+266.60 | 8+288.17 | 3.10 | -0.0 | 0.21 | Normativa 12% |
| C-210 | 8+310.44 | 9471586.91 | 608100.04 | 10.1 | D | 251.68 | 22.3 | 44.4 | 0.98 | 8+288.17 | 8+332.60 | 0.69 | -0.0 | 1.03 | Normativa 8% |
| C-211 | 8+334.54 | 9471610.09 | 608093.05 | 14.3 | I | 15.47 | 1.9 | 3.9 | 0.12 | 8+332.60 | 8+336.46 | 9.33 | 36.6 | 1.34 | Vuelta |
| C-212 | 8+385.37 | 9471653.65 | 608066.81 | 27.6 | D | 50.00 | 12.3 | 24.1 | 1.49 | 8+373.09 | 8+397.17 | 2.82 | 15.6 | 0.28 | Normativa 8% |
| C-213 | 8+429.26 | 9471697.94 | 608064.12 | 59.2 | I | 29.10 | 16.5 | 30.1 | 4.36 | 8+412.74 | 8+442.79 | 4.70 | 40.6 | 0.47 | Excepcional |
| C-214 | 8+502.06 | 9471732.77 | 607996.81 | 63.8 | D | 30.00 | 18.7 | 33.4 | 5.34 | 8+483.39 | 8+516.79 | 4.56 | 31.1 | 0.55 | Excepcional |
| C-215 | 8+554.83 | 9471789.46 | 607997.95 | 22.3 | I | 35.00 | 6.9 | 13.6 | 0.67 | 8+547.93 | 8+561.55 | 3.93 | 0.4 | 0.42 | Excepcional |
| C-216 | 8+573.73 | 9471807.26 | 607991.07 | 29.3 | D | 45.00 | 11.7 | 23.0 | 1.51 | 8+561.98 | 8+584.96 | 3.10 | 21.0 | 0.45 | Normativa 12% |
| C-217 | 8+618.85 | 9471852.43 | 607997.51 | 56.2 | I | 24.10 | 12.9 | 23.6 | 3.21 | 8+605.99 | 8+629.61 | 5.68 | 1.3 | 1.04 | Vuelta |
| C-218 | 8+652.88 | 9471876.58 | 607970.65 | 40.3 | D | 60.00 | 22.0 | 42.2 | 3.91 | 8+630.88 | 8+673.05 | 2.39 | 37.9 | 0.72 | Normativa 8% |
| C-219 | 8+721.25 | 9471946.14 | 607961.16 | 69.0 | I | 15.00 | 10.3 | 18.1 | 3.20 | 8+710.95 | 8+729.01 | 9.71 | 10.2 | 0.64 | Vuelta |
| C-220 | 8+752.06 | 9471953.79 | 607928.69 | 32.0 | D | 45.00 | 12.9 | 25.1 | 1.81 | 8+739.18 | 8+764.28 | 3.10 | 14.2 | 0.78 | Normativa 12% |
| C-221 | 8+800.84 | 9471988.89 | 607893.86 | 138.0 | I | 8.60 | 22.4 | 20.7 | 15.40 | 8+778.44 | 8+799.15 | - | 0.0 | 1.14 | Vuelta |
| C-222 | 8+807.20 | 9471958.47 | 607895.33 | 36.7 | I | 24.30 | 8.1 | 15.6 | 1.30 | 8+799.15 | 8+814.70 | 5.63 | 26.4 | 0.64 | Vuelta |
| C-223 | 8+854.73 | 9471921.34 | 607925.88 | 68.6 | D | 20.00 | 13.6 | 23.9 | 4.21 | 8+841.09 | 8+865.03 | 6.91 | 17.6 | 0.48 | Vuelta |
| C-224 | 8+906.65 | 9471873.08 | 607898.97 | 62.6 | I | 39.59 | 24.0 | 43.2 | 6.73 | 8+882.60 | 8+925.82 | 3.50 | 0.0 | 0.73 | Excepcional |
| C-225 | 9+011.02 | 9471781.88 | 607959.13 | 169.3 | D | 8.00 | 85.2 | 23.6 | 77.58 | 8+925.82 | 8+949.45 | - | 18.4 | 1.04 | Vuelta |
| C-226 | 8+981.79 | 9471866.23 | 607877.28 | 50.7 | D | 29.40 | 13.9 | 26.0 | 3.13 | 8+967.86 | 8+993.87 | 4.65 | 10.1 | 0.90 | Excepcional |
| C-227 | 9+014.86 | 9471900.92 | 607881.25 | 88.5 | I | 11.20 | 10.9 | 17.3 | 4.44 | 9+003.95 | 9+021.25 | 16.08 | 33.5 | 0.65 | Vuelta |
| C-228 | 9+084.96 | 9471911.35 | 607807.37 | 67.8 | D | 45.00 | 30.2 | 53.2 | 9.20 | 9+054.75 | 9+107.96 | 3.10 | 7.1 | 0.94 | Normativa 12% |
| C-229 | 9+128.51 | 9471960.55 | 607794.90 | 113.0 | I | 8.90 | 13.5 | 17.6 | 7.23 | 9+115.05 | 9+132.61 | - | 23.2 | 0.76 | Vuelta |
| C-230 | 9+159.84 | 9471935.93 | 607762.51 | 40.8 | I | 10.74 | 4.0 | 7.7 | 0.72 | 9+155.85 | 9+163.50 | 18.64 | 0.0 | 0.47 | Vuelta |
| C-231 | 9+205.30 | 9471891.12 | 607753.03 | 93.0 | I | 39.70 | 41.8 | 64.4 | 17.95 | 9+163.50 | 9+227.91 | 3.49 | 16.9 | 0.65 | Excepcional |
| C-232 | 9+266.49 | 9471878.56 | 607832.43 | 120.4 | D | 12.40 | 21.7 | 26.1 | 12.56 | 9+244.82 | 9+270.89 | 12.90 | 12.1 | 1.13 | Vuelta |
| C-233 | 9+303.08 | 9471836.95 | 607798.23 | 63.9 | I | 32.20 | 20.1 | 35.9 | 5.74 | 9+283.02 | 9+318.90 | 4.26 | 6.3 | 0.40 | Excepcional |
| C-234 | 9+334.66 | 9471804.34 | 607813.04 | 23.8 | D | 45.00 | 9.5 | 18.7 | 0.99 | 9+325.16 | 9+343.89 | 3.10 | 4.5 | 0.42 | Normativa 12% |
| C-235 | 9+358.36 | 9471780.36 | 607813.29 | 25.0 | I | 45.00 | 10.0 | 19.6 | 1.09 | 9+348.39 | 9+368.02 | 3.10 | 17.7 | 0.21 | Normativa 12% |
| C-236 | 9+387.55 | 9471753.76 | 607826.04 | 4.0 | D | 53.35 | 1.9 | 3.7 | 0.03 | 9+385.68 | 9+389.41 | 2.65 | 0.0 | 0.14 | Normativa 8% |
| C-237 | 9+426.68 | 9471717.37 | 607840.44 | 154.9 | D | 8.30 | 37.3 | 22.4 | 29.88 | 9+389.41 | 9+411.85 | - | 17.6 | 1.68 | Vuelta |
| C-238 | 9+447.40 | 9471767.31 | 607787.43 | 43.5 | D | 44.98 | 17.9 | 34.1 | 3.45 | 9+429.46 | 9+463.60 | 3.11 | 0.0 | 1.25 | Normativa 12% |
| C-239 | 9+466.96 | 9471788.57 | 607786.24 | 27.9 | I | 13.50 | 3.4 | 6.6 | 0.41 | 9+463.60 | 9+470.18 | 11.24 | 30.9 | 0.38 | Vuelta |
| C-240 | 9+517.37 | 9471831.83 | 607760.09 | 96.0 | I | 14.70 | 16.3 | 24.6 | 7.27 | 9+501.04 | 9+525.68 | 9.97 | -2.1 | 1.34 | Vuelta |
| C-241 | 9+563.76 | 9471798.96 | 607716.73 | 46.3 | D | 93.92 | 40.1 | 75.9 | 8.22 | 9+523.61 | 9+599.49 | 1.60 | -0.0 | 0.64 | Normativa 8% |
| C-242 | 9+623.58 | 9471809.13 | 607653.30 | 57.6 | D | 43.80 | 24.1 | 44.1 | 6.19 | 9+599.49 | 9+643.55 | 3.18 | 12.0 | 0.79 | Excepcional |
| C-243 | 9+670.81 | 9471856.32 | 607633.02 | 55.0 | I | 29.30 | 15.2 | 28.1 | 3.73 | 9+655.58 | 9+683.68 | 4.67 | 17.7 | 0.66 | Excepcional |
| C-244 | 9+719.73 | 9471866.80 | 607582.82 | 13.5 | D | 154.75 | 18.3 | 36.4 | 1.08 | 9+701.42 | 9+737.87 | 1.04 | 0.0 | 0.99 | Normativa 8% |
| C-245 | 9+751.83 | 9471880.59 | 607553.65 | 61.2 | D | 23.60 | 14.0 | 25.2 | 3.82 | 9+737.87 | 9+763.08 | 5.80 | 15.5 | 0.71 | Vuelta |
| C-246 | 9+807.38 | 9471938.74 | 607550.09 | 146.4 | I | 8.70 | 28.8 | 22.2 | 21.42 | 9+778.55 | 9+800.78 | - | 18.8 | 0.76 | Vuelta |
| C-247 | 9+841.54 | 9471878.52 | 607515.21 | 82.7 | I | 25.00 | 22.0 | 36.1 | 8.30 | 9+819.55 | 9+855.62 | 5.47 | 1.1 | 0.47 | Excepcional |
| C-248 | 9+874.91 | 9471853.44 | 607548.00 | 50.6 | D | 38.40 | 18.2 | 33.9 | 4.08 | 9+856.75 | 9+890.69 | 3.60 | 26.2 | 0.32 | Excepcional |
| C-249 | 9+943.67 | 9471782.33 | 607550.43 | 14.4 | I | 211.33 | 26.8 | 53.3 | 1.69 | 9+916.89 | 9+970.17 | 0.80 | -0.0 | 0.99 | Normativa 8% |
| C-250 | 10+000.99 | 9471727.07 | 607566.69 | 68.8 | I | 45.00 | 30.8 | 54.1 | 9.54 | 9+970.17 | 10+024.22 | 3.10 | 6.2 | 0.90 | Normativa 12% |
| C-251 | 10+057.44 | 9471721.73 | 607630.51 | 13.4 | I | 229.40 | 27.0 | 53.8 | 1.59 | 10+030.41 | 10+084.22 | 0.75 | 0.0 | 1.41 | Normativa 8% |
| C-252 | 10+085.50 | 9471725.99 | 607658.50 | 19.2 | I | 7.51 | 1.3 | 2.5 | 0.11 | 10+084.22 | 10+086.74 | - | -0.0 | 0.96 | Vuelta |
| C-253 | 10+091.53 | 9471728.83 | 607663.85 | 73.6 | D | 6.40 | 4.8 | 8.2 | 1.59 | 10+086.74 | 10+094.96 | - | -0.0 | 1.87 | Vuelta |
| C-254 | 10+109.36 | 9471715.10 | 607677.25 | 54.4 | D | 28.02 | 14.4 | 26.6 | 3.48 | 10+094.96 | 10+121.56 | 4.88 | -0.0 | 1.59 | Excepcional |
| C-255 | 10+124.83 | 9471697.71 | 607674.16 | 12.9 | I | 28.83 | 3.3 | 6.5 | 0.18 | 10+121.56 | 10+128.07 | 4.74 | 56.0 | 1.99 | Excepcional |
| C-256 | 10+185.96 | 9471636.63 | 607677.21 | 21.7 | D | 10.10 | 1.9 | 3.8 | 0.18 | 10+184.02 | 10+187.85 | - | 1.5 | 0.60 | Vuelta |
| C-257 | 10+225.90 | 9471598.79 | 607664.28 | 67.2 | I | 55.00 | 36.6 | 64.6 | 11.05 | 10+189.32 | 10+253.88 | 2.58 | 1.5 | 1.54 | Normativa 8% |
| C-258 | 10+259.16 | 9471570.99 | 607695.58 | 39.6 | D | 10.60 | 3.8 | 7.3 | 0.67 | 10+255.35 | 10+262.68 | 20.37 | -0.0 | 1.25 | Vuelta |
| C-259 | 10+281.05 | 9471549.06 | 607698.96 | 132.3 | D | 8.13 | 18.4 | 18.8 | 11.96 | 10+262.68 | 10+281.44 | - | -0.4 | 0.82 | Vuelta |
| C-260 | 10+302.69 | 9471570.91 | 607665.92 | 39.6 | D | 60.00 | 21.6 | 41.5 | 3.77 | 10+281.09 | 10+322.55 | 2.39 | 57.0 | 0.80 | Normativa 8% |
| C-261 | 10+391.29 | 9471657.34 | 607639.62 | 20.5 | D | 65.00 | 11.7 | 23.2 | 1.05 | 10+379.54 | 10+402.78 | 2.22 | 7.7 | 0.33 | Normativa 8% |
| C-262 | 10+419.87 | 9471686.11 | 607641.42 | 74.0 | I | 12.40 | 9.3 | 16.0 | 3.13 | 10+410.53 | 10+426.54 | 12.90 | 4.6 | 0.51 | Vuelta |
| C-263 | 10+453.60 | 9471698.31 | 607607.12 | 53.0 | I | 45.00 | 22.4 | 41.6 | 5.29 | 10+431.16 | 10+472.80 | 3.10 | -0.0 | 2.00 | Normativa 12% |
| C-264 | 10+477.15 | 9471683.55 | 607584.76 | 11.9 | D | 41.61 | 4.3 | 8.7 | 0.23 | 10+472.80 | 10+481.47 | 3.34 | 28.8 | 0.28 | Excepcional |
| C-265 | 10+591.04 | 9471641.79 | 607478.77 | 98.1 | D | 70.00 | 80.7 | 119.9 | 36.85 | 10+510.31 | 10+630.21 | 2.08 | 32.7 | 2.92 | Normativa 8% |
| C-266 | 10+674.17 | 9471763.10 | 607449.96 | 28.0 | I | 45.00 | 11.2 | 22.0 | 1.37 | 10+662.96 | 10+684.92 | 3.10 | 33.2 | 0.52 | Normativa 12% |
| C-267 | 10+744.43 | 9471816.20 | 607403.26 | 38.6 | D | 75.00 | 26.3 | 50.5 | 4.47 | 10+718.15 | 10+768.70 | 1.95 | 28.8 | 1.26 | Normativa 8% |
| C-268 | 10+823.05 | 9471896.74 | 607399.45 | 54.1 | D | 50.00 | 25.5 | 47.2 | 6.14 | 10+797.53 | 10+844.72 | 2.82 | 7.0 | 0.48 | Normativa 8% |
| C-269 | 10+856.98 | 9471920.32 | 607428.95 | 13.4 | I | 45.00 | 5.3 | 10.6 | 0.31 | 10+851.68 | 10+862.24 | 3.10 | 17.7 | 0.33 | Normativa 12% |
| C-270 | 10+895.60 | 9471950.83 | 607452.72 | 22.2 | D | 80.00 | 15.7 | 31.0 | 1.52 | 10+879.92 | 10+910.89 | 1.84 | 42.2 | 0.31 | Normativa 8% |
| C-271 | 10+960.04 | 9471983.14 | 607508.92 | 44.7 | I | 17.00 | 7.0 | 13.3 | 1.38 | 10+953.05 | 10+966.31 | 8.31 | 6.4 | 0.18 | Vuelta |
| C-272 | 10+979.99 | 9472003.07 | 607514.41 | 18.5 | D | 45.00 | 7.3 | 14.5 | 0.59 | 10+972.67 | 10+987.20 | 3.10 | 23.7 | 0.61 | Normativa 12% |
| C-273 | 11+028.04 | 9472043.05 | 607541.28 | 37.9 | I | 50.00 | 17.2 | 33.1 | 2.86 | 11+010.87 | 11+043.94 | 2.82 | 0.0 | 1.13 | Normativa 8% |
| C-274 | 11+059.34 | 9472075.53 | 607539.02 | 105.8 | I | 11.65 | 15.4 | 21.5 | 7.66 | 11+043.94 | 11+065.45 | 14.58 | 17.4 | 1.00 | Vuelta |
| C-275 | 11+098.06 | 9472059.31 | 607493.84 | 37.4 | D | 45.00 | 15.2 | 29.4 | 2.51 | 11+082.84 | 11+112.20 | 3.10 | 70.2 | 0.96 | Normativa 12% |
| C-276 | 11+217.48 | 9472095.79 | 607378.98 | 56.7 | D | 65.00 | 35.1 | 64.3 | 8.86 | 11+182.40 | 11+246.74 | 2.22 | 1.8 | 0.48 | Normativa 8% |
| C-277 | 11+265.44 | 9472147.58 | 607364.46 | 34.1 | I | 55.00 | 16.9 | 32.8 | 2.53 | 11+248.56 | 11+281.33 | 2.58 | 38.2 | 0.70 | Normativa 8% |
| C-278 | 11+330.15 | 9472189.99 | 607314.27 | 11.0 | D | 110.00 | 10.6 | 21.1 | 0.51 | 11+319.56 | 11+340.67 | 1.40 | 1.0 | 0.17 | Normativa 8% |
| C-279 | 11+356.43 | 9472210.52 | 607297.76 | 14.1 | I | 120.00 | 14.8 | 29.5 | 0.91 | 11+341.62 | 11+371.08 | 1.29 | 39.5 | 0.47 | Normativa 8% |
| C-280 | 11+413.07 | 9472244.80 | 607252.48 | 5.8 | D | 50.00 | 2.5 | 5.0 | 0.06 | 11+410.56 | 11+415.58 | 2.82 | 21.5 | 0.41 | Normativa 8% |
| C-281 | 11+445.21 | 9472266.68 | 607228.93 | 9.3 | I | 100.00 | 8.1 | 16.2 | 0.33 | 11+437.09 | 11+453.30 | 1.52 | 8.1 | 0.11 | Normativa 8% |
| C-282 | 11+464.85 | 9472277.57 | 607212.54 | 10.0 | D | 40.00 | 3.5 | 7.0 | 0.15 | 11+461.36 | 11+468.34 | 3.47 | 4.6 | 0.12 | Excepcional |

# Anexo B. Archivos entregados

- `EJE_DG2018_circular.xml`: eje en LandXML 1.2 para importar en Civil 3D (IMPORTLANDXML).
- `EJE_DG2018_circular_curvas.csv`: tabla de curvas con observaciones detalladas por curva.
- `EJE_DG2018_circular_PI_PNEZD.csv` y `EJE_DG2018_circular_PI_polilinea.scr`: PIs como puntos y como polilínea de AutoCAD.
- `EJE_DG2018_circular_planta.svg` y `.png`: croquis de planta con el trazo actual y el eje coloreado por clase de curva.
- `DG2018_Corregido_2.xml`: archivo de criterios de diseño DG-2018 para Civil 3D.
- `EJE_DG2018_clotoides.xml`: variante con clotoides de 40 m en las 5 curvas donde caben.
