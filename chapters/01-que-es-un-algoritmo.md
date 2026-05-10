# Que es un algoritmo

La palabra algoritmo suele presentarse con una definicion demasiado breve: una serie finita de pasos para resolver un problema. La frase no es falsa, pero es insuficiente. Sirve como puerta de entrada; no sirve como concepto rector para medicina, ciencia de datos, inteligencia artificial o software clinico.

En un dominio trivial, un algoritmo puede parecer una receta. En un dominio serio, un algoritmo es una arquitectura de decision: define que informacion importa, que transformaciones son validas, que condiciones cambian el curso de accion, que errores deben anticiparse y cuando el procedimiento debe detenerse.

<div class="definition-block">
<strong>Definicion de trabajo.</strong><br />
Un algoritmo es una especificacion finita, ordenada y verificable de transformaciones y decisiones que convierte entradas en salidas bajo un conjunto explicito de reglas, restricciones y criterios de terminacion.
</div>

Esa definicion tiene mas peso porque obliga a mirar el concepto por capas. Un algoritmo no es solo "hacer pasos". Es una forma de someter una decision a inspeccion.

## Las capas de un algoritmo

Un algoritmo serio tiene al menos seis componentes.

**Entrada.** Algo debe ingresar al sistema: datos, mediciones, texto, senales, sintomas, parametros, archivos, observaciones o estados previos.

**Representacion.** La entrada no entra desnuda. Debe convertirse en una forma manipulable: numeros, cadenas, listas, tablas, diccionarios, objetos, grafos, matrices o estructuras mas especializadas.

**Reglas.** El procedimiento necesita operaciones definidas. Comparar, filtrar, ordenar, sumar, buscar, clasificar, transformar, validar, inferir.

**Control.** No basta con tener reglas. Debe existir un orden: condiciones, ramas, repeticiones, excepciones, ciclos de revision y criterios de parada.

**Salida.** El algoritmo produce algo: una clasificacion, una alerta, una recomendacion, un calculo, una visualizacion, un reporte, una accion.

**Verificacion.** El resultado debe poder examinarse. Si no podemos revisar por que una salida aparecio, el procedimiento puede funcionar como maquinaria, pero no como conocimiento confiable.

Estas capas importan porque impiden una confusion frecuente: creer que el codigo es el algoritmo. El codigo es una encarnacion posible. El algoritmo es la estructura intelectual que el codigo ejecuta.

## Algoritmos antes del computador

La medicina ha usado pensamiento algorítmico mucho antes de que el software entrara al hospital. Un triage, una escala pronostica, un protocolo de reanimacion, un esquema diagnostico, una ruta de vigilancia epidemiologica o una pauta de seguimiento son intentos de ordenar decisiones bajo restricciones.

La diferencia es que el computador vuelve intolerable la ambiguedad. Una instruccion humana puede apoyarse en contexto tacito; una instruccion computacional exige precision. Donde el lenguaje natural dice "si el paciente esta grave", el programa pregunta:

- que variables definen gravedad;
- que umbral separa bajo y alto riesgo;
- que ocurre si falta un dato;
- que pasa si dos signos se contradicen;
- que excepcion tiene prioridad;
- que salida debe generarse;
- quien recibe esa salida y con que responsabilidad.

La programacion no elimina el juicio. Lo expone. Obliga a declarar lo que antes podia permanecer implicito.

## Un ejemplo deliberadamente pequeño

Supongamos que queremos clasificar una temperatura corporal.

```python
temperatura_celsius = 38.4

if temperatura_celsius >= 38.0:
    estado_termico = "fiebre"
else:
    estado_termico = "sin fiebre"

print(estado_termico)
```

Este fragmento es simple, pero ya contiene una tesis completa.

Hay una entrada: `temperatura_celsius`. Hay una regla: comparar con `38.0`. Hay una bifurcacion: fiebre o no fiebre. Hay una salida: `estado_termico`. Y hay una decision conceptual escondida: aceptar un umbral.

El programa no sabe medicina. No sabe si la medicion fue axilar, oral, timpanica o rectal. No sabe la edad del paciente, el contexto clinico, el uso de antipireticos, el estado inmune ni la trayectoria temporal. Tampoco sabe si clasificar fiebre es suficiente o si la pregunta relevante era otra: riesgo de sepsis, indicacion de aislamiento, necesidad de hemocultivos, prioridad de atencion.

Ese es el punto. Un algoritmo no se vuelve inteligente por estar escrito en Python. Se vuelve util cuando la estructura de decision corresponde al problema real.

## De regla a modelo de decision

Podemos volver el ejemplo un poco menos ingenuo:

```python
temperatura_celsius = 38.4
frecuencia_cardiaca = 118
presion_sistolica = 88

fiebre = temperatura_celsius >= 38.0
taquicardia = frecuencia_cardiaca >= 100
hipotension = presion_sistolica < 90

alto_riesgo = fiebre and (taquicardia or hipotension)

if alto_riesgo:
    conducta = "evaluacion_prioritaria"
else:
    conducta = "seguimiento_clinico"

print(conducta)
```

Seguimos ante una miniatura, no ante una escala clinica validada. Pero la estructura ya cambio. El algoritmo no clasifica un dato aislado; integra variables, crea conceptos intermedios y produce una conducta.

Esta diferencia es fundamental. Muchos programas fallan no porque la sintaxis sea incorrecta, sino porque la decision representada es pobre. El error profundo no esta en el `if`; esta en haber reducido un fenomeno complejo a una regla sin suficiente estructura.

## La pregunta que separa programar de pensar

Antes de escribir un algoritmo conviene detenerse en una pregunta:

> Que decision estoy intentando hacer explicita?

La respuesta rara vez es inmediata. Puede requerir separar varias capas:

- estoy describiendo un estado o tomando una decision;
- estoy clasificando riesgo o prediciendo un resultado;
- estoy filtrando datos o generando una recomendacion;
- estoy automatizando una tarea administrativa o formalizando razonamiento clinico;
- estoy ayudando a un humano o sustituyendo una parte de su proceso;
- estoy creando una herramienta exploratoria o un sistema que afectara decisiones reales.

Esta pregunta es mas importante que elegir una libreria. Sin ella, el codigo puede crecer rapido y aun asi carecer de inteligencia.

## Correcto no significa suficiente

En ciencias de la computacion, un algoritmo puede evaluarse por correccion: produce la salida esperada para las entradas definidas. En medicina y ciencias de la vida, esa evaluacion es necesaria, pero incompleta.

Un algoritmo puede ser sintacticamente correcto y clinicamente irrelevante. Puede ser eficiente y biologicamente ingenuo. Puede ser reproducible y metodologicamente sesgado. Puede ser transparente y aun asi operar sobre datos pobres. Puede acertar en promedio y fallar justo en los casos donde mas importa.

Por eso este libro no tratara los algoritmos como ornamentos matematicos ni como juguetes de programacion. Los trata como instrumentos de pensamiento. Un instrumento debe ser elegante, pero tambien debe responder a su uso.

## Lo que aprenderemos a ver

A partir de este punto, cada concepto tecnico tendra doble lectura.

Cuando aparezca una variable, preguntaremos que representa y que oculta. Cuando aparezca una condicion, preguntaremos que decision formaliza. Cuando aparezca un bucle, preguntaremos que proceso se repite y bajo que criterio debe detenerse. Cuando aparezca una estructura de datos, preguntaremos que mundo permite organizar y que consultas vuelve posibles.

La programacion empieza a volverse poderosa cuando deja de ser mecanica y se convierte en epistemologia practica: una manera de investigar que sabemos, que asumimos, que ignoramos y que estamos dispuestos a automatizar.
