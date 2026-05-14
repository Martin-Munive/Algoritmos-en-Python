# Variables, datos y decisiones

Una variable es un nombre para un valor.

En Python:

```python
edad = 67
presion_sistolica = 92
frecuencia_respiratoria = 28
```

La variable permite que el dato pueda usarse después en una decisión.

```python
alto_riesgo = presion_sistolica < 90 or frecuencia_respiratoria > 30
```

El código anterior no es una escala clínica completa. Es una miniatura: muestra cómo un dato puede alimentar una regla.

## Datos no son decisiones

Un error frecuente es confundir almacenar datos con razonar.

Tener una lista de signos vitales no significa haber definido qué hacer con ellos. Para convertir datos en decisión necesitamos:

- reglas;
- umbrales;
- contexto;
- manejo de excepciones;
- verificación.

## Por qué importa

En programación biomédica, nombrar bien las variables no es estética. Es seguridad cognitiva.

```python
pas = 92
```

es más opaco que:

```python
presion_arterial_sistolica = 92
```

El segundo nombre ocupa más espacio, pero reduce ambigüedad. En sistemas donde los errores importan, la claridad también es una forma de control.
