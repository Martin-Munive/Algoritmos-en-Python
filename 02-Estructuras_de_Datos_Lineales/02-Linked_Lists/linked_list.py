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