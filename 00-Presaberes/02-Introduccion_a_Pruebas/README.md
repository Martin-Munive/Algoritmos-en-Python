# Capítulo 0.02: Introducción a las Pruebas en Python

## 1. ¿Qué son las Pruebas y Por Qué Son Cruciales?

Imagina que construyes un motor de coche complejo. Antes de ponerlo en un coche y salir a la autopista, lo pones en un banco de pruebas. Mides su potencia, verificas que no haya fugas, te aseguras de que cada pieza funcione como se espera bajo estrés.

En programación, las **pruebas automatizadas** son nuestro "banco de pruebas". Son fragmentos de código que escribimos con un único propósito: verificar que nuestro código principal se comporta exactamente como esperamos.

Su utilidad es inmensa:
*   **Confianza:** Te dan la seguridad para hacer cambios. ¿Necesitas mejorar el rendimiento de una función? Hazlo, y luego corre las pruebas. Si todas pasan, sabes que no has roto su funcionalidad principal.
*   **Red de Seguridad (Pruebas de Regresión):** Evitan que un cambio en una parte del programa rompa inesperadamente otra parte. Si introduces un bug, las pruebas te lo dirán inmediatamente.
*   **Documentación Viva:** Una buena prueba describe exactamente lo que se supone que debe hacer una función, sirviendo como un ejemplo de uso práctico.
*   **Mejor Diseño:** Escribir código que sea fácil de probar a menudo te obliga a escribir código mejor, más modular y más organizado.

## 2. Anatomía de Nuestro Archivo de Pruebas

Analicemos el archivo `test_arrays_listas.py` que veremos más adelante cuando hablemos de Listas y Tuplas.

```python
# 1. El Nombre del Archivo
# Comienza con "test_". Esta es una convención estándar. Herramientas
# profesionales como pytest buscan automáticamente archivos con este patrón.

# 2. Funciones de Prueba
def test_list_operations():
    # El nombre de la función también empieza con "test_".
    # Cada función agrupa un conjunto de verificaciones relacionadas.
    """Verifica las operaciones básicas de las listas."""

    # 3. El Corazón de la Prueba: `assert`
    frutas = ["manzana", "banana", "cereza"]
    # `assert` es una afirmación. Le dice a Python:
    # "Afirmo que la siguiente condición ES VERDADERA."
    assert frutas[0] == "manzana"

    # Si la condición es verdadera, el programa continúa silenciosamente.
    # Si es FALSA, el programa se detiene y lanza un `AssertionError`.
    # Este "fallo ruidoso" es exactamente lo que queremos.

# 4. El Bloque de Ejecución
if __name__ == "__main__":
    # Este es un modismo estándar en Python. Significa:
    # "Ejecuta el siguiente código SOLO si este archivo es ejecutado
    # directamente, no si es importado por otro archivo."
    test_list_operations()
    test_tuple_operations()
    print("\nComportamiento verificado.")
```

## 3. La Lógica del Silencio

Cuando ejecutas un archivo de prueba como el nuestro, el **éxito es el silencio**. Si el script termina y solo ves los mensajes de `print` que pusimos al final, significa que todas y cada una de las afirmaciones (`assert`) fueron verdaderas.

El momento en que una prueba falla, se vuelve "ruidosa", detiene todo y te muestra exactamente qué afirmación falló y por qué. Esto te permite identificar y corregir bugs de manera precisa y eficiente.
