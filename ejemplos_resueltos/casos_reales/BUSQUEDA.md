# Casos resueltos por terceros para validar el software de alcantarillas

Investigación bibliográfica del 2026-11-17. Sólo hice búsqueda web y lectura. No toqué ningún repositorio.

---

## 0. Cómo leer este informe. Grado de verificación

**Ningún PDF se abrió.** En esta sesión la red sólo deja usar el buscador. La lectura directa de páginas falló por DNS con `repositorio.upeu.edu.pe` y con `core.ac.uk`: los dos hosts quedan fuera del dominio permitido. Por la regla del entorno dejé de probar más sitios. Todo lo que sigue sale de los resultados del buscador, que devuelve fragmentos del texto o del índice. Cada fuente lleva una de estas cuatro marcas:

| Marca | Significado |
|---|---|
| **[E]** extracto | El buscador devolvió texto del documento que confirma lo que se cita: un número, un título de tabla o un capítulo. No se abrió el PDF. |
| **[F]** ficha | Sólo hay título, ficha de repositorio o resumen. El contenido técnico **no** está confirmado. |
| **[M]** memoria | Viene de mi conocimiento previo y no se contrastó en esta búsqueda. Hay que verificarlo antes de usarlo. |
| **[X]** | Se intentó y no se confirmó. |

**Advertencia de método.** Las tesis de pregrado peruanas tienen calidad muy variable. Sirven para **comparar**, no como oráculo. Si el programa discrepa de una tesis, primero se rehace la cuenta a mano contra la fuente normativa. Dos tipos de fuente de terceros son más fiables que una tesis:

- los ejemplos resueltos de la FHWA, como HDS-5, HEC-14 y HY-8. El repositorio ya los tiene en `NORMAS_DIR`, porque `hif12026.pdf` es el HDS-5;
- las memorias de expedientes oficiales de Provías Nacional (línea C).

**Lista de control para cada documento, una vez descargado.** Un caso es reproducible con el programa sólo si trae las cinco cosas:

1. La serie anual de P24 máx impresa: año por año, con la estación y su código SENAMHI.
2. Las cuencas tabuladas: área, longitud del cauce, pendiente o desnivel, y C o CN.
3. El caudal por punto, con su TR y su método: racional, Témez o HEC-HMS.
4. La sección adoptada con HW (o HW/D), las velocidades y el tipo de control.
5. Opcional: la estructura, con la altura de relleno, el material o espesor, los momentos y las cuantías.

---

## A. Tesis y trabajos académicos con cálculo de alcantarillas de carretera

Orden: primero las que prometen el ciclo más completo (hidrología, hidráulica y estructura), después las parciales.

### A1. UPAO: obras de arte de la carretera La Jalca – Nueva Esperanza (Chachapoyas)
- **Título:** «Diseño hidráulico y estructural de las obras de arte de la carretera La Jalca – Nueva Esperanza km 41.00 al km 53.00, distrito La Jalca, provincia de Chachapoyas».
- **Autor y año:** no aparecen en el extracto. Están en la ficha.
- **URL:** https://repositorio.upao.edu.pe/handle/20.500.12759/4417
- **PDF (probablemente el mismo trabajo):** https://repositorio.upao.edu.pe/backend/api/core/bitstreams/09629608-3c34-4b42-b68f-f0ef931fd8d3/content
- **Host:** `repositorio.upao.edu.pe`
- **Acceso:** gratis, sin registro (DSpace).
- **Qué trae [E]:** diseño hidráulico **y estructural** de alcantarillas de paso y de alivio, cunetas y puentes. Ajusta la lluvia con Gumbel y usa los criterios del USBR y las normas del MTC. Caudales de diseño de los puentes: Tinas 115.52 m³/s y Quiramachay 94.25 m³/s.
- **Pendiente de verificar:** cuántas alcantarillas trae y si imprime la serie.
- **Módulos:** hidrología, hidráulica, cabezal y estructura.
- **Utilidad:** **alta**. Es de las pocas que en el título promete la estructura.
- **Verificación:** [E] resumen; [F] contenido de las alcantarillas.

### A2. UNSAAC: tesis de carretera con 42 alcantarillas de TMC
- **Título y autor:** no salen en el extracto. El documento tiene un «Capítulo VI: Estudio hidrológico y diseño de drenaje vial», desde la pág. 78.
- **URL:** https://repositorio.unsaac.edu.pe/server/api/core/bitstreams/b2fd2434-950e-4c19-83b3-aab210e25499/content
- **Host:** `repositorio.unsaac.edu.pe`
- **Acceso:** gratis.
- **Qué trae [E]:** «42 alcantarillas, 23 de alivio y 19 de paso», de tubería metálica corrugada (TMC). El capítulo VI cubre el análisis de precipitación y caudales, la delimitación de microcuencas, el caudal de aporte y el diseño de alcantarillas.
- **Módulos:** hidrología, hidráulica, y quizá la Fase 10 (alivios y cunetas).
- **Utilidad:** **alta** por volumen: 42 puntos, con alivios (Familia B) y pasos (Familia A).
- **Verificación:** [E] cifras y capítulo; [F] completitud de los datos.

### A3. UNH: modelamiento hidrológico de obras de arte de la carretera HV-107 (Angaraes, Huancavelica)
- **Título:** «Modelamiento hidrológico de obras de arte, en la carretera HV-107; tramo EMP-26B km 0+000 al km 12+150, provincia de Angaraes – Huancavelica».
- **Año:** 2018 según el extracto.
- **URL:** https://repositorio.unh.edu.pe/handle/UNH/2879 (también https://repositorio.unh.edu.pe/items/badaa6bd-99a8-49ac-b243-55d6c56f76d0)
- **Host:** `repositorio.unh.edu.pe`
- **Acceso:** gratis.
- **Qué trae [E]:**
  - inventario vial;
  - análisis estadístico de la P máx diaria hecho **en Python**;
  - dimensionamiento de alcantarillas, badenes y puentes;
  - conclusión: «subdimensionamiento en todas las alcantarillas», con reemplazo por TMC de 36".
- **Módulos:** hidrología (ajuste de distribuciones) e hidráulica.
- **Utilidad:** **alta** para contrastar el ajuste estadístico, porque es un cálculo programado y no sólo hecho en Excel.
- **Verificación:** [E].

### A4. UPeU: drenaje superficial de la carretera Colpahuayco – Langui (Canas, Cusco)
- **Título:** «Análisis hidrológico para el diseño hidráulico del sistema de drenaje superficial en la carretera Colpahuayco – Langui del km 19+840 al km 29+840, provincia de Canas, Cusco».
- **Autores:** Paúl Yelsin Huamán Guerra, Heydy Kinberly Marrujo Carpio y Reymundo Jaulis Palomino. El año no se confirmó.
- **Tipo:** artículo o trabajo de la UPeU.
- **Ficha:** https://repositorio.upeu.edu.pe/items/789a44bf-e429-4ac9-be91-4514f4946b6a
- **PDF:** https://repositorio.upeu.edu.pe/bitstreams/01d4a93e-46c2-465a-b240-69934247e13a/download
- **Host:** `repositorio.upeu.edu.pe`. **No resolvió en esta sesión:** está fuera del dominio permitido.
- **Acceso:** gratis.
- **Qué trae [E]:**
  - 61 alcantarillas existentes evaluadas, en estado regular a bueno;
  - propone reemplazar 22 y añadir 7 de alivio;
  - método racional y racional modificado;
  - caudales calculados en Excel y HEC-HMS;
  - diseño de alcantarillas y cunetas.
- **Módulos:** hidrología (racional y Témez), hidráulica y Fase 10.
- **Utilidad:** **alta**: muchos puntos y los dos métodos que usa el programa.
- **Verificación:** [E] resumen; [F] tablas.

### A5. UNP: obras de arte del camino vecinal Culuguero – Los Molinos (Ayabaca, Piura), 2021
- **Título:** «Diseño de obras de arte en el camino vecinal Culuguero – Los Molinos, provincia de Ayabaca, Piura, 2021».
- **URL:** https://repositorio.unp.edu.pe/handle/20.500.12676/3623
- **Host:** `repositorio.unp.edu.pe`
- **Acceso:** gratis.
- **Qué trae [E]:** estudio hidrológico seguido de diseño hidráulico. Recomienda más alcantarillas de alivio, una alcantarilla de paso de quebrada, cunetas revestidas y redimensionar las existentes.
- **Módulos:** hidrología, hidráulica y Fase 10.
- **Utilidad:** **media-alta**. Es de la región Piura, pero de la sierra: hay que comprobar si usa estaciones afectadas por el FEN.
- **Verificación:** [E] resumen.

### A6. UNTumbes: drenaje transversal de la vía TU-107 Bocapán – Tamarindo (Tumbes), 2025
- **Título:** «Estudio hidrológico para los diseños hidráulicos del drenaje transversal de la vía departamental TU-107, Bocapán – Tamarindo, Tumbes 2025». Facultad de Ciencias Agrarias, Ingeniería Agrícola.
- **URL:** https://repositorio.untumbes.edu.pe/bitstreams/565eeb64-7f28-4ecc-88b6-ab2fab27ceb3/download
- **Host:** `repositorio.untumbes.edu.pe`
- **Acceso:** gratis.
- **Qué trae [E]:** sólo carátula e índice: estudio hidrológico para el diseño del drenaje transversal.
- **Pendiente de verificar [F]:** el autor, el método, los resultados y el tratamiento de los años FEN.
- **Módulos:** hidrología e hidráulica.
- **Utilidad:** **alta en potencia**. Es costa norte, la misma zona sísmica y climática del FEN que Piura, y es muy reciente.
- **Verificación:** [E] título e índice.

### A7. UNFV: estructuras de drenaje para conservación de una carretera según las normas peruanas (2024)
- **Autor:** José Apaza Huallpa. Título profesional, 2024.
- **PDF:** https://repositorio.unfv.edu.pe/bitstream/handle/20.500.13084/8709/UNFV_FIC_Apaza_Huallpa_Jose_Titulo_profesional_2024.pdf?sequence=1
- **Ficha:** https://repositorio.unfv.edu.pe/items/d72d595d-7ffa-4c98-9b72-25a63ad6cd3d
- **Host:** `repositorio.unfv.edu.pe`
- **Acceso:** gratis.
- **Qué trae [E]:**
  - aplica el Manual de Hidrología, Hidráulica y Drenaje (MTC);
  - caudales máximos de 2.23 m³/s y 1.71 m³/s en dos estaciones;
  - cunetas, zanjas de coronación y alcantarillas TMC de 48";
  - menciona alcantarillas marco y TMC con cabezales y aleros.
- **Módulos:** hidrología, hidráulica y Fase 10.
- **Utilidad:** **media**: pocos puntos, pero con número.
- **Verificación:** [E].

### A8. ESPOL (Ecuador): rediseño hidráulico de una alcantarilla de la vía Intervalles (El Tambo, Catamayo, Loja)
- **Título:** «Rediseño hidráulico de una alcantarilla que intercepta la vía Intervalles».
- **Tesis:** https://www.dspace.espol.edu.ec/retrieve/3b7c456c-e817-419c-ae8f-d8c2044aa4c7/T-70549%20LUNA%20CHAL%c3%83%20N%20CORREGIR%20Y%20SUBIR%20AL%20DSPACE.pdf
- **Artículo derivado:** https://revistacym.com/index.php/home/article/view/156
- **Hosts:** `www.dspace.espol.edu.ec` y `revistacym.com`
- **Acceso:** gratis.
- **Qué trae [E]:**
  - Q = 0.61 m³/s (0.613 en el artículo) para TR = 25 años y lluvia de 30 min;
  - hidráulica con HY-8, H Canales y Excel;
  - cajón de concreto armado de 1.10 × 1.10 m, verificado estructuralmente con Excel y CYPE;
  - estructura existente azolvada al 48.28 %.
- **Módulos:** hidrología, hidráulica (contraste con HY-8) y conducto de cajón.
- **Utilidad:** **media-alta**. Es un caso único y completo, pequeño y fácil de reproducir. La norma es ecuatoriana (MTOP): hay que separar los criterios.
- **Verificación:** [E].

### A9. Gencel (UNP), 2013: «Diseño mejorado de alcantarillas de drenaje pluvial en carreteras»
- **Revista:** *Ingeniería Hidráulica y Ambiental* (Cuba), v. 34, n. 3.
- **PDF:** http://scielo.sld.cu/pdf/riha/v34n3/riha07313.pdf
- **HTML:** http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S1680-03382013000300007
- **Host:** `scielo.sld.cu`
- **Acceso:** gratis, acceso abierto.
- **Qué trae [E]:**
  - caso de la vía a Paita (Piura): la lluvia inusual de 1999 en la quebrada Pajaritos llevó el caudal a superar ligeramente la capacidad de las alcantarillas; una colapsó;
  - propone un desborde controlado sobre la vía con protección aguas abajo;
  - trata la cimentación de los aleros y su ángulo.
- **Módulos:** hidráulica (evento extremo, V8) y protección de salida.
- **Utilidad:** **media**. Es más un criterio que un caso con todos sus datos, pero es costa de Piura.
- **Verificación:** [E] resumen; [F] números.

### A10. UNICA: riesgo hidrológico e hidráulico de la carretera Puente Chontay – Antioquia (Huarochirí)
- **URL:** https://repositorio.unica.edu.pe/server/api/core/bitstreams/9e9e0344-2e37-4077-9155-7a089ff04bcd/content
- **Host:** `repositorio.unica.edu.pe`
- **Acceso:** gratis.
- **Qué trae [E]:** **método racional modificado de Témez** con Q, C, intensidad máxima horaria, área en km² y coeficiente de uniformidad.
- **Módulos:** hidrología (Témez).
- **Utilidad:** **media-alta** para el estimador de Témez.
- **Verificación:** [E] método; [F] números.

### A11. Saldaña Vitón, 2022: caudales máximos por Témez en la subcuenca del río Chetillano (Chota)
- **Título:** «Generación de caudales máximos a través del método Témez en cuencas sin información pluviométrica de 24 horas, subcuenca del río Chetillano, Chota, 2021».
- **URL (agregador):** https://repositorioslatinoamericanos.uchile.cl/handle/2250/6453634
- **Host:** `repositorioslatinoamericanos.uchile.cl`, que remite al repositorio de origen. La universidad no se confirmó.
- **Qué trae [E]:**
  - cuatro estaciones con P24 (Cutervo, Llama, A. Weberbauer y Udima);
  - prueba K-S;
  - Cutervo como estación representativa;
  - morfometría de la subcuenca;
  - Q para TR 50, 100, 200 y 500.
- **Módulos:** hidrología (K-S, Témez y transposición).
- **Utilidad:** **media-alta** para la hidrología. No tiene alcantarillas.
- **Verificación:** [E].

### A12. UCV: alcantarillas y cunetas de la carretera Antilla – Ccollpa (Abancay)
- **URL:** https://repositorio.ucv.edu.pe/handle/20.500.12692/73013
- **Host:** `repositorio.ucv.edu.pe`
- **Qué trae [E]:** diseño hidráulico de una alcantarilla **tipo marco**, caudal máximo, verificación de la sección y longitud máxima de cuneta.
- **Acceso:** según el extracto el PDF está **embargado**: hay que comprobarlo.
- **Módulos:** hidráulica de cajón y Fase 10.
- **Utilidad:** media si se libera; baja mientras siga embargado.

### A13. UNI: tres informes de suficiencia sobre drenaje vial
- **a) Cabrera Loayza, O. del R. (2006), «Alcantarillas de drenaje de carreteras»**
  - PDF: https://repositorio.uni.edu.pe/bitstream/20.500.14076/15868/1/cabrera_lo.pdf
  - Qué trae [E]: metodología para evaluar alcantarillas flexibles; anexos con SMADA y HEC-HMS, datos de campo y planos.
- **b) Pérez Forero, R., «Análisis hidrológico e hidráulico: monitoreo de la conservación de la carretera Cañete – Huancayo, km 205+000 al 220+000»**
  - PDF: https://repositorio.uni.edu.pe/bitstream/20.500.14076/6618/1/perez_fr.pdf
- **c) «Ampliación y mejoramiento de la carretera Cañete – Yauyos – Huancayo, km 167+400 al 167+700: estudio del sistema de drenaje»**
  - PDF: https://repositorio.uni.edu.pe/bitstream/20.500.14076/8080/4/pomacaja_rm.pdf
  - Tiene un capítulo 11, «Evaluación y diseño de obras de arte y drenaje».
- **Host:** `repositorio.uni.edu.pe`. Acceso gratis.
- **Módulos:** hidrología e hidráulica.
- **Utilidad:** media. Los informes de suficiencia de la UNI suelen reproducir proyectos reales.
- **Verificación:** [E] títulos e índices.

### A14. Otras tesis peruanas con evaluación de alcantarillas (utilidad media-baja, sólo [F]/[E] de índice)
- **UPT, carretera Tacna – Tarata, km 40–60:** inventario y evaluación de obras de drenaje con estudio hidrológico.
  - https://repositorio.upt.edu.pe/bitstream/handle/20.500.12969/555/Melchor_Vargas-Mamani_Ayala.pdf
  - Host: `repositorio.upt.edu.pe`
- **Continental (2024), Huacho Ochoa, Haquira (Apurímac):** alcantarillas y cunetas en estado deficiente; menciona 21 alcantarillas metálicas requeridas y HEC-RAS.
  - https://repositorio.continental.edu.pe/bitstream/20.500.12394/15161/2/IV_FIN_105_TE_Huacho_Ochoa_2024.pdf
  - Host: `repositorio.continental.edu.pe`
- **UCSS (2021), camino vecinal Valle Callacate – Sinchimache (Cutervo):** evaluación hidrológica e hidráulica para obras de arte. Según un extracto secundario, TMC de 48" y 60" [X].
  - https://repositorio.ucss.edu.pe/handle/20.500.14095/2134
  - Host: `repositorio.ucss.edu.pe`
- **UNSA, vulnerabilidad hidrológica de la Interoceánica, km 12–14 (variante Uchumayo):** Q para TR 75.
  - Ficha: https://alicia.concytec.gob.pe/vufind/Record/UNSA_1513f5a8d35fd52f5e9e97f1da7c6783

### A15. Trabajos latinoamericanos útiles para la estructura y la hidráulica
- **Bejarano Caballero, R. (2017), «Presentación estándar para diseño hidráulico de alcantarillas».** Maestría, Escuela Colombiana de Ingeniería.
  - PDF: https://apiescuelaing.bibliolabtech.com/server/api/core/bitstreams/7703ddf5-76c1-40a9-bcf0-9da2a19e1f3c/content
  - Ficha: https://kujane.minciencias.gov.co/Record/ESCUELAIG2_c79424e22d47a9f100f1fa899a2a3f82/Description
  - Licencia CC BY-NC 4.0.
  - Qué trae [E]: control de entrada y de salida, alcantarilla circular y cajón; el extracto de un documento hermano tabula HW y velocidades de salida con el enfoque FHWA.
  - Módulo: hidráulica (HDS-5). Utilidad **media-alta** como contraste en español del procedimiento HDS-5.
- **Mendoza Macedo, Linaja Ayala y Challco Mamani (UTP), LACCEI 2025, n.º 1392, «Comparative analysis of AASHTO and Eurocode regulations for the design of cantilever walls».**
  - PDF: https://laccei.org/LACCEI2025-Mexico/full-papers/Contribution_1392_final_a.pdf
  - Host: `laccei.org`. Acceso abierto.
  - Qué trae [E]: un muro en voladizo de la defensa ribereña del río Tumbes, diseñado por AASHTO LRFD y por Eurocódigo, con costo por metro.
  - Módulo: **cabezal y muro de ala** (estabilidad y armado LRFD). Utilidad **media**: hay que comprobar que imprime todas las entradas.
- **TEC Costa Rica, «Diseño parametrizado de alcantarillas cuadradas».**
  - https://repositoriotec.tec.ac.cr/handle/2238/6052 (host `repositoriotec.tec.ac.cr`)
  - Qué trae [E]: alrededor de 700 diseños de cajón de 1, 2 y 3 celdas con rellenos de 0 a 10 m, en nueve planos. El extracto no nombra la norma.
  - Módulo: conducto de cajón. Utilidad media, como tabla de contraste masiva.
- **UVG Guatemala, cajón prefabricado de 10'×10' por AASHTO LRFD 2018.**
  - https://repositorio.uvg.edu.gt/handle/123456789/6363
  - Módulo: conducto de cajón. Utilidad media. Verificación [E] resumen.

> **Hallazgo negativo.** No encontré ninguna tesis peruana que diseñe el **conducto de TMC por AASHTO LRFD Sec. 12** (pandeo, empuje anular, rigidez de manejo) con número. Para ese módulo la validación de terceros hay que buscarla fuera de las tesis peruanas: ver B6.

---

## B. Libros y manuales con ejemplos resueltos

### B1. Villón Béjar, M.: HidroEsta y sus artículos. Copia **legal y gratuita**.
- **Artículo de 2012:** «HidroEsta, software para cálculos hidrológicos». *Revista Digital Matemática, Educación e Internet*, v. 12, n. 2.
  - PDF: https://tecdigital.tec.ac.cr/servicios/revistamatematica/ARTICULOS_V12_N2_2012/RevistaDigital_MVillon_V12_N2_2012/RevistaDigital_MVillon_V12_N2_2012_pdfScr.pdf (host `tecdigital.tec.ac.cr`)
  - Espejo: https://www.redalyc.org/pdf/6079/607972985007.pdf (host `www.redalyc.org`)
- **Versión en inglés:** *Tecnología en Marcha*, 2016, pp. 95–108.
  - https://dialnet.unirioja.es/descarga/articulo/5414868.pdf (host `dialnet.unirioja.es`)
- **Ficha del software (TEC):** https://www.tec.ac.cr/sites/default/files/media/doc/hidroesta.pdf (host `www.tec.ac.cr`)
- **Qué trae [E]:**
  - el ajuste a normal, lognormal 2 y 3, gamma, log-Pearson III, Gumbel y log-Gumbel;
  - la prueba Smirnov-Kolmogorov;
  - el caudal máximo por métodos racional, Mac Math, Gumbel y Nash.
- **Pendiente de verificar [F]:** si el artículo trae un ejemplo con números de entrada y salida.
- **Módulo:** hidrología (distribuciones y K-S).
- **Utilidad:** **alta**: el programa de referencia de facto en el Perú. Si las tesis usan HidroEsta, el programa debe reproducir HidroEsta.

### B2. Villón, M.: «Hidrología estadística» (Ed. Tecnológica de Costa Rica, 2006) e «Hidrología», 2.ª ed. (TEC, 2022)
- **Qué trae [E]:**
  - *Hidrología estadística*: cap. V sobre pruebas de bondad de ajuste (gráfica, χ² y Smirnov-Kolmogorov) y cap. VI sobre distribuciones (normal, lognormal, gamma, LP III, Gumbel y log-Gumbel). El **ejemplo 5.2** es una prueba K-S, aunque contra la normal.
  - *Hidrología*, 2.ª ed.: el **cap. 7** trata los caudales máximos (nota del TEC: https://tec.ac.cr/hoyeneltec/printpdf/4220).
- **Copia legal:** sólo **de pago**, en la Editorial Tecnológica de Costa Rica o en Ediciones Villón (Lima), o **en biblioteca**.
- **Copias no autorizadas:** circulan en Scribd (requiere cuenta o suscripción para descargar), idoc.pub, pdfcoffee y doku.pub. **No recomiendo bajarlas.**
- **Módulo:** hidrología.
- **Utilidad:** **alta** (manual de HidroEsta y ejemplos K-S y Gumbel).
- **Verificación:** [E] índice.

### B3. Chow, Maidment y Mays, «Hidrología aplicada» (McGraw-Hill, 1994; original en inglés de 1988)
- **Ejemplos útiles [M], de memoria:**
  - **Ej. 12.2.1:** EV1 o Gumbel sobre las lluvias máximas anuales de 10 min en Chicago, 1913–1947, con la lluvia de 5 años;
  - **sec. 12.3:** factores de frecuencia (Gumbel, LP III);
  - **sec. 12.4:** posiciones de graficación;
  - **cap. 14:** IDF y tormentas de diseño;
  - **sec. 15.1:** método racional.
  - El buscador **no** confirmó estos números [X]: hay que verificarlos con el ejemplar.
- **Copia legal:** sólo de pago o en biblioteca. Las copias de Scribd, SlideShare y similares no están autorizadas.
- **Módulo:** hidrología.
- **Utilidad:** alta para el Gumbel por momentos y por factor de frecuencia: son números clásicos y fáciles de reproducir.

### B4. Aparicio Mijares, F. J., «Fundamentos de hidrología de superficie» (Limusa)
- **Qué trae [M]:** un capítulo de análisis estadístico con Gumbel. El buscador sólo confirmó que se cita su tabla de media y desviación reducidas de Gumbel (fuente: artículo de la U. de Guanajuato) [E parcial]. Capítulo y página no verificados.
- **Copia legal:** sólo de pago o en biblioteca.
- **Utilidad:** media. Es útil para el Gumbel con la corrección de Nielsen por el tamaño de muestra, que muchas tesis peruanas usan sin decirlo.

### B5. Rodríguez Serquén, A., «Puentes con AASHTO-LRFD» y «Análisis y diseño de alcantarillas tipo cajón de concreto armado con AASHTO»
- **Libro.** Hay ediciones de 2010 (5.ª), 2014 (7.ª), 2017, 2020 (9.ª, sobre AASHTO 2020) y **2025**, esta última con ISBN en la BNP: https://isbn.bnp.gob.pe/catalogo.php?mode=detalle&nt=155659
  - **Acceso:** el autor **distribuye** el PDF por su cuenta. Civilgeeks publicó la edición 2020 diciendo que el autor se la envió: https://civilgeeks.com/2020/12/15/puentes-con-aashto-lrfd-libro-actualizado-al-2020-msc-ing-arturo-rodriguez-serquen/ (host `civilgeeks.com`).
  - El propio libro **prohíbe la reproducción sin permiso del autor**. Contacto publicado: ing_ars@hotmail.com. Recomiendo pedírselo a él o comprar la edición de 2025.
  - **Pendiente de verificar [M]:** un capítulo de estribos con un problema resuelto de estribo en voladizo y empuje sísmico (Mononobe-Okabe). El buscador no lo confirmó.
- **Documento de alcantarillas tipo cajón** (AASHTO 2014).
  - **Qué trae [E]:** cargas (peso propio, empuje de tierra, agua y sobrecargas), carga viva con factor de presencia múltiple, impacto y distribución para relleno bajo, combinaciones de Resistencia y Servicio, modelo en SAP2000 con envolventes y revisión por cortante de la losa inferior y los muros. Datos de relleno: γ = 2000 kg/m³ y φ = 21.5°.
  - **Dónde circula:** SlideShare (https://www.slideshare.net/slideshow/analisis-y-diseno-de-alcantarillas-tipo-cajon-de-concreto-armado-con-aashtomsc-ing-arturo-rodriguez-serquen-pdf/265387069), Studocu y Scribd. Los tres piden cuenta para descargar y su autorización no consta.
- **Módulos:** conducto de cajón (AASHTO 12 y 5) y cabezal o estribo (AASHTO 11 y 5).
- **Utilidad:** **alta**. Es el texto peruano de referencia para LRFD y trae ejemplos con todos sus números.

### B6. Manuales de terceros en inglés, de dominio público o gratuitos
- **FHWA HDS-5 (2012, FHWA-HIF-12-026), HEC-14 (2006) y HY-8.** Dominio público.
  - Ficha de HDS-5: https://rosap.ntl.bts.gov/view/dot/41317 (host `rosap.ntl.bts.gov`)
  - Archivo de HEC-14: https://webarchive.library.unt.edu/web/20081107052121/http://www.fhwa.dot.gov/engineering/hydraulics/pubs/06086
  - El proyecto **ya los tiene** en `NORMAS_DIR` y ya valida contra ellos (`validacion_hds5.md`, `validacion_hy8.md`). No los repito como «nuevos».
- **ACPA, *Concrete Pipe Design Manual*.** Tiene derechos de autor (© 2007) y **no hay copia oficial gratuita**. Sí son gratis sus hojas *Design Data*.
  - DD 9, instalaciones normalizadas y *bedding factors*: https://old.concretepipe.org/wp-content/uploads/2014/09/DD_9.pdf (host `old.concretepipe.org`)
  - DD 40 sirve para el cálculo manual por diseño indirecto.
  - Un curso del NJIT reproduce un ejemplo con Bfe = 2.8 y BfLL = 1.9: https://web.njit.edu/~washd/cim305/download/notes/CHAPTERS/CH%204.pdf
  - Módulo: **conducto de concreto** (D-load y clase de AASHTO M 170). Utilidad **alta** para la Fase 8.
- **NCSPA, *Corrugated Steel Pipe Design Manual*.** De pago, en ncspa.org.
  - Contech publica gratis una guía con cálculos de ejemplo: https://www.conteches.com/media/qujfuekl/spdg.pdf (host `www.conteches.com`) [F].
  - Módulo: **conducto de TMC** (empuje anular, pandeo, rigidez de manejo). Utilidad **alta** si los ejemplos traen todos sus números.
- **Manuales de puentes de DOT estatales con capítulo de alcantarillas LRFD.** Iowa DOT, cap. 7; DelDOT, cap. 7; SCDOT, criterios de cajón.
  - Missouri DOT trae un **ejemplo resuelto de cajón con aleros**, pero por **LFD**, no LRFD [E].
  - Utilidad: media-baja (criterios y planos tipo más que casos con todos sus datos).
- **Keller y Sherar (USFS), «Ingeniería de caminos rurales», en español y gratis.**
  - https://webarchive.library.unt.edu/eot2008/20080922033800/http:/www.fs.fed.us/global/topic/sfm/roads_manual_espagnol_012908.pdf
  - Utilidad baja: tablas de dimensionamiento y control de erosión, sin casos completos.

### B7. Concreto armado peruano (E.060), para el cabezal y el muro de ala
- **Harmsen, T., «Diseño de estructuras de concreto armado», 5.ª ed.** Fondo Editorial PUCP, 2017; ACI 318-14 y E.030-2016.
  - Ficha: https://repositorio.pucp.edu.pe/index/handle/123456789/199468
  - Trae muros y cimentaciones [E]. El capítulo y el ejemplo de muro en voladizo no se confirmaron [F].
  - Acceso: **de pago**, en la biblioteca PUCP o en libro electrónico (Digitalia).
  - Utilidad: media-alta para el contraste E.060 (A5).
- **Morales Morales, R., «Diseño en concreto armado» (ICG).** Ejemplos de muros de contención [M].
  - Acceso: de pago.
  - Utilidad: media.
- **Anexos de tesis PUCP de diseño de puentes.** Ejemplo: https://tesis.pucp.edu.pe/repositorio/bitstream/handle/20.500.12404/6302/ACEVEDO_V%C3%8DCTOR_DISE%C3%91O_PUENTE_ANEXOS.pdf
  - Diseño numérico de un muro de contención con empuje activo ka·γ·H²/2 = 22 094 kg/m [E], sin LRFD ni Mononobe-Okabe.
  - Host `tesis.pucp.edu.pe`. Utilidad media-baja.
- **INVIAS (Colombia), «Manual de drenaje para carreteras» (2009).** Es oficial y gratuito en invias.gov.co, pero no confirmé que traiga ejemplos resueltos de control de entrada o salida [X]. Utilidad baja.

---

## C. Expedientes técnicos y estudios definitivos públicos (Perú)

### C1. **Servidor de expedientes de Provías Nacional, `gis.proviasnac.gob.pe`.** Hallazgo principal de la línea C.
- **Qué es [E]:** un listado de directorios **abierto** (HTTP, sin HTTPS) de expedientes técnicos de licitaciones de PVN. Trae memorias en PDF, anexos de hidrología y planos de alcantarillas en DWG y PDF. También responde con el alias `gis.pvn.gob.pe`.
- **Acceso:** gratis, sin registro.

| Expediente | URL | Qué trae [E] |
|---|---|---|
| **Carretera Central (UGE), raíz** | http://gis.proviasnac.gob.pe/expedientes/UGE/Carretera%20Central/ | Carpetas numeradas; la 05 es «Hidrología e Hidráulica» y la 06 «Estructuras y O_Arte». |
| Carretera Central, planos de alcantarillas | http://gis.proviasnac.gob.pe/expedientes/UGE/Carretera%20Central/05.%20Hidrologia%20e%20Hidraulica/10.-alcantarillas%20planos/ | DWG de diciembre de 2018 y curvas de nivel cada 5 m. |
| **Carretera Central, memoria estructural del cajón de 3.00 × 3.00** | http://gis.proviasnac.gob.pe/expedientes/UGE/Carretera%20Central/06.%20Estructuras%20y%20O_Arte/1_INFORME/04_Alcantarillas/5_3.00x3.00.pdf | Cálculo **AASHTO LRFD** del cajón: f'c = 28 MPa, fy = 4200 kg/cm², factores de carga LRFD, franja de carga viva con umbral de relleno de 0.60 m, cita de 5.14.5.3 y modelo en SAP2000. |
| **Carretera Central, memoria estructural del cajón de 5.00 × 3.00** | http://gis.pvn.gob.pe/expedientes/UGE/Carretera%20Central/06.%20Estructuras%20y%20O_Arte/1_INFORME/04_Alcantarillas/6_5.00x3.00.pdf | Ídem para 5 × 3 m. |
| 2010 / LP0001-2010 (HOB Consultores; por el contexto, Chongoyape – Cochabamba – Cajamarca [F]) | http://gis.proviasnac.gob.pe/expedientes/2010/LP0001-2010/Disk1/Vol%20I%20Anexo%20C%20Tomo%20I.pdf | **Anexo C, Estudio de Hidrología e Hidráulica (Tomos I y II)**: antecedentes y análisis hidrológico; quebradas resueltas con alcantarillas TMC, de losa y de marco. |
| 2017 / LP_02_2017 | http://gis.proviasnac.gob.pe/Expedientes/2017/LP_02_2017/ | «07 Memoria Descriptiva Hidrología e Hidráulica.pdf» y «Hidrología e Hidráulica Vol. II», Tomos VI.1 y VI.2. |
| 2019 / LPI_0002_2019 | http://gis.proviasnac.gob.pe/expedientes/2019/LPI_0002_2019/ExpedienteTecnico/ | «14 Estudio Hidrología e Hidráulica Tomo 1-2.pdf». |
| 2020 / LP_0006_2020 | http://gis.proviasnac.gob.pe/expedientes/2020/LP_0006_2020/ExpedienteTecnico/SECCION%203/06%20ESTUDIOS%20TECNICOS/ | «07 Estudio de Hidrología e Hidráulica.pdf». |
| 2014 / Pampas | http://gis.proviasnac.gob.pe/Expedientes/2014/Pampas/ | «Anexo – Estudios básicos D – Hidrología e Hidráulica.pdf». |
| 2011 / LP 0007, Chota – Bambamarca – Hualgayoc | http://gis.proviasnac.gob.pe/expedientes/2011/LP%200007/CD%20CHOTA-BAMBAMARCA-HUALGAYOC/ | Expediente completo; hay que buscar dentro el volumen de hidrología. |
| 2016 / LP009, Puente Tingo y accesos | http://gis.proviasnac.gob.pe/expedientes/2016/LP009/INF-FINAL/DIA%20Pte%20Tingo%20y%20accesos/Anexos/B.%20Planos/b.3%20Obras%20de%20Drenaje/ | Planos de alcantarillas, cajas, cunetas y badenes. |

- **Módulos:** **todos**: hidrología con estaciones SENAMHI, hidráulica por punto, conducto de cajón LRFD y obras de arte.
- **Utilidad:** **la más alta de todo el informe.** Son estudios definitivos **oficiales**, firmados por consultores y revisados por PVN. Las memorias LRFD de cajón son el mejor caso de terceros para el módulo estructural.
- **Verificación:** [E] listados y fragmentos. No abrí los volúmenes de hidrología para comprobar que imprimen las series.

### C2. SEACE: expediente técnico de obra (ETO) en el buscador público
- **Obligación [E]:** desde el **30-01-2019** las entidades registran el ETO en el SEACE en los procedimientos de obra regidos por la Ley 30225. Cualquiera puede descargarlo.
- **Buscador:** https://prod2.seace.gob.pe/seacebus-uiwd-pub/fichaSeleccion/fichaArchivoExpedienteTecnicoObra.xhtml (host `prod2.seace.gob.pe`)
- **Guía del OSCE:** https://cdn.www.gob.pe/uploads/document/file/1116393/Gu%C3%ADa_r%C3%A1pida_para_la_visualizaci%C3%B3n_del_Expediente_T%C3%A9cnico_de_Obra_en_la_Ficha_de_selecci%C3%B3n_del_SEACE.pdf (host `cdn.www.gob.pe`)
- **Cómo se usa:** se busca el procedimiento, se abre la ficha de selección, se pulsa el ícono del ETO y se descarga por secciones.
- **Acceso:** gratis y sin registro. La interfaz es JSF con validaciones y no conviene automatizarla: se descarga a mano.
- **Qué trae:** el expediente completo (memoria, estudios básicos con hidrología, planos y presupuesto) de **obras convocadas desde 2019**: carreteras regionales y vecinales, y la reconstrucción tras el Niño Costero en Piura, Tumbes y Lambayeque.
- **Utilidad:** **alta**, porque permite elegir obras en la costa norte con FEN, pero exige búsqueda manual proyecto por proyecto.
- **Verificación:** [E] normativa y guía.

### C3. Invierte.pe (MEF): consulta avanzada de inversiones
- **URL:** http://ofi5.mef.gob.pe/wp/BusquedaAvanzada.aspx, según el manual del MEF de 2018 (host `ofi5.mef.gob.pe`).
- **Qué trae [E]:** la base de inversiones con el campo «último estudio». **No confirmé** que adjunte los estudios en PDF; en la práctica suele dar sólo fichas y formatos.
- **Utilidad:** **baja** para obtener cálculos. Sirve para hallar el código y el nombre exacto del proyecto y luego buscarlo en el SEACE o en PVN.

### C4. Copias de terceros de estudios reales: SlideShare, Scribd, pdfcoffee
- Capítulos de hidrología y drenaje de estudios definitivos [E]:
  - Motupe – Pampa Bernilla, con TR de 100 años para puentes y de 50 para alcantarillas de paso, y alcantarillas tipo marco;
  - Ilave – Mazocruz (Puno), km 10–83;
  - Mollepata – Pallasca (recopilación de OCTSAC);
  - Yauriske – Huanoquite, con 41 alcantarillas.
- URLs vistas:
  - https://www.slideshare.net/slideshow/18-capitulo-vii-estudio-de-hidrologia-y-drenaje/74822261
  - https://www.slideshare.net/slideshow/informe-hidrologia-hidraulica-y-drenaje-i/71965404
  - No verifiqué cuál de las dos es cuál.
- **Acceso:** SlideShare y Scribd piden cuenta para descargar, a veces de pago. pdfcoffee no tiene autorización clara.
- **Utilidad:** baja-media. Sirve si el original no está en PVN ni en el SEACE.

### C5. Gobierno Regional de Piura (SIAR) y estudios de cuenca
- **«Estudio para el tratamiento integral del río Piura – Apéndice D»:** https://siar.regionpiura.gob.pe/documentos/normativa/204.pdf (host `siar.regionpiura.gob.pe`).
  - Es hidrología de río, no de alcantarillas. Afirma que la estación Miraflores es la única con P24 confiable en la cuenca baja [E].
  - Utilidad: media, para los datos de sitio de la costa de Piura.

---

## D. Datos hidrológicos reales: SENAMHI y estudios con serie impresa

### D1. SENAMHI: descarga de datos diarios por estación
- **Portal:** https://www.senamhi.gob.pe/site/descarga-datos/ (ruta antigua: https://www.senamhi.gob.pe/?p=descarga-datos-hidrometeorologicos)
- **Tutorial oficial:** https://www.senamhi.gob.pe/mapas/descarga-datos/pdf/tutorial-para-la-descarga-de-datos.pdf
- **Ficha del servicio en gob.pe:** https://www.gob.pe/9312-conocer-los-datos-hidrometeorologicos-del-peru-descargar-los-datos-meteorologicos
- **Host:** `www.senamhi.gob.pe` (también `web2.senamhi.gob.pe`).
- **Cómo funciona [E]:**
  - menú «Datos» → «Descarga de datos» → mapa de estaciones → se elige la estación;
  - hay que **registrarse** con DNI, correo y teléfono; la contraseña llega por correo;
  - se descarga un **archivo de texto** con año, mes, día, precipitación, Tmáx y Tmín;
  - el valor **−99.9** significa sin dato;
  - el archivo se abre en Excel.
- **Costo:** la descarga web se describe como de libre acceso [E, fuente antigua]. **No confirmé** que hoy sea gratuita. La información **procesada** (series ya agregadas, certificadas) se pide por el TUSNE, que es **de pago** según el tarifario: https://www.senamhi.gob.pe/pdf/trans/tusne_senamhi_2024.pdf y https://www.senamhi.gob.pe/?p=solicitud-servicio
- **Consulta tabular sin descarga:** https://www.senamhi.gob.pe/servicios/?p=estaciones (tabla por estación y mes).
- **Procedimiento para el programa:**
  1. Se baja el diario de la estación.
  2. Se extrae el **máximo anual de 24 h** por año hidrológico.
  3. Se descarta todo año con meses faltantes en la temporada de lluvias, y se declara.
  4. Se aplica el factor de lluvia fija contra lluvia de 24 h si la serie es pluviométrica de lectura diaria.
- **Utilidad:** **alta**, porque es la fuente primaria de la serie.

### D2. PISCOp v2.1 (SENAMHI): precipitación en grilla diaria y mensual
- **Descarga:** https://piscoprec.github.io/ (host `piscoprec.github.io`). Según un blog [E], los archivos NetCDF se sirven desde Google Drive (`drive.google.com`).
- **Ficha y artículo:** https://repositorio.senamhi.gob.pe/handle/20.500.12542/288. Aybar et al. (2020), *Hydrological Sciences Journal*, DOI 10.1080/02626667.2019.1649411.
- **Mensual en IRIDL:** https://iridl.ldeo.columbia.edu/SOURCES/.SENAMHI/.HSR/.PISCO/.Prec/.v2p1/.unstable/.monthly/.Prec
- **Qué trae [E]:**
  - resolución 0.1°;
  - versión estable de 1981 a 2016; versión «unstable» operativa hasta hoy;
  - productos diario y mensual;
  - licencia **CC BY-NC-ND**.
- **Utilidad:** media. Sirve para rellenar huecos o para el contraste regional. **No sustituye** a la estación en un expediente: es un producto interpolado y su máximo diario tiende a quedar por debajo del puntual.

### D3. Estudios con la **serie de P24 máx impresa**, para reproducir el ajuste
1. **INDECI / PNUD, «Mapa de peligros de Piura», informe principal, Vol. I.**
   - PDF: https://sigrid.cenepred.gob.pe/docs/PARA%20PUBLICAR/INDECI/INFORME%20PRINCIPAL%20DEL%20%20ESTUDIO%20MAPA%20DE%20PELIGROS%20DE%20PIURA%20(VOLUMEN%20I).pdf (host `sigrid.cenepred.gob.pe`)
   - Qué trae [E]:
     - **Cuadro 13:** P máx 24 h de la estación **Miraflores, 1971–2008**;
     - **Cuadros 14 y 15:** años **1983** y **1998**;
     - histogramas y curvas de período de retorno;
     - **Anexos 07.1 y 07.2:** análisis de frecuencia de la P24 **con y sin El Niño**.
   - Módulo: hidrología, **y en particular el criterio de homogeneidad de la serie FEN** (`homogeneidad_serie_fen`): es un contraste de terceros directo de la separación con y sin FEN.
   - Dato secundario para control cruzado: un estudio del CENEPRED en Castilla cita 173.6 mm el 24-01-1998 en Miraflores [E].
   - Utilidad: **muy alta** para la costa de Piura.
2. **ANA (2010), «Estudio de máximas avenidas en las cuencas de la vertiente del Pacífico – Cuencas de la Costa Norte».** Informe final; Cayo Ramos Taipe, con Marcelo Portuguez Maurtua.
   - PDF: https://sigrid.cenepred.gob.pe/sigridv3/documento/9242/descargar
   - Qué trae [E]: análisis de P24 máx; subcuencas del río Piura con características físicas tabuladas; Gumbel, Pearson III y LP III sobre caudales máximos anuales; HEC-HMS.
   - Utilidad: **alta**: oficial, con cuencas tabuladas.
3. **Rojas Marmolejo, S., tesis PUCP, «Cálculo de precipitaciones y caudales de diseño de sistema de drenaje pluvial urbano en zonas de Huancavelica, Junín y Ayacucho».**
   - PDF: https://tesis.pucp.edu.pe/repositorio/bitstream/handle/20.500.12404/10192/ROJAS_MARMOLEJO_SHEYLA_CALCULO_PRECIPITACIONES_TESIS.pdf (host `tesis.pucp.edu.pe`)
   - Qué trae [E]:
     - **tablas 3.11 a 3.15** con las P máx anuales de San Pedro de Cachi, Huanca Sancos, Huamanga, La Quinua y otra estación (datos SENAMHI);
     - Gumbel y log-Gumbel;
     - tabla de valores críticos de K-S;
     - IDF;
     - racional contra hidrograma unitario.
   - Licencia CC. Utilidad: **alta** para reproducir el ajuste y la prueba K-S con varias estaciones.
4. **Luque Pari, G. N. (2022), «Modelamiento probabilístico de las lluvias máximas en 24 horas en la vertiente del Pacífico de la región Piura, 1965–2019».**
   - https://repositorioslatinoamericanos.uchile.cl/handle/2250/6455238
   - Qué trae [E]: valores atípicos, independencia y modelo regional. Que use 20 estaciones no se confirmó.
   - Utilidad: alta en potencia para Piura.
5. **JICA, estudios de control de inundaciones de las cuencas Chira y Piura.**
   - Probablemente https://openjicareport.jica.go.jp/pdf/12124475_01.pdf (host `openjicareport.jica.go.jp`).
   - Qué trae [E]: Tabla 2.2.1-4 con la P máx 24 h **por año y por estación** de la cuenca del Chira.
   - Acceso: gratis.
   - Utilidad: alta para el norte. No confirmé qué PDF exacto de la serie la contiene.
6. **SENAMHI, estudios técnicos con PDF libre.**
   - Análisis regional de precipitaciones máximas: https://www.senamhi.gob.pe/load/file/01401SENA-62.pdf (momentos L y fórmulas de Gumbel).
   - Extremos hidrológicos de la cuenca del Chicama: http://sigrid.cenepred.gob.pe/docs/PARA%20PUBLICAR/SENAMHI/Estudio%20extremos%20hidrologicos%20-%20Cuenca%20Rio%20Chicama.pdf
   - Utilidad: media. Sirven para comparar parámetros; puede que no impriman la serie completa.
7. **Saldaña Vitón (2022), ver A11:** cuatro estaciones con P24 y K-S.

---

## E. Qué fuente valida qué módulo (resumen)

| Módulo del programa | Mejores fuentes de terceros |
|---|---|
| Hidrología: ajuste de distribuciones, K-S, homogeneidad FEN | D3.1 (INDECI Piura, con y sin Niño), D3.3 (PUCP Rojas Marmolejo), B1 y B2 (Villón y HidroEsta), A3 (UNH, Python), D3.2 (ANA 2010), B3 (Chow) |
| Hidrología: caudal por racional o Témez | A4 (UPeU), A10 (UNICA, Témez), A11 (Saldaña Vitón), A2 (UNSAAC), C1 (volúmenes de hidrología de PVN) |
| Hidráulica: HW, control, velocidades | C1 (PVN), A8 (ESPOL, HY-8), A15 (Bejarano, HDS-5), A1 (UPAO), y los ejemplos propios de HDS-5 y HY-8 que el proyecto ya tiene |
| Fase 10: alivios y cunetas | A2, A4, A5, A7, A12 |
| Conducto de concreto o cajón (AASHTO 12 y 5) | **C1, memorias LRFD de cajón 3×3 y 5×3 de la Carretera Central**, B5 (Rodríguez Serquén, cajón), A15 (TEC y UVG), B6 (ACPA, D-load) |
| Conducto de TMC (AASHTO 12) | Sin tesis peruana. B6: guía Contech o NCSPA |
| Cabezal y muro de ala (AASHTO 11 y 5, E.060) | B5 (Rodríguez Serquén, estribos [M]), A15 (LACCEI 2025, Tumbes), B7 (Harmsen, Morales), A1 (UPAO, estructural) |
| Protección de salida (HEC-14) | Ejemplos de HEC-14, ya en el proyecto. A9 (Gencel, criterio de desborde y protección) |

---

## F. Hosts que hay que habilitar, por orden de prioridad

Los hosts de esta lista que se probaron (`repositorio.upeu.edu.pe` y `core.ac.uk`) **no resolvieron**: están fuera del dominio permitido de la sesión. Hay que habilitarlos para poder descargar.

| # | Host exacto | Para qué | Nota |
|---|---|---|---|
| 1 | `gis.proviasnac.gob.pe` | Expedientes PVN: hidrología y memorias LRFD de alcantarillas (C1) | **Sólo HTTP, puerto 80** |
| 2 | `gis.pvn.gob.pe` | Alias del anterior (C1) | **Sólo HTTP, puerto 80** |
| 3 | `sigrid.cenepred.gob.pe` | INDECI Piura (serie de Miraflores, con y sin Niño), ANA 2010 Costa Norte, SENAMHI Chicama (D3) | |
| 4 | `www.senamhi.gob.pe` | Descarga de datos, tutorial, TUSNE y estudios técnicos (D1, D3.6) | El registro se hace a mano |
| 5 | `web2.senamhi.gob.pe` | Portal SENAMHI (D1) | |
| 6 | `repositorio.senamhi.gob.pe` | Portal SENAMHI (D2) | |
| 7 | `piscoprec.github.io` | PISCOp (D2) | |
| 8 | `drive.google.com` | Archivos NetCDF de PISCOp (D2) | Sólo si la descarga redirige allí |
| 9 | `drive.usercontent.google.com` | Ídem | Sólo si la descarga redirige allí |
| 10 | `tesis.pucp.edu.pe` | Series SENAMHI de Rojas Marmolejo y anexos de muros (D3.3, B7) | |
| 11 | `repositorio.upao.edu.pe` | La Jalca: hidrología, hidráulica y estructura (A1) | |
| 12 | `repositorio.unsaac.edu.pe` | 42 alcantarillas TMC (A2) | |
| 13 | `repositorio.unp.edu.pe` | Piura (A5) | |
| 14 | `repositorio.untumbes.edu.pe` | TU-107 Bocapán – Tamarindo, costa norte con FEN (A6) | |
| 15 | `repositorio.unh.edu.pe` | HV-107 (A3) | |
| 16 | `repositorio.upeu.edu.pe` | Colpahuayco – Langui (A4) | No resolvió en esta sesión |
| 17 | `www.dspace.espol.edu.ec` | Intervalles: caso completo con cajón (A8) | |
| 18 | `repositorio.unfv.edu.pe` | A7 | |
| 19 | `repositorio.unica.edu.pe` | Témez (A10) | |
| 20 | `repositorio.uni.edu.pe` | Informes de suficiencia (A13) | |
| 21 | `openjicareport.jica.go.jp` | Series del Chira y Piura (D3.5) | |
| 22 | `tecdigital.tec.ac.cr` | Artículo de HidroEsta (B1) | |
| 23 | `www.tec.ac.cr` | Ficha de HidroEsta (B1) | |
| 24 | `www.redalyc.org` | Espejo del artículo de HidroEsta (B1) | |
| 25 | `dialnet.unirioja.es` | Versión en inglés de HidroEsta (B1) | |
| 26 | `scielo.sld.cu` | Gencel, Piura (A9) | |
| 27 | `laccei.org` | Muro en voladizo LRFD, Tumbes (A15) | |
| 28 | `apiescuelaing.bibliolabtech.com` | Bejarano, HDS-5 (A15) | |
| 29 | `repositoriotec.tec.ac.cr` | Cajón parametrizado (A15) | |
| 30 | `repositorio.uvg.edu.gt` | Cajón por LRFD 2018 (A15) | |
| 31 | `prod2.seace.gob.pe` | Expedientes técnicos de obra del SEACE (C2) | Uso manual; interfaz JSF |
| 32 | `cdn.www.gob.pe` | Guías del OSCE (C2) | |
| 33 | `old.concretepipe.org` | Hojas *Design Data* de ACPA (B6) | |
| 34 | `www.conteches.com` | Guía de TMC (B6) | |
| 35 | `repositorioslatinoamericanos.uchile.cl` | Agregador que remite a A11 y D3.4 | |
| 36 | `core.ac.uk` | Espejo de muchas tesis peruanas | No resolvió en esta sesión |
| 37 | `siar.regionpiura.gob.pe` | Estudios del río Piura (C5) | Prioridad baja |
| 38 | `repositorio.ucv.edu.pe` | A12 | Prioridad baja |
| 39 | `repositorio.continental.edu.pe` | A14 | Prioridad baja |
| 40 | `repositorio.upt.edu.pe` | A14 | Prioridad baja |
| 41 | `repositorio.ucss.edu.pe` | A14 | Prioridad baja |

**Dejo fuera, a propósito,** los sitios de copias sin autorización clara: Scribd, SlideShare, Studocu, pdfcoffee, idoc.pub, doku.pub y elsolucionario.
