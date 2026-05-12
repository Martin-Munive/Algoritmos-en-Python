# Auditoria de estructura heredada

## Proposito

Este documento registra solo la estructura tematica heredada del repositorio antes de la reconstruccion editorial. No reutiliza ni valida el contenido antiguo como texto final. La nueva edicion del libro se construye con `INMERSION CIENTIFICA`, bibliografia rastreable y una arquitectura editorial nueva.

## Estructura heredada detectada

### 00-Presaberes

- Introduccion a pruebas en Python.
- Formateo de cadenas con f-strings.
- Clases y programacion orientada a objetos.

### 01-Analisis_de_Complejidad_Big_O

- Notacion Big O, Omega y Theta.

### 02-Estructuras_de_Datos_Lineales

- Arrays, listas y tuplas.
- Listas enlazadas.
- Codigo demostrativo y pruebas asociadas.

## Valor estructural

La estructura antigua aporta una pista util sobre temas que el libro debe cubrir, pero no define el orden final ni la profundidad final. Debe tratarse como mapa de posibles estaciones, no como indice vigente.

## Temas que conviene vincular en la nueva arquitectura

1. **Pruebas y verificacion.** Deben vincularse con seguridad del calculo, reproducibilidad, software medico responsable y auditoria de decisiones.
2. **F-strings y salida de informacion.** Deben aparecer como recurso tecnico puntual cuando el libro trabaje reportes, trazabilidad y comunicacion de resultados.
3. **Programacion orientada a objetos.** Debe reservarse para modelos, entidades clinicas, estructuras de datos y sistemas mas complejos; no corresponde al arranque conceptual.
4. **Complejidad Big O/Omega/Theta.** Debe convertirse en un capitulo fuerte posterior, conectado con costo computacional, triage, busqueda, genomas, sistemas hospitalarios y escalabilidad.
5. **Arrays, listas y tuplas.** Deben integrarse en la unidad de estructuras de datos para ciencias de la vida, con ejemplos de signos vitales, tablas, series, matrices e imagen biomédica.
6. **Listas enlazadas.** Deben tratarse como estructura historica y conceptual para entender punteros, memoria, colas, pilas y flujos; no como prioridad inicial.

## Temas que no deben vincularse como capitulos independientes

- F-strings.
- Presaberes aislados sin problema biomedico.
- Clases y POO mientras no exista una necesidad estructural clara.

## Decision operativa aceptada

No restaurar carpetas antiguas en la rama activa.

Usar la estructura heredada para enriquecer el indice maestro y decidir destinos tematicos, pero redactar cada seccion desde cero con el estandar actual del proyecto.

## Vinculacion acordada por destino

| Tema heredado | Destino editorial | Forma de integracion |
| --- | --- | --- |
| Presaberes de Python | Front Matter: `Presaberes mínimos` | Guia breve de orientacion, no capitulo numerado. |
| Pruebas | Capitulo futuro sobre verificacion, seguridad del calculo y software medico responsable | Redaccion nueva con ejemplos biomédicos y pruebas ejecutables. |
| F-strings | Secciones donde aparezcan reportes, trazabilidad y salida de resultados | Recurso tecnico puntual, no tema independiente. |
| Programacion orientada a objetos | Capitulo futuro sobre modelos, entidades, reglas y sistemas | Solo cuando exista una necesidad estructural clara. |
| Big O, Omega y Theta | Unidad de algoritmos clasicos y costo clinico-operativo | Capitulo fuerte con `INMERSION CIENTIFICA`. |
| Arrays, listas y tuplas | Unidad de estructuras de datos para ciencias de la vida | Secciones sobre representacion, signos vitales, tablas, series y matrices. |
| Listas enlazadas | Unidad de estructuras lineales, memoria y flujos | Tema conceptual posterior; no prioridad inicial. |

## Decision sobre presaberes

Los presaberes no deben convertirse en el capitulo 1. Hacerlo moveria el centro del libro hacia un curso introductorio de Python y debilitaria la entrada intelectual de la obra.

La solucion adoptada es crear una pagina de Front Matter llamada **Presaberes mínimos**. Esa pagina ayuda al lector primerizo a no perderse, pero mantiene el primer capitulo real como **El lenguaje de las decisiones**.

## Punto actual del libro

La reconstruccion esta trabajando el primer capitulo real: **El lenguaje de las decisiones**.

Sus secciones actuales son:

1. Que es un algoritmo.
2. Pensar en pasos.
3. Variables, datos y decisiones.

Esta lista no esta cerrada. El capitulo debe crecer si la arquitectura intelectual lo exige. Candidatos razonables:

- estados y transiciones;
- condiciones y umbrales;
- excepciones y datos faltantes;
- trazabilidad de decisiones;
- del razonamiento clinico al flujo computable.
