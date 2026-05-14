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
- bibliografía científica y técnica disponible;
- capacidad de progresar desde fundamentos hacia frontera.

## Decisión editorial 2026-05-10

El libro debe tener una ambición mayor que introducir Python con ejemplos médicos.

Decision:
- los ejemplos como calculadora de riesgo cardiovascular, clasificador de urgencias o mini motor de reglas pertenecen al tramo inicial o intermedio;
- el tramo avanzado debe conducir a algoritmos de bioinformática, genética computacional, neurología computacional, redes biológicas, modelos probabilísticos, medicina de precisión y sistemas de soporte de decisión;
- cada tema debe pasar por un protocolo de fuentes, modelos mentales, argumentos críticos y evaluación profunda antes de convertirse en texto publicable;
- cada capítulo o tema importante debe incluir una entrada histórica breve cuando el origen, episodio, dato curioso o aplicación histórica ayude a entender el concepto;
- el libro debe entrenar al autor/usuario en la materia mientras produce páginas publicables;
- toda afirmación científica fuerte debe apoyarse en bibliografía, fuente primaria, fuente técnica o declararse como interpretación razonada.

La pregunta editorial que gobierna cada unidad será:

> Esto enseña un concepto de forma clara sin reducirlo por debajo de la inteligencia del lector ni del autor?

El objetivo es iniciar una versión nueva y publicable sin perder el valor acumulado del repositorio previo.

## Directiva editorial 2026-05-14: integridad textual y glosario vivo

El libro debe apoyarse en bibliografía científica, técnica e histórica sin copiar la voz ni el texto de las fuentes.

Decisión:
- el resultado publicable debe ser digestión intelectual propia;
- las fuentes se citan para sustentar afirmaciones, no para transferir bloques de texto al libro;
- las formulaciones clásicas solo pueden conservarse de forma breve, atribuida y cuando la precisión lo justifique;
- se evitarán paráfrasis demasiado cercanas a la estructura verbal de los autores;
- la bibliografía debe acompañar los temas, pero no reemplazar la elaboración conceptual del autor.

Además, el glosario queda definido como una sección viva del libro. No debe abandonarse después de su creación inicial.

Regla:
- cada capítulo o tema importante debe revisar y actualizar el glosario maestro antes de considerarse terminado;
- los términos recurrentes, transversales o necesarios para capítulos posteriores deben entrar al glosario;
- los términos locales pueden quedar explicados en el capítulo si no tendrán recurrencia;
- toda redefinición importante debe propagarse al glosario y, si corresponde, a capítulos anteriores.

## Limpieza editorial 2026-05-11

Las carpetas heredadas `00-Presaberes`, `01-Analisis_de_Complejidad_Big_O` y `02-Estructuras_de_Datos_Lineales` fueron retiradas de la rama activa.

Decision:
- no publicar ni mostrar en GitHub la estructura antigua mientras se reconstruye el libro;
- conservar el material en el historial Git para recuperarlo si aporta valor;
- reintroducir Big O, estructuras de datos y presaberes solo cuando encajen en la nueva progresión editorial.

## Recomendación preliminar

1. Conservar el nombre editorial principal:
   - `Materia Médica Digitalis`
2. Usar como subtítulo:
   - `Algoritmos en Python para Medicina y Ciencias de la Vida`
3. Migrar progresivamente los capítulos a la estructura `chapters/` de Jupyter Book.
4. Mantener el índice maestro como brújula, pero con control de alcance.

## Próximo paso recomendado

Construir una hoja de ruta editorial que decida:
- módulos prioritarios;
- capítulos mínimos del primer lanzamiento;
- tono definitivo;
- criterio de ejemplos y casos clínicos/computacionales.
