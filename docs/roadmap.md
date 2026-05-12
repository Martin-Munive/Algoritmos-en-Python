# Hoja de ruta editorial

## Objetivo central

Convertir `Materia Medica Digitalis` en un libro cientifico y computacional de progresion profunda: inicia en pensamiento algorítmico y Python, pero avanza hacia algoritmos avanzados, bioinformatica, genetica, neurologia computacional, medicina de precision y problemas al borde de la ciencia actual.

El libro no debe terminar en calculadoras clinicas, clasificadores simples o automatizaciones basicas. Esos recursos son puntos de entrada, no destino final.

## Tesis de progresion

La obra debe construir una escalera intelectual:

1. **Fundamentos:** que es un algoritmo, como se formaliza una decision, como se expresa en Python.
2. **Algoritmos clasicos:** busqueda, ordenamiento, complejidad, recursividad, grafos, programacion dinamica, estructuras de datos.
3. **Algoritmos cientificos:** optimizacion, modelos probabilisticos, simulacion, inferencia, aprendizaje automatico, procesamiento de señales, analisis de secuencias.
4. **Dominio biomedico:** datos clinicos, laboratorio, imagen, texto medico, redes biologicas, genomas, proteomas, fenotipos, señales neurologicas.
5. **Frontera:** bioinformatica moderna, genetica computacional, neurologia de sistemas, medicina de precision, modelos fundacionales, sistemas de soporte de decision, incertidumbre y responsabilidad.

## Fase 1. Infraestructura y tono

Estado:
- Jupyter Book clasico `jupyter-book<2`.
- Sphinx Book Theme.
- GitHub Pages.
- Portada formal.
- Credenciales visibles.
- Primer capitulo reescrito con mayor profundidad.

Pendiente:
- ajustar indice maestro para reflejar progresion hasta frontera;
- separar claramente ejemplos introductorios de capitulos avanzados;
- definir politica de bibliografia por capitulo;
- decidir recursos visuales, notebooks y simulaciones iniciales.

Decision sobre presaberes:
- Los presaberes no son el capitulo 1.
- Se ubican en Front Matter como orientacion minima para lectores primerizos.
- No deben convertir la obra en un curso basico de Python.
- Su funcion es reducir friccion sintactica antes de entrar al pensamiento algorítmico.

## Fase 2. Fundamentos fuertes

Objetivo:
Construir los capitulos iniciales sin infantilizar.

Decision estructural:
Una pagina navegable no equivale automaticamente a un capitulo. Los temas introductorios que pertenecen a una misma unidad intelectual deben organizarse como secciones de un capitulo mayor. Esto evita que el libro parezca una sucesion de fragmentos breves y permite una estructura editorial normal, profunda y acumulativa.

Capitulo inicial:
- El lenguaje de las decisiones.

Secciones iniciales:
- Que es un algoritmo.
- Pensar en pasos.
- Variables, datos y decisiones.
- Estados, condiciones y umbrales.
- Excepciones, datos faltantes y trazabilidad.
- Condicionales como arquitectura de decision.
- Bucles como control de procesos.
- Funciones como encapsulamiento de criterio.
- Errores, excepciones y seguridad del calculo.

Criterio:
- cada tema debe tener definicion, intuicion, limites, ejemplos, codigo, consecuencias y preguntas de comprension profunda.

## Fase 3. Algoritmos clasicos con lectura biomedica

Temas:
- busqueda lineal, binaria y busqueda en espacios de estados;
- ordenamiento, priorizacion y triage;
- hashing, indices y recuperacion de informacion;
- recursion y divide-and-conquer;
- grafos, caminos, centralidad y redes biologicas;
- programacion dinamica;
- algoritmos voraces;
- complejidad temporal, espacial y costo clinico-operativo.

Meta:
Mostrar que los algoritmos clasicos no son piezas escolares, sino modelos mentales para organizar informacion, costo, incertidumbre y decision.

## Fase 4. Algoritmos para datos biomedicos

Temas:
- analisis de tablas clinicas;
- series temporales de signos vitales;
- señales fisiologicas;
- texto medico y recuperacion semantica;
- imagen biomedica como matriz y señal;
- modelos probabilisticos;
- sensibilidad, especificidad, calibracion, validacion y sesgo.

## Fase 5. Bioinformatica y genetica computacional

Temas:
- alineamiento de secuencias;
- distancia y similitud;
- programacion dinamica en bioinformatica;
- ensamblaje y busqueda en grandes genomas;
- variantes geneticas;
- redes genicas;
- modelos de expresion;
- interpretacion computacional de datos omicos.

## Fase 6. Neurologia computacional y sistemas complejos

Temas:
- señales neurologicas;
- redes neuronales biologicas y artificiales;
- grafos cerebrales;
- modelos dinamicos;
- aprendizaje, plasticidad y representacion;
- limites de la analogia cerebro-computador.

## Fase 7. Frontera y responsabilidad

Temas:
- algoritmos en medicina de precision;
- modelos fundacionales en biomedicina;
- sistemas de soporte de decision;
- agentes, herramientas y seguimiento longitudinal;
- explicabilidad, incertidumbre y seguridad;
- sesgo, responsabilidad y limites de automatizacion.

## Protocolo por tema

Antes de redactar un tema:

1. Identificar fuentes cientificas, tecnicas y clasicas disponibles.
2. Preparar una entrada historica breve si el concepto tiene origen, episodio, dato curioso o aplicacion historica relevante.
3. Revisar definiciones canonicas.
4. Revisar ejemplos clasicos.
5. Explorar vanguardia.
6. Extraer modelos mentales expertos.
7. Identificar desacuerdos criticos.
8. Crear preguntas de evaluacion profunda.
9. Decidir si el tema requiere imagen, animacion, codigo, notebook, simulacion o recurso interactivo.
10. Redactar con bibliografia vinculada.

## Plantilla para capitulos o temas importantes

Cuando el tema tenga suficiente densidad conceptual, la estructura base sera:

1. **Entrada intelectual:** por que el tema importa dentro del libro.
2. **Origen historico:** de donde viene el concepto, que problema lo hizo necesario, que episodio o dato historico ayuda a entenderlo.
3. **Definicion formal de trabajo:** formulacion precisa, no escolar.
4. **Intuicion operativa:** como debe imaginarlo el lector sin perder rigor.
5. **Modelos mentales expertos:** herramientas cognitivas que comparten quienes dominan el tema.
6. **Ejemplos clasicos:** casos canonicos del campo.
7. **Ejemplo biomédico progresivo:** una miniatura inicial que luego pueda crecer hacia casos serios.
8. **Limites y errores frecuentes:** donde la definicion falla, se simplifica demasiado o se usa mal.
9. **Tensiones criticas:** desacuerdos o trade-offs reales.
10. **Puente hacia frontera:** como el concepto escala hacia bioinformatica, genetica, neurologia computacional, medicina de precision o sistemas avanzados.
11. **Evaluacion profunda:** preguntas que distingan comprension de memorizacion.
12. **Bibliografia y fuentes.**

## Estructura propuesta del capitulo 1: Que es un algoritmo

El primer capitulo debe funcionar como puerta conceptual de todo el libro. No debe limitarse a definir "secuencia de pasos"; debe mostrar que un algoritmo es una forma de formalizar decisiones bajo restricciones.

Indice operativo:

1. **La definicion insuficiente**
   - Presentar la definicion comun.
   - Explicar por que es correcta pero pobre.

2. **Breve historia de la idea algorítmica**
   - De Al-Juarismi y los procedimientos aritmeticos al concepto moderno de computacion.
   - Euclides como ejemplo temprano de procedimiento finito.
   - Ada Lovelace, Babbage y la separacion entre maquina y procedimiento.
   - Turing y la formalizacion de lo computable.
   - Dato historico: la palabra algoritmo nace de la latinización del nombre de Al-Juarismi, no de la computacion moderna.

3. **Definicion formal de trabajo**
   - Entrada.
   - Representacion.
   - Transformacion.
   - Control.
   - Salida.
   - Terminacion.
   - Verificacion.

4. **Algoritmo, programa, modelo y decision**
   - El algoritmo no es el codigo.
   - El programa es una implementacion.
   - El modelo define que parte del mundo entra al sistema.
   - La decision define por que la transformacion importa.

5. **Modelos mentales expertos**
   - El algoritmo como contrato.
   - El algoritmo como compresion de una decision.
   - El algoritmo como estructura de representacion.
   - El algoritmo como maquina de errores posibles.
   - El algoritmo como puente entre dominio y ejecucion.

6. **Ejemplo inicial: temperatura, fiebre y riesgo**
   - Mantenerlo como miniatura.
   - Explicitar que no es una escala clinica.
   - Usarlo para mostrar datos, umbrales, contexto, excepciones y consecuencias.

7. **Correcto no significa suficiente**
   - Correccion computacional.
   - Relevancia clinica.
   - Sesgo, datos incompletos, seguridad y responsabilidad.

8. **Tres tensiones criticas**
   - Formalizacion vs juicio clinico.
   - Simplicidad vs fidelidad al fenomeno.
   - Automatizacion vs responsabilidad.

9. **De aqui a la frontera**
   - Busqueda y recuperacion.
   - Grafos biologicos.
   - Programacion dinamica.
   - Alineamiento de secuencias.
   - Redes cerebrales.
   - Sistemas de decision clinica.
   - Modelos fundacionales biomedicos.

10. **Preguntas de comprension profunda**
    - Preguntas de razonamiento, no memoria.
    - Casos donde la regla general falla.
    - Comparaciones entre algoritmo, modelo, programa y decision.

11. **Bibliografia**
    - Fuentes clasicas de algoritmos.
    - Historia de computacion.
    - Razonamiento diagnostico y sistemas clinicos.

## Criterio de exito

El libro funciona si un lector puede:
- aprender desde cero sin sentirse tratado como principiante intelectual;
- entender algoritmos clasicos con rigor;
- conectar cada concepto con medicina y ciencias de la vida;
- avanzar hacia temas de frontera sin ruptura brusca;
- reconocer al autor como medico, programador y pensador interdisciplinario de alto nivel.
