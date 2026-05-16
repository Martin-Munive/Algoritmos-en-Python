# Brief de rediseño de portada

## Propósito

Documentar cómo debe evolucionar la portada de `Materia Médica Digitalis` para que funcione como primera pantalla editorial profesional, atractiva y coherente con un libro técnico-científico en Jupyter Book.

## Diagnóstico

La portada actual cumple una función mínima:

- muestra título;
- muestra subtítulo;
- muestra autor y credenciales;
- declara propósito.

Pero es demasiado simple. No comunica con suficiente fuerza:

- el cruce entre medicina, algoritmos y Python;
- la ambición de la obra;
- la progresión desde fundamentos hasta frontera;
- la autoridad intelectual del autor;
- una ruta clara de entrada para el lector.

## Hallazgos de referencias externas

### Sphinx Book Theme

La documentación del Sphinx Book Theme enfatiza un diseño limpio para libros y documentación científica. Sus principios favorecen elementos visuales mínimos, uso de espacio en blanco, navegación consistente y baja fricción de lectura.

Fuentes:
- <https://sphinx-book-theme.readthedocs.io/en/latest/>
- <https://sphinx-book-theme-test.readthedocs.io/en/stable/contributing/style.html>

Implicación para este libro:
- la portada no debe convertirse en una landing page comercial pesada;
- debe seguir pareciendo libro académico;
- el atractivo debe venir de jerarquía editorial, composición, promesa intelectual y recursos visuales sobrios.

### Sphinx

Sphinx permite personalización mediante temas, CSS, plantillas y archivos estáticos. La documentación oficial presenta Sphinx como sistema para crear documentación estructurada, con soporte de temas HTML y salida navegable.

Fuentes:
- <https://www.sphinx-doc.org/>
- <https://www.sphinx-doc.org/en/master/usage/theming.html>

Implicación:
- el rediseño puede realizarse con `chapters/00-portada.md` y `_static/custom.css` sin cambiar de stack;
- no conviene migrar de tecnología solo por estética.

### The Turing Way

The Turing Way, también construido como libro web, usa una entrada que explica propósito, audiencia, navegación y rutas de lectura. Su guía de estilo enfatiza consistencia, legibilidad, estructura modular y referencias.

Fuentes:
- <https://book.the-turing-way.org/>
- <https://book.the-turing-way.org/community-handbook/style/consistency/consistency-formatting>
- <https://book.the-turing-way.org/community-handbook/style/consistency/consistency-structure/>

Implicación:
- la portada debe orientar al lector, no solo decorar;
- debe incluir rutas de lectura claras;
- debe evitar una tabla de contenidos manual redundante con la navegación generada si no aporta valor.

### Think Python

`Think Python` funciona como referencia editorial de libro web técnico sobrio: navegación clara, énfasis en lectura, capítulos progresivos y bajo ruido visual.

Fuente:
- <https://allendowney.github.io/ThinkPython/>

Implicación:
- conservar sobriedad académica;
- mejorar primera impresión sin transformar el libro en sitio promocional.

## Principio de rediseño

La portada debe sentirse como la entrada a una obra científica y computacional seria, no como un README ni como una página de marketing.

Debe resolver cinco preguntas en la primera pantalla:

1. Qué es el libro.
2. Para quién existe.
3. Qué promesa intelectual ofrece.
4. Qué lo diferencia.
5. Por dónde empezar.

## Propuesta de estructura

### 1. Bloque hero editorial

Elementos:

- kicker: `Algoritmos en Python para Medicina y Ciencias de la Vida`;
- título grande: `Materia Médica Digitalis`;
- subtítulo breve y potente;
- autor y credenciales;
- micro-resumen de una frase.

Objetivo:
- captar identidad y autoridad en segundos.

### 2. Panel de promesa intelectual

Tres o cuatro enunciados breves:

- pensar decisiones como algoritmos;
- convertir datos biomédicos en estructuras verificables;
- aprender Python sin reducirlo a sintaxis;
- avanzar hacia bioinformática, genética y medicina digital.

Objetivo:
- mostrar ambición sin inflar el texto.

### 3. Rutas de lectura

Tres rutas:

- `Empieza desde cero`: prefacio + presaberes + primer capítulo.
- `Ruta médica`: decisiones, riesgo, datos faltantes, trazabilidad.
- `Ruta computacional`: variables, estados, condiciones, estructuras y algoritmos.

Objetivo:
- enganchar a lectores distintos sin romper la navegación formal.

### 4. Mapa de progresión

Una banda breve con etapas:

`Decisiones -> Python -> Estructuras -> Algoritmos -> Datos biomédicos -> Frontera`

Objetivo:
- comunicar que el libro no se queda en ejemplos introductorios.

### 5. Aviso de responsabilidad

Una nota breve:

- los ejemplos médicos son pedagógicos;
- no reemplazan juicio clínico ni validación.

Objetivo:
- proteger el proyecto y reforzar seriedad.

## Dirección visual

Estilo recomendado:

- académico moderno;
- sobrio;
- alto contraste;
- tipografía clara;
- tarjetas discretas solo para rutas o promesas;
- sin exceso de color;
- sin imagen decorativa genérica;
- posible motivo visual abstracto basado en red, matriz, señal o flujo de decisión.

Paleta sugerida:

- texto principal: `#111827`;
- texto secundario: `#374151`;
- línea/acento: `#0f766e` o `#2563eb`;
- fondo suave: `#f8fafc`;
- borde: `#d1d5db`.

## Reglas de implementación

1. Implementar solo con Markdown/HTML seguro y `_static/custom.css`.
2. No cambiar stack editorial.
3. No introducir dependencias nuevas para la portada.
4. Mantener compatibilidad con Jupyter Book/Sphinx Book Theme.
5. No duplicar todo el índice generado por `_toc.yml`.
6. Verificar en build local antes de commit.

## Estado

- Investigación inicial realizada.
- Rediseño implementado en `chapters/00-portada.md` y `_static/custom.css`.
- Pendiente: revisar visualmente el HTML en navegador antes de consolidar commit.
