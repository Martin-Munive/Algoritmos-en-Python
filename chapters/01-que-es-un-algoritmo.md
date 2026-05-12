# Que es un algoritmo

La palabra algoritmo suele presentarse con una definicion demasiado breve: una serie finita de pasos para resolver un problema. La frase no es falsa, pero es insuficiente. Sirve como puerta de entrada; no sirve como concepto rector para medicina, ciencia de datos, inteligencia artificial, bioinformatica o software clinico.

En un dominio trivial, un algoritmo puede parecer una receta. En un dominio serio, un algoritmo es una arquitectura de decision: define que informacion importa, como se representa, que transformaciones son validas, que condiciones cambian el curso de accion, que errores deben anticiparse y cuando el procedimiento debe detenerse.

Este capitulo no busca que memorices una definicion. Busca que aprendas a mirar cualquier algoritmo como una pieza de pensamiento formal: una forma de domesticar una pregunta hasta volverla ejecutable, verificable y criticable.

## Breve historia de una idea antigua

La computacion moderna hizo famosa la palabra algoritmo, pero la idea es mucho mas antigua que el computador.

Uno de los ejemplos clasicos es el algoritmo de Euclides para encontrar el maximo comun divisor de dos numeros. Aparece en los *Elementos*, alrededor del 300 a. C., y sigue siendo una pieza viva de la matematica computacional. Su fuerza no esta solo en que calcula un resultado; esta en que muestra algo profundo: un problema puede resolverse por reduccion sucesiva, transformando una pregunta dificil en otra mas pequena hasta que aparece una condicion de parada.

Muchos siglos despues, el termino algoritmo quedo asociado al nombre de Muhammad ibn Musa al-Khwarizmi, matematico del siglo IX. La palabra procede de formas latinizadas de su nombre usadas en textos medievales sobre calculo con numerales hindu-arabigos. El dato curioso importa: "algoritmo" no nacio como una palabra de Silicon Valley, ni siquiera como una palabra de computacion electronica. Nacio ligado a la transmision cultural de tecnicas de calculo.

En el siglo XIX, Charles Babbage imagino la Maquina Analitica, un dispositivo mecanico programable que nunca llego a construirse completamente. Ada Lovelace, al comentar ese proyecto, entendio algo decisivo: una maquina de calculo podia manipular simbolos de acuerdo con reglas, no solo numeros como cantidades. Sus notas sobre la Maquina Analitica incluyeron procedimientos para calcular numeros de Bernoulli y anticiparon la separacion entre maquina, datos e instrucciones.

En 1936, Alan Turing llevo la pregunta a otro nivel. No se limito a preguntar como calcular algo, sino que formalizo que significa que un procedimiento sea mecanico. La maquina de Turing no fue importante por ser una maquina fisica, sino por convertir la intuicion de "metodo efectivo" en un objeto matematico. Desde ahi, la pregunta por los algoritmos quedo conectada con una frontera: hay problemas que ningun procedimiento general puede decidir.

La historia deja una leccion para este libro: un algoritmo no es simplemente una lista de pasos. Es una forma historica, matematica y tecnica de responder una pregunta: que parte del razonamiento puede hacerse explicita?

## Definicion formal de trabajo

<div class="definition-block">
<strong>Definicion de trabajo.</strong><br />
Un algoritmo es una especificacion finita, ordenada y verificable de transformaciones y decisiones que convierte entradas en salidas bajo un conjunto explicito de reglas, restricciones y criterios de terminacion.
</div>

La definicion tiene varias piezas.

**Entrada.** Algo ingresa al sistema: numeros, texto, signos vitales, imagenes, secuencias geneticas, resultados de laboratorio, grafos, sintomas, historiales o estados previos.

**Representacion.** La entrada debe adoptar una forma manipulable: variables, listas, tablas, matrices, diccionarios, grafos, tensores, cadenas de caracteres o estructuras especializadas.

**Transformacion.** El algoritmo opera sobre esa representacion: compara, filtra, busca, ordena, suma, estima, clasifica, alinea, optimiza, infiere o simula.

**Control.** No basta con tener operaciones. Debe existir una arquitectura de flujo: condiciones, ramas, ciclos, recursion, excepciones y criterios de parada.

**Salida.** El procedimiento produce algo: una clasificacion, alerta, recomendacion, calculo, reporte, ruta, prediccion, visualizacion o accion.

**Terminacion.** El algoritmo debe saber cuando detenerse o declarar que no puede continuar bajo las condiciones dadas.

**Verificacion.** La salida debe poder examinarse. Si no podemos revisar por que aparecio, el procedimiento puede funcionar como maquinaria, pero no como conocimiento confiable.

Estas capas impiden una confusion frecuente: creer que el codigo es el algoritmo. El codigo es una encarnacion posible. El algoritmo es la estructura intelectual que el codigo ejecuta.

## Algoritmo, programa, modelo y decision

Cuatro palabras se confunden con facilidad.

Un **algoritmo** define un procedimiento. Un **programa** implementa ese procedimiento en un lenguaje concreto. Un **modelo** decide que aspectos del mundo se representan y cuales se ignoran. Una **decision** define por que la transformacion importa.

La diferencia no es academica. En medicina, un programa puede estar bien escrito y aun asi representar un modelo pobre. Un modelo puede ser estadisticamente elegante y aun asi apoyar una decision equivocada. Una decision puede ser razonable para poblacion general y peligrosa para un subgrupo.

Por eso la pregunta central no es "corre el codigo?". La pregunta madura es:

> Que decision, bajo que representacion del mundo, esta intentando ejecutar este algoritmo?

## Modelos mentales expertos

### 1. El algoritmo como contrato

Un algoritmo establece un contrato entre entrada, procedimiento y salida. Si la entrada cumple ciertas condiciones, el procedimiento promete una salida bajo reglas especificas. El contrato tambien define sus limites: que no sabe manejar, que datos requiere y cuando debe detenerse.

En medicina, esto cambia una decision real. Si un score de riesgo exige creatinina y edad, no se debe producir una recomendacion completa cuando esos datos faltan. El contrato esta incompleto.

### 2. El algoritmo como compresion de una decision

Un buen algoritmo comprime una decision compleja en una forma operable. Esa compresion no es neutral: conserva ciertas variables y descarta otras.

Ejemplo: clasificar fiebre por temperatura conserva un umbral y descarta contexto. Puede ser util, pero no equivale a evaluar sepsis, inmunosupresion o trayectoria clinica.

### 3. El algoritmo como estructura de representacion

Antes de calcular, el algoritmo decide como existe el problema dentro del sistema. Una secuencia genomica puede ser una cadena; una red metabolica puede ser un grafo; una imagen medica puede ser una matriz; una historia clinica puede ser texto estructurado.

El experto no pregunta solo "que algoritmo uso?", sino "que representacion hace visible el fenomeno que quiero estudiar?".

### 4. El algoritmo como maquina de errores posibles

Cada algoritmo abre una familia de errores. Puede fallar por entrada incorrecta, variable mal definida, regla insuficiente, sesgo de datos, mala calibracion, excepcion no contemplada o salida mal interpretada.

En dominios biomédicos, esta idea es central: un algoritmo no se evalua solo por aciertos promedio, sino por el tipo de error que puede producir y por las consecuencias de ese error.

### 5. El algoritmo como puente entre dominio y ejecucion

Un algoritmo serio no vive solo en la matematica ni solo en el codigo. Vive entre un dominio y una maquina. Su calidad depende de traducir correctamente conocimiento del dominio a operaciones ejecutables.

Ese puente es la razon de este libro. El medico que aprende algoritmos no esta aprendiendo "a programar por programar"; esta aprendiendo a hacer explicito un razonamiento en un medio que exige precision.

## Un ejemplo deliberadamente pequeno

Supongamos que queremos clasificar una temperatura corporal.

```python
temperatura_celsius = 38.4

if temperatura_celsius >= 38.0:
    estado_termico = "fiebre"
else:
    estado_termico = "sin fiebre"

print(estado_termico)
```

Este fragmento es simple, pero contiene la anatomia de un algoritmo.

Hay una entrada: `temperatura_celsius`. Hay una regla: comparar con `38.0`. Hay una bifurcacion: fiebre o no fiebre. Hay una salida: `estado_termico`. Y hay una decision conceptual escondida: aceptar un umbral.

El programa no sabe medicina. No sabe si la medicion fue axilar, oral, timpanica o rectal. No sabe la edad del paciente, el contexto clinico, el uso de antipireticos, el estado inmune ni la trayectoria temporal. Tampoco sabe si clasificar fiebre es suficiente o si la pregunta relevante era otra: riesgo de sepsis, indicacion de aislamiento, necesidad de hemocultivos, prioridad de atencion.

Ese es el punto. Un algoritmo no se vuelve inteligente por estar escrito en Python. Se vuelve util cuando la estructura de decision corresponde al problema real.

## De regla a modelo de decision

Podemos volver el ejemplo menos ingenuo:

```python
temperatura_celsius = 38.4
frecuencia_cardiaca = 118
presion_sistolica = 88

fiebre = temperatura_celsius >= 38.0
taquicardia = frecuencia_cardiaca >= 100
hipotension = presion_sistolica < 90

criterios_riesgo = []

if fiebre:
    criterios_riesgo.append("fiebre")

if taquicardia:
    criterios_riesgo.append("taquicardia")

if hipotension:
    criterios_riesgo.append("hipotension")

alto_riesgo = fiebre and (taquicardia or hipotension)

if alto_riesgo:
    conducta = "evaluacion_prioritaria"
else:
    conducta = "seguimiento_clinico"

print(conducta)
print(criterios_riesgo)
```

Seguimos ante una miniatura, no ante una escala clinica validada. Pero la estructura ya cambio. El algoritmo no clasifica un dato aislado; integra variables, crea conceptos intermedios, conserva razones y produce una conducta.

Esta diferencia es fundamental. Muchos programas fallan no porque la sintaxis sea incorrecta, sino porque la decision representada es pobre. El error profundo no esta en el `if`; esta en haber reducido un fenomeno complejo a una regla sin suficiente estructura.

## Correcto no significa suficiente

En ciencias de la computacion, un algoritmo puede evaluarse por correccion: produce la salida esperada para las entradas definidas. En medicina y ciencias de la vida, esa evaluacion es necesaria, pero incompleta.

Un algoritmo puede ser sintacticamente correcto y clinicamente irrelevante. Puede ser eficiente y biologicamente ingenuo. Puede ser reproducible y metodologicamente sesgado. Puede ser transparente y aun asi operar sobre datos pobres. Puede acertar en promedio y fallar justo en los casos donde mas importa.

Los informes sobre seguridad diagnostica insisten en que diagnosticar no es una etiqueta aislada, sino un proceso complejo de recoleccion, integracion e interpretacion de informacion. Esta idea debe acompanar cualquier algoritmo clinico: una salida computacional no equivale a comprension clinica.

## Tres tensiones criticas

### 1. Formalizacion vs juicio clinico

Formalizar permite auditar, programar y reproducir. Pero no todo juicio experto cabe en una regla simple. La tension no se resuelve negando el juicio ni rechazando el algoritmo. Se resuelve definiendo donde el algoritmo ayuda, donde advierte y donde debe dejar espacio a revision humana.

### 2. Simplicidad vs fidelidad al fenomeno

Un algoritmo simple puede ser robusto, explicable y facil de usar. Pero tambien puede borrar variables decisivas. Un algoritmo complejo puede capturar mas estructura, pero volverse opaco, fragil o dificil de validar.

La pregunta no es si la simplicidad es buena o mala. La pregunta es que costo paga el modelo por ser simple.

### 3. Automatizacion vs responsabilidad

Automatizar una decision cambia quien ve el error, quien lo interpreta y quien responde por sus consecuencias. En biomedicina, el algoritmo no elimina responsabilidad; la redistribuye.

Por eso este libro no estudiara algoritmos como ornamentos matematicos. Los tratara como instrumentos de conocimiento y accion.

## De aqui a la frontera

La misma idea de algoritmo que aparece en una regla de fiebre reaparece, con mayor sofisticacion, en problemas de frontera.

En bioinformatica, el alineamiento de secuencias usa programacion dinamica para comparar ADN, ARN o proteinas. En genomica moderna, los volumenes de datos exigen indices, grafos, modelos probabilisticos y aprendizaje automatico. En neurologia computacional, las senales y redes cerebrales requieren representaciones temporales, graficas y dinamicas. En medicina de precision, algoritmos y modelos convierten datos moleculares, clinicos e imagenologicos en hipotesis de estratificacion y tratamiento.

La escalera del libro sera esta: primero entenderemos que es una decision formalizable; despues aprenderemos estructuras y algoritmos clasicos; luego veremos como esas herramientas se transforman cuando el objeto ya no es un numero, sino un sistema vivo.

## Evaluar si entendiste

Estas preguntas buscan distinguir comprension de memorizacion.

1. Por que la definicion "serie finita de pasos" es correcta pero insuficiente?
2. En que se diferencia un algoritmo de un programa?
3. Que parte del mundo queda fuera cuando representas fiebre como `temperatura >= 38.0`?
4. Por que una salida correcta puede ser clinicamente insuficiente?
5. Como cambiaria el algoritmo de fiebre si el paciente fuera inmunosuprimido?
6. Que significa que un algoritmo tenga contrato?
7. Que errores nuevos aparecen cuando automatizas una decision?
8. Como se conecta el algoritmo de Euclides con la idea moderna de reduccion iterativa de problemas?
9. Por que la maquina de Turing importa para entender los limites de los algoritmos?
10. Como puede una misma idea algorítmica aparecer en triage, alineamiento genomico y redes biologicas?

## Bibliografia y fuentes

- Britannica. "Algorithm." <https://www.britannica.com/science/algorithm>
- Britannica. "Euclidean algorithm." <https://www.britannica.com/science/Euclidean-algorithm>
- Britannica. "Al-Khwarizmi." <https://www.britannica.com/biography/al-Khwarizmi>
- Computer History Museum. "A Brief History: Babbage Engine." <https://www.computerhistory.org/babbage/history/>
- Stanford Encyclopedia of Philosophy. "The Church-Turing Thesis." <https://plato.stanford.edu/archives/spr2021/entries/church-turing/>
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. *Introduction to Algorithms*, 4th ed. MIT Press, 2022. <https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/>
- National Academies of Sciences, Engineering, and Medicine. *Improving Diagnosis in Health Care*. National Academies Press, 2015. <https://doi.org/10.17226/21794>
- Berger, B., Peng, J., & Singh, M. "Computational solutions for omics data." *Nature Reviews Genetics* 14, 333-346 (2013). <https://www.nature.com/articles/nrg3433>
- Eddy, S. R. "What is dynamic programming?" *Nature Biotechnology* 22, 909-910 (2004). <https://doi.org/10.1038/nbt0704-909>
- Moor, M. et al. "Foundation models for generalist medical artificial intelligence." *Nature* 616, 259-265 (2023). <https://www.nature.com/articles/s41586-023-05881-4>

## Siguiente paso

Ahora podemos estudiar como pensar en pasos. Si un algoritmo es una decision formalizada, el siguiente problema es aprender a descomponer una situacion compleja sin destruir lo importante.
