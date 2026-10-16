---
title: "Memoria de diseño geométrico en planta"
subtitle: "Eje EJE DG2018 V40 CIRCULAR, ajustado al trazo existente según el Manual de Carreteras: Diseño Geométrico DG-2018"
date: "16/10/2026"
lang: es
---

# 1. Objeto y alcance

Este documento describe el eje en planta contenido en el archivo `EJE_DG2018_circular.xml` (LandXML 1.2, alineamiento "EJE DG2018 V40 CIRCULAR", longitud 11,482.58 m), obtenido a partir de la poligonal del trazo existente `PROCESAMIENTO DISEÑO GEOMETRICO` (11,491.71 m, 1181 vértices, UTM WGS84 zona 17 Sur), y contrasta cada parámetro adoptado con lo que exige el Manual de Carreteras: Diseño Geométrico DG-2018 (MTC, revisada y corregida a enero de 2018).

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
| Radio mínimo con peralte normal 8 % | 50 m | Tabla 302.02, área rural plana u ondulada: "40 km/h, 8.00 %, 0.17, 50.4 m, 50 m". | Tabla 302.02 | 79 curvas (28 %) tienen R ≥ 50 m y pueden peraltarse con 8 %. |
| Radio excepcional | 25 m ≤ R < 45 m | La DG-2018 no define un radio mínimo excepcional para carreteras de Segunda Clase. Se adopta el radio mínimo de la fila de 30 km/h de la Tabla 302.02: "30 km/h, 12.00 %, 0.17, 24.4 m, 25 m", es decir, la curva se diseña con velocidad específica de 30 km/h. | Tabla 302.02 y Tópico 204.03 | 51 curvas (18 %). Listado en el capítulo 6.2. |
| Curvas de vuelta | Radio interior Ri ≥ 8 m (normal) o 6 m (absoluto); Re según Tabla 302.12 | "Son aquellas curvas que se proyectan sobre una ladera, en terrenos accidentados, con el propósito de obtener o alcanzar una cota mayor (...) Este tipo de curvas no se emplearán en autopistas, en tanto que en carreteras de Primera Clase podrán utilizarse en casos excepcionales (...) El radio interior de 8 m, representa un mínimo normal. El radio interior de 6 m, representa un mínimo absoluto y sólo podrá ser usado en forma excepcional." | Tópico 302.07 y Tabla 302.12 | 85 curvas con R de eje < 25 m (30 %): 39 con Ri ≥ 8 m, 12 con 6 ≤ Ri < 8 m y 34 con Ri < 6 m (no cumplen ni el mínimo absoluto). Capítulo 6.3. |
| Radio a partir del cual no se requiere peralte | 3 500 m (V = 40 km/h) | Tabla 304.04: "Velocidad 40 km/h: radio 3 500 m". | Tabla 304.04 | Ninguna curva del eje supera 3 500 m; todas se peraltan. |
| Peralte mínimo | 2 % para 2 500 ≤ R < 3 500 m | Tabla 304.06: "40 ≤ V < 100: 2 500 ≤ R < 3 500". | Tabla 304.06 | - |
| Transición del peralte | ipmáx = 1.8 − 0.01 V = 1.4 %; Lmín = (pf − pi)/ipmáx · B | "ipmáx = 1.8 − 0.01 V (...) Lmín = (pf − pi)/ipmáx · B". | Tópico 302.08 | Para Civil 3D se entrega el archivo de criterios DG2018_Corregido_2.xml (tablas "DG2018 _PMax 12%" y método "DG2018 METRICO"). |
| Longitud mínima de tangentes | 56 m entre curvas en S; 111 m entre curvas del mismo sentido; máx. deseable 668 m | Tabla 302.01: "40 km/h: L mín.s 56, L mín.o 111, L máx 668". | Tabla 302.01 | 8 de 281 tangentes intermedias cumplen; además 28 pares del mismo sentido se resolvieron como curva compuesta sin tangente (Tópico 302.06.03). El resto es limitación del trazo existente (capítulo 6.4 y capítulo 7). |
| Curvas vecinas del mismo sentido | Fundidas en una sola curva o en compuesta cuando la tangente intermedia era corta | "En general se evitará el empleo de curvas del mismo sentido, cuando estén separadas por un tramo en tangente de una longitud menor a 400 m, en longitudes menores excepcionalmente puede utilizarse una curva policéntrica." | Tópico 302.06.03 | Ver capítulo 7 (pasada de tangentes). |
| Longitud mínima de curva | 3V = 120 m; para Δ ≤ 5°: L > 30(10 − Δ); nunca Δ < 59′ | "La longitud mínima de curva (L) será: carreteras de dos carriles 3V (...) En el caso de ángulos de deflexión Δ pequeños, iguales o inferiores a 5º (...) L > 30(10 − Δ) (...) No se usará nunca ángulos de deflexión menores de 59' (minutos)." | Tópico 302.02 | Ninguna curva alcanza 120 m (la mayor tiene 120 m). 10 curvas tienen Δ < 5°; ninguna tiene Δ < 59′. |
| Curvas de transición (clotoides) | No incluidas en esta variante | Tabla 302.11A: para 40 km/h se puede prescindir de la transición si R ≥ 150 m. Tabla 302.10: longitud mínima de transición 40 m a 40 km/h; "En ningún caso se adoptarán longitudes de transición menores a 30 m". Tópico 302.05.06: R/3 ≤ A ≤ R. | Tópicos 302.05.06 y 302.05.07, Tablas 302.10 y 302.11A | 279 curvas tienen R < 150 m y requerirían clotoide; con Le = 40 m solo cabe en 5 (variante EJE_DG2018_clotoides.xml) porque las tangentes disponibles son demasiado cortas. |
| Relación entre radios consecutivos | Tabla 302.08 (grupo 2) | "cuando se enlacen curvas circulares consecutivas sin tangente intermedia, así como mediante tangente de longitud menor o igual a 200 m, la relación de radios (...) no sobrepasará los valores (...) Grupo 2: Carreteras de Segunda y Tercera Clase." | Tópico 302.04.05 y Tabla 302.08 | 40 de 281 pares cumplen. |
| Curvas compuestas (policéntricas) y curvas inversas enlazadas | 42 grupos de curvas consecutivas sin tangente intermedia | "En general, se evitará el empleo de curvas compuestas, tratando de reemplazarlas por una sola curva (...) En caso excepcional se podrá usar curvas compuestas, aclarando las razones, técnico-económicas u otras (...) En el caso de usar una curva compuesta de tres centros denominada policéntrica, deberán respetarse las siguientes condiciones: El radio de una de las curvas no será mayor de 1.5 veces el radio de la otra. Para armonizar los valores del peralte y sobreancho de cada una de las curvas vecinas, se empleará una transición de peralte determinada acorde a lo establecido en el Tópico 302.08. Para una sucesión de curvas de radio decreciente cada curva debe ser de longitud suficiente para permitir una desaceleración gradual." | Tópicos 302.06.01, 302.06.02 y 302.06.03 | 10 de 48 uniones cumplen la relación 1.5. Detalle completo en el capítulo 6.6. |
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
| Longitud del trazo original / del eje corregido | 11,491.71 m / 11,482.58 m |
| Número de curvas / tangentes | 282 / 283 |
| Curvas con R ≥ 50 m (cumple con peralte 8 %) | 79 (28 %) |
| Curvas con 45 ≤ R < 50 m (cumple con peralte 12 %) | 67 (24 %) |
| Curvas excepcionales, 25 ≤ R < 45 m (Ve = 30 km/h) | 51 (18 %) |
| Curvas de vuelta, R < 25 m | 85 (30 %) |
| Curvas llevadas al radio mínimo normativo (R = 45 m) | 66 |
| Separación lateral del trazo actual respecto al eje: promedio / percentil 95 / máxima | 0.37 m / 1.21 m / 5.22 m |
| Longitud de trazo con separación mayor a 1.5 m / 2.5 m / 4.0 m | 355 m / 146 m / 25 m |
| Tangentes intermedias que cumplen la Tabla 302.01 | 8 de 281 |
| Pares de curvas consecutivas que cumplen la Tabla 302.08 | 40 de 281 |
| Curvas con longitud ≥ 3V = 120 m | 0 de 282 |
| Grupos de curvas enlazadas sin tangente intermedia | 42: 23 compuesta de dos centros, 15 inversas enlazadas (S sin tangente), 2 mixta (compuesta + inversa), 1 policéntrica de tres centros, 1 inversas enlazadas (3 curvas) |
| Uniones curva-curva sin tangente (compuestas / inversas) | 48 (28 / 20) |
| Uniones que cumplen la relación de radios ≤ 1.5 (Tópico 302.06.02) | 10 de 48 |

# 5. Interpretación

El 52 % de las curvas cumple el radio mínimo de la DG-2018 para 40 km/h. El 18 % queda entre 25 y 45 m y debe tratarse como curva excepcional con velocidad específica de 30 km/h y señalización preventiva y reglamentaria. El 30 % restante corresponde a curvas de vuelta y esquinas urbanas con radios de eje entre 6 y 25 m, que es lo que impone la geometría existente; en 34 de ellas el radio interior resultante es menor de 6 m, de modo que para cumplir siquiera el mínimo absoluto habría que ampliar la plataforma o expropiar.

Las longitudes mínimas de tangente, la longitud mínima de curva de 120 m, las clotoides y la relación de radios consecutivos no se cumplen en la mayor parte del eje. No es un defecto del ajuste sino de la premisa de seguir el trazo existente: con curvas cada 35 m en promedio no hay espacio para tangentes de 56 a 111 m ni para espirales de 40 m. Si el proyecto exige cumplir esos parámetros, habrá que rediseñar tramos completos con expropiación.

# 6. Inventario de curvas por tipo

## 6.1 Curvas en el radio mínimo normativo (R = 45 m)

66 curvas quedan exactamente en el radio mínimo de la Tabla 302.02; de ellas 48 fueron llevadas a 45 m desde un radio ajustado menor (separación admitida ≤ 2.0 m). Deben peraltarse con el máximo de 12 %.

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | Lc (m) | Sep. máx. trazo (m) | Origen |
|------|---------|---------|---------|------|----|-----|-----|------|----------|
| C-3 | 0+099.59 | 9472189.807 | 612980.759 | 31.5 | D | 44.97 | 24.7 | 1.89 | subido al mínimo |
| C-16 | 0+479.76 | 9472384.202 | 612870.599 | 46.7 | D | 45.00 | 36.7 | 1.55 | subido al mínimo |
| C-17 | 0+523.34 | 9472424.822 | 612849.548 | 22.8 | I | 45.00 | 17.9 | 0.29 | ajuste al trazo |
| C-20 | 0+695.09 | 9472567.487 | 612812.812 | 40.5 | D | 45.00 | 31.8 | 0.70 | subido al mínimo |
| C-25 | 0+887.28 | 9472672.597 | 612728.598 | 84.0 | D | 45.00 | 66.0 | 1.56 | ajuste al trazo |
| C-28 | 1+015.21 | 9472810.529 | 612756.323 | 41.3 | I | 44.95 | 32.4 | 0.86 | subido al mínimo |
| C-30 | 1+075.63 | 9472804.918 | 612716.138 | 19.3 | D | 45.00 | 15.2 | 0.33 | subido al mínimo |
| C-32 | 1+126.45 | 9472772.919 | 612676.667 | 14.7 | D | 45.00 | 11.6 | 0.34 | subido al mínimo |
| C-35 | 1+354.24 | 9472719.756 | 612471.344 | 74.3 | D | 45.00 | 58.3 | 0.93 | ajuste al trazo |
| C-36 | 1+417.34 | 9472791.596 | 612458.780 | 30.4 | I | 45.00 | 23.9 | 1.18 | subido al mínimo |
| C-41 | 1+616.82 | 9472827.619 | 612299.230 | 22.3 | D | 45.00 | 17.5 | 0.51 | subido al mínimo |
| C-48 | 1+930.28 | 9472694.509 | 612081.130 | 11.8 | I | 45.00 | 9.3 | 0.17 | subido al mínimo |
| C-49 | 1+954.55 | 9472679.553 | 612061.984 | 19.2 | D | 45.00 | 15.1 | 0.16 | ajuste al trazo |
| C-52 | 2+017.50 | 9472686.709 | 612008.290 | 27.4 | D | 45.00 | 21.5 | 0.76 | subido al mínimo |
| C-57 | 2+154.94 | 9472744.752 | 611933.459 | 32.0 | I | 45.00 | 25.1 | 0.60 | subido al mínimo |
| C-62 | 2+390.38 | 9472704.516 | 611756.000 | 16.2 | I | 45.00 | 12.7 | 0.57 | ajuste al trazo |
| C-68 | 2+659.59 | 9472577.483 | 611564.659 | 30.8 | I | 45.00 | 24.2 | 0.74 | subido al mínimo |
| C-69 | 2+694.04 | 9472583.502 | 611530.134 | 25.8 | D | 45.00 | 20.2 | 0.95 | subido al mínimo |
| C-71 | 2+828.70 | 9472619.144 | 611414.752 | 17.3 | I | 45.00 | 13.6 | 0.31 | ajuste al trazo |
| C-77 | 3+180.17 | 9472715.476 | 611163.313 | 30.6 | I | 45.00 | 24.1 | 0.58 | subido al mínimo |
| C-79 | 3+259.15 | 9472661.808 | 611105.823 | 21.6 | I | 45.00 | 16.9 | 0.32 | ajuste al trazo |
| C-84 | 3+413.85 | 9472653.181 | 611030.052 | 10.5 | D | 45.00 | 8.3 | 0.25 | subido al mínimo |
| C-94 | 3+726.30 | 9472479.485 | 610955.759 | 27.8 | I | 45.00 | 21.8 | 1.14 | subido al mínimo |
| C-96 | 3+836.93 | 9472502.060 | 610850.676 | 5.5 | D | 45.00 | 4.4 | 0.43 | subido al mínimo |
| C-101 | 3+968.91 | 9472553.981 | 610730.567 | 9.1 | D | 45.00 | 7.2 | 0.24 | subido al mínimo |
| C-104 | 4+109.21 | 9472570.961 | 610592.995 | 29.6 | I | 45.00 | 23.3 | 0.83 | ajuste al trazo |
| C-105 | 4+190.97 | 9472551.054 | 610513.146 | 31.8 | D | 45.00 | 25.0 | 0.94 | ajuste al trazo |
| C-106 | 4+222.41 | 9472560.856 | 610482.581 | 28.2 | I | 45.00 | 22.1 | 0.51 | subido al mínimo |
| C-112 | 4+486.26 | 9472546.514 | 610260.006 | 4.1 | I | 45.00 | 3.2 | 0.17 | subido al mínimo |
| C-115 | 4+557.60 | 9472519.929 | 610197.194 | 25.5 | D | 45.00 | 20.0 | 1.27 | subido al mínimo |
| C-122 | 4+687.70 | 9472463.422 | 610081.749 | 18.4 | I | 45.00 | 14.4 | 0.13 | ajuste al trazo |
| C-124 | 4+750.65 | 9472448.886 | 610029.585 | 21.3 | I | 45.00 | 16.7 | 0.22 | ajuste al trazo |
| C-125 | 4+800.66 | 9472438.535 | 609980.467 | 44.2 | D | 45.00 | 34.7 | 1.65 | subido al mínimo |
| C-132 | 5+081.61 | 9472346.474 | 609762.633 | 8.9 | D | 45.00 | 7.0 | 0.27 | subido al mínimo |
| C-134 | 5+213.33 | 9472300.221 | 609640.768 | 18.3 | I | 45.00 | 14.4 | 0.87 | subido al mínimo |
| C-137 | 5+329.89 | 9472263.851 | 609530.347 | 8.8 | D | 45.00 | 6.9 | 0.23 | subido al mínimo |
| C-138 | 5+358.92 | 9472257.218 | 609502.075 | 13.6 | I | 45.00 | 10.7 | 0.29 | subido al mínimo |
| C-139 | 5+382.32 | 9472246.628 | 609481.152 | 5.9 | D | 45.00 | 4.6 | 0.21 | subido al mínimo |
| C-140 | 5+445.79 | 9472223.926 | 609421.873 | 4.4 | D | 45.00 | 3.5 | 0.25 | subido al mínimo |
| C-141 | 5+500.17 | 9472208.438 | 609369.745 | 17.6 | I | 45.00 | 13.8 | 0.68 | subido al mínimo |
| C-146 | 5+806.57 | 9472283.459 | 609143.685 | 14.3 | D | 45.00 | 11.3 | 0.48 | subido al mínimo |
| C-153 | 6+245.33 | 9471930.530 | 608927.705 | 23.8 | I | 45.00 | 18.7 | 0.59 | subido al mínimo |
| C-154 | 6+280.05 | 9471905.424 | 608903.335 | 8.9 | D | 45.00 | 7.0 | 0.26 | subido al mínimo |
| C-155 | 6+329.22 | 9471875.881 | 608864.013 | 11.8 | D | 45.00 | 9.3 | 0.32 | subido al mínimo |
| C-158 | 6+467.03 | 9471809.087 | 608744.190 | 77.1 | D | 45.00 | 60.6 | 1.93 | subido al mínimo |
| C-163 | 6+667.46 | 9471914.358 | 608657.337 | 25.0 | D | 45.00 | 19.7 | 0.39 | subido al mínimo |
| C-186 | 7+485.28 | 9471612.913 | 608386.663 | 28.3 | I | 45.00 | 22.2 | 0.31 | subido al mínimo |
| C-201 | 7+997.12 | 9471436.095 | 608307.908 | 9.5 | I | 45.00 | 7.5 | 0.15 | subido al mínimo |
| C-202 | 8+009.17 | 9471435.790 | 608295.844 | 2.0 | D | 45.00 | 1.6 | 0.02 | subido al mínimo |
| C-204 | 8+112.12 | 9471424.264 | 608193.881 | 15.9 | D | 45.00 | 12.5 | 0.64 | subido al mínimo |
| C-207 | 8+247.57 | 9471529.574 | 608141.225 | 11.8 | D | 45.00 | 9.3 | 0.30 | ajuste al trazo |
| C-209 | 8+286.15 | 9471557.242 | 608115.098 | 27.5 | D | 45.00 | 21.6 | 0.21 | ajuste al trazo |
| C-210 | 8+319.00 | 9471586.912 | 608100.043 | 10.1 | D | 45.00 | 7.9 | 0.23 | subido al mínimo |
| C-216 | 8+582.28 | 9471807.256 | 607991.071 | 29.3 | D | 45.00 | 23.0 | 0.45 | ajuste al trazo |
| C-220 | 8+760.62 | 9471953.791 | 607928.689 | 32.0 | D | 45.00 | 25.1 | 0.78 | subido al mínimo |
| C-228 | 9+093.51 | 9471911.350 | 607807.368 | 67.8 | D | 45.00 | 53.2 | 0.94 | ajuste al trazo |
| C-234 | 9+343.21 | 9471804.341 | 607813.043 | 23.8 | D | 45.00 | 18.7 | 0.42 | subido al mínimo |
| C-235 | 9+366.92 | 9471780.365 | 607813.290 | 25.0 | I | 45.00 | 19.6 | 0.21 | ajuste al trazo |
| C-238 | 9+455.96 | 9471767.309 | 607787.435 | 43.5 | D | 44.98 | 34.1 | 1.25 | subido al mínimo |
| C-244 | 9+728.70 | 9471866.802 | 607582.823 | 13.5 | D | 45.00 | 10.6 | 0.41 | subido al mínimo |
| C-250 | 10+010.24 | 9471727.071 | 607566.691 | 68.8 | I | 45.00 | 54.1 | 0.90 | ajuste al trazo |
| C-263 | 10+463.20 | 9471698.310 | 607607.115 | 53.0 | I | 45.00 | 41.6 | 2.00 | subido al mínimo |
| C-266 | 10+683.76 | 9471763.099 | 607449.956 | 28.0 | I | 45.00 | 22.0 | 0.52 | ajuste al trazo |
| C-269 | 10+866.58 | 9471920.322 | 607428.954 | 13.4 | I | 45.00 | 10.6 | 0.33 | subido al mínimo |
| C-272 | 10+989.59 | 9472003.071 | 607514.411 | 18.5 | D | 45.00 | 14.5 | 0.61 | subido al mínimo |
| C-275 | 11+107.66 | 9472059.305 | 607493.835 | 37.4 | D | 45.00 | 29.4 | 0.96 | subido al mínimo |

## 6.2 Curvas excepcionales (25 m ≤ R < 45 m)

51 curvas. La velocidad específica se calcula con Ve = √(127 · R · (0.12 + 0.17)), que reproduce los radios de la Tabla 302.02 para 30 y 40 km/h (25 m → 30 km/h, 45 m → 41 km/h). Todas requieren peralte 12 %, sobreancho y señalización de velocidad máxima 30 km/h.

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | Ve (km/h) | Sa (m) | Lc (m) | Sep. máx. trazo (m) |
|------|---------|---------|---------|------|----|-----|------|-----|-----|------|
| C-1 | 0+037.84 | 9472166.454 | 613022.231 | 44.7 | I | 38.83 | 38 | 3.56 | 30.3 | 1.16 |
| C-6 | 0+169.69 | 9472248.915 | 612948.678 | 36.4 | D | 25.00 | 30 | 5.47 | 15.9 | 0.43 |
| C-12 | 0+326.45 | 9472347.878 | 613017.986 | 28.7 | I | 40.00 | 38 | 3.47 | 20.1 | 0.21 |
| C-18 | 0+614.55 | 9472483.412 | 612779.332 | 77.8 | D | 39.90 | 38 | 3.47 | 54.2 | 1.74 |
| C-23 | 0+767.38 | 9472618.128 | 612836.504 | 45.9 | I | 29.88 | 33 | 4.58 | 24.0 | 0.97 |
| C-24 | 0+783.00 | 9472622.422 | 612820.063 | 14.1 | D | 35.00 | 36 | 3.93 | 8.6 | 0.39 |
| C-26 | 0+928.31 | 9472724.322 | 612750.290 | 31.9 | I | 43.60 | 40 | 3.20 | 24.3 | 1.38 |
| C-38 | 1+498.12 | 9472779.312 | 612398.742 | 60.8 | D | 40.48 | 39 | 3.43 | 43.0 | 0.76 |
| C-40 | 1+588.56 | 9472824.333 | 612331.803 | 66.4 | I | 29.90 | 33 | 4.58 | 34.6 | 0.61 |
| C-42 | 1+645.19 | 9472841.054 | 612273.997 | 35.4 | I | 38.90 | 38 | 3.56 | 24.1 | 1.21 |
| C-43 | 1+668.21 | 9472837.985 | 612250.375 | 32.3 | D | 39.31 | 38 | 3.52 | 22.2 | 0.38 |
| C-50 | 1+986.05 | 9472669.378 | 612032.020 | 27.0 | D | 43.90 | 40 | 3.18 | 20.7 | 0.17 |
| C-54 | 2+065.42 | 9472732.887 | 611995.109 | 37.0 | D | 37.28 | 37 | 3.70 | 24.1 | 0.65 |
| C-58 | 2+197.13 | 9472717.221 | 611900.604 | 86.8 | D | 30.00 | 33 | 4.56 | 45.4 | 1.24 |
| C-65 | 2+575.60 | 9472606.735 | 611624.722 | 71.4 | I | 29.40 | 33 | 4.65 | 36.6 | 0.37 |
| C-66 | 2+614.10 | 9472567.615 | 611604.346 | 38.9 | D | 37.30 | 37 | 3.70 | 25.4 | 1.18 |
| C-74 | 3+003.47 | 9472588.315 | 611253.691 | 75.6 | D | 25.00 | 30 | 5.47 | 33.0 | 0.57 |
| C-83 | 3+383.68 | 9472683.873 | 611029.183 | 32.2 | I | 35.01 | 36 | 3.93 | 19.7 | 1.18 |
| C-88 | 3+566.25 | 9472511.901 | 611065.550 | 36.1 | D | 30.00 | 33 | 4.56 | 18.9 | 5.17 |
| C-91 | 3+645.92 | 9472449.657 | 611030.786 | 43.7 | D | 35.00 | 36 | 3.93 | 26.7 | 5.84 |
| C-92 | 3+670.88 | 9472453.707 | 611004.763 | 37.7 | D | 32.50 | 35 | 4.22 | 21.4 | 4.64 |
| C-107 | 4+244.16 | 9472556.841 | 610460.744 | 22.9 | D | 44.89 | 41 | 3.11 | 17.9 | 0.25 |
| C-109 | 4+317.70 | 9472504.737 | 610429.794 | 89.7 | D | 32.58 | 35 | 4.21 | 51.0 | 0.90 |
| C-145 | 5+759.70 | 9472297.505 | 609198.596 | 80.4 | I | 34.20 | 35 | 4.02 | 48.0 | 0.42 |
| C-160 | 6+604.83 | 9471936.611 | 608671.898 | 15.1 | I | 44.69 | 41 | 3.12 | 11.8 | 0.29 |
| C-164 | 6+711.84 | 9471869.912 | 608662.043 | 32.1 | I | 30.00 | 33 | 4.56 | 16.8 | 0.66 |
| C-165 | 6+728.07 | 9471856.784 | 608672.342 | 27.4 | D | 33.14 | 35 | 4.14 | 15.8 | 0.21 |
| C-170 | 6+893.55 | 9471803.158 | 608604.034 | 19.0 | I | 34.00 | 35 | 4.04 | 11.3 | 0.25 |
| C-171 | 6+937.64 | 9471765.017 | 608581.692 | 45.2 | I | 34.50 | 36 | 3.99 | 27.2 | 0.47 |
| C-174 | 7+125.30 | 9471643.281 | 608471.076 | 90.7 | D | 40.00 | 38 | 3.47 | 63.3 | 1.02 |
| C-180 | 7+260.20 | 9471666.658 | 608430.695 | 19.2 | I | 42.46 | 40 | 3.28 | 14.2 | 0.62 |
| C-187 | 7+545.67 | 9471556.942 | 608362.774 | 86.9 | D | 40.00 | 38 | 3.47 | 60.6 | 0.51 |
| C-193 | 7+716.07 | 9471559.037 | 608419.344 | 20.1 | D | 39.19 | 38 | 3.53 | 13.7 | 0.13 |
| C-200 | 7+974.72 | 9471432.294 | 608334.781 | 71.2 | D | 25.00 | 30 | 5.47 | 31.1 | 0.40 |
| C-206 | 8+198.92 | 9471492.268 | 608176.443 | 56.5 | I | 30.00 | 33 | 4.56 | 29.6 | 0.47 |
| C-208 | 8+266.26 | 9471545.530 | 608131.436 | 22.8 | I | 40.00 | 38 | 3.47 | 15.9 | 0.53 |
| C-213 | 8+437.81 | 9471697.937 | 608064.124 | 59.2 | I | 29.10 | 33 | 4.70 | 30.1 | 0.47 |
| C-214 | 8+510.61 | 9471732.769 | 607996.813 | 63.8 | D | 30.00 | 33 | 4.56 | 33.4 | 0.55 |
| C-215 | 8+563.38 | 9471789.463 | 607997.954 | 22.3 | I | 35.00 | 36 | 3.93 | 13.6 | 0.42 |
| C-224 | 8+915.20 | 9471873.080 | 607898.972 | 62.6 | I | 39.59 | 38 | 3.50 | 43.2 | 0.73 |
| C-226 | 8+990.34 | 9471866.233 | 607877.279 | 50.7 | D | 29.40 | 33 | 4.65 | 26.0 | 0.90 |
| C-231 | 9+213.86 | 9471891.124 | 607753.031 | 93.0 | I | 39.70 | 38 | 3.49 | 64.4 | 0.65 |
| C-233 | 9+311.64 | 9471836.954 | 607798.225 | 63.9 | I | 32.20 | 34 | 4.26 | 35.9 | 0.40 |
| C-242 | 9+632.56 | 9471809.135 | 607653.305 | 57.6 | D | 43.80 | 40 | 3.18 | 44.1 | 0.79 |
| C-243 | 9+679.79 | 9471856.323 | 607633.025 | 55.0 | I | 29.30 | 33 | 4.67 | 28.1 | 0.66 |
| C-247 | 9+850.63 | 9471878.523 | 607515.210 | 82.7 | I | 25.00 | 30 | 5.47 | 36.1 | 0.47 |
| C-248 | 9+884.01 | 9471853.443 | 607548.005 | 50.6 | D | 38.40 | 38 | 3.60 | 33.9 | 0.32 |
| C-254 | 10+118.61 | 9471715.102 | 607677.255 | 54.4 | D | 28.02 | 32 | 4.88 | 26.6 | 1.59 |
| C-255 | 10+134.08 | 9471697.708 | 607674.164 | 12.9 | I | 28.83 | 33 | 4.74 | 6.5 | 1.99 |
| C-264 | 10+486.74 | 9471683.547 | 607584.758 | 11.9 | D | 41.61 | 39 | 3.34 | 8.7 | 0.28 |
| C-282 | 11+474.45 | 9472277.571 | 607212.541 | 10.0 | D | 40.00 | 38 | 3.47 | 7.0 | 0.12 |

## 6.3 Curvas de vuelta (R < 25 m)

85 curvas. El radio interior Ri se obtiene de Ri + ancho/2 = R, con el ancho de calzada en curva de vuelta (Re − Ri) de la Tabla 302.12 para la maniobra C2 (camión de dos ejes cruzándose con un vehículo ligero), que considera calzada de 6 m en tangente. Criterio: Ri ≥ 8 m cumple el mínimo normal; 6 ≤ Ri < 8 m es el mínimo absoluto de uso excepcional; Ri < 6 m no cumple.

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R eje (m) | Ri (m) | Re (m) | Ancho (m) | Evaluación DG-2018 | Sep. máx. trazo (m) |
|------|---------|---------|---------|------|----|-----|-----|-----|-----|-------------|------|
| C-2 | 0+059.92 | 9472190.090 | 613024.156 | 95.0 | I | 7.10 | 2.2 | 12.0 | 9.75 | no cumple (Ri < 6 m) | 1.08 |
| C-4 | 0+121.86 | 9472201.640 | 612961.140 | 48.6 | D | 22.70 | 18.7 | 26.7 | 8.07 | cumple (Ri ≥ 8 m) | 1.76 |
| C-7 | 0+186.75 | 9472266.013 | 612952.910 | 42.2 | I | 10.75 | 5.9 | 15.6 | 9.75 | no cumple (Ri < 6 m) | 0.36 |
| C-8 | 0+195.73 | 9472274.247 | 612948.468 | 81.8 | D | 6.00 | 1.1 | 10.9 | 9.75 | no cumple (Ri < 6 m) | 1.15 |
| C-9 | 0+208.69 | 9472283.050 | 612960.368 | 35.0 | I | 23.80 | 19.8 | 27.8 | 8.01 | cumple (Ri ≥ 8 m) | 0.45 |
| C-10 | 0+223.51 | 9472297.545 | 612965.224 | 51.6 | D | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 2.11 |
| C-11 | 0+315.18 | 9472328.984 | 613052.387 | 131.4 | I | 13.10 | 8.5 | 17.7 | 9.11 | cumple (Ri ≥ 8 m) | 1.18 |
| C-15 | 0+438.63 | 9472372.920 | 612910.184 | 16.4 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.15 |
| C-19 | 0+637.20 | 9472512.525 | 612794.601 | 9.3 | I | 8.07 | 3.2 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.74 |
| C-21 | 0+732.10 | 9472587.366 | 612845.663 | 6.5 | I | 17.37 | 13.2 | 21.6 | 8.40 | cumple (Ri ≥ 8 m) | 0.45 |
| C-22 | 0+739.32 | 9472591.784 | 612851.375 | 81.7 | I | 7.20 | 2.3 | 12.1 | 9.75 | no cumple (Ri < 6 m) | 0.69 |
| C-29 | 1+043.74 | 9472836.729 | 612741.678 | 112.0 | I | 8.80 | 3.9 | 13.7 | 9.75 | no cumple (Ri < 6 m) | 0.65 |
| C-37 | 1+461.72 | 9472825.871 | 612429.694 | 106.1 | I | 24.20 | 20.2 | 28.2 | 8.00 | cumple (Ri ≥ 8 m) | 0.98 |
| C-39 | 1+547.51 | 9472783.479 | 612344.963 | 67.7 | D | 11.70 | 6.9 | 16.5 | 9.51 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.49 |
| C-45 | 1+790.90 | 9472806.914 | 612152.660 | 1.3 | I | 11.60 | 6.8 | 16.4 | 9.54 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.05 |
| C-51 | 1+999.89 | 9472671.422 | 612017.929 | 49.5 | D | 8.01 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.27 |
| C-53 | 2+030.68 | 9472700.257 | 612007.144 | 15.4 | I | 19.40 | 15.3 | 23.5 | 8.24 | cumple (Ri ≥ 8 m) | 0.17 |
| C-55 | 2+104.51 | 9472771.151 | 612006.630 | 135.3 | I | 11.30 | 6.5 | 16.1 | 9.63 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.39 |
| C-60 | 2+333.82 | 9472761.933 | 611770.429 | 88.4 | I | 9.10 | 4.2 | 14.0 | 9.75 | no cumple (Ri < 6 m) | 0.94 |
| C-67 | 2+633.48 | 9472559.465 | 611585.644 | 64.2 | D | 11.50 | 6.7 | 16.3 | 9.57 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.37 |
| C-70 | 2+788.73 | 9472638.901 | 611452.915 | 63.0 | I | 23.80 | 19.8 | 27.8 | 8.01 | cumple (Ri ≥ 8 m) | 0.63 |
| C-76 | 3+149.90 | 9472730.524 | 611203.135 | 97.0 | I | 21.70 | 17.6 | 25.8 | 8.12 | cumple (Ri ≥ 8 m) | 1.29 |
| C-80 | 3+291.75 | 9472636.120 | 611085.416 | 89.0 | D | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.91 |
| C-82 | 3+380.54 | 9472717.578 | 611049.115 | 147.0 | I | 8.60 | 3.7 | 13.5 | 9.75 | no cumple (Ri < 6 m) | 0.39 |
| C-87 | 3+551.07 | 9472520.056 | 611052.384 | 35.5 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 2.64 |
| C-89 | 3+585.48 | 9472493.487 | 611073.043 | 53.0 | D | 17.70 | 13.5 | 21.9 | 8.37 | cumple (Ri ≥ 8 m) | 4.60 |
| C-93 | 3+683.34 | 9472463.336 | 610995.637 | 24.5 | I | 10.02 | 5.1 | 14.9 | 9.75 | no cumple (Ri < 6 m) | 1.50 |
| C-100 | 3+948.12 | 9472551.225 | 610751.467 | 31.7 | I | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.60 |
| C-108 | 4+266.11 | 9472561.633 | 610439.068 | 93.2 | I | 12.40 | 7.7 | 17.1 | 9.31 | mínimo absoluto (6 ≤ Ri < 8 m) | 1.46 |
| C-114 | 4+528.27 | 9472540.972 | 610218.570 | 45.4 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.19 |
| C-116 | 4+611.64 | 9472502.142 | 610145.809 | 4.3 | I | 11.40 | 6.6 | 16.2 | 9.60 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.44 |
| C-118 | 4+617.49 | 9472500.023 | 610140.360 | 7.0 | I | 6.31 | 1.4 | 11.2 | 9.75 | no cumple (Ri < 6 m) | 0.33 |
| C-119 | 4+618.31 | 9472499.660 | 610139.619 | 8.4 | D | 6.00 | 1.1 | 10.9 | 9.75 | no cumple (Ri < 6 m) | 0.11 |
| C-120 | 4+619.43 | 9472499.320 | 610138.552 | 3.2 | D | 24.06 | 20.1 | 28.1 | 8.00 | cumple (Ri ≥ 8 m) | 0.13 |
| C-123 | 4+711.50 | 9472442.070 | 610070.965 | 72.6 | D | 13.80 | 9.3 | 18.3 | 8.91 | cumple (Ri ≥ 8 m) | 0.46 |
| C-126 | 4+838.72 | 9472459.837 | 609946.745 | 103.1 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.99 |
| C-127 | 4+890.88 | 9472400.337 | 609926.104 | 123.8 | D | 15.60 | 11.3 | 19.9 | 8.59 | cumple (Ri ≥ 8 m) | 1.31 |
| C-128 | 4+921.42 | 9472444.464 | 609892.798 | 90.1 | I | 8.00 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.26 |
| C-143 | 5+619.69 | 9472172.908 | 609260.939 | 30.0 | D | 12.91 | 8.3 | 17.5 | 9.17 | cumple (Ri ≥ 8 m) | 0.28 |
| C-147 | 5+837.99 | 9472283.454 | 609112.203 | 82.6 | I | 24.00 | 20.0 | 28.0 | 8.00 | cumple (Ri ≥ 8 m) | 1.09 |
| C-161 | 6+730.65 | 9472049.546 | 608616.265 | 168.7 | I | 11.85 | 7.1 | 16.6 | 9.47 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.98 |
| C-162 | 6+650.15 | 9471929.222 | 608648.383 | 16.1 | I | 18.40 | 14.2 | 22.6 | 8.31 | cumple (Ri ≥ 8 m) | 0.15 |
| C-166 | 6+795.88 | 9471789.864 | 608685.060 | 41.9 | D | 20.66 | 16.6 | 24.7 | 8.17 | cumple (Ri ≥ 8 m) | 0.72 |
| C-167 | 6+814.40 | 9471773.408 | 608675.123 | 107.5 | D | 8.30 | 3.4 | 13.2 | 9.75 | no cumple (Ri < 6 m) | 0.44 |
| C-169 | 6+881.56 | 9471811.787 | 608614.087 | 56.8 | I | 13.97 | 9.5 | 18.4 | 8.87 | cumple (Ri ≥ 8 m) | 0.71 |
| C-175 | 7+177.67 | 9471709.489 | 608448.163 | 45.7 | D | 6.00 | 1.1 | 10.9 | 9.75 | no cumple (Ri < 6 m) | 1.08 |
| C-176 | 7+185.37 | 9471716.611 | 608451.725 | 71.7 | I | 7.52 | 2.6 | 12.4 | 9.75 | no cumple (Ri < 6 m) | 5.24 |
| C-177 | 7+203.74 | 9471730.601 | 608437.667 | 112.4 | I | 9.40 | 4.5 | 14.3 | 9.75 | no cumple (Ri < 6 m) | 5.64 |
| C-179 | 7+252.12 | 9471674.476 | 608428.671 | 6.9 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 2.86 |
| C-181 | 7+347.62 | 9471593.808 | 608479.262 | 17.1 | I | 8.00 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 2.08 |
| C-182 | 7+382.08 | 9471572.038 | 608505.994 | 151.7 | D | 7.97 | 3.1 | 12.8 | 9.75 | no cumple (Ri < 6 m) | 0.56 |
| C-183 | 7+380.62 | 9471579.670 | 608466.114 | 42.9 | D | 23.00 | 19.0 | 27.0 | 8.05 | cumple (Ri ≥ 8 m) | 0.43 |
| C-185 | 7+457.71 | 9471631.255 | 608409.634 | 63.3 | I | 14.34 | 10.0 | 18.7 | 8.76 | cumple (Ri ≥ 8 m) | 0.21 |
| C-188 | 7+574.98 | 9471572.115 | 608321.039 | 19.3 | I | 8.89 | 4.0 | 13.8 | 9.75 | no cumple (Ri < 6 m) | 0.63 |
| C-189 | 7+594.90 | 9471572.337 | 608301.096 | 133.6 | I | 7.90 | 3.0 | 12.8 | 9.75 | no cumple (Ri < 6 m) | 0.52 |
| C-190 | 7+601.69 | 9471553.874 | 608318.287 | 36.7 | I | 20.48 | 16.4 | 24.6 | 8.18 | cumple (Ri ≥ 8 m) | 0.33 |
| C-192 | 7+703.24 | 9471578.882 | 608409.225 | 106.8 | D | 11.40 | 6.6 | 16.2 | 9.60 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.27 |
| C-195 | 7+858.02 | 9471431.884 | 608477.901 | 149.4 | D | 13.10 | 8.5 | 17.7 | 9.11 | cumple (Ri ≥ 8 m) | 1.48 |
| C-196 | 7+846.19 | 9471454.320 | 608433.604 | 10.5 | I | 10.80 | 5.9 | 15.7 | 9.75 | no cumple (Ri < 6 m) | 0.32 |
| C-197 | 7+847.82 | 9471454.780 | 608432.037 | 9.1 | D | 8.02 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.23 |
| C-199 | 7+924.87 | 9471482.198 | 608360.027 | 83.8 | I | 18.30 | 14.1 | 22.5 | 8.32 | cumple (Ri ≥ 8 m) | 1.02 |
| C-205 | 8+144.69 | 9471427.707 | 608161.406 | 97.1 | D | 21.20 | 17.1 | 25.3 | 8.14 | cumple (Ri ≥ 8 m) | 1.16 |
| C-217 | 8+627.40 | 9471852.429 | 607997.510 | 56.2 | I | 24.10 | 20.1 | 28.1 | 8.00 | cumple (Ri ≥ 8 m) | 1.04 |
| C-219 | 8+729.81 | 9471946.138 | 607961.163 | 69.0 | I | 15.00 | 10.7 | 19.3 | 8.67 | cumple (Ri ≥ 8 m) | 0.64 |
| C-221 | 8+809.39 | 9471988.888 | 607893.859 | 138.0 | I | 8.60 | 3.7 | 13.5 | 9.75 | no cumple (Ri < 6 m) | 1.14 |
| C-222 | 8+815.76 | 9471958.469 | 607895.335 | 36.7 | I | 24.30 | 20.3 | 28.3 | 8.00 | cumple (Ri ≥ 8 m) | 0.64 |
| C-223 | 8+863.28 | 9471921.340 | 607925.882 | 68.6 | D | 20.00 | 15.9 | 24.1 | 8.21 | cumple (Ri ≥ 8 m) | 0.48 |
| C-225 | 9+019.58 | 9471781.884 | 607959.128 | 169.3 | D | 8.00 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 1.04 |
| C-227 | 9+023.42 | 9471900.924 | 607881.254 | 88.5 | I | 11.20 | 6.4 | 16.0 | 9.66 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.65 |
| C-229 | 9+137.06 | 9471960.554 | 607794.904 | 113.0 | I | 8.90 | 4.0 | 13.8 | 9.75 | no cumple (Ri < 6 m) | 0.76 |
| C-230 | 9+168.40 | 9471935.932 | 607762.515 | 40.8 | I | 10.74 | 5.9 | 15.6 | 9.75 | no cumple (Ri < 6 m) | 0.47 |
| C-232 | 9+275.04 | 9471878.559 | 607832.428 | 120.4 | D | 12.40 | 7.7 | 17.1 | 9.31 | mínimo absoluto (6 ≤ Ri < 8 m) | 1.13 |
| C-237 | 9+435.23 | 9471717.373 | 607840.435 | 154.9 | D | 8.30 | 3.4 | 13.2 | 9.75 | no cumple (Ri < 6 m) | 1.68 |
| C-239 | 9+475.51 | 9471788.571 | 607786.239 | 27.9 | I | 13.50 | 9.0 | 18.0 | 9.00 | cumple (Ri ≥ 8 m) | 0.38 |
| C-240 | 9+525.93 | 9471831.834 | 607760.094 | 96.0 | I | 14.70 | 10.3 | 19.1 | 8.71 | cumple (Ri ≥ 8 m) | 1.34 |
| C-245 | 9+760.92 | 9471880.585 | 607553.646 | 61.2 | D | 23.60 | 19.6 | 27.6 | 8.02 | cumple (Ri ≥ 8 m) | 0.71 |
| C-246 | 9+816.48 | 9471938.742 | 607550.086 | 146.4 | I | 8.70 | 3.8 | 13.6 | 9.75 | no cumple (Ri < 6 m) | 0.76 |
| C-252 | 10+094.75 | 9471725.993 | 607658.496 | 19.2 | I | 7.51 | 2.6 | 12.4 | 9.75 | no cumple (Ri < 6 m) | 0.96 |
| C-253 | 10+100.78 | 9471728.828 | 607663.850 | 73.6 | D | 6.40 | 1.5 | 11.3 | 9.75 | no cumple (Ri < 6 m) | 1.87 |
| C-256 | 10+195.21 | 9471636.629 | 607677.205 | 21.7 | D | 10.10 | 5.2 | 15.0 | 9.75 | no cumple (Ri < 6 m) | 0.60 |
| C-258 | 10+268.42 | 9471570.989 | 607695.578 | 39.6 | D | 10.60 | 5.7 | 15.5 | 9.75 | no cumple (Ri < 6 m) | 1.25 |
| C-259 | 10+290.30 | 9471549.058 | 607698.960 | 132.3 | D | 7.98 | 3.1 | 12.9 | 9.75 | no cumple (Ri < 6 m) | 0.82 |
| C-262 | 10+429.47 | 9471686.112 | 607641.417 | 74.0 | I | 12.40 | 7.7 | 17.1 | 9.31 | mínimo absoluto (6 ≤ Ri < 8 m) | 0.51 |
| C-271 | 10+969.63 | 9471983.138 | 607508.918 | 44.7 | I | 17.00 | 12.8 | 21.2 | 8.43 | cumple (Ri ≥ 8 m) | 0.18 |
| C-274 | 11+068.93 | 9472075.534 | 607539.017 | 105.8 | I | 11.65 | 6.9 | 16.4 | 9.53 | mínimo absoluto (6 ≤ Ri < 8 m) | 1.04 |

Agrupación en zonas (curvas de vuelta consecutivas):

| Zona | Prog. inicio | Prog. fin | Curvas | R mín. eje (m) | Ri mín. (m) | Evaluación |
|-----|--------|--------|------------|------|------|-------------|
| V-1 | 0+052.16 | 0+063.94 | C-2 | 7.1 | 2.2 | no cumple |
| V-2 | 0+111.62 | 0+130.86 | C-4 | 22.7 | 18.7 | cumple |
| V-3 | 0+182.60 | 0+316.21 | C-7, C-8, C-9, C-10, C-11 | 6.0 | 1.1 | no cumple |
| V-4 | 0+436.46 | 0+440.77 | C-15 | 15.0 | 10.7 | cumple |
| V-5 | 0+636.54 | 0+637.85 | C-19 | 8.1 | 3.2 | no cumple |
| V-6 | 0+731.11 | 0+743.36 | C-21, C-22 | 7.2 | 2.3 | no cumple |
| V-7 | 1+030.68 | 1+047.89 | C-29 | 8.8 | 3.9 | no cumple |
| V-8 | 1+429.56 | 1+474.36 | C-37 | 24.2 | 20.2 | cumple |
| V-9 | 1+539.66 | 1+553.49 | C-39 | 11.7 | 6.9 | mínimo absoluto |
| V-10 | 1+790.77 | 1+791.03 | C-45 | 11.6 | 6.8 | mínimo absoluto |
| V-11 | 1+996.20 | 2+003.12 | C-51 | 8.0 | 3.1 | no cumple |
| V-12 | 2+028.05 | 2+033.27 | C-53 | 19.4 | 15.3 | cumple |
| V-13 | 2+077.03 | 2+103.71 | C-55 | 11.3 | 6.5 | mínimo absoluto |
| V-14 | 2+324.96 | 2+339.01 | C-60 | 9.1 | 4.2 | no cumple |
| V-15 | 2+626.27 | 2+639.15 | C-67 | 11.5 | 6.7 | mínimo absoluto |
| V-16 | 2+774.14 | 2+800.32 | C-70 | 23.8 | 19.8 | cumple |
| V-17 | 3+125.38 | 3+162.11 | C-76 | 21.7 | 17.6 | cumple |
| V-18 | 3+277.02 | 3+300.31 | C-80 | 15.0 | 10.7 | cumple |
| V-19 | 3+351.50 | 3+373.56 | C-82 | 8.6 | 3.7 | no cumple |
| V-20 | 3+546.27 | 3+555.57 | C-87 | 15.0 | 10.7 | cumple |
| V-21 | 3+576.66 | 3+593.02 | C-89 | 17.7 | 13.5 | cumple |
| V-22 | 3+681.17 | 3+685.45 | C-93 | 10.0 | 5.1 | no cumple |
| V-23 | 3+942.45 | 3+953.50 | C-100 | 20.0 | 15.9 | cumple |
| V-24 | 4+253.00 | 4+273.17 | C-108 | 12.4 | 7.7 | mínimo absoluto |
| V-25 | 4+521.99 | 4+533.88 | C-114 | 15.0 | 10.7 | cumple |
| V-26 | 4+611.21 | 4+612.07 | C-116 | 11.4 | 6.6 | mínimo absoluto |
| V-27 | 4+617.10 | 4+620.11 | C-118, C-119, C-120 | 6.0 | 1.1 | no cumple |
| V-28 | 4+701.37 | 4+718.85 | C-123 | 13.8 | 9.3 | cumple |
| V-29 | 4+819.81 | 4+925.99 | C-126, C-127, C-128 | 8.0 | 3.1 | no cumple |
| V-30 | 5+616.24 | 5+622.99 | C-143 | 12.9 | 8.3 | cumple |
| V-31 | 5+816.91 | 5+851.51 | C-147 | 24.0 | 20.0 | cumple |
| V-32 | 6+610.69 | 6+652.72 | C-161, C-162 | 11.8 | 7.1 | mínimo absoluto |
| V-33 | 6+787.98 | 6+818.65 | C-166, C-167 | 8.3 | 3.4 | no cumple |
| V-34 | 6+874.00 | 6+887.86 | C-169 | 14.0 | 9.5 | cumple |
| V-35 | 7+175.15 | 7+208.14 | C-175, C-176, C-177 | 6.0 | 1.1 | no cumple |
| V-36 | 7+251.22 | 7+253.03 | C-179 | 15.0 | 10.7 | cumple |
| V-37 | 7+346.41 | 7+388.80 | C-181, C-182, C-183 | 8.0 | 3.1 | no cumple |
| V-38 | 7+448.88 | 7+464.71 | C-185 | 14.3 | 10.0 | cumple |
| V-39 | 7+573.47 | 7+608.02 | C-188, C-189, C-190 | 7.9 | 3.0 | no cumple |
| V-40 | 7+687.90 | 7+709.14 | C-192 | 11.4 | 6.6 | mínimo absoluto |
| V-41 | 7+810.20 | 7+848.46 | C-195, C-196, C-197 | 8.0 | 3.1 | no cumple |
| V-42 | 7+908.44 | 7+935.22 | C-199 | 18.3 | 14.1 | cumple |
| V-43 | 8+120.71 | 8+156.62 | C-205 | 21.2 | 17.1 | cumple |
| V-44 | 8+614.54 | 8+638.16 | C-217 | 24.1 | 20.1 | cumple |
| V-45 | 8+719.50 | 8+737.56 | C-219 | 15.0 | 10.7 | cumple |
| V-46 | 8+786.99 | 8+873.59 | C-221, C-222, C-223 | 8.6 | 3.7 | no cumple |
| V-47 | 8+934.37 | 8+958.01 | C-225 | 8.0 | 3.1 | no cumple |
| V-48 | 9+012.51 | 9+029.81 | C-227 | 11.2 | 6.4 | mínimo absoluto |
| V-49 | 9+123.61 | 9+172.05 | C-229, C-230 | 8.9 | 4.0 | no cumple |
| V-50 | 9+253.38 | 9+279.44 | C-232 | 12.4 | 7.7 | mínimo absoluto |
| V-51 | 9+397.97 | 9+420.40 | C-237 | 8.3 | 3.4 | no cumple |
| V-52 | 9+472.16 | 9+534.23 | C-239, C-240 | 13.5 | 9.0 | cumple |
| V-53 | 9+746.96 | 9+809.88 | C-245, C-246 | 8.7 | 3.8 | no cumple |
| V-54 | 10+093.47 | 10+104.21 | C-252, C-253 | 6.4 | 1.5 | no cumple |
| V-55 | 10+193.27 | 10+197.10 | C-256 | 10.1 | 5.2 | no cumple |
| V-56 | 10+264.60 | 10+290.69 | C-258, C-259 | 8.0 | 3.1 | no cumple |
| V-57 | 10+420.12 | 10+436.14 | C-262 | 12.4 | 7.7 | mínimo absoluto |
| V-58 | 10+962.64 | 10+975.90 | C-271 | 17.0 | 12.8 | cumple |
| V-59 | 11+053.54 | 11+075.05 | C-274 | 11.7 | 6.9 | mínimo absoluto |

## 6.4 Tangentes

| Longitud de la tangente intermedia | Cantidad |
|------------------------|------|
| 0 (curvas enlazadas) | 48 |
| 0 a 20 m | 143 |
| 20 a 56 m | 75 |
| 56 a 111 m | 15 |
| más de 111 m | 0 |

Las 8 tangentes que cumplen la Tabla 302.01 son:

| Entre curvas | Longitud (m) | Mínimo exigido (m) | Tipo |
|---------|------|------|------|
| C-10 y C-11 | 56.4 | 56 | curvas en S |
| C-69 y C-70 | 70.2 | 56 | curvas en S |
| C-75 y C-76 | 61.0 | 56 | curvas en S |
| C-104 y C-105 | 57.6 | 56 | curvas en S |
| C-144 y C-145 | 84.4 | 56 | curvas en S |
| C-147 y C-148 | 63.6 | 56 | curvas en S |
| C-151 y C-152 | 59.3 | 56 | curvas en S |
| C-203 y C-204 | 56.4 | 56 | curvas en S |

## 6.5 Sitios donde el eje se separa más de 2.5 m del trazo actual

Son los puntos a revisar en campo o en Civil 3D antes de aprobar el eje, por su posible afectación a edificaciones.

| Curva | Prog. PC | Prog. PT | Norte PI | Este PI | R (m) | Separación máx. (m) | Comentario |
|------|--------|--------|---------|---------|-----|------|----------------|
| C-87 | 3+546.27 | 3+555.57 | 9472520.056 | 611052.384 | 15.0 | 2.64 | cadena de curvas de radio variable en el trazo |
| C-88 | 3+556.48 | 3+575.37 | 9472511.901 | 611065.550 | 30.0 | 5.17 | cadena de curvas de radio variable en el trazo |
| C-89 | 3+576.66 | 3+593.02 | 9472493.487 | 611073.043 | 17.7 | 4.60 | cadena de curvas de radio variable en el trazo |
| C-90 | 3+594.56 | 3+630.59 | 9472468.891 | 611058.366 | 85.0 | 3.29 | cadena de curvas de radio variable en el trazo |
| C-91 | 3+631.88 | 3+658.59 | 9472449.657 | 611030.786 | 35.0 | 5.84 | cadena de curvas de radio variable en el trazo |
| C-92 | 3+659.79 | 3+681.17 | 9472453.707 | 611004.763 | 32.5 | 4.64 | cadena de curvas de radio variable en el trazo |
| C-176 | 7+179.93 | 7+189.35 | 9471716.611 | 608451.725 | 7.5 | 5.24 | cadena de curvas de radio variable en el trazo |
| C-177 | 7+189.70 | 7+208.14 | 9471730.601 | 608437.667 | 9.4 | 5.64 | cadena de curvas de radio variable en el trazo |
| C-178 | 7+209.27 | 7+243.40 | 9471700.434 | 608425.197 | 65.0 | 2.84 | cadena de curvas de radio variable en el trazo |
| C-179 | 7+251.22 | 7+253.03 | 9471674.476 | 608428.671 | 15.0 | 2.86 | cadena de curvas de radio variable en el trazo |
| C-265 | 10+519.90 | 10+639.81 | 9471641.793 | 607478.766 | 70.0 | 2.92 | cadena de curvas de radio variable en el trazo |

## 6.6 Curvas compuestas (policéntricas) y curvas inversas enlazadas sin tangente

El eje tiene 42 grupos de curvas consecutivas sin tangente intermedia, con 48 uniones curva-curva: 28 entre curvas del mismo sentido (curvas compuestas) y 20 entre curvas de sentido contrario (curvas inversas enlazadas, S sin tangente). Por número de centros: 23 compuesta de dos centros, 15 inversas enlazadas (S sin tangente), 2 mixta (compuesta + inversa), 1 policéntrica de tres centros, 1 inversas enlazadas (3 curvas). Los grupos provienen de dos orígenes: los que ya existían en el trazo (cadenas de curvatura variable) y los creados por la pasada de tangentes al reemplazar tangentes cortas entre curvas del mismo sentido (Tópico 302.06.03).

**Parte de la norma que rige estos casos especiales.** Los grupos de curvas sin tangente intermedia no son geometría ordinaria: la DG-2018 los regula como caso excepcional en el Tópico 302.06 "Curvas compuestas" (302.06.01 Definición; 302.06.02 Caso excepcional, que exige "aclarar las razones, técnico-económicas u otras, que justifican el empleo de dos curvas continuas de radio diverso" y fija las tres condiciones de la policéntrica de tres centros; 302.06.03 Curvas vecinas del mismo sentido, que admite la policéntrica cuando la tangente sería menor de 400 m; 302.06.04 Configuraciones no recomendables, Figura 302.12). Lo complementan el Tópico 302.04.05 "Coordinación entre curvas circulares" con la Tabla 302.08 (grupo 2: Segunda y Tercera Clase) para la relación de radios, y el Tópico 302.08 "Transición de peralte" para el peralte entre arcos. Para las curvas inversas enlazadas rigen el Tópico 302.02 "Consideraciones de diseño" (curvas opuestas sin espiral: la tangente debe permitir la transición del peralte) y la Tabla 302.01 (tangente mínima en S). Cuando el grupo incluye radios menores de 45 m rigen además el Tópico 204.03 (velocidad específica) y la Tabla 302.02 con 30 km/h, y si incluye radios menores de 25 m, el Tópico 302.07 "Curvas de vuelta" y la Tabla 302.12. El Tópico 502.07.02 "Curvas compuestas" pertenece al diseño de intersecciones y no se aplica al eje. La justificación técnico-económica que pide el 302.06.02 es, en este proyecto, seguir el trazo existente en zona poblada para evitar expropiaciones y, en los grupos creados por la pasada de tangentes, sustituir una tangente corta entre curvas del mismo sentido (302.06.03); así debe quedar en el expediente.

Criterios de la DG-2018 aplicados a cada unión:

1. Tópico 302.06.01: "Consisten en dos o más curvas simples de diferente radio, orientadas en la misma dirección, y dispuestas una a continuación de la otra. En general, se evitará el empleo de curvas compuestas, tratando de reemplazarlas por una sola curva."
2. Tópico 302.06.02 (caso excepcional, policéntrica): "El radio de una de las curvas no será mayor de 1.5 veces el radio de la otra"; "se empleará una transición de peralte determinada acorde a lo establecido en el Tópico 302.08"; "Para una sucesión de curvas de radio decreciente cada curva debe ser de longitud suficiente para permitir una desaceleración gradual."
3. Tópico 302.04.05 y Tabla 302.08 (grupo 2, Segunda y Tercera Clase): rango admisible del radio de salida en función del radio de entrada para curvas enlazadas sin tangente o con tangente ≤ 200 m. La tabla empieza en 40 m de radio de entrada y nunca admite un radio de salida menor de 50 m; en la tabla el máximo es 1.5 veces el radio de entrada y el mínimo es el radio de entrada entre 1.5, con piso de 50 m.
4. Tópico 302.08: transición de peralte con ipmáx = 1.8 − 0.01·V = 1.4 % y Lmín = (pf − pi)/ipmáx · B, con B = 3.0 m (media calzada de 6.00 m girando sobre el eje). El peralte de cada curva se toma de la tabla "DG2018 _PMax 12%" del archivo de criterios para 40 km/h (12 % para R ≤ 45 m). En una unión compuesta la diferencia de peralte es |p2 − p1|; en una unión inversa el peralte se invierte y la diferencia es p1 + p2. La transición debe desarrollarse dentro de los arcos, por lo que se compara con sus longitudes.
5. Curvas inversas: Tabla 302.01 (56 m de tangente mínima en S a 40 km/h) y Tópico 302.02 Consideraciones de diseño ("Las curvas sucesivas en sentidos opuestos, dotadas de curvas de transición, deberán tener sus extremos coincidentes o separados por cortas extensiones en tangente. En el caso de curvas opuestas sin espiral, la extensión mínima de la tangente intermedia deberá permitir la transición del peralte"). Con tangente nula no se cumple; la solución normativa es una tangente de 56 m o clotoides de vértice, ambas fuera del trazo actual.
6. Desaceleración (criterio adoptado: la DG-2018 solo fija 3.4 m/s² para el frenado de la distancia de parada, Tópico 205.01, que no es una desaceleración gradual): entre dos curvas compuestas de radio decreciente se verifica que el primer arco permita pasar de la velocidad específica de la curva de entrada a la de salida con una desaceleración de 1.0 m/s², es decir d = (v1² − v2²)/(2·1.0), con Ve = mín(40, √(127·R·0.29)) km/h.

### 6.6.1 Resumen por grupo

| Grupo | Tipo | Curvas | Entidades Civil 3D | Prog. inicio | Prog. fin | Radios (m) | Longitudes (m) | Δ total (°) | Relación máx. R/r | ≤ 1.5 (302.06.02) | Tabla 302.08 | Transición 302.08 | Desaceleración | Sep. máx. trazo (m) | Artículos DG-2018 que rigen | Origen y justificación (302.06.02) |
|----|------|------|------|------|------|------|------|----|----|----|----|----|----|----|----------|----------|
| P-1 | compuesta de dos centros | C-1, C-2 | 2, 3 | 0+021.88 | 0+063.94 | 38.83 / 7.10 | 30.3 / 11.8 | 139.7 | 5.47 | no cumple | fuera de tabla | cabe | no cumple | 1.16 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-2 | compuesta de dos centros | C-3, C-4 | 5, 6 | 0+086.92 | 0+130.86 | 44.97 / 22.70 | 24.7 / 19.2 | 80.0 | 1.98 | no cumple | no cumple | cabe | no cumple | 1.89 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-3 | inversas enlazadas (S sin tangente) | C-7, C-8 | 12, 13 | 0+182.60 | 0+199.09 | 10.75 / 6.00 | 7.9 / 8.6 | 124.1 | 1.79 | no cumple | fuera de tabla | no cabe | cumple | 1.15 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-4 | compuesta de dos centros | C-11, C-12 | 19, 20 | 0+286.17 | 0+336.27 | 13.10 / 40.00 | 30.0 / 20.1 | 160.1 | 3.05 | no cumple | fuera de tabla | cabe | cumple | 1.18 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-5 | inversas enlazadas (S sin tangente) | C-18, C-19 | 32, 33 | 0+582.34 | 0+637.85 | 39.90 / 8.07 | 54.2 / 1.3 | 87.2 | 4.94 | no cumple | fuera de tabla | cabe | cumple | 1.74 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-6 | compuesta de dos centros | C-21, C-22 | 37, 38 | 0+731.11 | 0+743.36 | 17.37 / 7.20 | 2.0 / 10.3 | 88.3 | 2.41 | no cumple | fuera de tabla | cabe | no cumple | 0.69 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-7 | inversas enlazadas (S sin tangente) | C-23, C-24 | 40, 41 | 0+754.72 | 0+787.29 | 29.88 / 35.00 | 24.0 / 8.6 | 60.0 | 1.17 | cumple | fuera de tabla | no cabe | cumple | 0.97 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 204.03 y Tabla 302.02 (Ve = 30 km/h) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-8 | compuesta de dos centros | C-28, C-29 | 49, 50 | 0+998.25 | 1+047.89 | 44.95 / 8.80 | 32.4 / 17.2 | 153.4 | 5.11 | no cumple | no cumple | cabe | no cumple | 0.86 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-9 | inversas enlazadas (S sin tangente) | C-37, C-38 | 66, 67 | 1+429.56 | 1+517.33 | 24.20 / 40.48 | 44.8 / 43.0 | 166.9 | 1.67 | no cumple | fuera de tabla | cabe | cumple | 0.98 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-10 | inversas enlazadas (S sin tangente) | C-42, C-43 | 75, 76 | 1+632.76 | 1+678.99 | 38.90 / 39.31 | 24.1 / 22.2 | 67.8 | 1.01 | cumple | fuera de tabla | no cabe | cumple | 1.21 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 204.03 y Tabla 302.02 (Ve = 30 km/h) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-11 | compuesta de dos centros | C-50, C-51 | 90, 91 | 1+975.50 | 2+003.12 | 43.90 / 8.01 | 20.7 / 6.9 | 76.5 | 5.48 | no cumple | no cumple | cabe | no cumple | 0.27 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-12 | inversas enlazadas (S sin tangente) | C-52, C-53 | 93, 94 | 2+006.53 | 2+033.27 | 45.00 / 19.40 | 21.5 / 5.2 | 42.8 | 2.32 | no cumple | no cumple | no cabe | cumple | 0.76 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-13 | inversas enlazadas (S sin tangente) | C-54, C-55 | 96, 97 | 2+052.95 | 2+103.71 | 37.28 / 11.30 | 24.1 / 26.7 | 172.3 | 3.30 | no cumple | fuera de tabla | no cabe | cumple | 0.65 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-14 | compuesta de dos centros | C-66, C-67 | 119, 120 | 2+600.91 | 2+639.15 | 37.30 / 11.50 | 25.4 / 12.9 | 103.1 | 3.24 | no cumple | fuera de tabla | cabe | no cumple | 1.18 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-15 | compuesta de dos centros | C-82, C-83 | 150, 151 | 3+351.50 | 3+393.25 | 8.60 / 35.01 | 22.1 / 19.7 | 179.2 | 4.07 | no cumple | fuera de tabla | cabe | cumple | 1.18 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-16 | inversas enlazadas (S sin tangente) | C-92, C-93 | 169, 170 | 3+659.79 | 3+685.45 | 32.50 / 10.02 | 21.4 / 4.3 | 62.2 | 3.24 | no cumple | fuera de tabla | no cabe | cumple | 4.64 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-17 | inversas enlazadas (S sin tangente) | C-107, C-108 | 198, 199 | 4+235.07 | 4+273.17 | 44.89 / 12.40 | 17.9 / 20.2 | 116.1 | 3.62 | no cumple | no cumple | no cabe | cumple | 1.46 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-18 | compuesta de dos centros | C-109, C-110 | 201, 202 | 4+285.30 | 4+375.07 | 32.58 / 79.95 | 51.0 / 38.8 | 117.5 | 2.45 | no cumple | fuera de tabla | cabe | cumple | 0.90 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 204.03 y Tabla 302.02 (Ve = 30 km/h) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-19 | inversas enlazadas (S sin tangente) | C-116, C-117 | 214, 215 | 4+611.21 | 4+617.00 | 11.40 / 65.41 | 0.9 / 4.9 | 8.7 | 5.74 | no cumple | fuera de tabla | no cabe | cumple | 0.44 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-20 | mixta (compuesta + inversa) | C-118, C-119, C-120 | 217, 218, 219 | 4+617.10 | 4+620.11 | 6.31 / 6.00 / 24.06 | 0.8 / 0.9 / 1.4 | 18.6 | 4.01 | no cumple | fuera de tabla | no cabe | cumple | 0.33 | 302.06.01 a 302.06.03 (uniones compuestas) y 302.02 + Tabla 302.01 (uniones inversas); 302.04.05 y Tabla 302.08; 302.08; configuración no contemplada, requiere justificación expresa; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-21 | compuesta de dos centros | C-142, C-143 | 263, 264 | 5+543.82 | 5+622.99 | 85.00 / 12.91 | 72.4 / 6.7 | 78.8 | 6.58 | no cumple | no cumple | cabe | cumple | 0.63 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-22 | compuesta de dos centros | C-148, C-149 | 274, 275 | 5+915.15 | 5+999.21 | 50.00 / 487.28 | 11.8 / 72.2 | 22.0 | 9.75 | no cumple | no cumple | cabe | cumple | 1.36 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08 | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-23 | compuesta de dos centros | C-160, C-161 | 297, 298 | 6+598.90 | 6+645.57 | 44.69 / 11.85 | 11.8 / 34.9 | 183.8 | 3.77 | no cumple | no cumple | cabe | no cumple | 0.98 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-24 | inversas enlazadas (S sin tangente) | C-164, C-165 | 304, 305 | 6+703.22 | 6+735.83 | 30.00 / 33.14 | 16.8 / 15.8 | 59.4 | 1.10 | cumple | fuera de tabla | no cabe | cumple | 0.66 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 204.03 y Tabla 302.02 (Ve = 30 km/h) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-25 | compuesta de dos centros | C-166, C-167 | 307, 308 | 6+787.98 | 6+818.65 | 20.66 / 8.30 | 15.1 / 15.6 | 149.4 | 2.49 | no cumple | fuera de tabla | cabe | no cumple | 0.72 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-26 | compuesta de dos centros | C-169, C-170 | 312, 313 | 6+874.00 | 6+899.13 | 13.97 / 34.00 | 13.9 / 11.3 | 75.8 | 2.43 | no cumple | fuera de tabla | cabe | cumple | 0.71 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-27 | inversas enlazadas (S sin tangente) | C-175, C-176 | 323, 324 | 7+175.15 | 7+189.35 | 6.00 / 7.52 | 4.8 / 9.4 | 117.4 | 1.25 | cumple | fuera de tabla | no cabe | cumple | 5.24 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-28 | compuesta de dos centros | C-179, C-180 | 330, 331 | 7+251.22 | 7+267.24 | 15.00 / 42.46 | 1.8 / 14.2 | 26.1 | 2.83 | no cumple | fuera de tabla | cabe | cumple | 2.86 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-29 | compuesta de dos centros | C-182, C-183 | 335, 336 | 7+350.50 | 7+388.80 | 7.97 / 23.00 | 21.1 / 17.2 | 194.5 | 2.89 | no cumple | fuera de tabla | cabe | cumple | 0.56 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-30 | compuesta de dos centros | C-184, C-185 | 338, 339 | 7+405.80 | 7+464.71 | 85.00 / 14.34 | 43.1 / 15.8 | 92.3 | 5.93 | no cumple | no cumple | cabe | cumple | 0.38 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-31 | policéntrica de tres centros | C-188, C-189, C-190 | 345, 346, 347 | 7+573.47 | 7+608.02 | 8.89 / 7.90 / 20.48 | 3.0 / 18.4 / 13.1 | 189.7 | 2.59 | no cumple | fuera de tabla | cabe | cumple | 0.63 | 302.06.02 (policéntrica de tres centros: relación 1.5, transición 302.08, longitud para desacelerar); 302.04.05 y Tabla 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-32 | compuesta de dos centros | C-192, C-193 | 351, 352 | 7+687.90 | 7+722.87 | 11.40 / 39.19 | 21.2 / 13.7 | 126.9 | 3.44 | no cumple | fuera de tabla | cabe | cumple | 0.27 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-33 | inversas enlazadas (3 curvas) | C-196, C-197, C-198 | 358, 359, 360 | 7+845.20 | 7+852.51 | 10.80 / 8.02 / 48.12 | 2.0 / 1.3 / 4.1 | 24.5 | 6.00 | no cumple | fuera de tabla | no cabe | cumple | 1.00 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-34 | compuesta de dos centros | C-221, C-222 | 406, 407 | 8+786.99 | 8+823.26 | 8.60 / 24.30 | 20.7 / 15.6 | 174.7 | 2.83 | no cumple | fuera de tabla | cabe | cumple | 1.14 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-35 | inversas enlazadas (S sin tangente) | C-224, C-225 | 411, 412 | 8+891.15 | 8+958.01 | 39.59 / 8.00 | 43.2 / 23.6 | 231.8 | 4.95 | no cumple | fuera de tabla | cabe | cumple | 1.04 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-36 | compuesta de dos centros | C-230, C-231 | 422, 423 | 9+164.40 | 9+236.46 | 10.74 / 39.70 | 7.7 / 64.4 | 133.8 | 3.70 | no cumple | fuera de tabla | cabe | cumple | 0.65 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-37 | compuesta de dos centros | C-236, C-237 | 433, 434 | 9+394.24 | 9+420.40 | 53.35 / 8.30 | 3.7 / 22.4 | 158.9 | 6.43 | no cumple | no cumple | cabe | no cumple | 1.68 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-38 | inversas enlazadas (S sin tangente) | C-238, C-239 | 436, 437 | 9+438.02 | 9+478.74 | 44.98 / 13.50 | 34.1 / 6.6 | 71.4 | 3.33 | no cumple | no cumple | no cabe | cumple | 1.25 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-39 | mixta (compuesta + inversa) | C-251, C-252, C-253, C-254, C-255 | 461, 462, 463, 464, 465 | 10+039.66 | 10+137.32 | 229.40 / 7.51 / 6.40 / 28.02 / 28.83 | 53.8 / 2.5 / 8.2 / 26.6 / 6.5 | 173.6 | 30.55 | no cumple | no cumple | no cabe | cumple | 1.99 | 302.06.01 a 302.06.03 (uniones compuestas) y 302.02 + Tabla 302.01 (uniones inversas); 302.04.05 y Tabla 302.08; 302.08; configuración no contemplada, requiere justificación expresa; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-40 | compuesta de dos centros | C-259, C-260 | 473, 474 | 10+272.28 | 10+332.15 | 7.98 / 60.00 | 18.4 / 41.5 | 171.8 | 7.52 | no cumple | fuera de tabla | cabe | cumple | 0.82 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |
| P-41 | inversas enlazadas (S sin tangente) | C-263, C-264 | 480, 481 | 10+440.76 | 10+491.06 | 45.00 / 41.61 | 41.6 / 8.7 | 64.9 | 1.08 | cumple | no cumple | no cabe | cumple | 2.00 | 302.02 Consideraciones de diseño (curvas opuestas sin espiral); Tabla 302.01 (L mín. S = 56 m); 302.04.05 y Tabla 302.08; 302.08; 204.03 y Tabla 302.02 (Ve = 30 km/h) | trazo existente: cadena de curvatura variable; se mantiene para no expropiar (302.06.02) |
| P-42 | compuesta de dos centros | C-273, C-274 | 499, 500 | 11+020.47 | 11+075.05 | 50.00 / 11.65 | 33.1 / 21.5 | 143.7 | 4.29 | no cumple | no cumple | cabe | no cumple | 1.13 | 302.06.01 a 302.06.03 (curva compuesta, caso excepcional); 302.04.05 y Tabla 302.08; 302.08; 302.07 y Tabla 302.12 (curva de vuelta) | pasada de tangentes: sustituye una tangente corta entre curvas del mismo sentido (302.06.03) |

### 6.6.2 Detalle de cada unión curva-curva

| Grupo | Unión | Relación | R entrada (m) | R salida (m) | R/r | Tabla 302.08 (rango admisible del R de salida) | p entrada / p salida (%) | Δp (%) | L mín. transición (m) | L arcos entrada / salida (m) | Transición | Ve entrada / salida (km/h) | Desaceleración |
|----|------|------|-----|-----|----|----------|------|----|-----|------|------|------|----------|
| P-1 | C-1 → C-2 | compuesta (mismo sentido) | 38.83 | 7.10 | 5.47 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 30.3 / 11.8 | cabe en cada arco | 38 / 16 | 38 -> 16 km/h: 45 m necesarios, 30 m disponibles: no cumple |
| P-2 | C-3 → C-4 | compuesta (mismo sentido) | 44.97 | 22.70 | 1.98 | 50 a 67 m: no cumple | 12.0 / 12.0 | 0.0 | 0.0 | 24.7 / 19.2 | cabe en cada arco | 40 / 29 | 40 -> 29 km/h: 29 m necesarios, 25 m disponibles: no cumple |
| P-3 | C-7 → C-8 | inversa (S) | 10.75 | 6.00 | 1.79 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 7.9 / 8.6 | no cabe (arcos cortos) | 20 / 15 | no aplica (curva inversa) |
| P-4 | C-11 → C-12 | compuesta (mismo sentido) | 13.10 | 40.00 | 3.05 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 30.0 / 20.1 | cabe en cada arco | 22 / 38 | no aplica |
| P-5 | C-18 → C-19 | inversa (S) | 39.90 | 8.07 | 4.94 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 54.2 / 1.3 | cabe repartida en los dos arcos | 38 / 17 | no aplica (curva inversa) |
| P-6 | C-21 → C-22 | compuesta (mismo sentido) | 17.37 | 7.20 | 2.41 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 2.0 / 10.3 | cabe en cada arco | 25 / 16 | 25 -> 16 km/h: 14 m necesarios, 2 m disponibles: no cumple |
| P-7 | C-23 → C-24 | inversa (S) | 29.88 | 35.00 | 1.17 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 24.0 / 8.6 | no cabe (arcos cortos) | 33 / 36 | no aplica (curva inversa) |
| P-8 | C-28 → C-29 | compuesta (mismo sentido) | 44.95 | 8.80 | 5.11 | 50 a 67 m: no cumple | 12.0 / 12.0 | 0.0 | 0.0 | 32.4 / 17.2 | cabe en cada arco | 40 / 18 | 40 -> 18 km/h: 49 m necesarios, 32 m disponibles: no cumple |
| P-9 | C-37 → C-38 | inversa (S) | 24.20 | 40.48 | 1.67 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 44.8 / 43.0 | cabe repartida en los dos arcos | 30 / 39 | no aplica (curva inversa) |
| P-10 | C-42 → C-43 | inversa (S) | 38.90 | 39.31 | 1.01 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 24.1 / 22.2 | no cabe (arcos cortos) | 38 / 38 | no aplica (curva inversa) |
| P-11 | C-50 → C-51 | compuesta (mismo sentido) | 43.90 | 8.01 | 5.48 | 50 a 66 m: no cumple | 12.0 / 12.0 | 0.0 | 0.0 | 20.7 / 6.9 | cabe en cada arco | 40 / 17 | 40 -> 17 km/h: 50 m necesarios, 21 m disponibles: no cumple |
| P-12 | C-52 → C-53 | inversa (S) | 45.00 | 19.40 | 2.32 | 50 a 67 m: no cumple | 12.0 / 12.0 | 24.0 | 51.4 | 21.5 / 5.2 | no cabe (arcos cortos) | 40 / 27 | no aplica (curva inversa) |
| P-13 | C-54 → C-55 | inversa (S) | 37.28 | 11.30 | 3.30 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 24.1 / 26.7 | no cabe (arcos cortos) | 37 / 20 | no aplica (curva inversa) |
| P-14 | C-66 → C-67 | compuesta (mismo sentido) | 37.30 | 11.50 | 3.24 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 25.4 / 12.9 | cabe en cada arco | 37 / 21 | 37 -> 21 km/h: 37 m necesarios, 25 m disponibles: no cumple |
| P-15 | C-82 → C-83 | compuesta (mismo sentido) | 8.60 | 35.01 | 4.07 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 22.1 / 19.7 | cabe en cada arco | 18 / 36 | no aplica |
| P-16 | C-92 → C-93 | inversa (S) | 32.50 | 10.02 | 3.24 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 21.4 / 4.3 | no cabe (arcos cortos) | 35 / 19 | no aplica (curva inversa) |
| P-17 | C-107 → C-108 | inversa (S) | 44.89 | 12.40 | 3.62 | 50 a 67 m: no cumple | 12.0 / 12.0 | 24.0 | 51.4 | 17.9 / 20.2 | no cabe (arcos cortos) | 40 / 21 | no aplica (curva inversa) |
| P-18 | C-109 → C-110 | compuesta (mismo sentido) | 32.58 | 79.95 | 2.45 | fuera de tabla (R entrada < 40 m) | 12.0 / 10.0 | 2.0 | 4.3 | 51.0 / 38.8 | cabe en cada arco | 35 / 40 | no aplica |
| P-19 | C-116 → C-117 | inversa (S) | 11.40 | 65.41 | 5.74 | fuera de tabla (R entrada < 40 m) | 12.0 / 11.2 | 23.2 | 49.7 | 0.9 / 4.9 | no cabe (arcos cortos) | 20 / 40 | no aplica (curva inversa) |
| P-20 | C-118 → C-119 | inversa (S) | 6.31 | 6.00 | 1.05 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 0.8 / 0.9 | no cabe (arcos cortos) | 15 / 15 | no aplica (curva inversa) |
| P-20 | C-119 → C-120 | compuesta (mismo sentido) | 6.00 | 24.06 | 4.01 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 0.9 / 1.4 | cabe en cada arco | 15 / 30 | no aplica |
| P-21 | C-142 → C-143 | compuesta (mismo sentido) | 85.00 | 12.91 | 6.58 | 57 a 128 m: no cumple | 9.6 / 12.0 | 2.4 | 5.1 | 72.4 / 6.7 | cabe en cada arco | 40 / 22 | 40 -> 22 km/h: 43 m necesarios, 72 m disponibles: cumple |
| P-22 | C-148 → C-149 | compuesta (mismo sentido) | 50.00 | 487.28 | 9.75 | 50 a 75 m: no cumple | 11.8 / 2.6 | 9.2 | 19.7 | 11.8 / 72.2 | cabe repartida en los dos arcos | 40 / 40 | no aplica |
| P-23 | C-160 → C-161 | compuesta (mismo sentido) | 44.69 | 11.85 | 3.77 | 50 a 67 m: no cumple | 12.0 / 12.0 | 0.0 | 0.0 | 11.8 / 34.9 | cabe en cada arco | 40 / 21 | 40 -> 21 km/h: 45 m necesarios, 12 m disponibles: no cumple |
| P-24 | C-164 → C-165 | inversa (S) | 30.00 | 33.14 | 1.10 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 16.8 / 15.8 | no cabe (arcos cortos) | 33 / 35 | no aplica (curva inversa) |
| P-25 | C-166 → C-167 | compuesta (mismo sentido) | 20.66 | 8.30 | 2.49 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 15.1 / 15.6 | cabe en cada arco | 28 / 17 | 28 -> 17 km/h: 18 m necesarios, 15 m disponibles: no cumple |
| P-26 | C-169 → C-170 | compuesta (mismo sentido) | 13.97 | 34.00 | 2.43 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 13.9 / 11.3 | cabe en cada arco | 23 / 35 | no aplica |
| P-27 | C-175 → C-176 | inversa (S) | 6.00 | 7.52 | 1.25 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 4.8 / 9.4 | no cabe (arcos cortos) | 15 / 17 | no aplica (curva inversa) |
| P-28 | C-179 → C-180 | compuesta (mismo sentido) | 15.00 | 42.46 | 2.83 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 1.8 / 14.2 | cabe en cada arco | 24 / 40 | no aplica |
| P-29 | C-182 → C-183 | compuesta (mismo sentido) | 7.97 | 23.00 | 2.89 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 21.1 / 17.2 | cabe en cada arco | 17 / 29 | no aplica |
| P-30 | C-184 → C-185 | compuesta (mismo sentido) | 85.00 | 14.34 | 5.93 | 57 a 128 m: no cumple | 9.6 / 12.0 | 2.4 | 5.1 | 43.1 / 15.8 | cabe en cada arco | 40 / 23 | 40 -> 23 km/h: 41 m necesarios, 43 m disponibles: cumple |
| P-31 | C-188 → C-189 | compuesta (mismo sentido) | 8.89 | 7.90 | 1.13 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 3.0 / 18.4 | cabe en cada arco | 18 / 17 | 18 -> 17 km/h: 1 m necesarios, 3 m disponibles: cumple |
| P-31 | C-189 → C-190 | compuesta (mismo sentido) | 7.90 | 20.48 | 2.59 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 18.4 / 13.1 | cabe en cada arco | 17 / 27 | no aplica |
| P-32 | C-192 → C-193 | compuesta (mismo sentido) | 11.40 | 39.19 | 3.44 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 21.2 / 13.7 | cabe en cada arco | 20 / 38 | no aplica |
| P-33 | C-196 → C-197 | inversa (S) | 10.80 | 8.02 | 1.35 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 2.0 / 1.3 | no cabe (arcos cortos) | 20 / 17 | no aplica (curva inversa) |
| P-33 | C-197 → C-198 | inversa (S) | 8.02 | 48.12 | 6.00 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 1.3 / 4.1 | no cabe (arcos cortos) | 17 / 40 | no aplica (curva inversa) |
| P-34 | C-221 → C-222 | compuesta (mismo sentido) | 8.60 | 24.30 | 2.83 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 20.7 / 15.6 | cabe en cada arco | 18 / 30 | no aplica |
| P-35 | C-224 → C-225 | inversa (S) | 39.59 | 8.00 | 4.95 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 43.2 / 23.6 | cabe repartida en los dos arcos | 38 / 17 | no aplica (curva inversa) |
| P-36 | C-230 → C-231 | compuesta (mismo sentido) | 10.74 | 39.70 | 3.70 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 7.7 / 64.4 | cabe en cada arco | 20 / 38 | no aplica |
| P-37 | C-236 → C-237 | compuesta (mismo sentido) | 53.35 | 8.30 | 6.43 | 50 a 80 m: no cumple | 11.6 / 12.0 | 0.4 | 0.9 | 3.7 / 22.4 | cabe en cada arco | 40 / 17 | 40 -> 17 km/h: 50 m necesarios, 4 m disponibles: no cumple |
| P-38 | C-238 → C-239 | inversa (S) | 44.98 | 13.50 | 3.33 | 50 a 67 m: no cumple | 12.0 / 12.0 | 24.0 | 51.4 | 34.1 / 6.6 | no cabe (arcos cortos) | 40 / 22 | no aplica (curva inversa) |
| P-39 | C-251 → C-252 | compuesta (mismo sentido) | 229.40 | 7.51 | 30.55 | 153 a 344 m: no cumple | 4.8 / 12.0 | 7.2 | 15.4 | 53.8 / 2.5 | cabe repartida en los dos arcos | 40 / 17 | 40 -> 17 km/h: 51 m necesarios, 54 m disponibles: cumple |
| P-39 | C-252 → C-253 | inversa (S) | 7.51 | 6.40 | 1.17 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 2.5 / 8.2 | no cabe (arcos cortos) | 17 / 15 | no aplica (curva inversa) |
| P-39 | C-253 → C-254 | compuesta (mismo sentido) | 6.40 | 28.02 | 4.38 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 0.0 | 0.0 | 8.2 / 26.6 | cabe en cada arco | 15 / 32 | no aplica |
| P-39 | C-254 → C-255 | inversa (S) | 28.02 | 28.83 | 1.03 | fuera de tabla (R entrada < 40 m) | 12.0 / 12.0 | 24.0 | 51.4 | 26.6 / 6.5 | no cabe (arcos cortos) | 32 / 33 | no aplica (curva inversa) |
| P-40 | C-259 → C-260 | compuesta (mismo sentido) | 7.98 | 60.00 | 7.52 | fuera de tabla (R entrada < 40 m) | 12.0 / 11.4 | 0.6 | 1.3 | 18.4 / 41.5 | cabe en cada arco | 17 / 40 | no aplica |
| P-41 | C-263 → C-264 | inversa (S) | 45.00 | 41.61 | 1.08 | 50 a 68 m: no cumple | 12.0 / 12.0 | 24.0 | 51.4 | 41.6 / 8.7 | no cabe (arcos cortos) | 40 / 39 | no aplica (curva inversa) |
| P-42 | C-273 → C-274 | compuesta (mismo sentido) | 50.00 | 11.65 | 4.29 | 50 a 75 m: no cumple | 11.8 / 12.0 | 0.2 | 0.4 | 33.1 / 21.5 | cabe en cada arco | 40 / 21 | 40 -> 21 km/h: 45 m necesarios, 33 m disponibles: no cumple |

Balance: 10 de 48 uniones cumplen la relación de radios 1.5 del Tópico 302.06.02; 0 cumplen el rango de la Tabla 302.08, 34 quedan fuera de la tabla por tener radio de entrada menor de 40 m y las demás no cumplen; la transición de peralte cabe dentro de los arcos en 31 uniones; 10 uniones de radio decreciente no permiten la desaceleración gradual con el criterio adoptado. Las 20 uniones inversas incumplen la tangente mínima de 56 m de la Tabla 302.01 por construcción.

Tratamiento recomendado:

- Grupos de tres o más curvas (P-20 (mixta (compuesta + inversa)), P-31 (policéntrica de tres centros), P-33 (inversas enlazadas (3 curvas)), P-39 (mixta (compuesta + inversa))): la DG-2018 solo contempla expresamente la policéntrica de tres centros del mismo sentido (302.06.02); los grupos mixtos y los de cuatro o más curvas deben simplificarse en la revisión del eje, salvo justificación expresa en el expediente.
- Uniones con R/r > 1.5: ajustar uno de los dos radios (subir el menor o bajar el mayor) dentro de la tolerancia de separación del trazo, o justificar la excepción con las razones técnico-económicas que pide el Tópico 302.06.02.
- Uniones inversas sin tangente: señalizar como curvas sucesivas y, donde el peralte no cabe, diseñar la transición repartida entre los dos arcos con pérdida de peralte en sus extremos; la corrección geométrica (tangente de 56 m o clotoides) implica expropiación.
- En Civil 3D, al crear la alineación desde la polilínea, cada curva de estos grupos queda como entidad fija; el script de Dynamo las reconstruye como curva flotante + curva libre para poder editarlas, y el cálculo de peralte con el archivo de criterios debe revisarse en estas uniones porque Civil 3D reparte la transición entre arcos contiguos.

# 7. Pasada de tangentes (Tabla 302.01 y Tópico 302.06.03)

Sobre el eje ajustado al trazo se aplicó una pasada para respetar las longitudes de tangente donde fuera posible, con una separación máxima adicional respecto al trazo de 1.5 m. Reglas aplicadas:

1. Curvas consecutivas del mismo sentido separadas por una tangente menor de 111 m: se reemplazan por una sola curva circular si cabe dentro de la tolerancia; si no, se convierten en curva compuesta (policéntrica) elevando el radio de una de ellas hasta eliminar la tangente intermedia, solución que el Tópico 302.06.03 admite excepcionalmente. Nunca se recorta una tangente vecina entre curvas en S.
2. Curvas en S con tangente menor de 56 m: se reducen los radios de ambas curvas, sin bajar de 45 m, hasta abrir la tangente a 56 m, siempre que la separación respecto al trazo no supere la tolerancia.
3. Las deflexiones menores de 12° cuya supresión desplaza el eje menos de 1.0 m se absorbieron en la tangente desde el ajuste base, lo que alarga las tangentes y reduce el número de curvas.

| Indicador | Antes de la pasada | Después |
|------------------------------|---------|---------|
| Número de curvas | 324 | 282 |
| Pares del mismo sentido con tangente corta (0 < L < 111 m) | 125 | 70 |
| Pares del mismo sentido resueltos como curva compuesta (sin tangente) | 11 | 24 |
| Pares del mismo sentido con tangente ≥ 111 m | 0 | 0 |
| Pares en S con tangente ≥ 56 m | 4 | 8 |
| Pares en S con tangente entre 20 y 56 m | 46 | 48 |
| Pares en S con tangente menor de 20 m (incluye 0) | 137 | 131 |

Resultado de la pasada: 42 fusiones en una sola curva, 17 pares convertidos en curva compuesta, 70 pares del mismo sentido que no admiten ninguna de las dos soluciones dentro de la tolerancia, 2 tangentes en S abiertas a 56 m y 177 que no pueden abrirse sin bajar de 45 m de radio o sin salirse del trazo más de 1.5 m.

Las tangentes en S son el incumplimiento que queda. Para abrir 56 m entre dos curvas de 45 m de radio y 40° de deflexión los PIs deben distar unos 90 m, y en este trazo distan típicamente de 30 a 80 m. Solo se puede corregir saliéndose del trazo existente, es decir, con expropiación, o reduciendo la velocidad específica del sector.

# 8. Conclusiones y recomendaciones

1. El eje cumple el radio mínimo de la DG-2018 (45 m a 40 km/h, peralte 12 %) en 146 de 282 curvas. En 51 curvas se adopta radio excepcional con velocidad específica de 30 km/h y en 85 se trata de curvas de vuelta o esquinas urbanas.
2. Las 34 curvas con radio interior menor de 6 m (zonas V-1, V-3 y otras indicadas en 6.3) no admiten justificación con la DG-2018. Se recomienda ampliar la plataforma en esos puntos o aceptar expropiaciones puntuales.
3. Los primeros 230 m (zona urbana de inicio) tienen geometría de calles, con radios de 6 a 22 m. Conviene tratar ese tramo como vía urbana con velocidad de 20 a 30 km/h.
4. Las clotoides, las tangentes mínimas y la longitud mínima de curva no se cumplen por la premisa de seguir el trazo existente. Debe dejarse constancia en el expediente, con la señalización vertical y horizontal correspondiente al Manual de Dispositivos de Control de Tránsito.
5. Hay 42 grupos de curvas enlazadas sin tangente (28 uniones compuestas y 20 inversas), detallados en el capítulo 6.6. La relación de radios 1.5 se cumple en 10 de 48 uniones; las que no cumplen deben corregirse ajustando radios o justificarse como caso excepcional (Tópico 302.06.02). Los grupos de tres o más curvas que no sean policéntricas puras deben simplificarse o justificarse.
6. Las tangentes en S que siguen por debajo de 56 m deben señalizarse como sector de curvas sucesivas; su corrección geométrica exige expropiación.
7. En Civil 3D, asociar al eje el archivo de criterios DG2018_Corregido_2.xml con velocidad 40 km/h; los triángulos de advertencia que queden marcan exactamente las curvas de los capítulos 6.2 y 6.3.
8. Verificar la visibilidad de parada (50 m) con banquetas en las curvas de radio menor a 60 m ubicadas en corte, según el Tópico 302.10.01.

# Anexo A. Tabla completa de curvas

| Curva | Prog. PI | Norte PI | Este PI | Δ (°) | Sent. | R (m) | T (m) | Lc (m) | E (m) | Prog. PC | Prog. PT | Sa (m) | Tang. sig. (m) | Sep. (m) | Clase |
|-----|--------|---------|---------|-----|---|-----|-----|-----|----|--------|--------|----|-----|----|---------|
| C-1 | 0+037.84 | 9472166.45 | 613022.23 | 44.7 | I | 38.83 | 16.0 | 30.3 | 3.15 | 0+021.88 | 0+052.16 | 3.56 | 0.0 | 1.16 | Excepcional |
| C-2 | 0+059.92 | 9472190.09 | 613024.16 | 95.0 | I | 7.10 | 7.8 | 11.8 | 3.41 | 0+052.16 | 0+063.94 | - | 23.0 | 1.08 | Vuelta |
| C-3 | 0+099.59 | 9472189.81 | 612980.76 | 31.5 | D | 44.97 | 12.7 | 24.7 | 1.75 | 0+086.92 | 0+111.62 | 3.11 | 0.0 | 1.89 | Normativa 12% |
| C-4 | 0+121.86 | 9472201.64 | 612961.14 | 48.6 | D | 22.70 | 10.2 | 19.2 | 2.20 | 0+111.62 | 0+130.86 | 6.04 | 11.9 | 1.76 | Vuelta |
| C-5 | 0+151.87 | 9472232.39 | 612955.53 | 12.2 | I | 85.00 | 9.1 | 18.1 | 0.48 | 0+142.80 | 0+160.87 | 1.75 | 0.6 | 0.21 | Normativa 8% |
| C-6 | 0+169.69 | 9472248.92 | 612948.68 | 36.4 | D | 25.00 | 8.2 | 15.9 | 1.32 | 0+161.47 | 0+177.36 | 5.47 | 5.2 | 0.43 | Excepcional |
| C-7 | 0+186.75 | 9472266.01 | 612952.91 | 42.2 | I | 10.75 | 4.2 | 7.9 | 0.77 | 0+182.60 | 0+190.52 | 18.57 | 0.0 | 0.36 | Vuelta |
| C-8 | 0+195.73 | 9472274.25 | 612948.47 | 81.8 | D | 6.00 | 5.2 | 8.6 | 1.94 | 0+190.52 | 0+199.09 | - | 2.1 | 1.15 | Vuelta |
| C-9 | 0+208.69 | 9472283.05 | 612960.37 | 35.0 | I | 23.80 | 7.5 | 14.5 | 1.15 | 0+201.19 | 0+215.73 | 5.75 | 0.5 | 0.45 | Vuelta |
| C-10 | 0+223.51 | 9472297.54 | 612965.22 | 51.6 | D | 15.00 | 7.3 | 13.5 | 1.66 | 0+216.25 | 0+229.77 | 9.71 | 56.4 | 2.11 | Vuelta |
| C-11 | 0+315.18 | 9472328.98 | 613052.39 | 131.4 | I | 13.10 | 29.0 | 30.0 | 18.73 | 0+286.17 | 0+316.21 | 11.77 | 0.0 | 1.18 | Vuelta |
| C-12 | 0+326.45 | 9472347.88 | 613017.99 | 28.7 | I | 40.00 | 10.2 | 20.1 | 1.29 | 0+316.21 | 0+336.27 | 3.47 | 23.1 | 0.21 | Excepcional |
| C-13 | 0+372.42 | 9472347.91 | 612971.58 | 19.7 | D | 75.00 | 13.0 | 25.8 | 1.12 | 0+359.39 | 0+385.20 | 1.95 | 30.8 | 0.69 | Normativa 8% |
| C-14 | 0+425.97 | 9472366.10 | 612920.95 | 12.6 | D | 90.00 | 9.9 | 19.8 | 0.55 | 0+416.04 | 0+435.82 | 1.66 | 0.6 | 0.17 | Normativa 8% |
| C-15 | 0+438.63 | 9472372.92 | 612910.18 | 16.4 | I | 15.00 | 2.2 | 4.3 | 0.16 | 0+436.46 | 0+440.77 | 9.71 | 19.6 | 0.15 | Vuelta |
| C-16 | 0+479.76 | 9472384.20 | 612870.60 | 46.7 | D | 45.00 | 19.4 | 36.7 | 4.01 | 0+460.34 | 0+497.01 | 3.10 | 17.3 | 1.55 | Normativa 12% |
| C-17 | 0+523.34 | 9472424.82 | 612849.55 | 22.8 | I | 45.00 | 9.1 | 17.9 | 0.90 | 0+514.28 | 0+532.16 | 3.10 | 50.2 | 0.29 | Normativa 12% |
| C-18 | 0+614.55 | 9472483.41 | 612779.33 | 77.8 | D | 39.90 | 32.2 | 54.2 | 11.38 | 0+582.34 | 0+636.54 | 3.47 | -0.0 | 1.74 | Excepcional |
| C-19 | 0+637.20 | 9472512.53 | 612794.60 | 9.3 | I | 8.07 | 0.7 | 1.3 | 0.03 | 0+636.54 | 0+637.85 | - | 40.6 | 0.74 | Vuelta |
| C-20 | 0+695.09 | 9472567.49 | 612812.81 | 40.5 | D | 45.00 | 16.6 | 31.8 | 2.96 | 0+678.50 | 0+710.30 | 3.10 | 20.8 | 0.70 | Normativa 12% |
| C-21 | 0+732.10 | 9472587.37 | 612845.66 | 6.5 | I | 17.37 | 1.0 | 2.0 | 0.03 | 0+731.11 | 0+733.09 | 8.10 | 0.0 | 0.45 | Vuelta |
| C-22 | 0+739.32 | 9472591.78 | 612851.37 | 81.7 | I | 7.20 | 6.2 | 10.3 | 2.32 | 0+733.09 | 0+743.36 | - | 11.4 | 0.69 | Vuelta |
| C-23 | 0+767.38 | 9472618.13 | 612836.50 | 45.9 | I | 29.88 | 12.7 | 24.0 | 2.57 | 0+754.72 | 0+778.67 | 4.58 | 0.0 | 0.97 | Excepcional |
| C-24 | 0+783.00 | 9472622.42 | 612820.06 | 14.1 | D | 35.00 | 4.3 | 8.6 | 0.27 | 0+778.67 | 0+787.29 | 3.93 | 59.5 | 0.39 | Excepcional |
| C-25 | 0+887.28 | 9472672.60 | 612728.60 | 84.0 | D | 45.00 | 40.5 | 66.0 | 15.55 | 0+846.76 | 0+912.74 | 3.10 | 3.1 | 1.56 | Normativa 12% |
| C-26 | 0+928.31 | 9472724.32 | 612750.29 | 31.9 | I | 43.60 | 12.5 | 24.3 | 1.75 | 0+915.84 | 0+940.13 | 3.20 | 8.0 | 1.38 | Excepcional |
| C-27 | 0+961.31 | 9472757.55 | 612744.92 | 21.3 | D | 70.00 | 13.2 | 26.0 | 1.23 | 0+948.14 | 0+974.18 | 2.08 | 24.1 | 0.33 | Normativa 8% |
| C-28 | 1+015.21 | 9472810.53 | 612756.32 | 41.3 | I | 44.95 | 17.0 | 32.4 | 3.09 | 0+998.25 | 1+030.68 | 3.11 | -0.0 | 0.86 | Normativa 12% |
| C-29 | 1+043.74 | 9472836.73 | 612741.68 | 112.0 | I | 8.80 | 13.1 | 17.2 | 6.94 | 1+030.68 | 1+047.89 | - | 20.1 | 0.65 | Vuelta |
| C-30 | 1+075.63 | 9472804.92 | 612716.14 | 19.3 | D | 45.00 | 7.7 | 15.2 | 0.65 | 1+067.96 | 1+083.15 | 3.10 | 2.1 | 0.33 | Normativa 12% |
| C-31 | 1+092.76 | 9472795.79 | 612701.47 | 10.8 | I | 80.00 | 7.6 | 15.1 | 0.36 | 1+085.21 | 1+100.27 | 1.84 | 20.4 | 0.07 | Normativa 8% |
| C-32 | 1+126.45 | 9472772.92 | 612676.67 | 14.7 | D | 45.00 | 5.8 | 11.6 | 0.37 | 1+120.64 | 1+132.20 | 3.10 | 9.1 | 0.34 | Normativa 12% |
| C-33 | 1+152.93 | 9472760.47 | 612653.23 | 21.9 | I | 60.00 | 11.6 | 22.9 | 1.11 | 1+141.33 | 1+164.24 | 2.39 | 20.2 | 0.25 | Normativa 8% |
| C-34 | 1+223.99 | 9472705.95 | 612607.21 | 55.6 | D | 75.00 | 39.6 | 72.8 | 9.80 | 1+184.41 | 1+257.24 | 1.95 | 62.9 | 0.53 | Normativa 8% |
| C-35 | 1+354.24 | 9472719.76 | 612471.34 | 74.3 | D | 45.00 | 34.1 | 58.3 | 11.45 | 1+320.15 | 1+378.49 | 3.10 | 26.6 | 0.93 | Normativa 12% |
| C-36 | 1+417.34 | 9472791.60 | 612458.78 | 30.4 | I | 45.00 | 12.2 | 23.9 | 1.63 | 1+405.12 | 1+428.99 | 3.10 | 0.6 | 1.18 | Normativa 12% |
| C-37 | 1+461.72 | 9472825.87 | 612429.69 | 106.1 | I | 24.20 | 32.2 | 44.8 | 16.04 | 1+429.56 | 1+474.36 | 5.65 | 0.0 | 0.98 | Vuelta |
| C-38 | 1+498.12 | 9472779.31 | 612398.74 | 60.8 | D | 40.48 | 23.8 | 43.0 | 6.46 | 1+474.36 | 1+517.33 | 3.43 | 22.3 | 0.76 | Excepcional |
| C-39 | 1+547.51 | 9472783.48 | 612344.96 | 67.7 | D | 11.70 | 7.8 | 13.8 | 2.39 | 1+539.66 | 1+553.49 | 14.45 | 15.5 | 0.49 | Vuelta |
| C-40 | 1+588.56 | 9472824.33 | 612331.80 | 66.4 | I | 29.90 | 19.6 | 34.6 | 5.83 | 1+569.00 | 1+603.64 | 4.58 | 4.3 | 0.61 | Excepcional |
| C-41 | 1+616.82 | 9472827.62 | 612299.23 | 22.3 | D | 45.00 | 8.9 | 17.5 | 0.86 | 1+607.97 | 1+625.46 | 3.10 | 7.3 | 0.51 | Normativa 12% |
| C-42 | 1+645.19 | 9472841.05 | 612274.00 | 35.4 | I | 38.90 | 12.4 | 24.1 | 1.94 | 1+632.76 | 1+656.82 | 3.56 | -0.0 | 1.21 | Excepcional |
| C-43 | 1+668.21 | 9472837.98 | 612250.37 | 32.3 | D | 39.31 | 11.4 | 22.2 | 1.62 | 1+656.82 | 1+678.99 | 3.52 | 11.0 | 0.38 | Excepcional |
| C-44 | 1+759.24 | 9472876.60 | 612167.27 | 103.1 | I | 55.00 | 69.2 | 99.0 | 33.43 | 1+689.99 | 1+788.95 | 2.58 | 1.8 | 1.57 | Normativa 8% |
| C-45 | 1+790.90 | 9472806.91 | 612152.66 | 1.3 | I | 11.60 | 0.1 | 0.3 | 0.00 | 1+790.77 | 1+791.03 | 14.73 | 26.6 | 0.05 | Vuelta |
| C-46 | 1+836.73 | 9472761.86 | 612144.28 | 23.9 | D | 90.00 | 19.1 | 37.6 | 2.00 | 1+817.65 | 1+855.25 | 1.66 | 29.1 | 1.03 | Normativa 8% |
| C-47 | 1+902.63 | 9472707.07 | 612106.66 | 29.3 | D | 70.00 | 18.3 | 35.8 | 2.36 | 1+884.31 | 1+920.15 | 2.08 | 5.5 | 0.43 | Normativa 8% |
| C-48 | 1+930.28 | 9472694.51 | 612081.13 | 11.8 | I | 45.00 | 4.7 | 9.3 | 0.24 | 1+925.63 | 1+934.90 | 3.10 | 12.0 | 0.17 | Normativa 12% |
| C-49 | 1+954.55 | 9472679.55 | 612061.98 | 19.2 | D | 45.00 | 7.6 | 15.1 | 0.64 | 1+946.92 | 1+962.03 | 3.10 | 13.5 | 0.16 | Normativa 12% |
| C-50 | 1+986.05 | 9472669.38 | 612032.02 | 27.0 | D | 43.90 | 10.5 | 20.7 | 1.25 | 1+975.50 | 1+996.20 | 3.18 | 0.0 | 0.17 | Excepcional |
| C-51 | 1+999.89 | 9472671.42 | 612017.93 | 49.5 | D | 8.01 | 3.7 | 6.9 | 0.81 | 1+996.20 | 2+003.12 | - | 3.4 | 0.27 | Vuelta |
| C-52 | 2+017.50 | 9472686.71 | 612008.29 | 27.4 | D | 45.00 | 11.0 | 21.5 | 1.32 | 2+006.53 | 2+028.05 | 3.10 | -0.0 | 0.76 | Normativa 12% |
| C-53 | 2+030.68 | 9472700.26 | 612007.14 | 15.4 | I | 19.40 | 2.6 | 5.2 | 0.18 | 2+028.05 | 2+033.27 | 7.15 | 19.7 | 0.17 | Vuelta |
| C-54 | 2+065.42 | 9472732.89 | 611995.11 | 37.0 | D | 37.28 | 12.5 | 24.1 | 2.03 | 2+052.95 | 2+077.03 | 3.70 | -0.0 | 0.65 | Excepcional |
| C-55 | 2+104.51 | 9472771.15 | 612006.63 | 135.3 | I | 11.30 | 27.5 | 26.7 | 18.42 | 2+077.03 | 2+103.71 | 15.69 | 3.5 | 0.39 | Vuelta |
| C-56 | 2+121.76 | 9472749.39 | 611966.63 | 20.6 | D | 80.00 | 14.5 | 28.7 | 1.31 | 2+107.24 | 2+135.97 | 1.84 | 6.1 | 0.24 | Normativa 8% |
| C-57 | 2+154.94 | 9472744.75 | 611933.46 | 32.0 | I | 45.00 | 12.9 | 25.1 | 1.81 | 2+142.04 | 2+167.17 | 3.10 | 1.6 | 0.60 | Normativa 12% |
| C-58 | 2+197.13 | 9472717.22 | 611900.60 | 86.8 | D | 30.00 | 28.4 | 45.4 | 11.28 | 2+168.78 | 2+214.21 | 4.56 | 14.0 | 1.24 | Excepcional |
| C-59 | 2+250.75 | 9472764.53 | 611856.19 | 48.5 | I | 50.00 | 22.5 | 42.4 | 4.85 | 2+228.21 | 2+270.56 | 2.82 | 54.4 | 1.33 | Normativa 8% |
| C-60 | 2+333.82 | 9472761.93 | 611770.43 | 88.4 | I | 9.10 | 8.9 | 14.0 | 3.60 | 2+324.96 | 2+339.01 | - | 0.4 | 0.94 | Vuelta |
| C-61 | 2+361.89 | 9472730.20 | 611770.53 | 29.7 | D | 85.00 | 22.5 | 44.0 | 2.93 | 2+339.36 | 2+383.40 | 1.75 | 0.6 | 0.34 | Normativa 8% |
| C-62 | 2+390.38 | 9472704.52 | 611756.00 | 16.2 | I | 45.00 | 6.4 | 12.7 | 0.45 | 2+383.98 | 2+396.70 | 3.10 | 18.6 | 0.57 | Normativa 12% |
| C-63 | 2+446.95 | 9472649.38 | 611742.96 | 43.2 | D | 80.00 | 31.7 | 60.3 | 6.05 | 2+415.26 | 2+475.61 | 1.84 | 36.6 | 0.54 | Normativa 8% |
| C-64 | 2+533.54 | 9472599.94 | 611668.21 | 42.4 | D | 55.00 | 21.3 | 40.7 | 3.98 | 2+512.23 | 2+552.89 | 2.58 | 1.6 | 0.45 | Normativa 8% |
| C-65 | 2+575.60 | 9472606.73 | 611624.72 | 71.4 | I | 29.40 | 21.1 | 36.6 | 6.79 | 2+554.49 | 2+591.10 | 4.65 | 9.8 | 0.37 | Excepcional |
| C-66 | 2+614.10 | 9472567.61 | 611604.35 | 38.9 | D | 37.30 | 13.2 | 25.4 | 2.26 | 2+600.91 | 2+626.27 | 3.70 | 0.0 | 1.18 | Excepcional |
| C-67 | 2+633.48 | 9472559.47 | 611585.64 | 64.2 | D | 11.50 | 7.2 | 12.9 | 2.07 | 2+626.27 | 2+639.15 | 15.03 | 8.1 | 0.37 | Vuelta |
| C-68 | 2+659.59 | 9472577.48 | 611564.66 | 30.8 | I | 45.00 | 12.4 | 24.2 | 1.67 | 2+647.22 | 2+671.38 | 3.10 | 12.4 | 0.74 | Normativa 12% |
| C-69 | 2+694.04 | 9472583.50 | 611530.13 | 25.8 | D | 45.00 | 10.3 | 20.2 | 1.16 | 2+683.75 | 2+703.99 | 3.10 | 70.2 | 0.95 | Normativa 12% |
| C-70 | 2+788.73 | 9472638.90 | 611452.91 | 63.0 | I | 23.80 | 14.6 | 26.2 | 4.12 | 2+774.14 | 2+800.32 | 5.75 | 21.5 | 0.63 | Vuelta |
| C-71 | 2+828.70 | 9472619.14 | 611414.75 | 17.3 | I | 45.00 | 6.8 | 13.6 | 0.52 | 2+821.85 | 2+835.45 | 3.10 | 12.6 | 0.31 | Normativa 12% |
| C-72 | 2+886.18 | 9472578.66 | 611373.81 | 69.5 | D | 55.00 | 38.2 | 66.7 | 11.95 | 2+848.01 | 2+914.74 | 2.58 | 6.4 | 1.02 | Normativa 8% |
| C-73 | 2+941.73 | 9472606.04 | 611314.68 | 41.1 | I | 55.00 | 20.6 | 39.4 | 3.73 | 2+921.14 | 2+960.55 | 2.58 | 23.5 | 0.40 | Normativa 8% |
| C-74 | 3+003.47 | 9472588.32 | 611253.69 | 75.6 | D | 25.00 | 19.4 | 33.0 | 6.63 | 2+984.09 | 3+017.06 | 5.47 | 19.3 | 0.57 | Excepcional |
| C-75 | 3+050.50 | 9472633.76 | 611226.77 | 16.9 | D | 95.00 | 14.1 | 28.0 | 1.04 | 3+036.38 | 3+064.42 | 1.59 | 61.0 | 0.64 | Normativa 8% |
| C-76 | 3+149.90 | 9472730.52 | 611203.13 | 97.0 | I | 21.70 | 24.5 | 36.7 | 11.04 | 3+125.38 | 3+162.11 | 6.33 | 5.7 | 1.29 | Vuelta |
| C-77 | 3+180.17 | 9472715.48 | 611163.31 | 30.6 | I | 45.00 | 12.3 | 24.1 | 1.66 | 3+167.84 | 3+191.90 | 3.10 | 19.5 | 0.58 | Normativa 12% |
| C-78 | 3+228.34 | 9472677.40 | 611132.85 | 21.4 | D | 90.00 | 17.0 | 33.6 | 1.59 | 3+211.36 | 3+244.92 | 1.66 | 5.7 | 0.15 | Normativa 8% |
| C-79 | 3+259.15 | 9472661.81 | 611105.82 | 21.6 | I | 45.00 | 8.6 | 16.9 | 0.81 | 3+250.58 | 3+267.51 | 3.10 | 9.5 | 0.32 | Normativa 12% |
| C-80 | 3+291.75 | 9472636.12 | 611085.42 | 89.0 | D | 15.00 | 14.7 | 23.3 | 6.02 | 3+277.02 | 3+300.31 | 9.71 | 2.3 | 0.91 | Vuelta |
| C-81 | 3+328.38 | 9472662.12 | 611051.43 | 50.2 | D | 55.00 | 25.8 | 48.2 | 5.73 | 3+302.62 | 3+350.80 | 2.58 | 0.7 | 0.61 | Normativa 8% |
| C-82 | 3+380.54 | 9472717.58 | 611049.12 | 147.0 | I | 8.60 | 29.0 | 22.1 | 21.69 | 3+351.50 | 3+373.56 | - | -0.0 | 0.39 | Vuelta |
| C-83 | 3+383.68 | 9472683.87 | 611029.18 | 32.2 | I | 35.01 | 10.1 | 19.7 | 1.43 | 3+373.56 | 3+393.25 | 3.93 | 16.4 | 1.18 | Excepcional |
| C-84 | 3+413.85 | 9472653.18 | 611030.05 | 10.5 | D | 45.00 | 4.2 | 8.3 | 0.19 | 3+409.69 | 3+417.97 | 3.10 | 0.8 | 0.25 | Normativa 12% |
| C-85 | 3+424.98 | 9472642.16 | 611028.32 | 10.1 | I | 70.00 | 6.2 | 12.4 | 0.27 | 3+418.78 | 3+431.15 | 2.08 | 39.1 | 0.36 | Normativa 8% |
| C-86 | 3+493.02 | 9472574.10 | 611029.76 | 21.5 | I | 120.00 | 22.8 | 45.0 | 2.15 | 3+470.23 | 3+515.28 | 1.29 | 31.0 | 0.22 | Normativa 8% |
| C-87 | 3+551.07 | 9472520.06 | 611052.38 | 35.5 | I | 15.00 | 4.8 | 9.3 | 0.75 | 3+546.27 | 3+555.57 | 9.71 | 0.9 | 2.64 | Vuelta |
| C-88 | 3+566.25 | 9472511.90 | 611065.55 | 36.1 | D | 30.00 | 9.8 | 18.9 | 1.55 | 3+556.48 | 3+575.37 | 4.56 | 1.3 | 5.17 | Excepcional |
| C-89 | 3+585.48 | 9472493.49 | 611073.04 | 53.0 | D | 17.70 | 8.8 | 16.4 | 2.08 | 3+576.66 | 3+593.02 | 7.93 | 1.5 | 4.60 | Vuelta |
| C-90 | 3+612.85 | 9472468.89 | 611058.37 | 24.3 | D | 85.00 | 18.3 | 36.0 | 1.94 | 3+594.56 | 3+630.59 | 1.75 | 1.3 | 3.29 | Normativa 8% |
| C-91 | 3+645.92 | 9472449.66 | 611030.79 | 43.7 | D | 35.00 | 14.0 | 26.7 | 2.71 | 3+631.88 | 3+658.59 | 3.93 | 1.2 | 5.84 | Excepcional |
| C-92 | 3+670.88 | 9472453.71 | 611004.76 | 37.7 | D | 32.50 | 11.1 | 21.4 | 1.84 | 3+659.79 | 3+681.17 | 4.22 | 0.0 | 4.64 | Excepcional |
| C-93 | 3+683.34 | 9472463.34 | 610995.64 | 24.5 | I | 10.02 | 2.2 | 4.3 | 0.23 | 3+681.17 | 3+685.45 | - | 29.7 | 1.50 | Vuelta |
| C-94 | 3+726.30 | 9472479.48 | 610955.76 | 27.8 | I | 45.00 | 11.1 | 21.8 | 1.35 | 3+715.18 | 3+736.98 | 3.10 | 24.6 | 1.14 | Normativa 12% |
| C-95 | 3+776.01 | 9472474.50 | 610905.86 | 32.2 | D | 50.00 | 14.5 | 28.1 | 2.05 | 3+761.56 | 3+789.70 | 2.82 | 45.1 | 0.36 | Normativa 8% |
| C-96 | 3+836.93 | 9472502.06 | 610850.68 | 5.5 | D | 45.00 | 2.2 | 4.4 | 0.05 | 3+834.75 | 3+839.11 | 3.10 | 4.4 | 0.43 | Normativa 12% |
| C-97 | 3+849.44 | 9472508.71 | 610840.08 | 12.3 | I | 55.00 | 5.9 | 11.8 | 0.32 | 3+843.52 | 3+855.30 | 2.58 | 13.2 | 0.14 | Normativa 8% |
| C-98 | 3+871.67 | 9472516.26 | 610819.12 | 4.6 | D | 80.00 | 3.2 | 6.4 | 0.06 | 3+868.47 | 3+874.87 | 1.84 | 49.0 | 0.14 | Normativa 8% |
| C-99 | 3+932.91 | 9472541.55 | 610763.34 | 14.8 | D | 70.00 | 9.1 | 18.0 | 0.59 | 3+923.84 | 3+941.88 | 2.08 | 0.6 | 0.27 | Normativa 8% |
| C-100 | 3+948.12 | 9472551.22 | 610751.47 | 31.7 | I | 20.00 | 5.7 | 11.0 | 0.79 | 3+942.45 | 3+953.50 | 6.91 | 11.8 | 0.60 | Vuelta |
| C-101 | 3+968.91 | 9472553.98 | 610730.57 | 9.1 | D | 45.00 | 3.6 | 7.2 | 0.14 | 3+965.33 | 3+972.49 | 3.10 | 17.1 | 0.24 | Normativa 12% |
| C-102 | 4+007.86 | 9472565.13 | 610693.24 | 24.2 | I | 85.00 | 18.2 | 35.9 | 1.93 | 3+989.63 | 4+025.54 | 1.75 | 14.1 | 0.23 | Normativa 8% |
| C-103 | 4+061.57 | 9472557.97 | 610639.45 | 23.2 | D | 106.70 | 21.9 | 43.2 | 2.22 | 4+039.67 | 4+082.87 | 1.43 | 14.4 | 1.44 | Normativa 8% |
| C-104 | 4+109.21 | 9472570.96 | 610592.99 | 29.6 | I | 45.00 | 11.9 | 23.3 | 1.55 | 4+097.31 | 4+120.58 | 3.10 | 57.6 | 0.83 | Normativa 12% |
| C-105 | 4+190.97 | 9472551.05 | 610513.15 | 31.8 | D | 45.00 | 12.8 | 25.0 | 1.79 | 4+178.16 | 4+203.12 | 3.10 | 8.0 | 0.94 | Normativa 12% |
| C-106 | 4+222.41 | 9472560.86 | 610482.58 | 28.2 | I | 45.00 | 11.3 | 22.1 | 1.40 | 4+211.11 | 4+233.26 | 3.10 | 1.8 | 0.51 | Normativa 12% |
| C-107 | 4+244.16 | 9472556.84 | 610460.74 | 22.9 | D | 44.89 | 9.1 | 17.9 | 0.91 | 4+235.07 | 4+253.00 | 3.11 | 0.0 | 0.25 | Excepcional |
| C-108 | 4+266.11 | 9472561.63 | 610439.07 | 93.2 | I | 12.40 | 13.1 | 20.2 | 5.65 | 4+253.00 | 4+273.17 | 12.90 | 12.1 | 1.46 | Vuelta |
| C-109 | 4+317.70 | 9472504.74 | 610429.79 | 89.7 | D | 32.58 | 32.4 | 51.0 | 13.37 | 4+285.30 | 4+336.30 | 4.21 | -0.0 | 0.90 | Excepcional |
| C-110 | 4+356.07 | 9472512.85 | 610378.25 | 27.8 | D | 79.95 | 19.8 | 38.8 | 2.41 | 4+336.30 | 4+375.07 | 1.85 | 31.0 | 0.38 | Normativa 8% |
| C-111 | 4+426.98 | 9472555.72 | 610320.80 | 45.3 | I | 50.00 | 20.9 | 39.6 | 4.19 | 4+406.09 | 4+445.66 | 2.82 | 39.0 | 1.48 | Normativa 8% |
| C-112 | 4+486.26 | 9472546.51 | 610260.01 | 4.1 | I | 45.00 | 1.6 | 3.2 | 0.03 | 4+484.64 | 4+487.88 | 3.10 | 16.2 | 0.17 | Normativa 12% |
| C-113 | 4+512.46 | 9472540.74 | 610234.46 | 13.6 | D | 70.00 | 8.3 | 16.6 | 0.49 | 4+504.13 | 4+520.70 | 2.08 | 1.3 | 0.16 | Normativa 8% |
| C-114 | 4+528.27 | 9472540.97 | 610218.57 | 45.4 | I | 15.00 | 6.3 | 11.9 | 1.26 | 4+521.99 | 4+533.88 | 9.71 | 13.6 | 0.19 | Vuelta |
| C-115 | 4+557.60 | 9472519.93 | 610197.19 | 25.5 | D | 45.00 | 10.2 | 20.0 | 1.13 | 4+547.43 | 4+567.43 | 3.10 | 43.8 | 1.27 | Normativa 12% |
| C-116 | 4+611.64 | 9472502.14 | 610145.81 | 4.3 | I | 11.40 | 0.4 | 0.9 | 0.01 | 4+611.21 | 4+612.07 | 15.35 | -0.0 | 0.44 | Vuelta |
| C-117 | 4+614.54 | 9472500.99 | 610143.15 | 4.3 | D | 65.41 | 2.5 | 4.9 | 0.05 | 4+612.07 | 4+617.00 | 2.21 | 0.1 | 0.15 | Normativa 8% |
| C-118 | 4+617.49 | 9472500.02 | 610140.36 | 7.0 | I | 6.31 | 0.4 | 0.8 | 0.01 | 4+617.10 | 4+617.87 | - | 0.0 | 0.33 | Vuelta |
| C-119 | 4+618.31 | 9472499.66 | 610139.62 | 8.4 | D | 6.00 | 0.4 | 0.9 | 0.02 | 4+617.87 | 4+618.75 | - | 0.0 | 0.11 | Vuelta |
| C-120 | 4+619.43 | 9472499.32 | 610138.55 | 3.2 | D | 24.06 | 0.7 | 1.4 | 0.01 | 4+618.75 | 4+620.11 | 5.69 | 1.0 | 0.13 | Vuelta |
| C-121 | 4+648.27 | 9472492.11 | 610110.63 | 30.3 | I | 100.00 | 27.1 | 53.0 | 3.61 | 4+621.16 | 4+674.11 | 1.52 | 6.3 | 0.31 | Normativa 8% |
| C-122 | 4+687.70 | 9472463.42 | 610081.75 | 18.4 | I | 45.00 | 7.3 | 14.4 | 0.59 | 4+680.42 | 4+694.86 | 3.10 | 6.5 | 0.13 | Normativa 12% |
| C-123 | 4+711.50 | 9472442.07 | 610070.96 | 72.6 | D | 13.80 | 10.1 | 17.5 | 3.32 | 4+701.37 | 4+718.85 | 10.88 | 23.4 | 0.46 | Vuelta |
| C-124 | 4+750.65 | 9472448.89 | 610029.59 | 21.3 | I | 45.00 | 8.4 | 16.7 | 0.79 | 4+742.21 | 4+758.90 | 3.10 | 23.5 | 0.22 | Normativa 12% |
| C-125 | 4+800.66 | 9472438.54 | 609980.47 | 44.2 | D | 45.00 | 18.3 | 34.7 | 3.57 | 4+782.39 | 4+817.09 | 3.10 | 2.7 | 1.65 | Normativa 12% |
| C-126 | 4+838.72 | 9472459.84 | 609946.75 | 103.1 | I | 15.00 | 18.9 | 27.0 | 9.14 | 4+819.81 | 4+846.81 | 9.71 | 14.8 | 0.99 | Vuelta |
| C-127 | 4+890.88 | 9472400.34 | 609926.10 | 123.8 | D | 15.60 | 29.2 | 33.7 | 17.53 | 4+861.65 | 4+895.37 | 9.23 | 18.0 | 1.31 | Vuelta |
| C-128 | 4+921.42 | 9472444.46 | 609892.80 | 90.1 | I | 8.00 | 8.0 | 12.6 | 3.32 | 4+913.41 | 4+925.99 | - | 11.3 | 0.26 | Vuelta |
| C-129 | 4+943.48 | 9472429.06 | 609872.47 | 8.3 | D | 85.00 | 6.2 | 12.3 | 0.22 | 4+937.30 | 4+949.63 | 1.75 | 24.4 | 0.18 | Normativa 8% |
| C-130 | 4+982.42 | 9472410.27 | 609838.34 | 17.4 | I | 55.00 | 8.4 | 16.7 | 0.64 | 4+973.99 | 4+990.71 | 2.58 | 19.1 | 0.19 | Normativa 8% |
| C-131 | 5+022.44 | 9472381.26 | 609810.57 | 10.3 | D | 140.00 | 12.6 | 25.2 | 0.57 | 5+009.84 | 5+034.99 | 1.13 | 43.1 | 0.12 | Normativa 8% |
| C-132 | 5+081.61 | 9472346.47 | 609762.63 | 8.9 | D | 45.00 | 3.5 | 7.0 | 0.14 | 5+078.09 | 5+085.12 | 3.10 | 69.8 | 0.27 | Normativa 12% |
| C-133 | 5+172.83 | 9472305.03 | 609681.36 | 20.3 | D | 100.00 | 17.9 | 35.4 | 1.58 | 5+154.96 | 5+190.32 | 1.52 | 15.7 | 1.16 | Normativa 8% |
| C-134 | 5+213.33 | 9472300.22 | 609640.77 | 18.3 | I | 45.00 | 7.3 | 14.4 | 0.58 | 5+206.06 | 5+220.47 | 3.10 | 15.0 | 0.87 | Normativa 12% |
| C-135 | 5+248.84 | 9472285.11 | 609608.50 | 12.7 | D | 120.00 | 13.3 | 26.6 | 0.74 | 5+235.49 | 5+262.07 | 1.29 | 31.5 | 0.24 | Normativa 8% |
| C-136 | 5+306.11 | 9472272.78 | 609552.45 | 9.6 | I | 150.00 | 12.6 | 25.1 | 0.53 | 5+293.53 | 5+318.64 | 1.07 | 7.8 | 0.17 | Normativa 8% |
| C-137 | 5+329.89 | 9472263.85 | 609530.35 | 8.8 | D | 45.00 | 3.5 | 6.9 | 0.13 | 5+326.43 | 5+333.34 | 3.10 | 20.2 | 0.23 | Normativa 12% |
| C-138 | 5+358.92 | 9472257.22 | 609502.07 | 13.6 | I | 45.00 | 5.4 | 10.7 | 0.32 | 5+353.54 | 5+364.25 | 3.10 | 15.8 | 0.29 | Normativa 12% |
| C-139 | 5+382.32 | 9472246.63 | 609481.15 | 5.9 | D | 45.00 | 2.3 | 4.6 | 0.06 | 5+380.00 | 5+384.63 | 3.10 | 59.4 | 0.21 | Normativa 12% |
| C-140 | 5+445.79 | 9472223.93 | 609421.87 | 4.4 | D | 45.00 | 1.7 | 3.5 | 0.03 | 5+444.06 | 5+447.52 | 3.10 | 45.7 | 0.25 | Normativa 12% |
| C-141 | 5+500.17 | 9472208.44 | 609369.74 | 17.6 | I | 45.00 | 7.0 | 13.8 | 0.53 | 5+493.21 | 5+507.02 | 3.10 | 36.8 | 0.68 | Normativa 12% |
| C-142 | 5+582.39 | 9472162.25 | 609301.59 | 48.8 | D | 85.00 | 38.6 | 72.4 | 8.34 | 5+543.82 | 5+616.24 | 1.75 | 0.0 | 0.63 | Normativa 8% |
| C-143 | 5+619.69 | 9472172.91 | 609260.94 | 30.0 | D | 12.91 | 3.5 | 6.7 | 0.45 | 5+616.24 | 5+622.99 | 12.05 | 4.7 | 0.28 | Vuelta |
| C-144 | 5+637.13 | 9472185.27 | 609248.42 | 21.4 | D | 50.00 | 9.5 | 18.7 | 0.89 | 5+627.67 | 5+646.36 | 2.82 | 84.4 | 0.21 | Normativa 8% |
| C-145 | 5+759.70 | 9472297.51 | 609198.60 | 80.4 | I | 34.20 | 28.9 | 48.0 | 10.58 | 5+730.80 | 5+778.80 | 4.02 | 22.1 | 0.42 | Excepcional |
| C-146 | 5+806.57 | 9472283.46 | 609143.68 | 14.3 | D | 45.00 | 5.7 | 11.3 | 0.35 | 5+800.91 | 5+812.17 | 3.10 | 4.7 | 0.48 | Normativa 12% |
| C-147 | 5+837.99 | 9472283.45 | 609112.20 | 82.6 | I | 24.00 | 21.1 | 34.6 | 7.94 | 5+816.91 | 5+851.51 | 5.70 | 63.6 | 1.09 | Vuelta |
| C-148 | 5+921.09 | 9472193.54 | 609100.53 | 13.5 | D | 50.00 | 5.9 | 11.8 | 0.35 | 5+915.15 | 5+926.97 | 2.82 | -0.0 | 0.47 | Normativa 8% |
| C-149 | 5+963.16 | 9472154.20 | 609085.48 | 8.5 | D | 487.28 | 36.2 | 72.2 | 1.34 | 5+926.97 | 5+999.21 | 0.41 | 5.3 | 1.36 | Normativa 8% |
| C-150 | 6+015.18 | 9472108.78 | 609059.84 | 12.1 | D | 100.00 | 10.6 | 21.2 | 0.56 | 6+004.56 | 6+025.73 | 1.52 | 40.1 | 0.52 | Normativa 8% |
| C-151 | 6+083.57 | 9472057.55 | 609014.42 | 22.3 | I | 90.00 | 17.8 | 35.1 | 1.74 | 6+065.79 | 6+100.89 | 1.66 | 59.3 | 0.70 | Normativa 8% |
| C-152 | 6+196.50 | 9471950.49 | 608977.09 | 48.8 | D | 80.00 | 36.3 | 68.1 | 7.84 | 6+160.23 | 6+228.33 | 1.84 | 7.5 | 0.88 | Normativa 8% |
| C-153 | 6+245.33 | 9471930.53 | 608927.71 | 23.8 | I | 45.00 | 9.5 | 18.7 | 0.99 | 6+235.83 | 6+254.56 | 3.10 | 22.0 | 0.59 | Normativa 12% |
| C-154 | 6+280.05 | 9471905.42 | 608903.34 | 8.9 | D | 45.00 | 3.5 | 7.0 | 0.14 | 6+276.53 | 6+283.55 | 3.10 | 41.0 | 0.26 | Normativa 12% |
| C-155 | 6+329.22 | 9471875.88 | 608864.01 | 11.8 | D | 45.00 | 4.7 | 9.3 | 0.24 | 6+324.55 | 6+333.84 | 3.10 | 0.8 | 0.32 | Normativa 12% |
| C-156 | 6+348.54 | 9471867.67 | 608846.49 | 14.4 | I | 110.00 | 13.9 | 27.6 | 0.87 | 6+334.68 | 6+362.25 | 1.40 | 18.3 | 0.26 | Normativa 8% |
| C-157 | 6+387.48 | 9471842.83 | 608816.30 | 14.4 | D | 55.00 | 6.9 | 13.8 | 0.44 | 6+380.54 | 6+394.35 | 2.58 | 36.8 | 0.54 | Normativa 8% |
| C-158 | 6+467.03 | 9471809.09 | 608744.19 | 77.1 | D | 45.00 | 35.9 | 60.6 | 12.56 | 6+431.14 | 6+491.73 | 3.10 | 35.9 | 1.93 | Normativa 12% |
| C-159 | 6+558.59 | 9471890.13 | 608681.03 | 26.8 | D | 130.00 | 31.0 | 60.9 | 3.64 | 6+527.59 | 6+588.45 | 1.21 | 10.4 | 0.94 | Normativa 8% |
| C-160 | 6+604.83 | 9471936.61 | 608671.90 | 15.1 | I | 44.69 | 5.9 | 11.8 | 0.39 | 6+598.90 | 6+610.69 | 3.12 | 0.0 | 0.29 | Excepcional |
| C-161 | 6+730.65 | 9472049.55 | 608616.27 | 168.7 | I | 11.85 | 120.0 | 34.9 | 108.70 | 6+610.69 | 6+645.57 | 14.08 | 2.0 | 0.98 | Vuelta |
| C-162 | 6+650.15 | 9471929.22 | 608648.38 | 16.1 | I | 18.40 | 2.6 | 5.2 | 0.18 | 6+647.54 | 6+652.72 | 7.58 | 4.8 | 0.15 | Vuelta |
| C-163 | 6+667.46 | 9471914.36 | 608657.34 | 25.0 | D | 45.00 | 10.0 | 19.7 | 1.09 | 6+657.48 | 6+677.13 | 3.10 | 26.1 | 0.39 | Normativa 12% |
| C-164 | 6+711.84 | 9471869.91 | 608662.04 | 32.1 | I | 30.00 | 8.6 | 16.8 | 1.21 | 6+703.22 | 6+720.01 | 4.56 | 0.0 | 0.66 | Excepcional |
| C-165 | 6+728.07 | 9471856.78 | 608672.34 | 27.4 | D | 33.14 | 8.1 | 15.8 | 0.97 | 6+720.01 | 6+735.83 | 4.14 | 52.1 | 0.21 | Excepcional |
| C-166 | 6+795.88 | 9471789.86 | 608685.06 | 41.9 | D | 20.66 | 7.9 | 15.1 | 1.46 | 6+787.98 | 6+803.08 | 6.67 | 0.0 | 0.72 | Vuelta |
| C-167 | 6+814.40 | 9471773.41 | 608675.12 | 107.5 | D | 8.30 | 11.3 | 15.6 | 5.73 | 6+803.08 | 6+818.65 | - | 9.7 | 0.44 | Vuelta |
| C-168 | 6+844.32 | 9471801.16 | 608650.67 | 32.4 | I | 55.00 | 16.0 | 31.1 | 2.28 | 6+828.33 | 6+859.45 | 2.58 | 14.5 | 0.42 | Normativa 8% |
| C-169 | 6+881.56 | 9471811.79 | 608614.09 | 56.8 | I | 13.97 | 7.6 | 13.9 | 1.91 | 6+874.00 | 6+887.86 | 10.69 | -0.0 | 0.71 | Vuelta |
| C-170 | 6+893.55 | 9471803.16 | 608604.03 | 19.0 | I | 34.00 | 5.7 | 11.3 | 0.47 | 6+887.86 | 6+899.13 | 4.04 | 24.1 | 0.25 | Excepcional |
| C-171 | 6+937.64 | 9471765.02 | 608581.69 | 45.2 | I | 34.50 | 14.4 | 27.2 | 2.87 | 6+923.27 | 6+950.51 | 3.99 | 1.0 | 0.47 | Excepcional |
| C-172 | 6+980.15 | 9471722.48 | 608592.99 | 55.1 | D | 55.00 | 28.7 | 52.9 | 7.03 | 6+951.48 | 7+004.34 | 2.58 | 20.3 | 0.50 | Normativa 8% |
| C-173 | 7+042.03 | 9471671.78 | 608550.16 | 30.0 | D | 65.00 | 17.4 | 34.0 | 2.29 | 7+024.62 | 7+058.64 | 2.22 | 26.1 | 0.40 | Normativa 8% |
| C-174 | 7+125.30 | 9471643.28 | 608471.08 | 90.7 | D | 40.00 | 40.5 | 63.3 | 16.93 | 7+084.79 | 7+148.13 | 3.47 | 27.0 | 1.02 | Excepcional |
| C-175 | 7+177.67 | 9471709.49 | 608448.16 | 45.7 | D | 6.00 | 2.5 | 4.8 | 0.51 | 7+175.15 | 7+179.93 | - | 0.0 | 1.08 | Vuelta |
| C-176 | 7+185.37 | 9471716.61 | 608451.72 | 71.7 | I | 7.52 | 5.4 | 9.4 | 1.76 | 7+179.93 | 7+189.35 | - | 0.4 | 5.24 | Vuelta |
| C-177 | 7+203.74 | 9471730.60 | 608437.67 | 112.4 | I | 9.40 | 14.0 | 18.4 | 7.50 | 7+189.70 | 7+208.14 | - | 1.1 | 5.64 | Vuelta |
| C-178 | 7+226.74 | 9471700.43 | 608425.20 | 30.1 | I | 65.00 | 17.5 | 34.1 | 2.31 | 7+209.27 | 7+243.40 | 2.22 | 7.8 | 2.84 | Normativa 8% |
| C-179 | 7+252.12 | 9471674.48 | 608428.67 | 6.9 | I | 15.00 | 0.9 | 1.8 | 0.03 | 7+251.22 | 7+253.03 | 9.71 | 0.0 | 2.86 | Vuelta |
| C-180 | 7+260.20 | 9471666.66 | 608430.70 | 19.2 | I | 42.46 | 7.2 | 14.2 | 0.60 | 7+253.03 | 7+267.24 | 3.28 | 79.2 | 0.62 | Excepcional |
| C-181 | 7+347.62 | 9471593.81 | 608479.26 | 17.1 | I | 8.00 | 1.2 | 2.4 | 0.09 | 7+346.41 | 7+348.81 | - | 1.7 | 2.08 | Vuelta |
| C-182 | 7+382.08 | 9471572.04 | 608505.99 | 151.7 | D | 7.97 | 31.6 | 21.1 | 24.60 | 7+350.50 | 7+371.59 | - | 0.0 | 0.56 | Vuelta |
| C-183 | 7+380.62 | 9471579.67 | 608466.11 | 42.9 | D | 23.00 | 9.0 | 17.2 | 1.71 | 7+371.59 | 7+388.80 | 5.96 | 17.0 | 0.43 | Vuelta |
| C-184 | 7+427.82 | 9471618.39 | 608437.67 | 29.0 | I | 85.00 | 22.0 | 43.1 | 2.80 | 7+405.80 | 7+448.88 | 1.75 | 0.0 | 0.38 | Normativa 8% |
| C-185 | 7+457.71 | 9471631.25 | 608409.63 | 63.3 | I | 14.34 | 8.8 | 15.8 | 2.50 | 7+448.88 | 7+464.71 | 10.31 | 9.2 | 0.21 | Vuelta |
| C-186 | 7+485.28 | 9471612.91 | 608386.66 | 28.3 | I | 45.00 | 11.3 | 22.2 | 1.41 | 7+473.94 | 7+496.15 | 3.10 | 11.7 | 0.31 | Normativa 12% |
| C-187 | 7+545.67 | 9471556.94 | 608362.77 | 86.9 | D | 40.00 | 37.9 | 60.6 | 15.08 | 7+507.80 | 7+568.45 | 3.47 | 5.0 | 0.51 | Excepcional |
| C-188 | 7+574.98 | 9471572.11 | 608321.04 | 19.3 | I | 8.89 | 1.5 | 3.0 | 0.13 | 7+573.47 | 7+576.47 | - | 0.0 | 0.63 | Vuelta |
| C-189 | 7+594.90 | 9471572.34 | 608301.10 | 133.6 | I | 7.90 | 18.4 | 18.4 | 12.15 | 7+576.47 | 7+594.89 | - | 0.0 | 0.52 | Vuelta |
| C-190 | 7+601.69 | 9471553.87 | 608318.29 | 36.7 | I | 20.48 | 6.8 | 13.1 | 1.10 | 7+594.89 | 7+608.02 | 6.74 | 23.1 | 0.33 | Vuelta |
| C-191 | 7+656.63 | 9471543.95 | 608372.80 | 54.1 | I | 50.00 | 25.5 | 47.2 | 6.15 | 7+631.09 | 7+678.31 | 2.82 | 9.6 | 0.94 | Normativa 8% |
| C-192 | 7+703.24 | 9471578.88 | 608409.22 | 106.8 | D | 11.40 | 15.3 | 21.2 | 7.71 | 7+687.90 | 7+709.14 | 15.36 | 0.0 | 0.27 | Vuelta |
| C-193 | 7+716.07 | 9471559.04 | 608419.34 | 20.1 | D | 39.19 | 6.9 | 13.7 | 0.61 | 7+709.14 | 7+722.87 | 3.53 | 9.7 | 0.13 | Excepcional |
| C-194 | 7+759.81 | 9471515.48 | 608424.65 | 25.6 | I | 120.00 | 27.2 | 53.5 | 3.05 | 7+732.59 | 7+786.12 | 1.29 | 24.1 | 0.99 | Normativa 8% |
| C-195 | 7+858.02 | 9471431.88 | 608477.90 | 149.4 | D | 13.10 | 47.8 | 34.1 | 36.48 | 7+810.20 | 7+844.35 | 11.77 | 0.8 | 1.48 | Vuelta |
| C-196 | 7+846.19 | 9471454.32 | 608433.60 | 10.5 | I | 10.80 | 1.0 | 2.0 | 0.05 | 7+845.20 | 7+847.18 | 18.20 | -0.0 | 0.32 | Vuelta |
| C-197 | 7+847.82 | 9471454.78 | 608432.04 | 9.1 | D | 8.02 | 0.6 | 1.3 | 0.03 | 7+847.18 | 7+848.46 | - | -0.0 | 0.23 | Vuelta |
| C-198 | 7+850.49 | 9471455.93 | 608429.63 | 4.8 | I | 48.12 | 2.0 | 4.1 | 0.04 | 7+848.46 | 7+852.51 | 2.92 | 55.9 | 1.00 | Normativa 12% |
| C-199 | 7+924.87 | 9471482.20 | 608360.03 | 83.8 | I | 18.30 | 16.4 | 26.8 | 6.29 | 7+908.44 | 7+935.22 | 7.63 | 21.6 | 1.02 | Vuelta |
| C-200 | 7+974.72 | 9471432.29 | 608334.78 | 71.2 | D | 25.00 | 17.9 | 31.1 | 5.75 | 7+956.81 | 7+987.89 | 5.47 | 5.5 | 0.40 | Excepcional |
| C-201 | 7+997.12 | 9471436.09 | 608307.91 | 9.5 | I | 45.00 | 3.7 | 7.5 | 0.15 | 7+993.39 | 8+000.84 | 3.10 | 7.5 | 0.15 | Normativa 12% |
| C-202 | 8+009.17 | 9471435.79 | 608295.84 | 2.0 | D | 45.00 | 0.8 | 1.6 | 0.01 | 8+008.39 | 8+009.95 | 3.10 | 25.9 | 0.02 | Normativa 12% |
| C-203 | 8+042.66 | 9471436.11 | 608262.36 | 10.4 | I | 75.00 | 6.8 | 13.6 | 0.31 | 8+035.86 | 8+049.41 | 1.95 | 56.4 | 0.67 | Normativa 8% |
| C-204 | 8+112.12 | 9471424.26 | 608193.88 | 15.9 | D | 45.00 | 6.3 | 12.5 | 0.43 | 8+105.85 | 8+118.31 | 3.10 | 2.4 | 0.64 | Normativa 12% |
| C-205 | 8+144.69 | 9471427.71 | 608161.41 | 97.1 | D | 21.20 | 24.0 | 35.9 | 10.81 | 8+120.71 | 8+156.62 | 6.49 | 26.2 | 1.16 | Vuelta |
| C-206 | 8+198.92 | 9471492.27 | 608176.44 | 56.5 | I | 30.00 | 16.1 | 29.6 | 4.05 | 8+182.81 | 8+212.38 | 4.56 | 30.5 | 0.47 | Excepcional |
| C-207 | 8+247.57 | 9471529.57 | 608141.23 | 11.8 | D | 45.00 | 4.7 | 9.3 | 0.24 | 8+242.92 | 8+252.20 | 3.10 | 6.0 | 0.30 | Normativa 12% |
| C-208 | 8+266.26 | 9471545.53 | 608131.44 | 22.8 | I | 40.00 | 8.1 | 15.9 | 0.81 | 8+258.18 | 8+274.12 | 3.47 | 1.0 | 0.53 | Excepcional |
| C-209 | 8+286.15 | 9471557.24 | 608115.10 | 27.5 | D | 45.00 | 11.0 | 21.6 | 1.32 | 8+275.15 | 8+296.72 | 3.10 | 18.3 | 0.21 | Normativa 12% |
| C-210 | 8+319.00 | 9471586.91 | 608100.04 | 10.1 | D | 45.00 | 4.0 | 7.9 | 0.18 | 8+315.01 | 8+322.96 | 3.10 | 9.0 | 0.23 | Normativa 12% |
| C-211 | 8+343.19 | 9471610.09 | 608093.05 | 14.3 | I | 90.00 | 11.3 | 22.4 | 0.70 | 8+331.92 | 8+354.35 | 1.66 | 27.3 | 1.00 | Normativa 8% |
| C-212 | 8+393.92 | 9471653.65 | 608066.81 | 27.6 | D | 50.00 | 12.3 | 24.1 | 1.49 | 8+381.64 | 8+405.73 | 2.82 | 15.6 | 0.28 | Normativa 8% |
| C-213 | 8+437.81 | 9471697.94 | 608064.12 | 59.2 | I | 29.10 | 16.5 | 30.1 | 4.36 | 8+421.29 | 8+451.35 | 4.70 | 40.6 | 0.47 | Excepcional |
| C-214 | 8+510.61 | 9471732.77 | 607996.81 | 63.8 | D | 30.00 | 18.7 | 33.4 | 5.34 | 8+491.94 | 8+525.35 | 4.56 | 31.1 | 0.55 | Excepcional |
| C-215 | 8+563.38 | 9471789.46 | 607997.95 | 22.3 | I | 35.00 | 6.9 | 13.6 | 0.67 | 8+556.48 | 8+570.11 | 3.93 | 0.4 | 0.42 | Excepcional |
| C-216 | 8+582.28 | 9471807.26 | 607991.07 | 29.3 | D | 45.00 | 11.7 | 23.0 | 1.51 | 8+570.54 | 8+593.52 | 3.10 | 21.0 | 0.45 | Normativa 12% |
| C-217 | 8+627.40 | 9471852.43 | 607997.51 | 56.2 | I | 24.10 | 12.9 | 23.6 | 3.21 | 8+614.54 | 8+638.16 | 5.68 | 1.3 | 1.04 | Vuelta |
| C-218 | 8+661.43 | 9471876.58 | 607970.65 | 40.3 | D | 60.00 | 22.0 | 42.2 | 3.91 | 8+639.43 | 8+681.60 | 2.39 | 37.9 | 0.72 | Normativa 8% |
| C-219 | 8+729.81 | 9471946.14 | 607961.16 | 69.0 | I | 15.00 | 10.3 | 18.1 | 3.20 | 8+719.50 | 8+737.56 | 9.71 | 10.2 | 0.64 | Vuelta |
| C-220 | 8+760.62 | 9471953.79 | 607928.69 | 32.0 | D | 45.00 | 12.9 | 25.1 | 1.81 | 8+747.73 | 8+772.83 | 3.10 | 14.2 | 0.78 | Normativa 12% |
| C-221 | 8+809.39 | 9471988.89 | 607893.86 | 138.0 | I | 8.60 | 22.4 | 20.7 | 15.40 | 8+786.99 | 8+807.70 | - | 0.0 | 1.14 | Vuelta |
| C-222 | 8+815.76 | 9471958.47 | 607895.33 | 36.7 | I | 24.30 | 8.1 | 15.6 | 1.30 | 8+807.70 | 8+823.26 | 5.63 | 26.4 | 0.64 | Vuelta |
| C-223 | 8+863.28 | 9471921.34 | 607925.88 | 68.6 | D | 20.00 | 13.6 | 23.9 | 4.21 | 8+849.64 | 8+873.59 | 6.91 | 17.6 | 0.48 | Vuelta |
| C-224 | 8+915.20 | 9471873.08 | 607898.97 | 62.6 | I | 39.59 | 24.0 | 43.2 | 6.73 | 8+891.15 | 8+934.37 | 3.50 | 0.0 | 0.73 | Excepcional |
| C-225 | 9+019.58 | 9471781.88 | 607959.13 | 169.3 | D | 8.00 | 85.2 | 23.6 | 77.58 | 8+934.37 | 8+958.01 | - | 18.4 | 1.04 | Vuelta |
| C-226 | 8+990.34 | 9471866.23 | 607877.28 | 50.7 | D | 29.40 | 13.9 | 26.0 | 3.13 | 8+976.42 | 9+002.42 | 4.65 | 10.1 | 0.90 | Excepcional |
| C-227 | 9+023.42 | 9471900.92 | 607881.25 | 88.5 | I | 11.20 | 10.9 | 17.3 | 4.44 | 9+012.51 | 9+029.81 | 16.08 | 33.5 | 0.65 | Vuelta |
| C-228 | 9+093.51 | 9471911.35 | 607807.37 | 67.8 | D | 45.00 | 30.2 | 53.2 | 9.20 | 9+063.30 | 9+116.52 | 3.10 | 7.1 | 0.94 | Normativa 12% |
| C-229 | 9+137.06 | 9471960.55 | 607794.90 | 113.0 | I | 8.90 | 13.5 | 17.6 | 7.23 | 9+123.61 | 9+141.16 | - | 23.2 | 0.76 | Vuelta |
| C-230 | 9+168.40 | 9471935.93 | 607762.51 | 40.8 | I | 10.74 | 4.0 | 7.7 | 0.72 | 9+164.40 | 9+172.05 | 18.64 | 0.0 | 0.47 | Vuelta |
| C-231 | 9+213.86 | 9471891.12 | 607753.03 | 93.0 | I | 39.70 | 41.8 | 64.4 | 17.95 | 9+172.05 | 9+236.46 | 3.49 | 16.9 | 0.65 | Excepcional |
| C-232 | 9+275.04 | 9471878.56 | 607832.43 | 120.4 | D | 12.40 | 21.7 | 26.1 | 12.56 | 9+253.38 | 9+279.44 | 12.90 | 12.1 | 1.13 | Vuelta |
| C-233 | 9+311.64 | 9471836.95 | 607798.23 | 63.9 | I | 32.20 | 20.1 | 35.9 | 5.74 | 9+291.57 | 9+327.46 | 4.26 | 6.3 | 0.40 | Excepcional |
| C-234 | 9+343.21 | 9471804.34 | 607813.04 | 23.8 | D | 45.00 | 9.5 | 18.7 | 0.99 | 9+333.71 | 9+352.44 | 3.10 | 4.5 | 0.42 | Normativa 12% |
| C-235 | 9+366.92 | 9471780.36 | 607813.29 | 25.0 | I | 45.00 | 10.0 | 19.6 | 1.09 | 9+356.94 | 9+376.58 | 3.10 | 17.7 | 0.21 | Normativa 12% |
| C-236 | 9+396.10 | 9471753.76 | 607826.04 | 4.0 | D | 53.35 | 1.9 | 3.7 | 0.03 | 9+394.24 | 9+397.97 | 2.65 | 0.0 | 0.14 | Normativa 8% |
| C-237 | 9+435.23 | 9471717.37 | 607840.44 | 154.9 | D | 8.30 | 37.3 | 22.4 | 29.88 | 9+397.97 | 9+420.40 | - | 17.6 | 1.68 | Vuelta |
| C-238 | 9+455.96 | 9471767.31 | 607787.43 | 43.5 | D | 44.98 | 17.9 | 34.1 | 3.45 | 9+438.02 | 9+472.16 | 3.11 | 0.0 | 1.25 | Normativa 12% |
| C-239 | 9+475.51 | 9471788.57 | 607786.24 | 27.9 | I | 13.50 | 3.4 | 6.6 | 0.41 | 9+472.16 | 9+478.74 | 11.24 | 30.9 | 0.38 | Vuelta |
| C-240 | 9+525.93 | 9471831.83 | 607760.09 | 96.0 | I | 14.70 | 16.3 | 24.6 | 7.27 | 9+509.60 | 9+534.23 | 9.97 | 1.8 | 1.34 | Vuelta |
| C-241 | 9+572.32 | 9471798.96 | 607716.73 | 46.3 | D | 85.00 | 36.3 | 68.7 | 7.44 | 9+535.98 | 9+604.65 | 1.75 | 3.8 | 1.00 | Normativa 8% |
| C-242 | 9+632.56 | 9471809.13 | 607653.30 | 57.6 | D | 43.80 | 24.1 | 44.1 | 6.19 | 9+608.47 | 9+652.52 | 3.18 | 12.0 | 0.79 | Excepcional |
| C-243 | 9+679.79 | 9471856.32 | 607633.02 | 55.0 | I | 29.30 | 15.2 | 28.1 | 3.73 | 9+664.55 | 9+692.65 | 4.67 | 30.7 | 0.66 | Excepcional |
| C-244 | 9+728.70 | 9471866.80 | 607582.82 | 13.5 | D | 45.00 | 5.3 | 10.6 | 0.31 | 9+723.38 | 9+733.97 | 3.10 | 13.0 | 0.41 | Normativa 12% |
| C-245 | 9+760.92 | 9471880.59 | 607553.65 | 61.2 | D | 23.60 | 14.0 | 25.2 | 3.82 | 9+746.96 | 9+772.17 | 5.80 | 15.5 | 0.71 | Vuelta |
| C-246 | 9+816.48 | 9471938.74 | 607550.09 | 146.4 | I | 8.70 | 28.8 | 22.2 | 21.42 | 9+787.64 | 9+809.88 | - | 18.8 | 0.76 | Vuelta |
| C-247 | 9+850.63 | 9471878.52 | 607515.21 | 82.7 | I | 25.00 | 22.0 | 36.1 | 8.30 | 9+828.64 | 9+864.71 | 5.47 | 1.1 | 0.47 | Excepcional |
| C-248 | 9+884.01 | 9471853.44 | 607548.00 | 50.6 | D | 38.40 | 18.2 | 33.9 | 4.08 | 9+865.84 | 9+899.78 | 3.60 | 40.9 | 0.32 | Excepcional |
| C-249 | 9+952.76 | 9471782.33 | 607550.43 | 14.4 | I | 95.00 | 12.0 | 24.0 | 0.76 | 9+940.72 | 9+964.67 | 1.59 | 14.7 | 0.20 | Normativa 8% |
| C-250 | 10+010.24 | 9471727.07 | 607566.69 | 68.8 | I | 45.00 | 30.8 | 54.1 | 9.54 | 9+979.42 | 10+033.47 | 3.10 | 6.2 | 0.90 | Normativa 12% |
| C-251 | 10+066.69 | 9471721.73 | 607630.51 | 13.4 | I | 229.40 | 27.0 | 53.8 | 1.59 | 10+039.66 | 10+093.47 | 0.75 | 0.0 | 1.41 | Normativa 8% |
| C-252 | 10+094.75 | 9471725.99 | 607658.50 | 19.2 | I | 7.51 | 1.3 | 2.5 | 0.11 | 10+093.47 | 10+095.99 | - | -0.0 | 0.96 | Vuelta |
| C-253 | 10+100.78 | 9471728.83 | 607663.85 | 73.6 | D | 6.40 | 4.8 | 8.2 | 1.59 | 10+095.99 | 10+104.21 | - | -0.0 | 1.87 | Vuelta |
| C-254 | 10+118.61 | 9471715.10 | 607677.25 | 54.4 | D | 28.02 | 14.4 | 26.6 | 3.48 | 10+104.21 | 10+130.82 | 4.88 | -0.0 | 1.59 | Excepcional |
| C-255 | 10+134.08 | 9471697.71 | 607674.16 | 12.9 | I | 28.83 | 3.3 | 6.5 | 0.18 | 10+130.82 | 10+137.32 | 4.74 | 56.0 | 1.99 | Excepcional |
| C-256 | 10+195.21 | 9471636.63 | 607677.21 | 21.7 | D | 10.10 | 1.9 | 3.8 | 0.18 | 10+193.27 | 10+197.10 | - | 1.5 | 0.60 | Vuelta |
| C-257 | 10+235.15 | 9471598.79 | 607664.28 | 67.2 | I | 55.00 | 36.6 | 64.6 | 11.05 | 10+198.57 | 10+263.13 | 2.58 | 1.5 | 1.54 | Normativa 8% |
| C-258 | 10+268.42 | 9471570.99 | 607695.58 | 39.6 | D | 10.60 | 3.8 | 7.3 | 0.67 | 10+264.60 | 10+271.93 | 20.37 | 0.4 | 1.25 | Vuelta |
| C-259 | 10+290.30 | 9471549.06 | 607698.96 | 132.3 | D | 7.98 | 18.0 | 18.4 | 11.73 | 10+272.28 | 10+290.69 | - | 0.0 | 0.82 | Vuelta |
| C-260 | 10+312.28 | 9471570.91 | 607665.92 | 39.6 | D | 60.00 | 21.6 | 41.5 | 3.77 | 10+290.69 | 10+332.15 | 2.39 | 57.0 | 0.80 | Normativa 8% |
| C-261 | 10+400.88 | 9471657.34 | 607639.62 | 20.5 | D | 65.00 | 11.7 | 23.2 | 1.05 | 10+389.14 | 10+412.38 | 2.22 | 7.7 | 0.33 | Normativa 8% |
| C-262 | 10+429.47 | 9471686.11 | 607641.42 | 74.0 | I | 12.40 | 9.3 | 16.0 | 3.13 | 10+420.12 | 10+436.14 | 12.90 | 4.6 | 0.51 | Vuelta |
| C-263 | 10+463.20 | 9471698.31 | 607607.12 | 53.0 | I | 45.00 | 22.4 | 41.6 | 5.29 | 10+440.76 | 10+482.39 | 3.10 | -0.0 | 2.00 | Normativa 12% |
| C-264 | 10+486.74 | 9471683.55 | 607584.76 | 11.9 | D | 41.61 | 4.3 | 8.7 | 0.23 | 10+482.39 | 10+491.06 | 3.34 | 28.8 | 0.28 | Excepcional |
| C-265 | 10+600.63 | 9471641.79 | 607478.77 | 98.1 | D | 70.00 | 80.7 | 119.9 | 36.85 | 10+519.90 | 10+639.81 | 2.08 | 32.7 | 2.92 | Normativa 8% |
| C-266 | 10+683.76 | 9471763.10 | 607449.96 | 28.0 | I | 45.00 | 11.2 | 22.0 | 1.37 | 10+672.55 | 10+694.52 | 3.10 | 33.2 | 0.52 | Normativa 12% |
| C-267 | 10+754.02 | 9471816.20 | 607403.26 | 38.6 | D | 75.00 | 26.3 | 50.5 | 4.47 | 10+727.75 | 10+778.30 | 1.95 | 28.8 | 1.26 | Normativa 8% |
| C-268 | 10+832.65 | 9471896.74 | 607399.45 | 54.1 | D | 50.00 | 25.5 | 47.2 | 6.14 | 10+807.13 | 10+854.32 | 2.82 | 7.0 | 0.48 | Normativa 8% |
| C-269 | 10+866.58 | 9471920.32 | 607428.95 | 13.4 | I | 45.00 | 5.3 | 10.6 | 0.31 | 10+861.27 | 10+871.83 | 3.10 | 17.7 | 0.33 | Normativa 12% |
| C-270 | 10+905.20 | 9471950.83 | 607452.72 | 22.2 | D | 80.00 | 15.7 | 31.0 | 1.52 | 10+889.51 | 10+920.49 | 1.84 | 42.2 | 0.31 | Normativa 8% |
| C-271 | 10+969.63 | 9471983.14 | 607508.92 | 44.7 | I | 17.00 | 7.0 | 13.3 | 1.38 | 10+962.64 | 10+975.90 | 8.31 | 6.4 | 0.18 | Vuelta |
| C-272 | 10+989.59 | 9472003.07 | 607514.41 | 18.5 | D | 45.00 | 7.3 | 14.5 | 0.59 | 10+982.26 | 10+996.79 | 3.10 | 23.7 | 0.61 | Normativa 12% |
| C-273 | 11+037.63 | 9472043.05 | 607541.28 | 37.9 | I | 50.00 | 17.2 | 33.1 | 2.86 | 11+020.47 | 11+053.54 | 2.82 | 0.0 | 1.13 | Normativa 8% |
| C-274 | 11+068.93 | 9472075.53 | 607539.02 | 105.8 | I | 11.65 | 15.4 | 21.5 | 7.66 | 11+053.54 | 11+075.05 | 14.58 | 17.4 | 1.04 | Vuelta |
| C-275 | 11+107.66 | 9472059.31 | 607493.84 | 37.4 | D | 45.00 | 15.2 | 29.4 | 2.51 | 11+092.43 | 11+121.79 | 3.10 | 70.2 | 0.96 | Normativa 12% |
| C-276 | 11+227.08 | 9472095.79 | 607378.98 | 56.7 | D | 65.00 | 35.1 | 64.3 | 8.86 | 11+192.00 | 11+256.33 | 2.22 | 1.8 | 0.48 | Normativa 8% |
| C-277 | 11+275.04 | 9472147.58 | 607364.46 | 34.1 | I | 55.00 | 16.9 | 32.8 | 2.53 | 11+258.15 | 11+290.92 | 2.58 | 38.2 | 0.70 | Normativa 8% |
| C-278 | 11+339.74 | 9472189.99 | 607314.27 | 11.0 | D | 110.00 | 10.6 | 21.1 | 0.51 | 11+329.15 | 11+350.27 | 1.40 | 1.0 | 0.17 | Normativa 8% |
| C-279 | 11+366.02 | 9472210.52 | 607297.76 | 14.1 | I | 120.00 | 14.8 | 29.5 | 0.91 | 11+351.22 | 11+380.68 | 1.29 | 39.5 | 0.47 | Normativa 8% |
| C-280 | 11+422.67 | 9472244.80 | 607252.48 | 5.8 | D | 50.00 | 2.5 | 5.0 | 0.06 | 11+420.15 | 11+425.18 | 2.82 | 21.5 | 0.41 | Normativa 8% |
| C-281 | 11+454.81 | 9472266.68 | 607228.93 | 9.3 | I | 100.00 | 8.1 | 16.2 | 0.33 | 11+446.69 | 11+462.90 | 1.52 | 8.1 | 0.11 | Normativa 8% |
| C-282 | 11+474.45 | 9472277.57 | 607212.54 | 10.0 | D | 40.00 | 3.5 | 7.0 | 0.15 | 11+470.95 | 11+477.93 | 3.47 | 4.6 | 0.12 | Excepcional |

# Anexo B. Archivos entregados

- `EJE_DG2018_circular.xml`: eje en LandXML 1.2 para importar en Civil 3D (IMPORTLANDXML).
- `EJE_DG2018_circular_curvas.csv`: tabla de curvas con observaciones detalladas por curva.
- `EJE_DG2018_circular_PI_PNEZD.csv` y `EJE_DG2018_circular_PI_polilinea.scr`: PIs como puntos y como polilínea de AutoCAD.
- `EJE_DG2018_circular_planta.svg` y `.png`: croquis de planta con el trazo actual y el eje coloreado por clase de curva.
- `DG2018_Corregido_2.xml`: archivo de criterios de diseño DG-2018 para Civil 3D.
- `EJE_DG2018_clotoides.xml`: variante con clotoides de 40 m en las 5 curvas donde caben.
- `EJE_DG2018_circular_polilinea_arcos.dxf`: polilínea con arcos para crear la alineación en Civil 3D por PIs (líneas fijas y curvas libres).
- `EJE_DG2018_circular_entidades_C3D.csv` y `EJE_DG2018_circular_grupos_sin_tangente.csv`: correspondencia entidad de Civil 3D ↔ curva y lista de los grupos del capítulo 6.6 con los pasos para rehacerlos como curva flotante + curva libre.
- `scripts/civil3d_crear_alineacion_dynamo.py`: script de Dynamo que crea la alineación entidad por entidad con sus restricciones.
