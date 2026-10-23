# Ensanches de plataforma (DG-2018 §304.12.03, Tabla 304.12)

Herramienta que, a partir de un **LandXML exportado de Civil 3D** (eje, rasante, bordes de calzada y
superficie de terreno), ubica los **ensanches de plataforma** exigidos cuando las bermas son menores a
2.60 m (aquí la vía **no tiene bermas**), a ambos lados de la vía y **en forma alternada**, eligiendo las
progresivas donde el **movimiento de tierras adicional es mínimo**, y los dibuja en archivos importables
en Civil 3D / AutoCAD.

## Datos del proyecto analizado

| Dato | Valor |
|---|---|
| Archivo | `DISEÑO EJE UNIDO - CARRETERA-EJE FINAL 2.0.xml` (Civil 3D 2027, UTM WGS84 17S, EPSG 32717) |
| Eje / rasante | `eje 01` (L = 26,154.04 m) / `Rs-eje 01` (213 PVI, cota 1438.65 → 338.34) |
| Bordes de calzada | `carril` (izquierdo, 3.30 m + sobreanchos) y `carril (6)` (derecho) → calzada 6.60 m |
| Superficie | `TN` (TIN, 66,719 triángulos; incluye la plataforma existente) |
| Clasificación asumida | Carretera de **Segunda Clase**, orografía **Escarpada**, V = 40 km/h (propiedad `speed` del eje) |
| Bermas | **0.00 m** (no se consideran bermas; por eso aplican los ensanches) |

## Criterio normativo aplicado (Tabla 304.12, fila *Escarpado*, columna *Carretera de Segunda Clase*)

| Parámetro | Valor |
|---|---|
| Ancho mínimo del ensanche | **2.50 m** |
| Largo mínimo del ensanche | **25.0 m** |
| Separación máxima **a cada lado** | **2,500 m** |
| Disposición | a cada lado de la carretera, **en forma alternada**, con transiciones de ingreso y salida |

## Resultado: 22 ensanches (11 izquierda + 11 derecha), todos con el núcleo en tangente, volumen adicional estimado ≈ 1571 m³

Lado IZQ/DER = izquierda/derecha **en el sentido de las progresivas crecientes** del eje `eje 01`
(convención de Civil 3D). **Numeración independiente por lado**: `EI-01…EI-11` (izquierda) y `ED-01…ED-11`
(derecha); la columna "Orden" es la posición a lo largo de la vía. Cada ensanche = núcleo de 25 m (ancho 2.5 m)
+ transición de ingreso y de salida de 15 m (afinamiento 1:6). "km centro" es el centro del núcleo.

| Orden | Nombre | Lado | km centro | Tramo total (con transiciones) | Núcleo en tangente | Transiciones en tangente | Vol. adic. (m³) | Corte (m³) | Relleno (m³) | h borde (m) | TIN extrap. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | EI-01 | IZQ | 1+245.00 | 1+217.50 – 1+272.50 | sí | no | 20 | 2 | 19 | -0.64 |  |
| 3 | EI-02 | IZQ | 3+530.00 | 3+502.50 – 3+557.50 | sí | no | 9 | 5 | 4 | -0.63 |  |
| 5 | EI-03 | IZQ | 5+900.00 | 5+872.50 – 5+927.50 | sí | no | 41 | 0 | 41 | -0.28 |  |
| 7 | EI-04 | IZQ | 8+045.00 | 8+017.50 – 8+072.50 | sí | no | 11 | 10 | 1 | -0.49 | sí |
| 9 | EI-05 | IZQ | 9+660.00 | 9+632.50 – 9+687.50 | sí | no | 22 | 10 | 12 | -0.81 |  |
| 11 | EI-06 | IZQ | 12+105.00 | 12+077.50 – 12+132.50 | sí | no | 25 | 0 | 25 | -0.42 |  |
| 13 | EI-07 | IZQ | 14+250.00 | 14+222.50 – 14+277.50 | sí | no | 94 | 93 | 1 | -0.48 | sí |
| 15 | EI-08 | IZQ | 16+485.00 | 16+457.50 – 16+512.50 | sí | sí | 190 | 190 | 1 | -0.16 |  |
| 17 | EI-09 | IZQ | 18+940.00 | 18+912.50 – 18+967.50 | sí | no | 119 | 116 | 3 | -0.18 |  |
| 19 | EI-10 | IZQ | 21+375.00 | 21+347.50 – 21+402.50 | sí | no | 65 | 64 | 1 | -0.33 |  |
| 21 | EI-11 | IZQ | 23+680.00 | 23+652.50 – 23+707.50 | sí | no | 64 | 63 | 1 | -0.37 |  |
| 2 | ED-01 | DER | 2+260.00 | 2+232.50 – 2+287.50 | sí | no | 354 | 353 | 1 | -0.56 | sí |
| 4 | ED-02 | DER | 4+425.00 | 4+397.50 – 4+452.50 | sí | no | 97 | 96 | 1 | -0.56 | sí |
| 6 | ED-03 | DER | 6+730.00 | 6+702.50 – 6+757.50 | sí | no | 51 | 12 | 39 | +0.08 |  |
| 8 | ED-04 | DER | 8+790.00 | 8+762.50 – 8+817.50 | sí | no | 88 | 24 | 64 | -1.04 |  |
| 10 | ED-05 | DER | 11+265.00 | 11+237.50 – 11+292.50 | sí | no | 220 | 218 | 1 | -0.25 | sí |
| 12 | ED-06 | DER | 13+690.00 | 13+662.50 – 13+717.50 | sí | no | 30 | 30 | 0 | -0.15 |  |
| 14 | ED-07 | DER | 16+005.00 | 15+977.50 – 16+032.50 | sí | no | 25 | 1 | 24 | -0.30 |  |
| 16 | ED-08 | DER | 18+455.00 | 18+427.50 – 18+482.50 | sí | no | 13 | 4 | 9 | -0.77 | sí |
| 18 | ED-09 | DER | 20+880.00 | 20+852.50 – 20+907.50 | sí | no | 7 | 6 | 1 | -0.39 |  |
| 20 | ED-10 | DER | 22+215.00 | 22+187.50 – 22+242.50 | sí | no | 1 | 1 | 0 | -0.19 |  |
| 22 | ED-11 | DER | 24+300.00 | 24+272.50 – 24+327.50 | sí | sí | 24 | 16 | 9 | -0.34 |  |
