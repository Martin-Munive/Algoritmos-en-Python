# Que es un algoritmo

Un algoritmo es una serie finita de pasos para transformar una entrada en una salida.

La definicion parece simple, pero contiene casi todo lo importante:

- hay una entrada;
- hay una salida esperada;
- hay pasos definidos;
- los pasos terminan;
- el procedimiento puede revisarse.

En medicina, muchas decisiones ya tienen forma algorítmica aunque no las llamemos asi. Un triage, una escala de riesgo, una ruta diagnostica o una pauta de seguimiento son formas de ordenar decisiones bajo condiciones.

La diferencia al programar es que la ambiguedad se vuelve visible. El computador obliga a precisar.

## Un ejemplo minimo

Supongamos que queremos clasificar una temperatura:

```python
temperatura = 38.4

if temperatura >= 38:
    estado = "fiebre"
else:
    estado = "sin fiebre"

print(estado)
```

Este programa no entiende medicina. Solo ejecuta una regla.

Pero esa limitacion es justamente la leccion: un algoritmo no es verdadero por estar escrito en codigo. Es util si la regla, los datos y el contexto son correctos.

## Pregunta central

Antes de escribir un algoritmo, conviene preguntar:

> Que decision estoy intentando hacer explicita?

Esa pregunta acompañara todo el libro.
