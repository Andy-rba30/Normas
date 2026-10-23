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

## Resultado: 26 ensanches (13 izquierda + 13 derecha), volumen adicional estimado ≈ 1208 m³

Lado IZQ/DER = izquierda/derecha **en el sentido de las progresivas crecientes** del eje `eje 01`
(convención de Civil 3D). **Numeración independiente por lado**: `EI-01…EI-13` (izquierda) y `ED-01…ED-13`
(derecha); la columna "Orden" es la posición a lo largo de la vía. Cada ensanche = núcleo de 25 m (ancho 2.5 m)
+ transición de ingreso y de salida de 15 m (afinamiento 1:6). "km centro" es el centro del núcleo.

| Orden | Nombre | Lado | km centro | Tramo total (con transiciones) | Vol. adic. (m³) | Corte (m³) | Relleno (m³) | h borde (m) | R mín. núcleo (m) | TIN extrap. |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | EI-01 | IZQ | 2+280.00 | 2+252.50 – 2+307.50 | 35 | 7 | 22 | -0.26 | tangente |  |
| 4 | EI-02 | IZQ | 4+465.00 | 4+437.50 – 4+492.50 | 34 | 16 | 12 | -0.66 | tangente |  |
| 6 | EI-03 | IZQ | 6+725.00 | 6+697.50 – 6+752.50 | 24 | 3 | 17 | +0.05 | tangente |  |
| 8 | EI-04 | IZQ | 9+005.00 | 8+977.50 – 9+032.50 | 89 | 0 | 74 | -0.97 | tangente |  |
| 10 | EI-05 | IZQ | 10+705.00 | 10+677.50 – 10+732.50 | 11 | 7 | 4 | -0.46 | 60 | sí |
| 12 | EI-06 | IZQ | 12+105.00 | 12+077.50 – 12+132.50 | 30 | 0 | 25 | -0.42 | tangente |  |
| 14 | EI-07 | IZQ | 13+815.00 | 13+787.50 – 13+842.50 | 8 | 6 | 2 | -0.19 | 200 | sí |
| 16 | EI-08 | IZQ | 15+510.00 | 15+482.50 – 15+537.50 | 85 | 85 | 0 | -0.54 | 100 |  |
| 18 | EI-09 | IZQ | 17+460.00 | 17+432.50 – 17+487.50 | 117 | 97 | 0 | -0.53 | tangente |  |
| 20 | EI-10 | IZQ | 19+190.00 | 19+162.50 – 19+217.50 | 44 | 43 | 1 | -0.04 | 80 |  |
| 22 | EI-11 | IZQ | 21+545.00 | 21+517.50 – 21+572.50 | 43 | 42 | 0 | -0.04 | 200 |  |
| 24 | EI-12 | IZQ | 23+350.00 | 23+322.50 – 23+377.50 | 36 | 35 | 0 | -0.19 | 200 |  |
| 26 | EI-13 | IZQ | 25+700.00 | 25+672.50 – 25+727.50 | 7 | 3 | 4 | +0.02 | tangente | sí |
| 1 | ED-01 | DER | 1+235.00 | 1+207.50 – 1+262.50 | 131 | 111 | 20 | -0.13 | 65 |  |
| 3 | ED-02 | DER | 3+480.00 | 3+452.50 – 3+507.50 | 104 | 85 | 2 | -0.14 | 80 |  |
| 5 | ED-03 | DER | 5+755.00 | 5+727.50 – 5+782.50 | 110 | 5 | 87 | +1.65 | tangente | sí |
| 7 | ED-04 | DER | 7+980.00 | 7+952.50 – 8+007.50 | 31 | 1 | 30 | -0.05 | tangente |  |
| 9 | ED-05 | DER | 9+915.00 | 9+887.50 – 9+942.50 | 25 | 4 | 17 | -0.15 | 200 |  |
| 11 | ED-06 | DER | 11+130.00 | 11+102.50 – 11+157.50 | 156 | 128 | 2 | -0.15 | 200 |  |
| 13 | ED-07 | DER | 13+160.00 | 13+132.50 – 13+187.50 | 32 | 0 | 32 | -0.06 | 200 | sí |
| 15 | ED-08 | DER | 14+215.00 | 14+187.50 – 14+242.50 | 25 | 12 | 12 | -0.51 | 80 |  |
| 17 | ED-09 | DER | 16+690.00 | 16+662.50 – 16+717.50 | 8 | 4 | 3 | -0.64 | 120 |  |
| 19 | ED-10 | DER | 18+690.00 | 18+662.50 – 18+717.50 | 2 | 0 | 2 | -0.18 | tangente |  |
| 21 | ED-11 | DER | 20+875.00 | 20+847.50 – 20+902.50 | 6 | 5 | 0 | -0.33 | 110 |  |
| 23 | ED-12 | DER | 22+215.00 | 22+187.50 – 22+242.50 | 1 | 1 | 0 | -0.19 | tangente |  |
| 25 | ED-13 | DER | 24+440.00 | 24+412.50 – 24+467.50 | 12 | 8 | 2 | -0.35 | tangente |  |
