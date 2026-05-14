# Hoja de ruta editorial

## Objetivo central

Convertir `Materia Médica Digitalis` en un libro científico y computacional de progresión profunda: inicia en pensamiento algorítmico y Python, pero avanza hacia algoritmos avanzados, bioinformática, genética, neurología computacional, medicina de precisión y problemas al borde de la ciencia actual.

El libro no debe terminar en calculadoras clínicas, clasificadores simples o automatizaciones básicas. Esos recursos son puntos de entrada, no destino final.

## Tesis de progresión

La obra debe construir una escalera intelectual:

1. **Fundamentos:** qué es un algoritmo, cómo se formaliza una decisión, cómo se expresa en Python.
2. **Algoritmos clásicos:** búsqueda, ordenamiento, complejidad, recursividad, grafos, programación dinámica, estructuras de datos.
3. **Algoritmos científicos:** optimización, modelos probabilísticos, simulación, inferencia, aprendizaje automático, procesamiento de señales, análisis de secuencias.
4. **Dominio biomédico:** datos clínicos, laboratorio, imagen, texto médico, redes biológicas, genomas, proteomas, fenotipos, señales neurológicas.
5. **Frontera:** bioinformática moderna, genética computacional, neurología de sistemas, medicina de precisión, modelos fundacionales, sistemas de soporte de decisión, incertidumbre y responsabilidad.

## Fase 1. Infraestructura y tono

Estado:
- Jupyter Book clásico `jupyter-book<2`.
- Sphinx Book Theme.
- GitHub Pages.
- Portada formal.
- Credenciales visibles.
- Primer capítulo reescrito con mayor profundidad.

Pendiente:
- ajustar índice maestro para reflejar progresión hasta frontera;
- separar claramente ejemplos introductorios de capítulos avanzados;
- definir política de bibliografía por capítulo;
- decidir recursos visuales, notebooks y simulaciones iniciales.

Decisión sobre presaberes:
- Los presaberes no son el capítulo 1.
- Se ubican en Front Matter como orientación mínima para lectores primerizos.
- No deben convertir la obra en un curso básico de Python.
- Su función es reducir fricción sintáctica antes de entrar al pensamiento algorítmico.

## Fase 2. Fundamentos fuertes

Objetivo:
Construir los capítulos iniciales sin infantilizar.

Decisión estructural:
Una página navegable no equivale automáticamente a un capítulo. Los temas introductorios que pertenecen a una misma unidad intelectual deben organizarse como secciones de un capítulo mayor. Esto evita que el libro parezca una sucesión de fragmentos breves y permite una estructura editorial normal, profunda y acumulativa.

Capítulo inicial:
- El lenguaje de las decisiones.

Secciones iniciales:
- Qué es un algoritmo.
- Pensar en pasos.
- Variables, datos y decisiones.
- Estados, condiciones y umbrales.
- Excepciones, datos faltantes y trazabilidad.
- Condicionales como arquitectura de decisión.
- Bucles como control de procesos.
- Funciones como encapsulamiento de criterio.
- Errores, excepciones y seguridad del cálculo.

Criterio:
- cada tema debe tener definición, intuición, límites, ejemplos, código, consecuencias y preguntas de comprensión profunda.

## Fase 3. Algoritmos clásicos con lectura biomédica

Temas:
- búsqueda lineal, binaria y búsqueda en espacios de estados;
- ordenamiento, priorización y triage;
- hashing, índices y recuperación de información;
- recursión y divide-and-conquer;
- grafos, caminos, centralidad y redes biológicas;
- programación dinámica;
- algoritmos voraces;
- complejidad temporal, espacial y costo clínico-operativo.

Meta:
Mostrar que los algoritmos clásicos no son piezas escolares, sino modelos mentales para organizar información, costo, incertidumbre y decisión.

## Fase 4. Algoritmos para datos biomédicos

Temas:
- análisis de tablas clínicas;
- series temporales de signos vitales;
- señales fisiológicas;
- texto médico y recuperación semántica;
- imagen biomédica como matriz y señal;
- modelos probabilísticos;
- sensibilidad, especificidad, calibración, validación y sesgo.

## Fase 5. Bioinformática y genética computacional

Temas:
- alineamiento de secuencias;
- distancia y similitud;
- programación dinámica en bioinformática;
- ensamblaje y búsqueda en grandes genomas;
- variantes genéticas;
- redes génicas;
- modelos de expresión;
- interpretación computacional de datos ómicos.

## Fase 6. Neurología computacional y sistemas complejos

Temas:
- señales neurológicas;
- redes neuronales biológicas y artificiales;
- grafos cerebrales;
- modelos dinámicos;
- aprendizaje, plasticidad y representación;
- límites de la analogía cerebro-computador.

## Fase 7. Frontera y responsabilidad

Temas:
- algoritmos en medicina de precisión;
- modelos fundacionales en biomedicina;
- sistemas de soporte de decisión;
- agentes, herramientas y seguimiento longitudinal;
- explicabilidad, incertidumbre y seguridad;
- sesgo, responsabilidad y límites de automatización.

## Protocolo por tema

Antes de redactar un tema:

1. Identificar fuentes científicas, técnicas y clásicas disponibles.
2. Preparar una entrada histórica breve si el concepto tiene origen, episodio, dato curioso o aplicación histórica relevante.
3. Revisar definiciones canónicas.
4. Revisar ejemplos clásicos.
5. Explorar vanguardia.
6. Extraer modelos mentales expertos.
7. Identificar desacuerdos críticos.
8. Crear preguntas de evaluación profunda.
9. Decidir si el tema requiere imagen, animación, código, notebook, simulación o recurso interactivo.
10. Redactar con bibliografía vinculada.

## Plantilla para capítulos o temas importantes

Cuando el tema tenga suficiente densidad conceptual, la estructura base será:

1. **Entrada intelectual:** por qué el tema importa dentro del libro.
2. **Origen histórico:** de dónde viene el concepto, qué problema lo hizo necesario, qué episodio o dato histórico ayuda a entenderlo.
3. **Definición formal de trabajo:** formulación precisa, no escolar.
4. **Intuición operativa:** cómo debe imaginarlo el lector sin perder rigor.
5. **Modelos mentales expertos:** herramientas cognitivas que comparten quienes dominan el tema.
6. **Ejemplos clásicos:** casos canónicos del campo.
7. **Ejemplo biomédico progresivo:** una miniatura inicial que luego pueda crecer hacia casos serios.
8. **Límites y errores frecuentes:** dónde la definición falla, se simplifica demasiado o se usa mal.
9. **Tensiones críticas:** desacuerdos o trade-offs reales.
10. **Puente hacia frontera:** cómo el concepto escala hacia bioinformática, genética, neurología computacional, medicina de precisión o sistemas avanzados.
11. **Evaluación profunda:** preguntas que distingan comprensión de memorización.
12. **Bibliografía y fuentes.**

## Estructura propuesta del capítulo 1: Qué es un algoritmo

El primer capítulo debe funcionar como puerta conceptual de todo el libro. No debe limitarse a definir "secuencia de pasos"; debe mostrar que un algoritmo es una forma de formalizar decisiones bajo restricciones.

Índice operativo:

1. **La definición insuficiente**
   - Presentar la definición común.
   - Explicar por qué es correcta pero pobre.

2. **Breve historia de la idea algorítmica**
   - De Al-Juarismi y los procedimientos aritméticos al concepto moderno de computación.
   - Euclides como ejemplo temprano de procedimiento finito.
   - Ada Lovelace, Babbage y la separación entre máquina y procedimiento.
   - Turing y la formalización de lo computable.
   - Dato histórico: la palabra algoritmo nace de la latinización del nombre de Al-Juarismi, no de la computación moderna.

3. **Definición formal de trabajo**
   - Entrada.
   - Representación.
   - Transformación.
   - Control.
   - Salida.
   - Terminación.
   - Verificación.

4. **Algoritmo, programa, modelo y decisión**
   - El algoritmo no es el código.
   - El programa es una implementación.
   - El modelo define qué parte del mundo entra al sistema.
   - La decisión define por qué la transformación importa.

5. **Modelos mentales expertos**
   - El algoritmo como contrato.
   - El algoritmo como compresión de una decisión.
   - El algoritmo como estructura de representación.
   - El algoritmo como máquina de errores posibles.
   - El algoritmo como puente entre dominio y ejecución.

6. **Ejemplo inicial: temperatura, fiebre y riesgo**
   - Mantenerlo como miniatura.
   - Explicitar que no es una escala clínica.
   - Usarlo para mostrar datos, umbrales, contexto, excepciones y consecuencias.

7. **Correcto no significa suficiente**
   - Corrección computacional.
   - Relevancia clínica.
   - Sesgo, datos incompletos, seguridad y responsabilidad.

8. **Tres tensiones criticas**
   - Formalización vs juicio clínico.
   - Simplicidad vs fidelidad al fenómeno.
   - Automatización vs responsabilidad.

9. **De aquí a la frontera**
   - Búsqueda y recuperación.
   - Grafos biológicos.
   - Programación dinámica.
   - Alineamiento de secuencias.
   - Redes cerebrales.
   - Sistemas de decisión clínica.
   - Modelos fundacionales biomédicos.

10. **Preguntas de comprensión profunda**
    - Preguntas de razonamiento, no memoria.
    - Casos donde la regla general falla.
    - Comparaciones entre algoritmo, modelo, programa y decisión.

11. **Bibliografía**
    - Fuentes clásicas de algoritmos.
    - Historia de computación.
    - Razonamiento diagnóstico y sistemas clínicos.

## Criterio de éxito

El libro funciona si un lector puede:
- aprender desde cero sin sentirse tratado como principiante intelectual;
- entender algoritmos clásicos con rigor;
- conectar cada concepto con medicina y ciencias de la vida;
- avanzar hacia temas de frontera sin ruptura brusca;
- reconocer al autor como médico, programador y pensador interdisciplinario de alto nivel.
