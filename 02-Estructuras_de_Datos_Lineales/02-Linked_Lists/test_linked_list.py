# Para poder probar nuestra LinkedList, primero debemos importarla
from linked_list import LinkedList

def test_linked_list_operations():
    """Verifica las operaciones de la lista enlazada."""
    llist = LinkedList()

    # 1. Test Append
    llist.append("A")
    llist.append("B")
    llist.append("C")
    assert llist.head.data == "A"
    assert llist.head.next.data == "B"
    assert llist.head.next.next.data == "C"

    # 2. Test Prepend
    llist.prepend("Start")
    assert llist.head.data == "Start"
    assert llist.head.next.data == "A"

    # 3. Test Search
    assert llist.search("B") == True
    assert llist.search("D") == False

    # 4. Test Delete
    # Eliminar un nodo del medio
    llist.delete_node("B")
    assert llist.search("B") == False
    assert llist.head.next.next.data == "C" # A ahora apunta a C

    # Eliminar la cabeza
    llist.delete_node("Start")
    assert llist.head.data == "A"

    # Eliminar el final
    llist.delete_node("C")
    assert llist.head.next is None

    print("Todas las pruebas de la lista enlazada pasaron exitosamente.")

if __name__ == "__main__":
    test_linked_list_operations()