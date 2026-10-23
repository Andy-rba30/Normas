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

## Resultado: 24 ensanches (12 izquierda + 12 derecha), **sin interferencias**, 23 de 24 con el núcleo en tangente, volumen adicional estimado ≈ 1924 m³

Lado IZQ/DER = izquierda/derecha **en el sentido de las progresivas crecientes** del eje `eje 01`
(convención de Civil 3D). **Numeración independiente por lado**: `EI-01…EI-12` (izquierda) y `ED-01…ED-12`
(derecha); la columna "Orden" es la posición a lo largo de la vía. Cada ensanche = núcleo de 25 m (ancho 2.5 m)
+ transición de ingreso y de salida de 15 m (afinamiento 1:6). "km centro" es el centro del núcleo.

| Orden | Nombre | Lado | km centro | Tramo total (con transiciones) | Núcleo en tangente | Transiciones en tangente | Interferencia | Vol. adic. (m³) | Corte (m³) | Relleno (m³) | h borde (m) | TIN extrap. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | EI-01 | IZQ | 2+260.00 | 2+232.50 – 2+287.50 | sí | no | ninguna | 51 | 1 | 49 | +0.77 |  |
| 4 | EI-02 | IZQ | 4+455.00 | 4+427.50 – 4+482.50 | sí | sí | ninguna | 50 | 11 | 40 | -0.74 |  |
| 6 | EI-03 | IZQ | 6+725.00 | 6+697.50 – 6+752.50 | sí | no | ninguna | 20 | 3 | 17 | +0.05 |  |
| 8 | EI-04 | IZQ | 9+005.00 | 8+977.50 – 9+032.50 | sí | no | ninguna | 74 | 0 | 74 | -0.97 |  |
| 10 | EI-05 | IZQ | 11+280.00 | 11+252.50 – 11+307.50 | sí | no | ninguna | 87 | 0 | 87 | -0.08 |  |
| 12 | EI-06 | IZQ | 12+910.00 | 12+882.50 – 12+937.50 | sí | no | ninguna | 7 | 3 | 5 | -1.05 |  |
| 14 | EI-07 | IZQ | 14+625.00 | 14+597.50 – 14+652.50 | sí | no | ninguna | 195 | 195 | 1 | -0.25 | sí |
| 16 | EI-08 | IZQ | 17+055.00 | 17+027.50 – 17+082.50 | sí | no | ninguna | 118 | 117 | 1 | -0.54 | sí |
| 18 | EI-09 | IZQ | 19+055.00 | 19+027.50 – 19+082.50 | sí | no | ninguna | 112 | 112 | 0 | -0.75 |  |
| 20 | EI-10 | IZQ | 21+375.00 | 21+347.50 – 21+402.50 | sí | no | ninguna | 65 | 64 | 1 | -0.33 |  |
| 22 | EI-11 | IZQ | 23+390.00 | 23+362.50 – 23+417.50 | sí | no | ninguna | 81 | 81 | 0 | -0.69 |  |
| 24 | EI-12 | IZQ | 24+970.00 | 24+942.50 – 24+997.50 | sí | no | ninguna | 66 | 65 | 1 | -0.35 |  |
| 1 | ED-01 | DER | 1+245.00 | 1+217.50 – 1+272.50 | sí | no | ninguna | 232 | 212 | 20 | -0.07 |  |
| 3 | ED-02 | DER | 3+165.00 | 3+137.50 – 3+192.50 | sí | no | ninguna | 142 | 141 | 0 | -0.05 | sí |
| 5 | ED-03 | DER | 5+645.00 | 5+617.50 – 5+672.50 | sí | sí | ninguna | 228 | 212 | 15 | -0.18 |  |
| 7 | ED-04 | DER | 7+980.00 | 7+952.50 – 8+007.50 | sí | no | ninguna | 31 | 1 | 30 | -0.05 |  |
| 9 | ED-05 | DER | 9+915.00 | 9+887.50 – 9+942.50 | R=200 | no | ninguna | 21 | 4 | 17 | -0.15 |  |
| 11 | ED-06 | DER | 12+015.00 | 11+987.50 – 12+042.50 | sí | no | ninguna | 211 | 210 | 1 | -1.66 |  |
| 13 | ED-07 | DER | 14+115.00 | 14+087.50 – 14+142.50 | sí | no | ninguna | 12 | 11 | 1 | -0.79 | sí |
| 15 | ED-08 | DER | 16+005.00 | 15+977.50 – 16+032.50 | sí | no | ninguna | 25 | 1 | 24 | -0.30 |  |
| 17 | ED-09 | DER | 18+455.00 | 18+427.50 – 18+482.50 | sí | no | ninguna | 13 | 4 | 9 | -0.77 | sí |
| 19 | ED-10 | DER | 20+880.00 | 20+852.50 – 20+907.50 | sí | no | ninguna | 7 | 6 | 1 | -0.39 |  |
| 21 | ED-11 | DER | 22+595.00 | 22+567.50 – 22+622.50 | sí | no | ninguna | 51 | 51 | 0 | -0.41 | sí |
| 23 | ED-12 | DER | 24+300.00 | 24+272.50 – 24+327.50 | sí | sí | ninguna | 24 | 16 | 9 | -0.34 |  |
