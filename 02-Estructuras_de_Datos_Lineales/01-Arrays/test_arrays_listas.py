# Este archivo sirve para verificar el comportamiento de listas y tuplas
# usando afirmaciones (asserts). Si ninguna afirmación falla, el
# comportamiento es el esperado.

def test_list_operations():
    """Verifica las operaciones básicas de las listas."""
    # Creación y acceso
    frutas = ["manzana", "banana", "cereza"]
    assert frutas[0] == "manzana"
    assert len(frutas) == 3

    # Modificación
    frutas[1] = "arándano"
    assert frutas == ["manzana", "arándano", "cereza"]

    # Append (inserción al final)
    frutas.append("dátil")
    assert frutas == ["manzana", "arándano", "cereza", "dátil"]
    assert len(frutas) == 4

    # Insert (inserción en medio)
    frutas.insert(1, "banana")
    assert frutas == ["manzana", "banana", "arándano", "cereza", "dátil"]

    # Pop (eliminación del final)
    fruta_eliminada = frutas.pop()
    assert fruta_eliminada == "dátil"
    assert len(frutas) == 4

    # Pop (eliminación por índice)
    fruta_eliminada_indice = frutas.pop(0)
    assert fruta_eliminada_indice == "manzana"
    assert frutas == ["banana", "arándano", "cereza"]

    print("Todas las pruebas de listas pasaron exitosamente.")

def test_tuple_operations():
    """Verifica las operaciones básicas y la inmutabilidad de las tuplas."""
    # Creación y acceso
    rgb_color = (255, 0, 128)
    assert rgb_color[0] == 255
    assert len(rgb_color) == 3

    # Verificación de inmutabilidad
    try:
        rgb_color[0] = 100
        # Si esta línea se ejecuta, la prueba debe fallar
        assert False, "La tupla no debería ser mutable"
    except TypeError:
        # Se espera un TypeError, lo que significa que la tupla es inmutable
        assert True

    # Búsqueda
    assert 128 in rgb_color
    assert 100 not in rgb_color

    print("Todas las pruebas de tuplas pasaron exitosamente.")


# --- Ejecución de las "Pruebas" ---
# Al ejecutar este archivo, se llamarán a las funciones de prueba.
if __name__ == "__main__":
    test_list_operations()
    test_tuple_operations()
    print("\nComportamiento de listas y tuplas verificado.")
