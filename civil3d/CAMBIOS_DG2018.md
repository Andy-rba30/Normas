# DG2018_Corregido.xml — registro de cambios

Normas de diseño de Autodesk Civil 3D (`Civil3DRoadwayDesignStandards`) ajustadas al
**Manual de Carreteras: Diseño Geométrico DG-2018** (revisado y corregido a enero de
2018, `normas/Manual.de.Carreteras.DG-2018.pdf`).

| Archivo | Contenido |
|---|---|
| `DG2018_original.xml` | Archivo de partida, sin cambios |
| `DG2018_Corregido.xml` | Archivo corregido, listo para importar |
| `generar_dg2018_corregido.py` | Script que produce el corregido a partir del original (requiere `lxml`) |
| `Reporte_Trazabilidad_DG2018.pdf` | Reporte de cambios con cita a la DG-2018 (tabla o tópico y página) |
| `generar_reporte_trazabilidad.py` | Script que produce el reporte PDF a partir de los dos XML (requiere `reportlab`) |

```
python3 generar_dg2018_corregido.py DG2018_original.xml DG2018_Corregido.xml
```

## 1. Radios mínimos (`MinimumRadiusTables`)

| Tabla | Cambio | Sustento |
|---|---|---|
| 4%, 6%, 8%, 12% | Se eliminan las filas de 140 km/h | Tabla 204.01 (30–130 km/h) |
| 8% | 110 km/h: 505 → **500 m**. Se mantiene 85 m a 50 km/h (la Tabla 302.04 da 80 m, pero redondea hacia abajo un valor calculado de 82.0 m) | Tabla 302.02 |
| 10% | Se eliminan 15 y 20 km/h. 30–70 km/h: 19/38/68/105/154 → **26/47/76/115/161 m** (el mayor valor oficial entre las Tablas 302.04 y 302.10). 80–130 km/h sin cambio (210/277/358/454/597/739) | Tablas 302.03, 302.04, 302.10; 739 = 130²/127(0.10+0.08) |
| SIN PERALTE | Se reemplazan los radios AASHTO con e = −2% (30–70 km/h) por el radio límite en contraperalte de **60 a 130 km/h**: 1000, 1000, 1200, 1600, 2000, 2800, 4000, 5500 m. Se conserva el nombre para no romper referencias | Tabla 302.05; Tópico 302.04.04 |

## 2. Peralte (`SuperelevationTables`)

**Nombre:** `AASHTO 2011 Metric eMax 10%` → `DG2018 _PMax 10%`.

**Escalón de peralte máximo**, igualado al radio mínimo de la Tabla 302.02 en todas las tablas:

- 6%: 80 km/h 225 → 255; 130 km/h 951 → 950.
- 8%: 40–120 km/h 55/90/135/195/255/335/440/501/667 → 50/85/125/175/230/305/395/500/670.
- 12%: 100 km/h 300 → 330.

**Erratas en radios intermedios** (corregidas por interpolación de los valores vecinos):

| Tabla | V (km/h) | eRate | Antes | Después |
|---|---|---|---|---|
| 8% | 40 | 2.6 | 349 | 449 |
| 8% | 40 | 3.8 | 248 | 286 |
| 8% | 80 | 3.4 | 1135 | 1070 |
| 8% | 80 | 4.4 | 722 | 792 |
| 12% | 70 | 2.4 | 1996 | 1296 |
| 12% | 100 | 6.8 | 774 | 744 |
| 12% | 110 | 8.4 | 969 | 696 |

**Bombeo normal (NC) y peralte mínimo (RC = 2%)**, según las Tablas 304.04 y 304.06:

| Velocidad | NC (sin peralte desde) | RC (2% desde) |
|---|---|---|
| < 60 km/h | Fila eliminada: no se permite contraperalte (Tópico 302.04.04) | 3,500 m (en 4% a 30 km/h, la fila `2.0`) |
| 60–90 km/h | 3,500 m | 2,500 m |
| 100–130 km/h | 7,500 m | 5,000 m |

90 km/h queda en el grupo de 3,500/2,500 m porque la Tabla 304.06 lo incluye
expresamente en el rango 40 ≤ V < 100 km/h. Por debajo de 60 km/h, la fila RC se
lleva a 3,500 m para que las curvas menores que ese radio reciban al menos 2% sin
depender de qué aplique Civil 3D a radios mayores que el de la primera fila. Entre RC y el escalón de 2.2% el
peralte queda entre 2.0 y 2.2%, ya sea que Civil 3D interpole o tome el escalón,
lo que cumple el mínimo de la Tabla 304.06.

**Bloques generados** con el método 5 de AASHTO, que es la distribución de las
Figuras 302.02–302.05, usando la fricción fmáx de la DG-2018 y el radio mínimo de la
Tabla 302.02 en el escalón máximo:

- 4%: 110, 120 y 130 km/h (faltaban).
- 8% y 12%: 130 km/h (faltaba).
- 10%: 30 a 70 km/h (estaban calculados con la fricción de AASHTO, entre 0.28 y 0.15).

El mismo cálculo reproduce la tabla AASHTO del 10% original con un error menor al 1%
entre 40 y 130 km/h.

**Longitudes de transición** (`TransitionLengthTables` "2 Lane" y "4 Lane"):

- Sus radios son ahora idénticos, fila por fila, a los de la tabla de peralte.
- Se eliminan los bloques huérfanos (12% a 20 km/h; 10% a 20 km/h).
- Los `tLength` existentes se conservan. En los bloques nuevos se calculan con la misma
  regla que el original: L = 3.6·e/Δ por carril girado (×1.5 en "4 Lane"), que es la
  base de la Tabla 302.13.

## 3. Clotoide (`TransitionLengthFormula`)

- `minimumValue` 0.0 → **30.0** (nota de la Tabla 302.10).
- `q` 0.3 → **0.4**: J de la Tabla 302.09. Civil 3D admite un solo `q`; 0.4 queda del
  lado conservador para V < 80 km/h, donde J = 0.5.

## 4. Sobreancho (`WideningMethods`)

En `DG2018 formula simple`, el término empírico pasa de `0.05*{v}/{r}^.5` a
**`0.1*{v}/{r}^.5`**: Sa = n(R − √(R² − L²)) + V/(10√R), Tópico 302.09.03.

## 5. Parámetro K (`MinimumKTables`)

La tabla `DG2018  metrico Standard` se divide en dos. Los valores se redondean hacia
arriba, como en las Tablas 303.02 y 303.03.

| V (km/h) | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 | 130 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Red Vial General** SSD = Dp²/404 | 1 | 4 | 7 | 11 | 18 | 28 | 42 | 64 | 85 | 120 | 155 | 202 |
| **Red Vial General** PSD = Da²/946 | 18 | 43 | 78 | 126 | 178 | 249 | 309 | 400 | 475 | 564 | 635 | 703 |
| **Red Vial General** HSD = Dp²/(120+3.5Dp) | 3 | 6 | 9 | 13 | 18 | 23 | 30 | 38 | 45 | 55 | 63 | 73 |
| **Tercera Clase** SSD (Tabla 303.02) | 1 | 2 | 4 | 7 | 11 | 17 | 26 | 39 | | | | |
| **Tercera Clase** PSD (Tabla 303.02) | | 46 | 84 | 138 | 195 | 272 | 338 | 438 | | | | |
| **Tercera Clase** HSD (Tabla 303.03) | 3 | 6 | 9 | 13 | 18 | 23 | 30 | 38 | | | | |

## Validación del archivo generado

- El XML está bien formado y conserva la codificación UTF-8 y los saltos de línea CRLF
  del original.
- Las cinco tablas DG2018 cubren de 30 a 130 km/h.
- En cada bloque, los radios decrecen a medida que sube el peralte.
- Para un mismo peralte, el radio crece con la velocidad. El original tenía 2 inversiones
  de este tipo; el corregido no tiene ninguna.
- No queda ningún salto irregular entre escalones vecinos.
- Los radios de las tablas de transición son idénticos a los de peralte.
- Las tablas de vehículos de diseño (WB-19, etc.) no se modificaron.

## Pendiente de revisar en Civil 3D

- **Velocidades menores a 60 km/h:** conviene trazar una curva de prueba de más de
  3,500 m y otra de menos para confirmar qué peralte aplica Civil 3D en cada caso.
- **Tablas renombradas:** en la pestaña de criterios de diseño de las propiedades del
  alineamiento y del perfil (no en sus estilos), las referencias a
  `AASHTO 2011 Metric eMax 10%` o `DG2018  metrico Standard` deben apuntar a los nuevos
  nombres.
- **Tabla `Superelevation Rate By Formula`:** solo se cambiaron `q` y `minimumValue`. Su
  fórmula de peralte `{v}^2/(2.82528*{r})` no proviene de la DG-2018.
- **Longitudes de transición por encima de 90 km/h:** la Tabla 302.13 solo llega a
  90 km/h, así que los `tLength` superiores extienden la misma regla AASHTO. Para
  Primera y Segunda Clase y Autopistas, la DG-2018 usa
  Lmín = (pf − pi)/(1.8 − 0.01V)·B (Tópico 302.08, Tablas 302.14 a 302.18).
