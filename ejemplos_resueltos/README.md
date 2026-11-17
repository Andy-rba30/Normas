# Ejemplos resueltos de terceros

Ejemplos de diseño publicados que sirven de **oráculo externo** para validar el programa de
alcantarillas (`Andy-rba30/Proyecto_alcantarillas`). No son normas: van aparte de `normas/`
para que el guardián del registro normativo de ese proyecto (que sólo mira `normas/*.pdf`)
no los confunda con fuentes. Descargados el 2026-11-17 de las URL indicadas; todos son de
acceso gratuito (documentos de agencias públicas, tesis de acceso abierto o documentos de
evaluación ambiental públicos). Cada uno conserva la licencia de su autor: se usan sus cifras
para contrastar, citándolas, no se redistribuye su texto.

Un ejemplo publicado también puede estar mal: las validaciones fijan el número
**recalculado** con la fórmula de la fuente y registran la errata.

## Cajón (marco de concreto armado)

| Archivo | Fuente | URL | Qué trae | sha1 |
|---|---|---|---|---|
| `cajon/mndot_lrfd_sec12.pdf` | MnDOT *LRFD Bridge Design Manual*, Sec. 12 «Buried Structures» (HNTB, sept. 2013) | https://www.dot.state.mn.us/bridge/pdf/lrfdmanual/section12.pdf | §12.5: cajón prefabricado de 10′ × 10′ con 6 ft de relleno, f′c = 5 ksi, losas de 0.75 y 0.83 ft, muros de 0.67 ft, cartelas de 12″, fy = 65 ksi (malla soldada): cargas, combinaciones, momentos, armado, fisuración y cortante paso a paso. §12.6 trae más | `90220b993100ad74bc87836f63da878595cc7cf4` |
| `cajon/uvg_melgar_cajon_10x10.pdf` | D. Melgar Morán, tesis, Universidad del Valle de Guatemala, 2025 | https://repositorio.uvg.edu.gt/bitstreams/a3e03604-5fdb-4449-9564-e5feb4a34221/download | El mismo cajón de 10′ × 10′ por AASHTO LRFD 2018, en español, con SAP2000: tablas 13 a 23 de momentos, cortantes, axiales, Mu y acero requerido | `c7bf0d883f3bc0fa8fbfb44ad711887cd65ff951` |
| `cajon/panama_cajon_palomo_esia.pdf` | Ingenieros Geotécnicos S.A., memoria estructural del cajón pluvial del río Palomo (Panamá, 2022), documento de EsIA | https://documentoesia.miambiente.gob.pa/58206.pdf | Proyecto real: cajón de tres celdas de 3.05 × 3.05 m con relleno de 0.50 a 3.20 m, AASHTO LRFD 7.ª ed.: cargas, combinaciones, φ, momentos resistentes y armado | `230e90a7c6d3fd037c274867e771d838bfec6197` |

## Cabezal y muros de contención (M9)

| Archivo | Fuente | URL | Qué trae | sha1 |
|---|---|---|---|---|
| `cabezal_muros/caltrans_bdp_11_2.pdf` | Caltrans *Bridge Design Practice*, Cap. 11.2 «Earth Retaining Systems», oct. 2022 | https://dot.ca.gov/-/media/dot-media/programs/engineering/documents/bridge-design-practices/202210bdpchapter112earthretainingsystemsa11y.pdf | §11.2.2: muro en voladizo de concreto armado por AASHTO-CA BDS-8 (estabilidad, sismo, armado) | `9d39f13e1e9522739326b702306dfc99aa278969` |
| `cabezal_muros/cdot_ex11.xlsx` | CDOT *Bridge Design Manual*, Example 11 «Cast-in-Place Concrete Cantilever Retaining Wall», feb. 2023 | https://www.codot.gov/programs/bridge/bridge-manuals/design_manual/bridge-design-manual-calculations-examples/example-11-cast-in-place-concrete-cantilever-retaining-wall_202302.xlsx | Hoja de cálculo completa del muro en voladizo | `ecab79d542eb76824a21e4b4c79fadecc261bc0f` |
| `cabezal_muros/cdot_ex8.xlsx` | CDOT *Bridge Design Manual*, Example 8 «Wingwall Design», 2021 | https://www.codot.gov/programs/bridge/bridge-manuals/design_manual/bridge-design-manual-calculations-examples/example-8-wingwall-design-2021.xlsx | Aleta que vuela desde el estribo | `0addeb4d13138007141e678032f4b8d047d45c2a` |

## Conducto (M8)

| Archivo | Fuente | URL | Qué trae | sha1 |
|---|---|---|---|---|
| `conducto/acpa_dd1.pdf` | ACPA Design Data 1, *Highway Live Loads on Concrete Pipe*, 2009 | https://old.concretepipe.org/wp-content/uploads/DD_1.pdf | Cuatro ejemplos de carga viva sobre tubo de concreto (págs. 6 a 9) | `14af1075df128394d20c4b538c74b53004e56d08` |
| `conducto/acpa_dd22.pdf` | ACPA Design Data 22, *Flotation of Circular Concrete Pipe*, rev. 2014 | https://old.concretepipe.org/wp-content/uploads/2014/09/DD_22.pdf | Flotación por el método de la columna | `e2548f1cbc695ad250d528e1269879076521c9b8` |
| `conducto/acpa_cpdm_cap4.pdf` | ACPA *Concrete Pipe Design Manual*, Cap. 4 (ed. 2000, copia de curso del NJIT) | https://web.njit.edu/~washd/cim305/download/notes/CHAPTERS/CH%204.pdf | Cargas y resistencia de soporte; ejemplos 4-2, 4-5 y 4-7 (el 4-7 tiene un intermedio errado) | `683583a287b0c539f281a741304eb2e7efb226de` |
| `conducto/usace_em_1110_2_2902.pdf` | USACE EM 1110-2-2902, *Conduits, Culverts and Pipes*, 1997 | https://damtoolbox.org/images/3/37/EM_1110-2-2902.pdf | Apéndice B «Design Examples», en SI y en unidades de EE. UU.: tubo de concreto, TMC por ASD | `cfdc3bfd1c9291d30c98de11f27b1f1fbf7a95d8` |
| `conducto/ppi_design_guide.pdf` | PPI Drainage Handbook, *Structural Design Guide* (Draft Rev 1), 2019 | https://clvr.imiscloud.com/common/Uploaded%20files/1-PPI/Manuals-Design%20Guides/Drainage%20Handbook/1st%20Edition/Design%20Guide%20Rev1%20.pdf | HDPE y PP (con vehículo de obra, no HL-93) | `28c8f97ff0e3a012de9c785574141061e42f6fd8` |

## Casos reales (hidrología e hidráulica)

Calificados el 2026-11-17 con una lista de control (serie, ajuste, cuencas, caudal,
hidráulica, estructura, cabezal): `casos_reales/CALIFICACION.md`; la búsqueda que los
encontró, con sus fuentes y grados de verificación: `casos_reales/BUSQUEDA.md`. La tesis de
cajón de la UVG ya está en `cajon/`.

| Archivo | Fuente | Para qué sirve | sha1 |
|---|---|---|---|
| `casos_reales/indeci_piura/mapa_peligros_vol1.pdf`, `..._vol2_anexos.pdf` | INDECI, mapa de peligros de Piura (SIGRID) | Estación Miraflores 1971-2008 con la serie impresa y tres análisis (sin FEN, con FEN, sólo FEN): distribuciones y el criterio de homogeneidad con El Niño | `18794242e0c52e867130169868cf77115de6fd03`, `505088ebc737c093d7ef03f42516898dabae800f` |
| `casos_reales/upeu_colpahuayco/doc.pdf` | Tesis UPeU, carretera Colpahuayco–Langui | 14 microcuencas con el racional modificado de Témez (K, I, C, TR 70); estación Sicuani 1993-2020 | `f126e2d407eeaf90e326d9531b57459533316d9d` |
| `casos_reales/untumbes_tu107/tesis.pdf` | Tesis UNTumbes, vía TU-107 | Cadena completa (8 distribuciones con K-S, IDF, racional); caso ADVERSARIAL: años duplicados en la serie y sin mención de El Niño | `fa20eacbd17b1ef4e6e4b1bc3e5a79b1f82b1aa0` |
| `casos_reales/espol_intervalles/tesis.pdf` | Tesis ESPOL (Ecuador), Intervalles | Hidráulica de un cajón de 1.10 × 1.10 m con HY-8 y la demanda LRFD HL-93 del marco | `f6cfd40d9d9c4fb0b7243d4133c753878289e68b` |
| `casos_reales/unsaac_42tmc/tesis.pdf` | Tesis UNSAAC, 42 alcantarillas de TMC | Reserva: Gumbel por momentos y 15 microcuencas | `66e41d2e03b3b4c9077e743ca479ac7c34eb5b3c` |
| `casos_reales/upao_la_jalca/tesis.pdf` | Tesis UPAO, La Jalca – Nueva Esperanza | No recomendada: trae dos series que no coinciden | `581b323bc3723236b9932bf6cf6e2f2c78273f62` |
