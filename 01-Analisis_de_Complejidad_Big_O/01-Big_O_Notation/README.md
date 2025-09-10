# Capítulo 1.01: Análisis de Complejidad - Un Día en Urgencias

## 1. El Problema: ¿Cómo Medimos la Eficiencia de un Hospital?

Imagina que eres el nuevo director de un hospital. Quieres saber si tus protocolos son eficientes. No te sirve de nada medir que "el Dr. Abreu tardó 10 minutos en atender a un paciente", porque ese tiempo depende de si el Dr. Abreu es rápido, si el paciente tenía un caso simple, o si el computador del hospital es lento.

Necesitas una forma de medir la **escalabilidad** de tus protocolos: ¿qué pasa con la carga de trabajo cuando, en lugar de 10 pacientes, llegan 100? ¿O 1000?

En ciencias de la computación, este es el propósito del **Análisis de Complejidad**. No medimos segundos, medimos cómo crece el número de operaciones a medida que aumenta el tamaño de la entrada (`n`).

## 2. El Escenario: Un Protocolo de Triaje

Nuestro escenario será una sala de urgencias. `n` es el número de pacientes en la sala de espera. Analizaremos la eficiencia de diferentes tareas.

### **Tarea 1: Atender al Paciente Crítico - Complejidad Constante O(1)**

**Protocolo:** *Si un paciente llega en ambulancia con código rojo (ej. paro cardíaco), se le asigna un box de reanimación de inmediato.*

*   **Análisis:** ¿Cuántas operaciones requiere este protocolo? Una: la asignación del box. ¿Este número de operaciones cambia si hay `n=5` pacientes en espera? No. ¿Y si hay `n=500`? Tampoco.
*   **Conclusión:** El tiempo de ejecución es **constante** e independiente del tamaño de `n`. Esto es una complejidad **O(1)**. Es el ideal de eficiencia.

```python
# En código, esto equivale a una operación directa
def asignar_box_critico(paciente):
    paciente.box = "Reanimación 1" # Una sola operación, no importa cuántos otros pacientes haya
```

### **Tarea 2: Ronda de Signos Vitales - Complejidad Lineal O(n)**

**Protocolo:** *Una enfermera debe pasar por cada uno de los `n` pacientes en la sala de espera para tomarles la temperatura.*

*   **Análisis:** Si hay `n=10` pacientes, la enfermera realiza 10 mediciones. Si la sala se llena y hay `n=50`, realiza 50 mediciones. El trabajo crece en una **relación directa y lineal** con el número de pacientes.
*   **Conclusión:** La complejidad es **O(n)**. Es un rendimiento muy común y aceptable para muchas tareas.

```python
# En código, esto equivale a un bucle simple
def tomar_temperaturas(pacientes_en_espera):
    for paciente in pacientes_en_espera: # El bucle se ejecuta 'n' veces
        paciente.tomar_temperatura()
```

### **Tarea 3: Búsqueda en Archivo Ordenado - Complejidad Logarítmica O(log n)**

**Protocolo:** *Un administrativo necesita encontrar el historial de un paciente en un archivo maestro de `n` expedientes, que está perfectamente ordenado por apellido.*

*   **Análisis:** El administrativo no empieza por la "A". Sabe que es más eficiente abrir el archivador por la mitad (letra "M").
    1.  Busca a "Pérez". Como "P" va después de "M", **descarta la primera mitad completa** del archivo.
    2.  Ahora solo tiene que buscar en la mitad restante. Vuelve a abrirla por la mitad (letra "T").
    3.  "P" va antes de "T", así que **descarta la segunda mitad de lo que quedaba**.
    Con cada paso, el tamaño del problema se reduce a la mitad. Incluso con un millón de expedientes, encontrará el correcto en unos 20 pasos (`2^20 ≈ 1,000,000`).
*   **Conclusión:** El trabajo crece de forma **logarítmica**. Aunque `n` se dispare, el tiempo de trabajo aumenta muy, muy lentamente. Esto es **O(log n)**, un rendimiento excepcionalmente bueno.

```python
# Esto es el algoritmo de Búsqueda Binaria, que veremos en detalle más adelante.
# Su eficiencia proviene de descartar la mitad del problema en cada paso.
```

## 3. El Diagnóstico Completo: Big O, Omega (Ω) y Theta (Θ)

Un buen diagnóstico no solo considera el peor resultado posible.

*   **Big O (O): El Peor Pronóstico (Cota Superior)**
    *   **Pregunta:** "¿Cuál es el **máximo** número de pacientes que tendré que revisar para encontrar a Juan Pérez en una lista desordenada?"
    *   **Respuesta:** En el peor caso, Juan es el último de la lista, así que tendrás que revisar a los `n` pacientes. El protocolo es **O(n)**. Big O nos da una garantía del peor escenario.

*   **Big Omega (Ω): El Mejor Pronóstico (Cota Inferior)**
    *   **Pregunta:** "¿Cuál es el **mínimo** número de pacientes que tendré que revisar?"
    *   **Respuesta:** En el mejor de los casos, Juan es el primero de la lista. Solo tienes que revisar a 1 paciente. El protocolo es **Ω(1)**. Omega nos da una garantía del mejor escenario.

*   **Big Theta (Θ): El Pronóstico Estable (Cota Ajustada)**
    *   **Pregunta:** "Nuestro protocolo de toma de temperaturas, ¿es predecible?"
    *   **Respuesta:** Para tomar la temperatura a todos, el mejor caso es que tienes que visitar a los `n` pacientes, y el peor caso también es que tienes que visitar a los `n` pacientes. Como el mejor (Ω) y el peor (O) escenario son iguales (`n`), decimos que el protocolo es **Θ(n)**. Su rendimiento es estable y predecible.

En la práctica, nos centramos en **Big O** porque en sistemas críticos (como el software médico), debemos diseñar para el peor escenario posible.

## 4. Relevancia Clínica y en Salud Digital

Entender la complejidad no es un ejercicio académico, es una cuestión de seguridad y eficiencia.
*   Un software para buscar historiales clínicos que use un algoritmo `O(n)` en lugar de `O(log n)` podría tardar minutos en lugar de milisegundos en un hospital grande, retrasando diagnósticos.
*   Un sistema de alerta en una UCI que analiza datos de pacientes con un algoritmo `O(n²)` podría fallar en detectar una crisis a tiempo si el número de pacientes aumenta.
*   La elección de la estructura de datos correcta, guiada por el análisis de complejidad, es un pilar fundamental en la construcción de software médico seguro y eficiente.
