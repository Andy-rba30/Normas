# Casos reales de terceros: documentos abiertos y calificados

Curaduría del 2026-11-17. Parte de `casos_reales.md`, el informe de búsqueda anterior. No se escribió en ningún repositorio git.

- **Descargas:** `/home/user/casos_reales/`, una subcarpeta por fuente (sección 7).
- **Texto extraído:** se sacó con PyMuPDF y está en `…/scratchpad/txt/`.
- **Escaneos:** ninguno de los documentos abiertos es escaneado. Todos tienen capa de texto. Las únicas excepciones son algunas tablas pegadas como imagen, y se indican donde aparecen.

**Convención de páginas:** «PDF n» es la página del archivo. Cuando la página impresa es distinta, va entre paréntesis: «imp. m».

**Lista de control.**

| Ítem | Qué se comprueba |
|---|---|
| (a) | Serie de P24 máx impresa año por año, con su estación |
| (b) | Ajuste con parámetros y P de diseño por TR |
| (c) | Cuencas con A, L, S o desnivel, y CN o C |
| (d) | Q por alcantarilla, con método y TR |
| (e) | Hidráulica: sección, S, L, HW o tirante, velocidades |
| (f) | Estructura |
| (g) | Cabezal |

**Regla de reproducibilidad:** un caso es REPRODUCIBLE si trae (a)+(b), o (c)+(d), con todas sus entradas.

---

## 1. Qué se pudo abrir y qué no

| Prioridad | Fuente | Resultado |
|---|---|---|
| 1 | Provías Nacional (`gis.proviasnac.gob.pe` y `gis.pvn.gob.pe`) | **No se pudo abrir** (sección 6) |
| 2 | UPAO La Jalca | Abierto |
| 2 | ESPOL Intervalles | Abierto. El enlace del informe previo daba 404; se recuperó por la API de DSpace |
| 2 | UPeU Colpahuayco–Langui | Abierto |
| 2 | UNSAAC (42 TMC) | Abierto |
| 2 | UNTumbes TU-107 | Abierto |
| 3 | INDECI, «Mapa de peligros de Piura», Vol. I | Abierto |
| 3 | INDECI, ídem, **Vol. II Anexos** | Abierto. Trae el Anexo 07, con el análisis de frecuencia con y sin El Niño y sus parámetros |
| Extra | UVG Guatemala, cajón 10'×10' por AASHTO LRFD 2018 | Abierto. Se añadió para cubrir (f), porque PVN no estuvo disponible |
| Extra | USAT Ferreñafe | Descargado y **descartado**: es drenaje pluvial urbano y pavimento, sin alcantarillas. Se borró |

---

## 2. Lista de control por documento

| Documento | (a) serie | (b) ajuste | (c) cuencas | (d) Q | (e) hidráulica | (f) estructura | (g) cabezal | ¿Reproducible? |
|---|---|---|---|---|---|---|---|---|
| **INDECI Piura**, Vol. I + Vol. II | **SÍ** (Vol. I PDF 105, imp. 89; Vol. II PDF 338, 346, 354) | **SÍ** (Vol. II PDF 338-340, 346-348, 354-355; Vol. I PDF 127-129) | PARCIAL (Vol. I PDF 172-173) | PARCIAL (ídem; i fija) | NO | NO | NO | **SÍ, (a)+(b) completo y en tres variantes FEN** |
| **UPeU** Colpahuayco–Langui (2023) | **SÍ** (p. 13) | PARCIAL (p. 19) | **SÍ** (p. 18) | **SÍ** (p. 20-21) | PARCIAL (p. 16-17, 21) | NO | NO (sólo inventario, p. 32-34) | **SÍ, (c)+(d)**, con I y K comprobados a mano |
| **UNTumbes** TU-107 (2025/26) | **SÍ** (p. 60-62) | **SÍ** (p. 66-74, 80) | **SÍ** (p. 64-65) | **SÍ** (p. 89-93) | PARCIAL (p. 94-95) | NO | NO | **SÍ, (a)+(b)+(c)+(d)**, con datos defectuosos |
| **ESPOL** Intervalles (2023) | **SÍ** (PDF 94-96) | **SÍ** (PDF 55, 96-98) | PARCIAL (PDF 51, 98) | **SÍ** (PDF 58) | **SÍ** (PDF 65-71) | PARCIAL (PDF 73-74, 92) | PARCIAL (PDF 88-89, 93) | **SÍ, (a)+(b) y (e)**. (c) incompleto |
| **UNSAAC** Roquepata (2019) | **SÍ** (PDF 101, imp. 89) | PARCIAL (PDF 104, imp. 92) | **SÍ** (PDF 98-100) | SÍ por cuenca, PARCIAL por obra (PDF 111, 118-119) | PARCIAL (PDF 118-119) | NO | NO | **SÍ, (a)+(b) y (c)+(d)** a nivel de microcuenca |
| **UPAO** La Jalca (2016) | SÍ, dos series discordantes (PDF 91-92, imp. 71-72; PDF 113-114) | **SÍ** (PDF 93, 114-115, 123) | PARCIAL (PDF 138-140) | **SÍ** (PDF 140-142) | PARCIAL (PDF 143) | NO | PARCIAL (PDF 144-150) | **SÍ, (a)+(b)**. (c)+(d) incompleto |
| **UVG** cajón 10'×10' (2025) | NO | NO | NO | NO | NO | **SÍ** (PDF 48-75) | NO | Sólo para la demanda estructural del marco |

---

## 3. Detalle por documento: cifras clave y defectos

### 3.1 INDECI-OEA, «Mapa de peligros de la ciudad de Piura»

**Datos del documento.**
- Vol. I y Vol. II Anexos, junio de 2009.
- Estación **Miraflores**.
- Fuente de la serie: División de Hidrometeorología del Proyecto Especial Chira-Piura. **No es SENAMHI**.

**(a) La serie.**
- Vol. I, Cuadro 13 (PDF 105, imp. 89): P24 mensual y máximo anual de **1971 a 2008, 38 años**.
- Vol. II reimprime la serie en tres versiones:
  - Anexo 07.1 (PDF 338): **sin FEN, 32 años**, con la lista de años explícita.
  - Anexo 07.2 (PDF 346): **con FEN, 38 años**.
  - Anexo 07.3 (PDF 354): **sólo FEN, 5 datos**: 1972 65.3, 1983 151.4, 1987 34.9, 1992 107.1 y 1998 173.6.

**(b) El ajuste.** Para cada serie trae μ, σ y Cs, en mm y en log10, los K_T y la P para TR de 2 a 1000 años. Distribuciones: Normal, Log Normal, Log Pearson III, Gumbel y «Gumbel modificado».
- Sin FEN: μ = 18.6 mm, σ = 21.66 mm; en log10, μ = 1.037 y σ = 0.467 (Vol. II PDF 338-339).
- Con FEN: μ = 30.5 mm, σ = 40.68 mm; en log10, μ = 1.170 y σ = 0.542 (PDF 346-347).
- Δc de Kolmogorov-Smirnov por distribución: Vol. I, Cuadros 21-23 (PDF 127-129).
  - Sin FEN, Δtab = 0.24: LN 0.080 (la mejor), Normal 0.236, LP3 0.223, Gumbel 0.220, Gumbel modificado 0.184.
  - Con FEN, Δtab = 0.22: LN 0.059.
- Comparación (Vol. I, Cuadro 26, PDF 134): con LN, P25 sin FEN = 71.61 mm y con FEN = 131.82 mm.
- **Decisión del estudio:** adopta la serie **con FEN** porque es la más conservadora (Vol. I PDF 133).
- **Comprobado a mano:**
  - LN sin FEN, P100 = 10^(1.037 + 2.327·0.467) = 132.96 mm. Impreso: 132.98.
  - LN con FEN, P25 = 131.5 mm. Impreso: 131.82.

**(c) y (d).** Vol. I, Cuadro 36 (PDF 172-173): subcuencas urbanas con A, CN, Pe y C. El caudal sale del racional con i constante de 22 mm/h (TR 25). No trae L ni S, y no hay alcantarillas.

**Defectos que hay que declarar al reproducirlo.**
1. 1971 es un año parcial: diez meses y máximo de 1.6 mm. Entra en las dos series.
2. 1973 sale de la serie «sin FEN» y tampoco está en «sólo FEN», porque el estudio trata 72/73 como un solo evento. Queda fuera de las dos poblaciones.
3. 1997 (54.0 mm, en diciembre, al inicio del FEN 97-98) y 2002 (103.5 mm) siguen en la serie «sin FEN».
4. Su columna «Gumbel» usa ȳN y σN **de N = 20** (tabla de Ponce), aunque la serie tiene 32 o 38 años. Esa columna **no** es comparable con el programa. La columna «Gumbel modificado» sí lo es: usa el K_T de Chow, que equivale a los momentos (ec. 9 del Manual), y para T = 5 da 0.7195.

### 3.2 UPeU: Huamán Guerra y Marrujo Carpio (2023), Colpahuayco–Langui (Canas, Cusco)

Tesis en formato de artículo, 39 páginas. La página impresa coincide con la del PDF.

**(a) La serie.** Tabla 2 (p. 13): estación automática **Sicuani** (SENAMHI), 3534 msnm, **1993-2020, 28 años**.

**(b) El ajuste.**
- K-S: todas las distribuciones pasan. Elige **Pearson III**, con Δ 0.0537 frente a Δtab 0.2570 (p. 19).
- P por TR (Tabla 7, p. 19): 34.83, 40.59, 42.62, 43.85, 44.98 y 46.15 mm para TR 5, 20, 35, 50, 70 y 100.
- No imprime los parámetros.

**(c) Las cuencas.** Tabla 6 (p. 18): 14 microcuencas con A, P, L, B, tc, Kf, Kc, Hmáx, hmín, Em, **S de cuenca y s de cauce**.
- Microcuenca 7: 29.94 km². Microcuenca 14: 10.60 km².
- C viene en la Tabla 8. Sale del CN por la ec. 35, pero **el CN no se imprime**.

**(d) Los caudales.** Tabla 8 (p. 20-21):
- **Racional modificado (Témez) con TR 70**, con K, I, A (ha), C y Q, en 12 microcuencas;
- HEC-HMS en las cuencas 07 y 14;
- alivios y cunetas por el racional con TR 35 (63 tramos).

**Comprobado a mano.**
- Microcuenca 1: tc de Témez = 0.63 h, K = 1.039 (impreso 1.04) e I = 27.12 mm/h (impreso 27.10).
- Microcuencas 2 y 10: I dentro del ±1 %, aplicando KA = 1 − log A/15 (29.85 frente a 30.04; 39.0 frente a 39.42).

**Defectos.**
1. El área de la Tabla 8 no coincide con la de la Tabla 6. Microcuenca 1: 113.89 ha frente a 0.97 km². Microcuenca 8: 403 ha frente a 3.70 km².
2. K se aplica en unas filas y en otras no. Microcuenca 2: Q = 0.74, con K. Microcuencas 1 y 8: 2.41 y 6.09, sin K (con K serían 2.50 y 6.64).

**(e) Hidráulica.** Sólo hay criterios: n = 0.020 en TMC y 0.014 en marco, 75 % de la capacidad, V de 0.25 a 5 m/s. Trae además el resumen de obras (Tabla 9, p. 21): 22 reemplazos, 37 que se mantienen y 7 alivios nuevos. No calcula HW ni da el cálculo por obra.

### 3.3 UNTumbes: Ramos Estrada, «Estudio hidrológico… TU-107 Bocapán–Tamarindo» (tesis de 2025, sustentada en 2026)

La página impresa coincide con la del PDF.

**(a) La serie.**
- Tabla 23 (p. 60): estación **Cañaveral**, máximos mensuales y anuales de 1983-87, 1989-2021 y 2023-24: **40 años**, tomados del portal de SENAMHI.
- Tabla 24 (p. 61): serie anual.
- Tabla 25 (p. 62): prueba de datos dudosos del WRC, con Kn = 2.682. No detecta ninguno.

**(b) El ajuste.**
- Tablas 28-35 (p. 66-73): ocho distribuciones, cada una con su Δ.
- Tabla 36 (p. 74), con Δcrit = 0.2150:
  - **LN2: 0.0535 (la elegida)**;
  - LN3: 0.0580; LP3: 0.0550; Gamma 2: 0.0881; Gamma 3: 0.1071;
  - Normal: 0.1618; Gumbel: 0.1074; Log Gumbel: 0.1000.
- Las Tablas 37-46 (p. 75-79) son **imágenes** de HidroEsta. El resumen de la Tabla 47 (p. 80) es texto: P5 = 278.23, P10 = 412.70, P25 = 628.29, P50 = 824.21, P100 = 1052.08 y P500 = 1724.28 mm, y después las multiplica por 1.13.
- **Comprobado:** exp(4.875 + 2.326·0.8955) = 1051.7 mm.

**(c) Las cuencas.**
- Tabla 26 (p. 64): **41 cuencas** con A, perímetro, L, cota máxima y mínima, S, Kc y coordenadas de descarga.
- Tabla 27 (p. 65): tc por Témez y por Bransby-Williams.
- C de 0.10 a 0.20 por cuenca (Tabla 66). CN de 62 a 70 en las 5 cuencas de más de 10 km² (Tabla 67).

**(d) Los caudales.**
- IDF: I = 408.81·T^0.391 / t^0.5375 (p. 87).
- TR 35, 70 y 140 (p. 89).
- I por cuenca (Tabla 65, p. 90): **hasta 766 mm/h**.
- Racional en 36 cuencas (Tabla 66, p. 92).
- Hidrograma unitario triangular en 5 cuencas (Tabla 67, p. 93). Sapotal: Q70 = 1827.9 m³/s.

**(e) Hidráulica.** Tabla 68 (p. 95): 11 alcantarillas existentes, revisadas con Manning a lleno. S = 0.02 y n = 0.024 son **supuestos** y no medidos. No calcula HW. Los badenes están en la Tabla 69 (p. 97).

**Defectos graves.** Por ellos sirve como caso **adversarial**.
1. Filas duplicadas mes a mes: 2001 es igual a 1996, y 2002 igual a 1989 (Tabla 23).
2. Valores inverosímiles para 24 h: 717 mm en marzo de 1991, que no fue año FEN, y 491 mm en enero de 1983. Como referencia, Miraflores registró como máximo 173.6 mm.
3. La tesis **no menciona El Niño** aunque la serie incluye 1983 y 1997-98.
4. El resultado son intensidades físicamente absurdas.

### 3.4 ESPOL: Luna Chalán (2023), «Rediseño hidráulico de una alcantarilla… vía Intervalles» (Loja, Ecuador)

La página impresa es la del PDF menos 5.

**(a) Las series.** Anexo 2 (PDF 94-96), estaciones INAMHI con su código:
- La Argelia M033: n = 50;
- Gonzanamá M149: n = 48;
- Malacatos M143: n = 49;
- Catamayo M060: n = 29.
- Periodo: 1964-2013.

**(b) El ajuste.**
- Dmax de K-S por distribución, calculado con Hydrognomon: Anexos 3-6 (PDF 96-98).
- P para TR 25, 50 y 100 por estación: Tabla 3.7 (PDF 55).
- Valor del proyecto por isomáximas: 73.24, 81.29 y 89.25 mm.

**(c) La cuenca.** 9.27 ha (PDF 51). C compuesto: 0.47 el actual y 0.59 el proyectado (Anexos 7-8, PDF 98). **Faltan L, S y el valor de tc** (lo calcula por onda cinemática).

**(d) El caudal.** Q25 = 0.613 m³/s para 30 min (Tablas 3.8-3.9, PDF 58). Usa la IDF del INAMHI, zona 17 (Anexo 9, PDF 99), y la fórmula del MTOP con el factor Cf. Es **norma ecuatoriana**, no la del MTC.

**(e) Hidráulica (HY-8).**
- Estructura existente: L = 45.35 m, S = 2.24 % (Tabla 3.11, PDF 65).
- Propuesta (PDF 69-71): cajón de 1.10 × 1.10 m, L = 80.40 m, S = 1.30 %, n = 0.016.
  - Flujo tipo 2-M2c; tirante normal 0.37 m; tirante a la entrada 0.32 m.
  - V = 1.76 m/s en el barril y 2.26 m/s a la salida.
  - Canal de salida trapezoidal: b = 1.10 m, talud 0.5, S = 1.5 %, n = 0.016.

**(f) Estructura.**
- AASHTO LRFD 2020, carga HL-93. Cargas DC, EV, EH, LS y WA en la Tabla 3.14 (PDF 73).
- Envolventes de momento en las Tablas 3.15-3.16 (PDF 74). Están rotuladas en «kgf·m», unidad inverosímil, y probablemente son t·m.
- Planilla de hierros del cajón: Plano 5 (PDF 92).
- SPT (Tabla 3.13, PDF 72): qadm = 1.066 kg/cm², φ = 20.28°, c = 1.22 t/m².

**(g) Cabezal.** Planos y planillas de los cabezales de entrada y salida (PDF 88-89 y 93). No trae estabilidad.

### 3.5 UNSAAC: Bermejo Colque y Cruz Huamán (2019), camino vecinal Emp. CU112–Roquepata (Paucartambo, Cusco)

La página impresa es la del PDF menos 12.

**(a) La serie.** Tabla 6.6 (PDF 101, imp. 89): estación **Colquepata**, **1990-2014, 25 años**, fuente SENAMHI. x̄ = 23.43 mm y s = 13.11 mm.

**(b) El ajuste.**
- Gumbel por factor de frecuencia (Tabla 6.7, PDF 104), para TR de 10 a 1000.
- Comprobado: K10 = 1.3046, y 23.43 + 1.3046·13.11 = 40.53 mm, que es el valor impreso.
- La prueba K-S se hizo con HidroEsta, pero su detalle (Anexo HID-04) **no se publicó**.

**(c) Las cuencas.** Tablas 6.4-6.5 (PDF 98-100): **15 microcuencas** con A, L, pendiente por tramos de Taylor-Schwarz y tc por Témez y por Bransby-Williams.

**(d) Los caudales.**
- IDF por Dick-Peschke e I = 328.64·T^0.0976 / D^0.75 (PDF 106-107).
- Q por el racional con **C = 0.5 único**, para TR 30, 35 y 70 (Tabla 6.13, PDF 111).

**(e) Hidráulica.**
- 42 alcantarillas TMC: 37 de 36" y 5 de 44" (Tabla 6.18, PDF 118-119).
- Para cada una trae Qd, V y QE a tubo lleno (Manning), y el FS.
- **No trae** HW, S ni L por obra.
- El Qd de cada obra suma la cuenca y las cunetas. El vínculo entre microcuenca y obra está en el Anexo HID-10, **que no se publicó**.

**Defectos.**
1. Serie inhomogénea: de 1990 a 1997 los valores van de 4.4 a 9.3 mm; desde 1998, de 20 a 48 mm.
2. Se contradice sobre la distribución. El texto dice Gumbel, la conclusión dice Normal y el título de la Tabla 6.7 dice «distribución normal».

### 3.6 UPAO: Campos Muñoz e Inga Yopan (2016), La Jalca – Nueva Esperanza (Chachapoyas)

La página impresa es la del PDF menos 20.

**(a) Las series.** Trae dos, y no coinciden. Las dos son de la estación Chachapoyas, sin código:
- Cuadro 18 (PDF 91-92): 1964-73 y 1995-2001;
- tabla mensual (PDF 113-114): 1965-73 y 2004-11.

**(b) El ajuste.**
- Cuadro 20 (PDF 93):
  - Δc: Normal 0.1591, LN 0.1149, **LP3 0.0932**, Gumbel 0.1032. Δt: 0.3298.
  - P con LP3: 57.94, 86.98, 102.62, 116.90 y 148.22 mm para TR 10, 50, 100, 175 y 500.
- Gumbel por momentos con ×1.13 (PDF 114-115): x̄ = 36.81, s = 7.87, α = 6.14, u = 33.26.
- IDF: K = 84.6176, m = 0.124, n = 0.540 (PDF 123-124).
- Hay un error de transcripción en la lluvia de 18 h para TR 25: 47.21 mm en lugar de unos 53.8. Contamina la regresión de TR 25.

**(c) y (d) Cuencas y caudales.**
- 46 alcantarillas con A, tc, C = 0.35 y TR 50 (PDF 140-142).
- L y S sólo vienen para la alcantarilla 19: A = 1.25 km², L = 2415.58 m, S = 0.211 (PDF 138-139).

**(e) Hidráulica.** Sólo Manning con n = 0.024, D e y (PDF 143). TMC de 24" y 36".

**(g) Cabezal.** Un muro con H = 1.5 m, γ = 1.9 t/m³, φ = 35° y μ = 0.45 (PDF 144-150).
- Ka = 0.271.
- FS al volteo 2.57; FS al deslizamiento 1.56.
- Presiones de 7.83 y **−2.06 t/m²**: la excentricidad pasa de B/6.
- Armado por ACI/E.060 con factor 1.7. **No es AASHTO**.

### 3.7 UVG: Melgar Morán (2025), cajón prefabricado de 10'×10' por AASHTO LRFD 2018

**Datos iniciales** (Tabla 8, PDF 48):
- relleno de 6 ft;
- f'c = 5 ksi; fy = 60 ksi; γs = 0.12 kcf;
- losa superior de 0.75 ft, losa inferior de 0.83 ft, muros de 0.67 ft, cartela de 12".

**Cargas** (Tablas 9-12, PDF 50-58):
- EV sobre la losa: 0.796 k/ft;
- EH mínimo y máximo;
- LLDF = 1.15, MPF = 1.2, IM;
- presión de carga viva: HL-93 0.369 ksf y tándem 0.38 ksf.

**Resultados:**
- Momentos calculados con SAP2000 (Tabla 13, PDF 65): losa superior 12.23 kip·ft.
- As por momento último y por fisuración (Tablas 22-25, PDF 70-75).

**Lo que no trae:** hidrología e hidráulica.

---

## 4. Casos recomendados para reproducir: 4

Antes de elegir revisé lo que hace hoy el programa:

- **Ajuste de distribuciones.** `MH_hidrologia` sólo ajusta **Normal, Log Normal 2P y Gumbel por momentos** (`DISTRIBUCIONES_CON_ESTIMADOR_IMPRESO`). No ajusta LP3 ni Pearson III.
- **Tratamiento FEN.** El tratamiento `dos_poblaciones` no está implementado.
- **Relación intensidad-duración.** La de archivo es Dick-Peschke. La alternativa es la Tabla N° 04, que no baja de 1 h.
- **Estructura del marco.** La Fase 8 sólo calcula la **demanda de la losa superior** (`M8.demanda_marco`: F_e, w_EV, w_LL, M_ref). El diseño del pórtico está diferido.

### Caso 1: INDECI Piura (Miraflores). Hidrología estadística y criterio `homogeneidad_serie_fen`

- **Qué valida.**
  - `MH_hidrologia`: estimadores Normal, LN2 y Gumbel por momentos, y el estadístico y el valor crítico de K-S.
  - Sobre todo, el criterio `homogeneidad_serie_fen`, porque trae la serie completa, la serie sin FEN y la de sólo FEN con números de terceros.
- **Contraste concreto.** El programa tiene que reproducir:
  - las columnas Normal, LN y «Gumbel modificado» de los Anexos 07.1 y 07.2;
  - los Δc de los Cuadros 21-22.
- **Lo que se espera que haga el programa.** Con `serie_sin_fen`, P25 baja de 131.8 a 71.6 mm, así que el programa **tiene que detenerse** según la regla de la ficha T1-09. El estudio tomó la misma decisión, la serie con FEN, por ser la conservadora. Es un contraste directo de esa regla.
- **Entradas que faltan o que hay que declarar.**
  1. La columna `fen` año por año. El estudio marca 1972, 1973, 1983, 1987, 1992 y 1998; hay que decidir y declarar el caso de 1973 y el de 1997.
  2. El año 1971 está incompleto. Se puede dejar o quitar, pero hay que declararlo.
  3. No hay cuencas ni alcantarillas, así que el caso termina en la P24 de diseño.
  4. `factor_intervalo_fijo_p24` debe ser 1.00, porque el estudio no aplica 1.13.
- **Archivos:**
  - `/home/user/casos_reales/indeci_piura/mapa_peligros_vol1.pdf`
  - `/home/user/casos_reales/indeci_piura/mapa_peligros_vol2_anexos.pdf`

### Caso 2: UPeU Colpahuayco–Langui (Sicuani). Racional modificado de Témez

- **Qué valida.** `MH_hidrologia` en estos pasos: tc de Témez (ec. 30), K, KA, I por la ec. 34 y el racional modificado. También K-S sobre una serie de sierra.
- **Contraste concreto.** I y K de la Tabla 8 frente a la Tabla 6. Las tres microcuencas comprobadas cuadran dentro del 1 %.
- **Entradas que faltan.**
  1. **CN** de las microcuencas. Sin él no corre el racional modificado de 10 km² en adelante, que son las microcuencas 07 y 14 (el estudio las hizo con HEC-HMS).
  2. `cobertura` y `suelo` de la Tabla N° 08. El estudio da C directamente, sacado del CN.
  3. La columna `fen`, todos los años «no». Hay que declararlo.
  4. La P24 elegida sale de Pearson III, que el programa no ajusta. Para comparar I y K hay que forzar la misma P24, o comparar las razones I/P24.
  5. Las 19 columnas del CSV de puntos (cotas, CBR, SUCS…). No están, así que el caso se queda en la Fase 1-bis.
- **Lo que se espera.** Bajo 10 km², el programa usa el racional con tc de Témez y K, según `coeficiente_uniformidad_temez`. El estudio usó el modificado completo. La diferencia es de método y hay que declararla.
- **Archivo:** `/home/user/casos_reales/upeu_colpahuayco/doc.pdf`

### Caso 3: UNTumbes TU-107 (Cañaveral). La cadena hidrológica completa en costa norte, como caso adversarial

- **Qué valida.**
  - `MH_hidrologia` de punta a punta, con 41 cuencas.
  - El contraste LN2 contra los Δ de la Tabla 36.
  - Las **guardias** del programa: serie con años FEN sin declarar, valores duplicados y extremos, intensidades fuera de rango.
- **Contraste numérico exacto.** P(TR) con LN2 de la Tabla 47, y los Δ de K-S de Normal, LN2 y Gumbel.
- **El valor del caso.** No es comparar caudales, sino comprobar que el programa **no entrega en silencio** un Q a partir de esta serie.
  - La serie obliga a declarar `fen` año por año: 1983 y 1997-98.
  - Con `serie_completa` el programa daría P100 del orden de 1000 mm.
  - Los duplicados 2001 = 1996 y 2002 = 1989 son datos inválidos que el programa no detecta hoy. Si se decide que los detecte, es una entrada nueva para la hoja de ruta, no algo que se rellene.
- **Entradas que faltan.**
  1. `cobertura` y `suelo`: el estudio da C de 0.10 a 0.20 sin decir de dónde.
  2. `S_terreno`, distinta de la S del cauce.
  3. `metodo_tc` = temez. El estudio promedia con Bransby-Williams, que el programa no tiene.
  4. La columna `fen`.
  5. Las cotas de las obras.
- **Archivo:** `/home/user/casos_reales/untumbes_tu107/tesis.pdf`

### Caso 4: ESPOL Intervalles. Hidráulica HY-8 de un cajón y demanda estructural LRFD

- **Qué valida.**
  - `M3/M4`: hidráulica del marco de 1.10 × 1.10 m. Se contrastan el tirante normal (0.37 m) y las velocidades (1.76 m/s y 2.26 m/s) con el resultado de HY-8.
  - `M8.demanda_marco`: EV y carga viva HL-93 a través del relleno (Tabla 3.14).
  - K-S de cuatro series reales (Anexos 3-6).
- **Lo que se espera.** HW/D = 0.32/1.10 ≈ 0.29, por debajo de 0.75. El programa debería levantar `MetodoNoEvaluableError` para la carga HW (HDS-5, pág. 3.24) y **no** dar un número. Es un contraste de esa guardia, no de HW.
- **Entradas que faltan.**
  1. Las cotas absolutas de entrada y salida. Sólo hay pendiente y longitud; la cota de terreno es aproximada.
  2. El TW, que hay que derivarlo del canal trapezoidal de salida.
  3. La altura de relleno y el paquete. Los espesores del cajón sólo están en los planos.
  4. CBR y SUCS. El SPT da CL.
  5. La hidrología no es comparable, porque usa la IDF del INAMHI y el factor Cf del MTOP: Q = 0.613 entra **declarado**.
- **Archivo:** `/home/user/casos_reales/espol_intervalles/tesis.pdf`

### Reservas

- **UNSAAC Roquepata.** Sirve para Gumbel por momentos, que coincide exactamente con el estimador del programa. Trae 15 microcuencas con A, L y S, y usa Dick-Peschke como el programa. Es un buen sustituto del Caso 2 si se prefiere el racional simple. **Falta** C por cobertura (usa 0.5 único) y el vínculo entre microcuenca y obra.
- **UVG cajón 10'×10'.** Es el mejor contraste de **`M8.demanda_marco`**: relleno, γs, LLDF, IM y presión de carga viva vienen explícitos. Los momentos del pórtico de SAP2000 no son comparables, porque el diseño del pórtico está diferido. Está en unidades imperiales.
- **UPAO La Jalca.** No se recomienda como caso principal. Trae dos series discordantes y un error de transcripción en la IDF. Su cabezal se calcula por ASD/ACI, no por AASHTO, y le faltan L y S en 45 de las 46 cuencas.

### Lo que sigue sin cubrir

**(f) TMC por AASHTO 12 y (g) estabilidad del cabezal por AASHTO 11.** Ninguno de los documentos abiertos lo trae con todas sus entradas. Las memorias LRFD de cajón de la Carretera Central de PVN eran la fuente prevista, y no se pudieron abrir.

---

## 5. Advertencias de método

- Las tesis se usan para **comparar**, no como oráculo. Cada caso tiene defectos medidos (sección 3).
- Las discrepancias que el programa encuentre hay que contrastarlas **primero a mano contra el Manual**, no contra la tesis.
- Ningún documento trae los años FEN declarados como columna. INDECI es el único que los nombra.
- En los Casos 1 y 3 el valor de `fen` por año es una **declaración del usuario**, con su trazabilidad.

---

## 6. Lo que no se pudo abrir y por qué

| Fuente | Intento | Resultado |
|---|---|---|
| **Provías Nacional** `gis.proviasnac.gob.pe` y `gis.pvn.gob.pe`: Carretera Central, memorias de cajón 3×3 y 5×3; LP0001-2010; LP_02_2017; LPI_0002_2019; LP_0006_2020 | HTTP por túnel CONNECT al puerto 80 del proxy | El túnel se abre, pero el servidor de origen corta la conexión: `503 upstream connect error … reset reason: connection termination` |
| Ídem | Con la ruta de la raíz y con el alias | Mismo corte, en tres reintentos |
| Ídem | Control con `example.com:80` | 200: el proxy sí deja salir por HTTP |
| Ídem | HTTPS (443) | `Connection reset`. Lo más probable es que el servidor de PVN rechace IP extranjeras o no atienda HTTPS |
| `www.proviasnac.gob.pe` y `www.pvn.gob.pe` | — | No respondieron |
| Wayback Machine (`web.archive.org`), como alternativa para PVN | — | El túnel se cerró a mitad del intercambio. `archive.org` sí respondió |
| UNH HV-107 (`repositorio.unh.edu.pe`) | Prioridad 2 extra | El túnel se cerró a mitad del intercambio |
| Gencel (`scielo.sld.cu`) | — | Ídem |
| PUCP Rojas Marmolejo (`tesis.pucp.edu.pe`) | — | 403 del proxy (política) |

**Cómo destrabar PVN.** Hay que bajarlo desde una máquina con salida peruana o pedirlo por transparencia a PVN. Las rutas exactas están en `casos_reales.md` §C1. No intenté rodeos.

---

## 7. Archivos locales

| Ruta | Bytes | sha1 (12) | Origen |
|---|---|---|---|
| `/home/user/casos_reales/indeci_piura/mapa_peligros_vol1.pdf` | 40 807 423 | 18794242e0c5 | sigrid.cenepred.gob.pe |
| `/home/user/casos_reales/indeci_piura/mapa_peligros_vol2_anexos.pdf` | 18 652 263 | 505088ebc737 | sigrid.cenepred.gob.pe, documento 3795 |
| `/home/user/casos_reales/upeu_colpahuayco/doc.pdf` | 4 910 603 | f126e2d407ee | repositorio.upeu.edu.pe |
| `/home/user/casos_reales/untumbes_tu107/tesis.pdf` | 9 395 570 | fa20eacbd17b | repositorio.untumbes.edu.pe |
| `/home/user/casos_reales/espol_intervalles/tesis.pdf` | 4 924 557 | f6cfd40d9d9c | dspace.espol.edu.ec, API del ítem 058a34e7 |
| `/home/user/casos_reales/unsaac_42tmc/tesis.pdf` | 5 507 132 | 66e41d2e03b3 | repositorio.unsaac.edu.pe, handle 20.500.12918/4412 |
| `/home/user/casos_reales/upao_la_jalca/tesis.pdf` | 37 885 978 | 581b323bc372 | repositorio.upao.edu.pe, handle 20.500.12759/4417 |
| `/home/user/casos_reales/upao_la_jalca/texto_extraido_dspace.txt` | 529 358 | — | Texto que generó el propio DSpace. Es el enlace del informe previo, que no apuntaba al PDF |
| `/home/user/casos_reales/uvg_cajon_lrfd/tesis.pdf` | 3 704 072 | c7bf0d883f3b | repositorio.uvg.edu.gt |

**Derechos.** Todo lo descargado es una tesis de repositorio institucional o un documento público del Estado (INDECI/CENEPRED). No se tocó ningún sitio de copias.

## Fuentes nuevas de esta sesión (búsqueda web)

- [Mapa de peligros de Piura, Vol. II Anexos (SIGRID/CENEPRED)](https://sigrid.cenepred.gob.pe/sigridv3/documento/3795/descargar)
- [UVG: cajón 10'×10' por AASHTO LRFD 2018](https://repositorio.uvg.edu.gt/bitstreams/a3e03604-5fdb-4449-9564-e5feb4a34221/download)
- [USAT Ferreñafe (descartado)](https://repositorio.usat.edu.pe/bitstreams/8de93540-b935-44bc-81d1-fd2d1c588da6/download)
