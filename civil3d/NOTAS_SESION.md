# Notas de sesión: eje DG-2018 para Civil 3D (estado al 16/10/2026)

Resumen para continuar el trabajo en una sesión nueva. Rama de trabajo: `claude/affectionate-edison-5o7cl1`.

## 1. Qué hay hecho
- `civil3d/DG2018_Corregido_2.xml`: criterios de diseño DG-2018 para Civil 3D, con la estructura del archivo que sí carga (verificado contra `DG2018.xml` del usuario). Datos revisados tabla por tabla contra el PDF `normas/Manual.de.Carreteras.DG-2018.pdf`.
- `civil3d/eje/EJE_DG2018_circular.xml`: eje en planta (LandXML 1.2, 282 curvas tras la pasada de tangentes, 11 483 m) ajustado al trazo existente. Variante `EJE_DG2018_clotoides.xml` (solo 5 clotoides caben). Tablas CSV, puntos PNEZD, script `.scr` de PIs, DXF con polilínea de arcos (`EJE_DG2018_circular_polilinea_arcos.dxf`, generado con `write_dxf.py`), planta SVG/PNG, reporte y memoria (`EJE_DG2018_circular_memoria.docx`).
- Insumos del usuario en `civil3d/eje/insumos/` (trazo original LandXML de 1 180 segmentos y documento de parámetros).
- Scripts en `civil3d/eje/scripts/` (copiados del scratchpad de la sesión).

## 2. Parámetros adoptados (confirmados por el usuario)
Carretera de Segunda Clase, orografía escarpada (única que admite 40 km/h en Tabla 204.01), V = 40 km/h, peralte máximo 12 % (8 % normal), Rmín 45 m (Tabla 302.02), radio excepcional 25 m ≤ R < 45 m justificado con Ve = 30 km/h (Tópico 204.03), curvas de vuelta Ri ≥ 8 m normal / 6 m absoluto (302.07, Tabla 302.12 maniobra C2), calzada 6.00 m, bermas 0.50 m, tangentes 56/111 m (Tabla 302.01), clotoides obligatorias si R < 150 m con Le = 40 m, sobreancho con vehículo B2 (L = 10.55 m). El documento del usuario dice 30 km/h y trocha carrozable pero Rmín 45 m; se siguió la indicación verbal de 40 km/h y Segunda Clase.

Premisas: zona poblada, mínima expropiación: el eje debe pegarse al trazo actual; se aceptan radios excepcionales y curvas de vuelta donde el terreno no permite 45 m.

## 3. Resultados actuales (variante circular)
324 curvas: 83 con R ≥ 50 m, 92 con 45 ≤ R < 50, 58 excepcionales (25 a 45 m), 91 curvas de vuelta (R < 25 m; 43 con Ri ≥ 8, 13 con 6 ≤ Ri < 8, 35 con Ri < 6). Separación del trazo: media 0.33 m, p95 1.13 m, máx 5.2 m (146 m de trazo con más de 2.5 m). Tangentes: solo 4 de 323 cumplen la Tabla 302.01 (136 entre curvas del mismo sentido exigen 111 m: 0 cumplen; 187 en S exigen 56 m: 4 cumplen). Sitios a revisar: km 3+580 a 3+690, 7+180 a 7+210, 10+280 a 10+360; los primeros 230 m son esquinas urbanas con R de 6 a 22 m.

## 4. Pasada de tangentes (ejecutada el 16/10/2026, tolerancia 1.5 m)
Aplicada con `tangent_pass.py` sobre el ajuste base (E_SMALL 0.5, DELTA_SMALL 8°). Reglas: curvas del mismo sentido con tangente < 111 m se funden en una sola curva o en compuesta (302.06.03) sin recortar tangentes en S; curvas en S con tangente < 56 m se abren reduciendo radios sin bajar de 45 m. Resultado final: 324 -> 282 curvas; 42 fusiones, 17 compuestas nuevas, 2 tangentes en S abiertas a 56 m; quedan 70 pares del mismo sentido con tangente < 111 m, 24 compuestas y 8 tangentes en S >= 56 m (177 en S imposibles sin salir del trazo); separación del trazo máx 5.2 m, p95 1.21 m; 8 de 281 tangentes cumplen la Tabla 302.01. Se probó también un ajuste base con DELTA_SMALL 12° / E_SMALL 1.0 / TOL_TAN 1.0 y se descartó (desvío máximo 7.9 m, tangentes negativas). Para repetir con otra tolerancia: `TOL=2.5 ./finalize.sh` y luego `build_memoria.sh model_t.pkl`.

## 5. Pendiente anterior (ya ejecutado; se deja como referencia)
Mejorar el cumplimiento de tangentes donde sea posible, sin desnaturalizar el trazo. Plan acordado en la conversación, a la espera de que el usuario fije la separación lateral máxima admisible (1.5 m o 2.5 m):
1. Curvas del mismo sentido con tangente corta (136 casos): fundirlas en una sola curva o compuesta (Tópico 302.06.03: evitar curvas del mismo sentido con tangente < 400 m; excepcionalmente policéntrica).
2. Curvas en S con tangente de 20 a 56 m (46 casos): reducir radios (manteniendo 45 m si se puede) o enderezar dentro de la tolerancia hasta llegar a 56 m.
3. Resto de curvas en S: documentar como excepción o enlazar con clotoides donde quepan.
4. Subir el umbral de deflexión mínima de 8° a ~12° para absorber ondulaciones leves en tangentes largas (separación < 1 m).
Después: regenerar entregables (`finalize.sh`), la memoria (`make_report.py`) y actualizar README. El usuario pidió no editar documentos hasta confirmar.

## 6. Cómo reproducir (desde `civil3d/eje/scripts/`, en un directorio de trabajo)
```
python3 parse.py ../insumos/PROCESAMIENTO_DISENO_GEOMETRICO_trazo_original.xml   # crea pts.npy (copiar in.xml al cwd como in.xml)
python3 fit_axis.py            # ~3.5 min -> model.pkl (circular)
python3 fit_axis.py --spirals  # -> model_sp.pkl
TOL=1.5 ./finalize.sh          # tangent_pass.py (model_t.pkl), write_outputs.py x2, check_landxml.py, plan.py -> out_final/ y copia a civil3d/eje
python3 make_report.py && pandoc memoria.md -t docx --reference-doc=ref_landscape.docx -o memoria.docx  # luego inyectar sectPr apaisado (ver make_report)
```
Notas: los scripts usan `sys.path.insert` del propio directorio (correr con `python3 -I` funciona). `write_outputs.py` espera `in.xml` en el cwd para copiar el CoordinateSystem. Parámetros del ajuste en el dict `PRM` de `fit_axis.py` (TOL_UP = 2.0 m al subir radios, E_SMALL = 0.5 m, R_THR = 250 m, LT_MIN = 10 m, TOL_TAN = 0.8 m). `fit_axis2.py` (ajuste por círculos y tangentes comunes) quedó inestable y no se usa.

## 7. Verificaciones hechas
LandXML bien formado (xmllint), continuidad de elementos 0.000 mm y quiebre máximo 0.0002° (`check_landxml.py`); orientación de arcos del SVG comprobada (`svgcheck.py`); el usuario ya importó el eje en Civil 3D 2027 (longitud 11 468.093 m) y los triángulos de advertencia que vio son el símbolo de incumplimiento de criterios, resuelto vía Propiedades de alineación > Criterios de diseño.

## 8. Edición en Civil 3D (consulta del 16/10/2026)
Al importar el LandXML, Civil 3D asigna las restricciones según *Element Constraint Assignment* (LandXML Settings > Import): *Fixed Only* (todas fijas, independientes) o *Floating Off the First Element* (cada entidad flota sobre la anterior; al cambiar un radio se recalcula toda la cadena y lo irresoluble desaparece). El XML no puede fijar esas restricciones. Para editar radios como alineación de PIs: insertar `EJE_DG2018_circular_polilinea_arcos.dxf` y usar Crear alineación a partir de objetos sobre la polilínea `EJE` (líneas fijas + curvas libres). Generación: `python3 write_dxf.py model_t.pkl salida.dxf` (usa el modelo con tangentes residuales absorbidas, igual que el LandXML; verifica centros/radios/tangencia al releer el DXF).

## 9. Script para crear la alineación con restricciones (16/10/2026)
`scripts/civil3d_crear_alineacion_dynamo.py`: nodo Python de Dynamo para Civil 3D; IN[0] ruta del LandXML, IN[1] nombre, IN[2] ruta de criterios. Usa AddFixedLine(Point3d, Point3d), AddFloatingCurve(id, Point3d, radio, >180, CurveType) y AddFreeCurve(id, id, radio, CurveParamType.Radius, >180, CurveType), con alternativas por punto de paso si una firma no existe. Probado solo en seco (lectura del XML y plan: 235 líneas, 48 flotantes, 234 libres). Pendiente de validación por el usuario en Civil 3D 2027; si falla, pedir el texto de OUT.

## 10. Capítulo 6.6 de la memoria: curvas compuestas e inversas enlazadas (16/10/2026)
`make_report.py` detecta los grupos de curvas con tangente nula (42 grupos: 38 de dos curvas, 3 de tres, 1 de cinco; 48 uniones: 28 compuestas y 20 inversas) y evalúa cada unión: relación de radios 1.5 (302.06.02), rango de la Tabla 302.08 (grupo 2: máx 1.5·Re, mín Re/1.5 con piso 50 m, solo Re ≥ 40), transición de peralte 302.08 (ipmáx 1.4 %, B 3.0 m, peralte de la tabla 'DG2018 _PMax 12%' a 40 km/h) frente a las longitudes de los arcos, y desaceleración gradual con 1.0 m/s² (criterio adoptado). Columna con los artículos que rigen cada grupo y el origen (trazo existente / pasada de tangentes, flag `compuesta`). Reconstruir con `build_memoria.sh model_t.pkl`.
