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
| `EJE_DG2018_circular_polilinea_arcos.dxf` | **Para editar en Civil 3D**: polilínea del eje con tangentes y arcos (radios exactos, capa `EJE`), polilínea de PIs (capa `EJE-PI`) y textos `C-n R=xx` (capa `EJE-PI-TXT`). Insertar el DXF y usar "Crear alineación a partir de objetos" sobre la polilínea `EJE` (sin marcar "Añadir curvas entre tangentes"): se obtiene una alineación de líneas fijas y curvas libres editable por PIs. |
| `EJE_DG2018_circular_entidades_C3D.csv` | Correspondencia entre el número de entidad que muestra Civil 3D (alineación creada desde el DXF) y la curva C-n del CSV y la memoria, con la restricción esperada (libre con PI, o fija por estar pegada a otra curva). |
| `EJE_DG2018_circular_grupos_sin_tangente.csv` | Los 42 grupos de curvas consecutivas sin tangente (compuestas y en S) que Civil 3D convierte en entidades fijas sin PI, con los pasos para rehacerlos como curva flotante + curva libre y que queden editables. |
| `scripts/civil3d_crear_alineacion_dynamo.py` | Script Python para Dynamo (Civil 3D) que crea la alineación entidad por entidad con la API .NET: líneas fijas, curvas aisladas libres (con PI) y grupos pegados como flotante + libre. Lee `EJE_DG2018_circular.xml`. No probado en Civil 3D: ver instrucciones en la cabecera del archivo. |
| `EJE_DG2018_*_PI_polilinea.scr` | Script de AutoCAD (comando `SCRIPT`) que dibuja solo la polilínea de PIs con etiquetas de radio; alternativa al DXF con "Añadir curvas entre tangentes" y luego tecleando los radios del CSV. |
| `EJE_DG2018_*_planta.svg` / `.png` | Croquis de planta: trazo actual en gris y eje corregido coloreado por clase de curva. |
| `EJE_DG2018_circular_memoria.docx` / `.md` | Memoria de diseño geométrico en planta: parámetros adoptados contrastados con las citas de la DG-2018, inventario de curvas normativas, en el mínimo, excepcionales y de vuelta (con progresivas y coordenadas de PI), tangentes, sitios a revisar y anexo con la tabla completa. |
| `EJE_DG2018_*_reporte.md` | Parámetros adoptados, resultados globales, lista de radios menores al normativo con coordenadas de PI, zonas de curvas de vuelta, tabla completa y guía de uso. |

### Nota sobre la importación LandXML en Civil 3D
El LandXML solo lleva geometría; Civil 3D decide las restricciones de tangencia al importar según el parámetro *Element Constraint Assignment* (Toolspace > Configuración > clic derecho en el dibujo > Editar configuración de LandXML > ficha Importar > alineaciones): *Fixed Only* crea todas las entidades fijas e independientes (al editar una no se altera el resto, pero tampoco se mantiene la tangencia), y *Floating Off the First Element* encadena cada entidad a la anterior (al editar una se recalcula todo lo que sigue y, si algo no se puede resolver, desaparece hasta deshacer). Para diseñar editando radios conviene crear la alineación desde la polilínea con arcos del DXF.
