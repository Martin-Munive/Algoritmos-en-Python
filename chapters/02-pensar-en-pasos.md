# Pensar en pasos

Programar no empieza escribiendo codigo. Empieza separando un problema en pasos.

Un medico no evalua a un paciente como una masa indiferenciada de datos. Ordena:

1. motivo de consulta;
2. signos de alarma;
3. antecedentes;
4. examen fisico;
5. hipotesis;
6. pruebas;
7. conducta.

Ese orden no es accidental. Reduce incertidumbre y evita olvidar partes criticas.

Un algoritmo hace algo parecido: convierte una intuicion en un procedimiento que puede revisarse.

## De intuicion a procedimiento

Una mala instruccion seria:

```text
Evalua si el paciente esta grave.
```

Una instruccion mas algorítmica seria:

```text
1. Revisa estado de conciencia.
2. Revisa presion arterial.
3. Revisa frecuencia respiratoria.
4. Revisa saturacion.
5. Si algun criterio cruza umbral de alarma, clasifica como alto riesgo.
```

Todavia falta validar los umbrales, pero la decision ya empezo a tomar forma computacional.

## Primer principio

Un algoritmo no elimina el juicio. Lo obliga a dejar huellas.
