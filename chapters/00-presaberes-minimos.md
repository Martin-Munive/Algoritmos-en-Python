# Presaberes mínimos

Este libro no exige que el lector llegue como programador profesional. Si ya sabe programar, puede avanzar directamente al primer capítulo. Si está empezando, esta página indica qué debe reconocer antes de leer con comodidad.

La función de estos presaberes no es convertir el libro en un curso básico de Python. Es evitar que la sintaxis bloquee la comprensión de las ideas importantes: representar datos, construir decisiones, verificar procedimientos y pensar algorítmicamente.

## Lo que debes reconocer

### 1. Variables

Una variable es un nombre que permite conservar un valor para usarlo después.

```python
edad = 67
presion_sistolica = 92
```

En este libro, una variable no será tratada solo como sintaxis. Será una decisión de representación: qué parte del mundo entra al programa y con qué nombre.

### 2. Tipos de datos básicos

Python distingue números, texto, valores lógicos y colecciones.

```python
frecuencia_cardiaca = 112      # entero
temperatura = 38.6             # decimal
diagnostico = "neumonia"       # texto
requiere_oxigeno = True        # booleano
```

Estos tipos importan porque una decisión computacional depende de la forma del dato. No se compara igual una cifra, una palabra, una lista o una ausencia de información.

### 3. Condiciones

Una condición permite que el programa tome caminos diferentes.

```python
if presion_sistolica < 90:
    clasificacion = "alto riesgo"
else:
    clasificacion = "reevaluar"
```

El libro volverá una y otra vez a esta idea: una condición no es solo una línea de código; es un umbral, una hipótesis y una responsabilidad.

### 4. Listas

Una lista agrupa varios valores.

```python
signos_alarma = ["hipotension", "hipoxemia", "confusion"]
```

Las listas serán la entrada natural a estructuras de datos, series de signos vitales, registros clínicos y colecciones biológicas.

### 5. Funciones

Una función encapsula una operación para poder repetirla, probarla y mejorarla.

```python
def es_hipotension(presion_sistolica):
    return presion_sistolica < 90
```

En software médico, una función bien nombrada puede hacer visible una regla. Una función mal nombrada puede ocultar una decisión peligrosa.

### 6. Pruebas

Una prueba verifica que una parte del programa hace lo esperado.

```python
assert es_hipotension(80) == True
assert es_hipotension(120) == False
```

El lector no necesita dominar pruebas desde el inicio, pero debe entender la idea: si una decisión va a convertirse en código, debe poder verificarse.

### 7. Salida de información

Python puede construir mensajes con valores usando f-strings.

```python
paciente = "Caso 01"
riesgo = "alto"
print(f"{paciente}: riesgo {riesgo}")
```

Esto será útil cuando el libro trabaje reportes, trazabilidad y explicación de resultados.

## Cómo usar esta página

Si estos ejemplos son familiares, continúa. Si no lo son, no detengas la lectura: vuelve a esta página cuando una sección use alguno de estos elementos. El objetivo no es memorizar sintaxis, sino reconocer las piezas mínimas con las que se construyen decisiones computables.
