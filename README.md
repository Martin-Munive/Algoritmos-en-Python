# Materia Medica Digitalis

**Algoritmos en Python para Medicina y Ciencias de la Vida**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter Book](https://img.shields.io/badge/Jupyter%20Book-Sphinx-F37626?logo=jupyter&logoColor=white)](https://jupyterbook.org/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-libro%20web-222222?logo=githubpages&logoColor=white)](https://martin-munive.github.io/Algoritmos-en-Python/)
[![Estado](https://img.shields.io/badge/estado-edici%C3%B3n%20limpia%20en%20construcci%C3%B3n-F59E0B)](#estado-editorial)
[![Licencia](https://img.shields.io/badge/licencia-MIT-16A34A)](LICENSE)

> Un libro web para aprender algoritmos desde problemas biomédicos: datos clínicos, decisiones, riesgo, estructuras de información, seguimiento de pacientes y sistemas computacionales para ciencias de la vida.

**Materia Medica Digitalis** nace de una premisa simple: los algoritmos se entienden mejor cuando dejan de ser abstracciones aisladas y se convierten en instrumentos para pensar problemas reales. Este libro usa Python como lenguaje de trabajo y la medicina como territorio de aplicación para construir pensamiento computacional con rigor, claridad y utilidad.

---

## Leer el libro

- **Sitio web:** <https://martin-munive.github.io/Algoritmos-en-Python/>
- **Portada del libro:** [`chapters/00-prefacio.md`](chapters/00-prefacio.md)
- **Configuración del libro:** [`_config.yml`](_config.yml)
- **Tabla de contenidos:** [`_toc.yml`](_toc.yml)
- **Auditoría editorial previa:** [`docs/editorial_audit.md`](docs/editorial_audit.md)
- **Hoja de ruta previa:** [`docs/roadmap.md`](docs/roadmap.md)

> El libro está en reconstrucción editorial. El contenido previo del repositorio se conserva como cantera técnica, pero la edición web se está rehaciendo desde una base limpia.

---

## Qué es este proyecto

Este repositorio contiene la edición web de un libro sobre algoritmos, estructuras de datos y pensamiento computacional aplicado a medicina y ciencias de la vida.

No es solo una colección de apuntes ni una lista de ejercicios. La aspiración editorial es construir una obra progresiva donde cada capítulo responda tres preguntas:

1. **Qué problema resuelve este concepto.**
2. **Cómo se implementa con Python.**
3. **Por qué importa en un contexto biomédico real.**

El objetivo no es enseñar Python como sintaxis aislada. El objetivo es enseñar a razonar con algoritmos.

---

## Para quién es

Este libro está escrito para:

- estudiantes y profesionales de medicina que quieren entrar a programación, ciencia de datos o inteligencia artificial;
- investigadores en ciencias de la vida que necesitan automatizar análisis, ordenar datos y construir herramientas reproducibles;
- programadores interesados en aplicaciones biomédicas con sentido clínico y científico;
- lectores que quieren aprender algoritmos desde casos concretos, no desde ejemplos genéricos.

No se asume formación avanzada en ciencias de la computación. Sí se espera curiosidad, paciencia y voluntad de pensar con precisión.

---

## Promesa editorial

Al avanzar por el libro, el lector debería poder:

- traducir problemas biomédicos a estructuras computacionales;
- distinguir datos, reglas, decisiones, flujos y estados;
- implementar algoritmos fundamentales en Python;
- evaluar complejidad temporal y espacial sin perder intuición práctica;
- construir herramientas pequeñas, verificables y útiles;
- entender por qué un algoritmo correcto puede ser clínicamente insuficiente si ignora contexto, sesgo o seguridad.

---

## Índice maestro

La edición limpia organizará el libro en siete partes.

### I. El lenguaje de las decisiones

- Qué es un algoritmo
- Pensar en pasos
- Variables, datos y decisiones
- Condicionales
- Bucles
- Funciones
- Errores, excepciones y seguridad del cálculo

### II. Python como instrumento clínico-científico

- Tipos de datos para problemas biomédicos
- Listas, diccionarios y tablas simples
- Lectura y limpieza de datos
- Cálculo clínico reproducible
- Automatización de tareas repetitivas
- Validación de entradas

### III. Algoritmos fundamentales

- Búsqueda lineal y búsqueda binaria
- Ordenamiento y priorización
- Conteo, frecuencia y distribución
- Filtrado de pacientes, eventos y resultados
- Agrupación y resumen
- Complejidad computacional
- Algoritmos voraces
- Programación dinámica

### IV. Datos médicos y razonamiento cuantitativo

- Sensibilidad, especificidad y valores predictivos
- Riesgo absoluto, riesgo relativo y NNT
- Scores clínicos como algoritmos
- Triage y estratificación de riesgo
- Series temporales en signos vitales
- Alertas, umbrales e incertidumbre

### V. Estructuras de datos para ciencias de la vida

- Arrays y matrices
- Tablas clínicas
- Grafos y redes biomédicas
- Árboles de decisión
- Pilas, colas y flujos de atención
- Índices y recuperación de información
- Representación de conocimiento médico

### VI. Casos aplicados

- Calculadora de riesgo cardiovascular
- Clasificador simple de urgencias
- Seguimiento longitudinal de laboratorio
- Detección de interacciones o contraindicaciones
- Banco de preguntas médico con seguimiento de intentos
- Sistema de priorización de pacientes
- Mini motor de reglas clínicas

### VII. Del algoritmo al sistema

- Organización de proyectos Python
- Pruebas y verificación
- Documentación técnica y médica
- Interfaces simples
- Ética, seguridad y responsabilidad
- Límites de la automatización clínica

---

## Primer lanzamiento editorial

La reconstrucción comenzará con una unidad breve, coherente y publicable:

1. **Inicio:** promesa, audiencia y mapa del libro.
2. **Prefacio:** por qué un médico o científico de la vida debe aprender algoritmos.
3. **Qué es un algoritmo:** definición, intuición y ejemplos biomédicos.
4. **Pensar en pasos:** del razonamiento clínico al procedimiento computacional.
5. **Variables, datos y decisiones:** primera conexión formal con Python.

Cada entrega buscará ser una unidad de aprendizaje completa, no una cuota arbitraria de páginas.

---

## Filosofía

Un algoritmo no es una receta vacía. Es una forma de hacer explícita una decisión.

En medicina y ciencias de la vida, esa decisión rara vez vive sola: aparece dentro de incertidumbre, datos incompletos, riesgos, umbrales, pacientes, poblaciones y consecuencias. Por eso este libro no separa la técnica del contexto. La técnica se estudia para pensar mejor.

---

## Estado editorial

El repositorio tuvo una primera etapa como colección de materiales sobre algoritmos y estructuras de datos. Esa etapa dejó contenido útil, pero la nueva edición requiere una arquitectura más limpia para publicarse como libro web.

Estado actual:

- **Identidad editorial:** definida.
- **Stack web:** Jupyter Book + Sphinx + GitHub Pages.
- **Contenido previo:** conservado como fuente de reconstrucción.
- **Edición limpia:** en construcción.
- **Publicación incremental:** prevista por unidades de aprendizaje.

---

## Estructura del repositorio

```text
.
├── docs/                  # Edición web publicable
├── chapters/              # Nueva edición Jupyter Book
├── _config.yml            # Configuración del libro
├── _toc.yml               # Tabla de contenidos del libro
├── docs/                  # Material editorial previo y transición
├── mkdocs.yml             # Configuración previa MkDocs, transitoria
├── requirements.txt       # Dependencias de publicación
├── .github/workflows/     # Despliegue con GitHub Pages
├── 00-Presaberes/         # Material previo conservado
├── 01-Analisis_.../       # Material previo conservado
└── 02-Estructuras_.../    # Material previo conservado
```

La carpeta `chapters/` será la fuente de la nueva edición web tipo libro. Las carpetas históricas y la carpeta `docs/` se conservan mientras se decide qué contenido se migra, reescribe o retira.

---

## Desarrollo local

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Levantar el sitio:

```bash
jupyter-book build .
```

Construir versión estática:

```bash
jupyter-book build .
```

---

## Licencia

El código y los materiales del repositorio se distribuyen bajo licencia MIT, salvo que un archivo específico indique otra cosa.

---

## Nota final

Este libro se construye con una ambición precisa: que aprender algoritmos no sea memorizar estructuras, sino adquirir una forma más clara, rigurosa y útil de pensar problemas de la vida real.
