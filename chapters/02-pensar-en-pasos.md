# Pensar en pasos

Programar no empieza escribiendo codigo. Empieza haciendo una operacion mucho mas exigente: convertir una situacion confusa en una secuencia de decisiones examinables.

Un principiante cree que pensar en pasos es enumerar acciones. Un experto sabe que la secuencia es solo la superficie. Debajo hay una arquitectura: que se observa primero, que se descarta, que se conserva, que se mide, que se interpreta, que se hace si aparece una excepcion y que evidencia autoriza pasar al siguiente estado.

En medicina esto es evidente. Un medico no evalua a un paciente como una masa indiferenciada de datos. Ordena. Pregunta por motivo de consulta, identifica signos de alarma, ubica antecedentes relevantes, examina, formula hipotesis, decide pruebas, interpreta resultados y actua. Ese orden no es decorativo. Reduce incertidumbre, protege memoria de trabajo y evita que una decision se adelante a la evidencia.

Un algoritmo hace algo parecido: transforma intuicion en procedimiento revisable.

## Origen historico: del metodo al procedimiento verificable

La idea de pensar en pasos no nacio con Python ni con los computadores personales. Es mucho mas antigua. El algoritmo de Euclides, descrito en *Elementos*, ya mostraba una intuicion poderosa: un problema matematico podia resolverse mediante una secuencia finita de operaciones repetibles. Siglos despues, Al-Juarismi sistematizo procedimientos aritmeticos y algebraicos cuyo nombre latinizado termino asociado a la palabra "algoritmo".

En el siglo XX, la pregunta se volvio mas radical. Turing no solo pregunto como resolver un calculo, sino que tipo de procedimiento podia considerarse mecanicamente ejecutable. Esa transicion importa porque separa dos niveles: una explicacion humana puede ser convincente, pero un procedimiento computable debe ser lo bastante explicito para ejecutarse sin intuicion tacita.

En medicina ocurre algo paralelo. Las listas de verificacion quirurgica de la OMS y los esquemas de triage no intentan reemplazar el juicio clinico; intentan convertir momentos de alto riesgo en secuencias visibles, auditables y menos dependientes de memoria, fatiga o improvisacion. El dato historico importante es este: la formalizacion por pasos no empobrece necesariamente el pensamiento experto. Bien disenada, lo protege de sus propios puntos ciegos.

## El paso no es una frase: es una unidad de decision

Una instruccion como esta parece clara:

```text
Evalua si el paciente esta grave.
```

Pero para un algoritmo no significa casi nada. No define variables, umbrales, excepciones, salida, prioridad ni criterio de terminacion. Un humano podria apoyarse en experiencia tacita. Un programa no.

Una formulacion mas algorítmica seria:

```text
1. Medir estado de conciencia.
2. Medir presion arterial sistolica.
3. Medir frecuencia respiratoria.
4. Medir saturacion de oxigeno.
5. Identificar signos de choque, dificultad respiratoria o alteracion neurologica.
6. Si algun criterio de emergencia esta presente, clasificar como alto riesgo.
7. Si no hay criterio de emergencia, evaluar criterios de prioridad.
8. Registrar clasificacion y motivo.
```

Todavia falta validar los umbrales, ajustar poblaciones, definir excepciones y decidir que escala usar. Pero el pensamiento ya cambio. La gravedad dejo de ser una impresion global y empezo a convertirse en una estructura.

## Definicion de trabajo

Pensar en pasos no significa partir una tarea en frases pequenas. Significa construir una trayectoria controlada desde un estado inicial hasta un estado final, especificando que informacion se observa, que transformaciones se permiten, que condiciones autorizan avanzar, que excepciones interrumpen el proceso y que evidencia debe quedar registrada.

En un contexto biomedico, esa definicion exige mas que orden. Exige prioridad. No todas las preguntas valen lo mismo cuando el tiempo, el riesgo y la incertidumbre son desiguales.

## Modelos mentales expertos

### 1. Separar observacion, interpretacion y accion

El experto no mezcla dato bruto con decision final. Primero distingue que se observo, luego que significa y finalmente que conducta se justifica. Este modelo aparece en el proceso diagnostico descrito por las National Academies, donde la informacion se recolecta, integra e interpreta antes de tomar decisiones clinicas, y tambien en ETAT, donde los signos de emergencia preceden a la intervencion.

Ejemplo: una saturacion de 88% no es por si sola "neumonia grave". Es un dato. Su interpretacion depende de contexto, tecnica de medicion, edad, enfermedad previa y signos asociados. La accion puede ser oxigeno, traslado, monitorizacion o busqueda de causa.

### 2. Convertir ambiguedad en estados

Un sistema experto no intenta resolver todo en una sola frase. Define estados intermedios: no evaluado, estable, prioridad, emergencia, pendiente de dato, excepcion. Esta forma de pensar conecta con la teoria algorítmica clasica, que exige estados, entrada, salida y terminacion, y con la practica clinica, que distingue pacientes no evaluados de pacientes realmente estables.

Ejemplo: un paciente sin presion arterial registrada no debe entrar automaticamente en "bajo riesgo". Debe entrar en un estado diferente: `dato_pendiente` o `evaluacion_incompleta`.

### 3. Priorizar riesgos antes que comodidad computacional

En salud, el orden de los pasos no se decide solo por elegancia tecnica. Se decide por consecuencias. ETAT clasifica rapido a los ninos con signos de emergencia porque el retraso cambia el desenlace. En cirugia, las listas de verificacion colocan puntos criticos antes de la incision y antes de salir del quirofano porque el momento de la pregunta modifica su valor.

Ejemplo: en una interfaz clinica, preguntar alergias antes de recomendar un medicamento no es una preferencia de formulario. Es una restriccion de seguridad.

### 4. Hacer visibles las excepciones

El pensamiento ingenuo disena el caso promedio. El pensamiento experto pregunta que rompe la regla. En programacion, una excepcion no es un estorbo: es informacion sobre los limites del modelo. En diagnostico, Croskerry ha insistido en que muchos errores no provienen de falta de datos, sino de fallas cognitivas, sesgos y heuristicas mal controladas.

Ejemplo: una regla para fiebre basada en `temperatura >= 38` puede fallar en inmunosuprimidos, ancianos, pacientes con antipireticos o mediciones poco confiables. El algoritmo debe permitir advertir ese limite.

### 5. Diseñar para revision

Un procedimiento serio deja huellas. Si una clasificacion aparece, debe poder responder: que datos la produjeron, que regla se aplico, que excepciones se ignoraron, que paso falto y que version del criterio estaba vigente.

Ejemplo: "alto riesgo" no basta. Un sistema util debe registrar: `alto_riesgo_por = ["hipotension", "taquicardia", "fiebre"]`.

## Donde se solapan

Estos modelos mentales se refuerzan mutuamente. Separar observacion, interpretacion y accion ayuda a convertir ambiguedad en estados. Definir estados permite capturar excepciones. Capturar excepciones facilita auditoria. Auditar obliga a priorizar riesgos de forma explicita.

El meta-modelo que los engloba es este:

> Pensar en pasos es disenar una trayectoria verificable desde datos incompletos hasta una decision responsable.

## Donde crean tension

Tambien hay tensiones. Un libro serio no debe ocultarlas.

Un algoritmo muy detallado puede ser mas seguro, pero mas lento de usar. Un triage muy sensible puede detectar mas emergencias, pero sobrecargar el sistema. Un procedimiento muy flexible puede respetar contexto, pero volverse dificil de auditar. Una regla simple puede ser rapida, pero pobre ante pacientes complejos.

La madurez consiste en reconocer que no existe "el paso correcto" en abstracto. Existe un orden defendible para un objetivo, un contexto, un riesgo y una poblacion.

## De procedimiento humano a codigo

Podemos traducir una miniatura del razonamiento anterior a Python:

```python
estado_conciencia_alterado = False
presion_sistolica = 88
frecuencia_respiratoria = 32
saturacion_oxigeno = 89

criterios_emergencia = []

if estado_conciencia_alterado:
    criterios_emergencia.append("alteracion del estado de conciencia")

if presion_sistolica < 90:
    criterios_emergencia.append("hipotension")

if frecuencia_respiratoria > 30:
    criterios_emergencia.append("taquipnea severa")

if saturacion_oxigeno < 90:
    criterios_emergencia.append("hipoxemia")

if criterios_emergencia:
    clasificacion = "alto riesgo"
else:
    clasificacion = "evaluacion no urgente"

print(clasificacion)
print(criterios_emergencia)
```

Este codigo sigue siendo una simplificacion. No es una guia clinica. No reemplaza una escala validada. Pero ya muestra una diferencia decisiva: la salida no aparece sola. Viene acompañada de razones.

Ese cambio es enorme. Un algoritmo que da una respuesta sin razones puede servir para automatizar. Un algoritmo que conserva razones puede servir para aprender, auditar y mejorar.

## Argumentos criticos

### Desacuerdo 1: rapidez contra exhaustividad

Pregunta: debe un algoritmo clinico pedir muchos datos para ser mas preciso o pocos datos para actuar rapido?

El argumento por rapidez es fuerte en triage: muchas muertes tempranas se previenen identificando signos de emergencia de inmediato, como enfatiza la estrategia ETAT de la OMS para clasificar y tratar ninos gravemente enfermos al ingreso. El argumento por exhaustividad es fuerte en diagnostico: las National Academies describen el diagnostico como un proceso complejo de recoleccion, integracion e interpretacion de informacion.

Importa porque un sistema demasiado lento puede fallar en urgencias, pero uno demasiado simple puede pasar por alto diagnosticos complejos.

Consenso emergente: no hay una unica profundidad correcta. La granularidad debe depender de riesgo, tiempo disponible, consecuencias del falso negativo, carga operativa y posibilidad de reevaluacion.

### Desacuerdo 2: reglas explicitas contra juicio experto

Pregunta: cuanto debe formalizarse y cuanto debe dejarse al criterio clinico?

Las reglas explicitas permiten reproducibilidad, auditoria y programacion. El juicio experto permite reconocer patrones, excepciones y contexto que la regla no captura. El conflicto no se resuelve eliminando uno de los lados. Se resuelve disenando algoritmos que hagan explicito su alcance y permitan intervencion humana cuando la situacion excede el modelo.

Consenso emergente: los procedimientos explicitos son especialmente utiles en tareas repetibles, de alto riesgo y sensibles a omisiones; pero deben declarar sus limites y no fingir que todo juicio clinico cabe en una regla.

### Desacuerdo 3: algoritmo como respuesta contra algoritmo como instrumento

Pregunta: el algoritmo debe entregar una decision final o estructurar mejor el pensamiento?

En sistemas de bajo riesgo, puede bastar una salida automatica. En medicina, con frecuencia el mayor valor del algoritmo no es sustituir al clinico, sino ordenar informacion, revelar omisiones y hacer visible la razon de una recomendacion. Esta distincion sera central en todo el libro.

Consenso emergente: en dominios biomedicos, el algoritmo mas valioso no siempre es el que decide por el humano, sino el que mejora la calidad de la representacion, reduce omisiones y permite revisar el razonamiento.

## Puente hacia la frontera

La capacidad de pensar en pasos sera indispensable cuando el libro avance hacia problemas mas exigentes.

En bioinformatica, un alineamiento de secuencias no es una comparacion intuitiva entre cadenas de ADN. Es una secuencia de decisiones sobre coincidencias, penalizaciones, brechas, costo y optimizacion. En neurologia computacional, analizar una senal electrofisiologica exige decidir ventanas temporales, filtros, artefactos, rasgos y estados. En medicina de precision, un sistema no puede limitarse a "predecir riesgo"; debe mostrar que datos uso, que supuestos hizo, que incertidumbre conserva y que accion es defendible.

Por eso esta seccion no es un tema menor de introduccion. Es la gramatica inicial de todo procedimiento cientifico computable.

## Evaluar si entendiste

Estas preguntas no buscan memoria. Buscan criterio. Estan ordenadas de mayor a menor dificultad.

1. Como disenarias un algoritmo que distinga entre "paciente estable" y "evaluacion incompleta" sin convertir la ausencia de datos en falsa tranquilidad?
2. En que circunstancias una regla mas simple puede ser epistemicamente mas honesta y clinicamente mas segura que un modelo mas complejo?
3. Como cambiaria tu secuencia de pasos si el objetivo no fuera diagnosticar, sino evitar muertes prevenibles en los primeros minutos de atencion?
4. Que informacion minima necesitarias registrar para que una clasificacion de alto riesgo sea auditable seis meses despues?
5. Donde trazarias el limite entre una excepcion que debe codificarse y una excepcion que debe escalarse a juicio humano?
6. Como distinguirias dato, interpretacion y accion en un sistema de triage, y que dano produce mezclarlos?
7. Que tension aparece entre sensibilidad y carga operativa en un sistema de alerta hospitalario?
8. Por que una lista de verificacion puede fracasar si se implementa como ritual y no como arquitectura de decision?
9. Que excepciones deberia contemplar una regla basada en temperatura corporal?
10. Como sabrias si un ejemplo introductorio esta simplificando de forma pedagogica o deformando el problema?

## Vacios de comprension que debes vigilar

1. Confundir orden narrativo con estructura algorítmica. Que una explicacion suene ordenada no significa que sea ejecutable, auditable o segura.
2. Confundir dato faltante con dato normal. En medicina y ciencia, lo no medido no debe entrar silenciosamente como normalidad.
3. Confundir automatizacion con inteligencia. Un sistema que produce una salida sin razones puede acelerar una mala decision.

## Orden de estudio para las proximas 3 horas

1. **Primera hora:** releer esta seccion y reescribir el ejemplo de triage separando observacion, interpretacion y accion.
2. **Segunda hora:** estudiar el proceso diagnostico de las National Academies y compararlo con ETAT: que pasos aparecen en ambos y cuales cambian por el contexto.
3. **Tercera hora:** implementar una version pequena del algoritmo con estados `dato_pendiente`, `alto_riesgo`, `prioridad` y `no_urgente`, registrando siempre la razon de la salida.

## Bibliografia y fuentes

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. *Introduction to Algorithms*, 4th ed. MIT Press, 2022. <https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/>
- National Academies of Sciences, Engineering, and Medicine. *Improving Diagnosis in Health Care*. National Academies Press, 2015. <https://www.ncbi.nlm.nih.gov/books/NBK338596/>
- National Academies of Sciences, Engineering, and Medicine. "The Diagnostic Process", en *Improving Diagnosis in Health Care*. 2015. <https://www.ncbi.nlm.nih.gov/books/NBK338593/>
- World Health Organization. *Emergency Triage Assessment and Treatment (ETAT) course*. 2005. <https://www.who.int/publications/i/item/9241546875>
- Haynes, A. B., et al. "A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population." *New England Journal of Medicine*, 2009;360:491-499. Reproducido en WHO Guidelines for Safe Surgery 2009. <https://www.ncbi.nlm.nih.gov/books/NBK143241/>
- Weiser, T. G., & Haynes, A. B. "Ten years of the Surgical Safety Checklist." *British Journal of Surgery*, 2018;105(8):927-929. <https://pubmed.ncbi.nlm.nih.gov/29770959/>
- Croskerry, P. "Cognitive forcing strategies in clinical decisionmaking." *Annals of Emergency Medicine*, 2003;41(1):110-120. <https://pubmed.ncbi.nlm.nih.gov/12514691/>
- Croskerry, P. "Clinical cognition and diagnostic error: applications of a dual process model of reasoning." *Advances in Health Sciences Education*, 2009;14 Suppl 1:27-35. <https://pubmed.ncbi.nlm.nih.gov/19669918/>

## Siguiente paso

Ahora podemos estudiar variables, datos y decisiones con mas precision: no como nombres para valores, sino como una teoria practica de representacion. Nombrar una variable es decidir que parte del mundo merece existir dentro del programa.
