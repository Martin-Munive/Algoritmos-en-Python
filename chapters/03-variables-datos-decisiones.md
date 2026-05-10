# Variables, datos y decisiones

Una variable es un nombre para un valor.

En Python:

```python
edad = 67
presion_sistolica = 92
frecuencia_respiratoria = 28
```

La variable permite que el dato pueda usarse despues en una decision.

```python
alto_riesgo = presion_sistolica < 90 or frecuencia_respiratoria > 30
```

El codigo anterior no es una escala clinica completa. Es una miniatura: muestra como un dato puede alimentar una regla.

## Datos no son decisiones

Un error frecuente es confundir almacenar datos con razonar.

Tener una lista de signos vitales no significa haber definido que hacer con ellos. Para convertir datos en decision necesitamos:

- reglas;
- umbrales;
- contexto;
- manejo de excepciones;
- verificacion.

## Por que importa

En programacion biomédica, nombrar bien las variables no es estetica. Es seguridad cognitiva.

```python
pas = 92
```

es mas opaco que:

```python
presion_arterial_sistolica = 92
```

El segundo nombre ocupa mas espacio, pero reduce ambiguedad. En sistemas donde los errores importan, la claridad tambien es una forma de control.
