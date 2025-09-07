# Capítulo 0.03: Formateo de Cadenas con F-Strings

## ¿Qué es `print(f"...")`?

Has visto líneas de código como esta:
```python
print(f"Se eliminó la última tarea: '{ultima_tarea_eliminada}'.")
```
Esto utiliza una característica de Python moderno (introducida en la versión 3.6) llamada **"f-string"** o **cadena literal formateada**. Es la forma más recomendada y legible de incrustar el valor de las variables directamente dentro de una cadena de texto.

## La Evolución del Formateo en Python

Para entender por qué las f-strings son tan buenas, veamos cómo se hacía antes.

#### **Método 1: Concatenación (El antiguo y torpe)**
```python
nombre = "Mundo"
print("Hola, " + nombre + "!") # Funciona, pero es difícil de leer con muchas variables
```

#### **Método 2: El operador `%` (Estilo C)**
```python
nombre = "Mundo"
edad = 30
print("Hola, %s! Tienes %d años." % (nombre, edad)) # Mejor, pero debes recordar los tipos (%s para string, %d para entero)
```

#### **Método 3: El método `.format()` (Más legible)**
```python
nombre = "Mundo"
edad = 30
print("Hola, {}! Tienes {} años.".format(nombre, edad)) # Bueno, pero un poco verboso
```

#### **Método 4: F-Strings (El estándar moderno)**
```python
nombre = "Mundo"
edad = 30
print(f"Hola, {nombre}! Tienes {edad} años.")
```
La sintaxis es simple:
1.  Pones una **`f`** justo antes de la comilla de apertura de la cadena.
2.  Dentro de la cadena, colocas el nombre de cualquier variable que quieras mostrar dentro de **llaves `{}`**.

Python reemplazará automáticamente `{nombre}` y `{edad}` con el valor que esas variables contienen en ese momento.

## ¿Por Qué Usarlas?

1.  **Legibilidad:** El código es mucho más fácil de leer. Ves exactamente dónde irán las variables en el contexto de la frase.
2.  **Concisión:** Requiere escribir menos código que los métodos anteriores.
3.  **Potencia:** Puedes poner expresiones complejas de Python directamente dentro de las llaves.
    ```python
    print(f"El resultado de 5 + 3 es: {5 + 3}")
    # Salida: El resultado de 5 + 3 es: 8
    ```

A lo largo de este libro, usaremos f-strings como nuestro método estándar para mostrar información, ya que es la práctica recomendada en el desarrollo profesional de Python hoy en día.
