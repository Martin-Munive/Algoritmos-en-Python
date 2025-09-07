# Capítulo 2.02: Listas Enlazadas (Linked Lists)

## 1. Historia y Contexto

Las listas enlazadas fueron desarrolladas en 1955-1956 por Allen Newell, Cliff Shaw y Herbert A. Simon en la RAND Corporation como la principal estructura de datos para su lenguaje de procesamiento de información (IPL). Mientras que los arrays requerían reservar un bloque de memoria contiguo y de tamaño fijo (un gran problema para las computadoras primitivas con memoria limitada), las listas enlazadas ofrecían una solución flexible. Podían almacenar datos en cualquier lugar disponible de la memoria, creando una estructura dinámica que podía crecer y encogerse con facilidad. Esta flexibilidad fue fundamental para el desarrollo de los primeros sistemas de inteligencia artificial.

## 2. Descripción Intuitiva y Analogía

Si un array es un pastillero, una lista enlazada es una **búsqueda del tesoro**.

*   **El `head` (la cabeza):** Tienes la primera pista. Esta es la única que necesitas saber para empezar.
*   **El `Node` (el nodo):** Cada pista es un "nodo". Un nodo contiene dos cosas:
    1.  **El dato:** El tesoro o la información que hay en esa parada (ej: "manzana").
    2.  **El puntero `next`:** La ubicación de la siguiente pista (ej: "la siguiente pista está debajo del puente").
*   **El final de la lista:** La última pista no apunta a ningún sitio. Su puntero `next` es `None` (Nulo), indicando que la búsqueda ha terminado.

La gran diferencia con un array es que no puedes saltar directamente a la tercera pista. **Debes seguir las pistas en orden**: empezar por la cabeza, ir a la segunda, y de ahí a la tercera.

## 3. Implementación en Python

Para implementar una lista enlazada, necesitamos dos "planos" o clases:

1.  **Clase `Node`:** Representa una única pista. Tiene dos atributos: `data` (el valor que almacena) y `next` (una referencia al siguiente objeto `Node`).
2.  **Clase `LinkedList`:** Representa la búsqueda del tesoro completa. Su único atributo esencial es `head`, que almacena el primer `Node` de la cadena. Esta clase contendrá los métodos para manipular la lista (añadir, eliminar, buscar, etc.).

## 4. Análisis de Rendimiento (Big O)

Aquí es donde las listas enlazadas brillan y flaquean en comparación con los arrays.

| Operación | Complejidad | Explicación |
| :--- | :--- | :--- |
| **Acceso por Índice (k-ésimo elemento)** | **O(n)** | Es la mayor debilidad. Para llegar al 5º elemento, debes empezar por la cabeza y seguir 4 punteros `next`. |
| **Búsqueda por Valor** | **O(n)** | Igual que en un array, en el peor caso debes recorrer toda la lista. |
| **Inserción/Eliminación (al inicio)** | **O(1)** | **¡Su superpoder!** Para añadir un nuevo elemento al principio, solo necesitas crear un nodo y reajustar 2 punteros. No hay que desplazar ningún otro elemento. |
| **Inserción/Eliminación (al final)** | **O(n)** | Para añadir al final, primero debes recorrer toda la lista para encontrar el último nodo. (Esto puede optimizarse a O(1) si la clase `LinkedList` también guarda una referencia a la cola `tail`). |
| **Inserción/Eliminación (en medio)** | **O(n)** | Primero debes recorrer la lista hasta la posición deseada (O(n)) y luego realizar la operación de reajuste de punteros (O(1)). El coste dominante es la búsqueda. |

**Conclusión:** Usa un **Array** cuando necesites acceso rápido por índice. Usa una **Lista Enlazada** cuando vayas a realizar muchas inserciones y eliminaciones al principio de la colección.

## 5. Código de Ejemplo (`linked_list.py`)

A continuación, se muestra el código que implementa las clases `Node` y `LinkedList` y demuestra sus operaciones.

```python
# --- Demostración de las clases `Node` y `LinkedList` ---
class Node:
    """
    Un objeto para almacenar un único nodo de una lista enlazada.
    Modela dos atributos: 'data' para almacenar el valor y 'next' para
    almacenar una referencia al siguiente nodo en la cadena.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Modela la lista enlazada completa.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """Añade un nodo al final de la lista."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Añade un nodo al principio de la lista."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        """Elimina un nodo por su valor (key)."""
        current_node = self.head

        # Si el nodo a eliminar es la cabeza
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        # Buscar el nodo a eliminar manteniendo una referencia al anterior
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        # Si la clave no está en la lista
        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None

    def search(self, key):
        """Busca un nodo por su valor y devuelve si lo encontró."""
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

    def display(self):
        """Muestra los elementos de la lista."""
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(elements) + " -> None")

# --- Demostración de Uso ---
if __name__ == "__main__":
    llist = LinkedList()
    
    # Añadir elementos
    llist.append("Manzana")
    llist.append("Banana")
    
    print("Lista Enlazada inicial:")
    llist.display()
    
    # Añadir al final
    llist.append("Cereza")
    print("Añadiendo 'Cereza' al final (append):")
    llist.display()
    
    # Añadir al principio
    llist.prepend("Dátil")
    print("Añadiendo 'Dátil' al principio (prepend):")
    llist.display()
    
    # Eliminar un nodo
    llist.delete_node("Manzana")
    print("Eliminando 'Manzana':")
    llist.display()
    
    # Buscar un nodo
    print("Buscando 'Banana':", end=" ")
    if llist.search("Banana"):
        print("Nodo encontrado.")
    else:
        print("Nodo no encontrado.")
        
    print("Buscando 'Fresa':", end=" ")
    if llist.search("Fresa"):
        print("Nodo encontrado.")
    else:
        print("Nodo no encontrado.")

```

### 5.1. Salida de Ejemplo de Ejecución

Al ejecutar el script `linked_list.py`, esta es la salida que se produce en la consola:

```console
Lista Enlazada inicial:
Manzana -> Banana -> None
Añadiendo 'Cereza' al final (append):
Manzana -> Banana -> Cereza -> None
Añadiendo 'Dátil' al principio (prepend):
Dátil -> Manzana -> Banana -> Cereza -> None
Eliminando 'Manzana':
Dátil -> Banana -> Cereza -> None
Buscando 'Banana': Nodo encontrado.
Buscando 'Fresa': Nodo no encontrado.
```

## 6. Aplicaciones en el Mundo Real

*   **Historial del Navegador:** El botón "Atrás" es una implementación perfecta de una lista enlazada. Cada página es un nodo que apunta a la página anterior.
*   **Listas de Reproducción de Música:** Cada canción es un nodo que apunta a la siguiente. Es fácil reorganizar la lista (mover una canción) o añadir una nueva al principio ("Siguiente a reproducir").
*   **Implementación de Stacks y Queues:** Las listas enlazadas son una forma muy natural y eficiente de implementar estas otras estructuras de datos.
*   **Manejo de Memoria:** Los sistemas operativos usan listas enlazadas para llevar un registro de los bloques de memoria libres y ocupados.

## 7. Referencias y Lecturas Adicionales

1.  Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press. (Capítulo 10.2: Linked lists).
