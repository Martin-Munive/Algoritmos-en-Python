# Auditoría editorial inicial

## Estado actual

El proyecto ya posee:
- una identidad temática fuerte;
- una orientación pedagógica clara;
- contenido técnico y curricular real;
- un eje diferencial médico/biológico muy valioso.

Hasta ahora, sin embargo, funcionaba más como repositorio estructurado en Markdown que como libro web navegable.

## Fortalezas

1. Identidad distintiva.
2. Cruce raro y valioso entre medicina, computación y algoritmos.
3. Índice curricular ambicioso.
4. Contenido ya escrito con vocación docente.

## Riesgos

1. La infraestructura editorial web aún no estaba montada.
2. El tamaño del índice puede crecer desordenadamente si no se gobierna bien.
3. Algunos capítulos pueden tener estilos distintos al haber sido escritos en momentos distintos.
4. El libro puede quedar demasiado amplio si no se prioriza bien la progresión.
5. El libro puede parecer superficial si termina en ejemplos introductorios como calculadoras o clasificadores simples.
6. El libro puede dañar la imagen intelectual del autor si confunde claridad con simplificacion escolar.

## Diagnóstico

Este proyecto sí merece convertirse en libro web.

No debe perder:
- su enfoque médico;
- su tono interdisciplinario;
- su visión aplicada.

## Decisión editorial vigente

El proyecto no debe limitarse a corregir errores de Markdown o a mover archivos hacia `docs/`.

La decisión vigente es recuperar la esencia completa del libro:
- intención original;
- índice maestro;
- estructura curricular;
- tono médico-computacional;
- analogías clínicas;
- casos de salud digital;
- progresión pedagógica.

Con esa esencia recuperada, el libro debe contrastarse con los análisis editoriales ya realizados y reconstruirse como libro web desde una base limpia. El contenido previo queda como fuente y cantera en el historial Git, no como estructura obligatoria visible en la rama activa.

La migración no debe ser mecánica. Cada capítulo debe reescribirse o normalizarse según:
- función dentro del índice;
- utilidad para el lector;
- claridad técnica;
- consistencia con la promesa `Algoritmos en Python para Medicina y Ciencias de la Vida`;
- compatibilidad real con Jupyter Book/Sphinx/GitHub Pages;
- bibliografia cientifica y tecnica disponible;
- capacidad de progresar desde fundamentos hacia frontera.

## Decisión editorial 2026-05-10

El libro debe tener una ambicion mayor que introducir Python con ejemplos medicos.

Decision:
- los ejemplos como calculadora de riesgo cardiovascular, clasificador de urgencias o mini motor de reglas pertenecen al tramo inicial o intermedio;
- el tramo avanzado debe conducir a algoritmos de bioinformatica, genetica computacional, neurologia computacional, redes biologicas, modelos probabilisticos, medicina de precision y sistemas de soporte de decision;
- cada tema debe pasar por un protocolo de fuentes, modelos mentales, argumentos criticos y evaluacion profunda antes de convertirse en texto publicable;
- cada capitulo o tema importante debe incluir una entrada historica breve cuando el origen, episodio, dato curioso o aplicacion historica ayude a entender el concepto;
- el libro debe entrenar al autor/usuario en la materia mientras produce paginas publicables;
- toda afirmacion cientifica fuerte debe apoyarse en bibliografia, fuente primaria, fuente tecnica o declararse como interpretacion razonada.

La pregunta editorial que gobierna cada unidad sera:

> Esto ensena un concepto de forma clara sin reducirlo por debajo de la inteligencia del lector ni del autor?

El objetivo es iniciar una versión nueva y publicable sin perder el valor acumulado del repositorio previo.

## Limpieza editorial 2026-05-11

Las carpetas heredadas `00-Presaberes`, `01-Analisis_de_Complejidad_Big_O` y `02-Estructuras_de_Datos_Lineales` fueron retiradas de la rama activa.

Decision:
- no publicar ni mostrar en GitHub la estructura antigua mientras se reconstruye el libro;
- conservar el material en el historial Git para recuperarlo si aporta valor;
- reintroducir Big O, estructuras de datos y presaberes solo cuando encajen en la nueva progresion editorial.

## Recomendación preliminar

1. Conservar el nombre editorial principal:
   - `Materia Medica Digitalis`
2. Usar como subtítulo:
   - `Algoritmos en Python para Medicina y Ciencias de la Vida`
3. Migrar progresivamente los capitulos a la estructura `chapters/` de Jupyter Book.
4. Mantener el índice maestro como brújula, pero con control de alcance.

## Próximo paso recomendado

Construir una hoja de ruta editorial que decida:
- módulos prioritarios;
- capítulos mínimos del primer lanzamiento;
- tono definitivo;
- criterio de ejemplos y casos clínicos/computacionales.
