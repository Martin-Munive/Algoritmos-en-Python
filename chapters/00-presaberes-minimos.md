# Presaberes mínimos

Este libro no exige que el lector llegue como programador profesional. Sí exige algo más importante: disposición para pensar con precisión. La obra avanza desde decisiones simples en Python hasta estructuras de datos, análisis de complejidad, sistemas biomédicos, bioinformática, genética computacional y problemas en la frontera de la medicina digital. Por eso los presaberes no pueden reducirse a "saber qué es una variable".

La función de esta sección no es reemplazar un curso completo de programación, matemáticas, estadística o medicina basada en evidencia. Su función es establecer el suelo mínimo desde el cual el lector puede avanzar sin que la sintaxis, la notación o el vocabulario oculten las ideas centrales.

Si ya dominas estos elementos, puedes pasar al primer capítulo. Si algunos te resultan nuevos, no necesitas detener el libro: usa esta página como mapa de retorno.

## 1. Leer código antes de escribir código

El lector debe poder mirar un fragmento breve de Python y responder tres preguntas:

1. qué datos entran;
2. qué transformación ocurre;
3. qué salida o decisión se produce.

```python
# Datos observados en una evaluación inicial.
presion_sistolica = 88
frecuencia_respiratoria = 32

# La variable booleana resume una regla mínima de riesgo.
alto_riesgo = presion_sistolica < 90 or frecuencia_respiratoria > 30
```

Salida esperada: este fragmento no imprime nada. Al ejecutarlo, `alto_riesgo` queda con valor `True`.

No basta con decir "esto es Python". Hay que reconocer que el código convierte dos observaciones en una clasificación booleana. Esa diferencia será central en todo el libro.

## 2. Variables como decisiones de representación

Una variable es un nombre para un valor.

```python
# Dos variables numéricas con nombres simples.
edad = 67
presion_sistolica = 92
```

Salida esperada: no imprime nada. El intérprete conserva los valores para usarlos después.

Pero en este libro una variable será más que un recipiente. Será una decisión de representación: qué parte del mundo entra al programa, con qué nombre, en qué unidad, con qué precisión y bajo qué supuesto.

`pas = 92` puede funcionar para un ejercicio escolar. `presion_arterial_sistolica_mmHg = 92` comunica mucho más: variable, magnitud, unidad y sentido clínico.

## 3. Tipos de datos básicos

Python distingue números, texto, valores lógicos y colecciones.

```python
# Cada línea ilustra un tipo de dato básico.
frecuencia_cardiaca = 112      # entero
temperatura = 38.6             # decimal
diagnostico = "neumonia"       # texto
requiere_oxigeno = True        # booleano
```

Salida esperada: no imprime nada. El objetivo es crear variables con tipos distintos.

Estos tipos importan porque una decisión computacional depende de la forma del dato. No se compara igual una cifra, una palabra, una lista o una ausencia de información.

## 4. Colecciones: listas, diccionarios y tablas

Una lista agrupa valores ordenados.

```python
# Lista: colección ordenada de elementos.
signos_alarma = ["hipotension", "hipoxemia", "confusion"]
```

Salida esperada: no imprime nada. `signos_alarma` queda como una lista de tres textos.

Un diccionario asocia nombres con valores.

```python
# Diccionario: registro simple de un paciente.
paciente = {
    "edad": 67,
    "presion_sistolica": 88,
    "saturacion_oxigeno": 89,
}
```

Salida esperada: no imprime nada. `paciente["edad"]` devolvería `67`.

Una tabla organiza observaciones en filas y variables en columnas. Más adelante, esta idea será la base para datos clínicos, laboratorios seriados, cohortes, secuencias biológicas y matrices.

## 5. Condiciones y ramas de decisión

Una condición permite que el programa tome caminos diferentes.

```python
# La condición separa dos ramas de decisión.
if presion_sistolica < 90:
    clasificacion = "alto riesgo"
else:
    clasificacion = "reevaluar"
```

Salida esperada: no imprime nada. Si `presion_sistolica` vale `88`, `clasificacion` queda como `"alto riesgo"`.

El libro volverá una y otra vez a esta idea: una condición no es solo una línea de código; es un umbral, una hipótesis y una responsabilidad.

## 6. Bucles y repetición

Un bucle permite aplicar una operación a varios elementos.

```python
# El bucle recorre cada medición de temperatura.
temperaturas = [37.2, 38.4, 37.9, 39.1]

for temperatura in temperaturas:
    # Solo imprime cuando la temperatura cruza el umbral definido.
    if temperatura >= 38.0:
        print("fiebre")
```

Salida esperada:

```text
fiebre
fiebre
```

Los bucles serán necesarios para recorrer pacientes, registros, genes, ventanas temporales, secuencias, imágenes y resultados de simulación.

## 7. Funciones

Una función encapsula una operación para poder repetirla, probarla y mejorarla.

```python
# La función encapsula una regla para reutilizarla.
def es_hipotension(presion_sistolica):
    return presion_sistolica < 90
```

Salida esperada: no imprime nada. La función queda disponible; `es_hipotension(80)` devolvería `True`.

En software médico, una función bien nombrada puede hacer visible una regla. Una función mal nombrada puede ocultar una decisión peligrosa.

## 8. Ausencia, error y dato faltante

En medicina y ciencias de la vida, lo que falta también informa.

```python
# None representa ausencia explícita de dato.
creatinina = None

if creatinina is None:
    estado = "evaluacion_incompleta"
```

Salida esperada: no imprime nada. `estado` queda como `"evaluacion_incompleta"`.

Un error frecuente es tratar un dato faltante como si fuera normal. Si no hay presión arterial registrada, el paciente no debe clasificarse automáticamente como estable. Debe quedar en un estado diferente: pendiente, incompleto o no evaluable.

## 9. Pruebas y verificación

Una prueba verifica que una parte del programa hace lo esperado.

```python
# Las aserciones fallan si la función no cumple lo esperado.
assert es_hipotension(80) == True
assert es_hipotension(120) == False
```

Salida esperada: no imprime nada si las pruebas pasan. Si alguna condición fuera falsa, Python produciría un `AssertionError`.

El lector no necesita dominar pruebas desde el inicio, pero debe entender la idea: si una decisión va a convertirse en código, debe poder verificarse.

## 10. Archivos, rutas y entorno de trabajo

El libro usará archivos, carpetas, notebooks y scripts. El lector debe reconocer que un programa no vive aislado: lee datos, guarda resultados, importa módulos y depende de un entorno.

Conceptos mínimos:

- carpeta de proyecto;
- archivo `.py`;
- notebook `.ipynb`;
- archivo `.csv`;
- ruta relativa y ruta absoluta;
- entorno virtual;
- instalación de paquetes;
- ejecución desde terminal o editor.

Estos temas aparecen con más detalle en el apéndice de entorno.

## 11. Matemática mínima

No se requiere cálculo avanzado para empezar. Sí se requiere familiaridad con algunas ideas:

- proporción y porcentaje;
- razón y tasa;
- promedio, mediana y dispersión;
- crecimiento lineal y crecimiento no lineal;
- escala logarítmica;
- función como transformación de entrada en salida;
- comparación entre órdenes de magnitud.

Cuando el libro llegue a complejidad computacional, bioinformática o modelos, estas ideas dejarán de ser ornamento. Serán lenguaje de trabajo.

## 12. Estadística mínima

El lector debe reconocer que los datos no hablan solos. Vienen con variabilidad, sesgo, incertidumbre y contexto.

Conceptos de entrada:

- muestra y población;
- distribución;
- falso positivo y falso negativo;
- sensibilidad y especificidad;
- valor predictivo;
- correlación;
- sesgo;
- incertidumbre;
- validación.

No necesitas dominarlos todos antes de empezar. Pero sí debes saber que una decisión computacional sobre datos clínicos nunca es puramente mecánica.

## 13. Lectura científica mínima

Este libro no será un diario de opiniones. Cada tema importante debe apoyarse en fuentes identificables. Por eso conviene que el lector distinga:

- definición operacional;
- ejemplo pedagógico;
- evidencia empírica;
- revisión;
- guía;
- consenso;
- limitación;
- extrapolación.

Una fuente científica no se usa para decorar una frase. Se usa para saber qué podemos afirmar, con qué fuerza y bajo qué límites.

## 14. Medicina y biología como dominios de consecuencias

Los ejemplos biomédicos del libro son pedagógicos, no instrucciones asistenciales. Aun así, no serán ejemplos vacíos. Un algoritmo que clasifica riesgo, procesa un laboratorio o analiza una secuencia biológica debe respetar el hecho de que el dominio tiene consecuencias.

Por eso hablaremos de:

- contexto clínico;
- seguridad;
- sesgo;
- trazabilidad;
- explicabilidad;
- validación externa;
- límites de automatización.

## Cómo usar esta página

Si estos conceptos son familiares, continúa. Si no lo son, avanza igual, pero vuelve aquí cuando una sección use alguno de ellos. El objetivo no es memorizar sintaxis. El objetivo es construir el vocabulario mínimo para estudiar algoritmos como instrumentos de pensamiento, ciencia y responsabilidad.
