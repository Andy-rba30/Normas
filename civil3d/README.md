# Archivos para Civil 3D (DG-2018)

## Criterios de diseño
- `DG2018_Corregido_2.xml`: archivo de criterios de diseño (Roadway Design Standards) basado en el Manual de Carreteras DG-2018 con la estructura del archivo que carga en Civil 3D. Copiar a `C:\ProgramData\Autodesk\C3D 20xx\esp\Data\Corridor Design Standards\Metric\` (o la carpeta equivalente) y asociarlo al alineamiento en Alignment Properties > Design Criteria.

## Eje corregido (carpeta `eje/`)
Eje ajustado al trazo existente (`PROCESAMIENTO DISEÑO GEOMETRICO`, 11.49 km) con los parámetros de la DG-2018 para carretera de Segunda Clase, orografía escarpada, V = 40 km/h, zona poblada (mínima expropiación).

| Archivo | Contenido |
|---|---|
| `EJE_DG2018_circular.xml` | LandXML 1.2 con el eje (tangentes + curvas circulares). Importar con `IMPORTLANDXML`. |
| `EJE_DG2018_clotoides.xml` | Variante con clotoides (Le = 40 m) en las curvas donde la geometría lo permite. |
| `EJE_DG2018_*_curvas.csv` | Tabla de curvas: PI (progresiva, N, E), deflexión, radio, tangente, longitudes, PC/PT, sobreancho, desvío respecto al trazo, clasificación DG-2018 y observaciones. Separador `;`. |
| `EJE_DG2018_*_PI_PNEZD.csv` | Puntos de PI en formato PNEZD (importar como grupo de puntos). |
| `EJE_DG2018_*_PI_polilinea.scr` | Script de AutoCAD que dibuja la polilínea de PIs con etiquetas de radio (para "Create Alignment from Objects"). |
| `EJE_DG2018_*_planta.svg` / `.png` | Croquis de planta: trazo actual en gris y eje corregido coloreado por clase de curva. |
| `EJE_DG2018_circular_memoria.docx` / `.md` | Memoria de diseño geométrico en planta: parámetros adoptados contrastados con las citas de la DG-2018, inventario de curvas normativas, en el mínimo, excepcionales y de vuelta (con progresivas y coordenadas de PI), tangentes, sitios a revisar y anexo con la tabla completa. |
| `EJE_DG2018_*_reporte.md` | Parámetros adoptados, resultados globales, lista de radios menores al normativo con coordenadas de PI, zonas de curvas de vuelta, tabla completa y guía de uso. |
