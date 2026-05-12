# Presaberes mínimos

Este libro no exige que el lector llegue como programador profesional. Si ya sabe programar, puede avanzar directamente al primer capitulo. Si esta empezando, esta pagina indica que debe reconocer antes de leer con comodidad.

La funcion de estos presaberes no es convertir el libro en un curso basico de Python. Es evitar que la sintaxis bloquee la comprension de las ideas importantes: representar datos, construir decisiones, verificar procedimientos y pensar algoritmicamente.

## Lo que debes reconocer

### 1. Variables

Una variable es un nombre que permite conservar un valor para usarlo despues.

```python
edad = 67
presion_sistolica = 92
```

En este libro, una variable no sera tratada solo como sintaxis. Sera una decision de representacion: que parte del mundo entra al programa y con que nombre.

### 2. Tipos de datos basicos

Python distingue numeros, texto, valores logicos y colecciones.

```python
frecuencia_cardiaca = 112      # entero
temperatura = 38.6             # decimal
diagnostico = "neumonia"       # texto
requiere_oxigeno = True        # booleano
```

Estos tipos importan porque una decision computacional depende de la forma del dato. No se compara igual una cifra, una palabra, una lista o una ausencia de informacion.

### 3. Condiciones

Una condicion permite que el programa tome caminos diferentes.

```python
if presion_sistolica < 90:
    clasificacion = "alto riesgo"
else:
    clasificacion = "reevaluar"
```

El libro volvera una y otra vez a esta idea: una condicion no es solo una linea de codigo; es un umbral, una hipotesis y una responsabilidad.

### 4. Listas

Una lista agrupa varios valores.

```python
signos_alarma = ["hipotension", "hipoxemia", "confusion"]
```

Las listas seran la entrada natural a estructuras de datos, series de signos vitales, registros clinicos y colecciones biologicas.

### 5. Funciones

Una funcion encapsula una operacion para poder repetirla, probarla y mejorarla.

```python
def es_hipotension(presion_sistolica):
    return presion_sistolica < 90
```

En software medico, una funcion bien nombrada puede hacer visible una regla. Una funcion mal nombrada puede ocultar una decision peligrosa.

### 6. Pruebas

Una prueba verifica que una parte del programa hace lo esperado.

```python
assert es_hipotension(80) == True
assert es_hipotension(120) == False
```

El lector no necesita dominar pruebas desde el inicio, pero debe entender la idea: si una decision va a convertirse en codigo, debe poder verificarse.

### 7. Salida de informacion

Python puede construir mensajes con valores usando f-strings.

```python
paciente = "Caso 01"
riesgo = "alto"
print(f"{paciente}: riesgo {riesgo}")
```

Esto sera util cuando el libro trabaje reportes, trazabilidad y explicacion de resultados.

## Como usar esta pagina

Si estos ejemplos son familiares, continua. Si no lo son, no detengas la lectura: vuelve a esta pagina cuando una seccion use alguno de estos elementos. El objetivo no es memorizar sintaxis, sino reconocer las piezas minimas con las que se construyen decisiones computables.
