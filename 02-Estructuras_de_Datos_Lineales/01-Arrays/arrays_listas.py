# --- Demostración de Listas (Arrays Dinámicos y Mutables) ---

print("--- LISTAS ---")

# 1. Creación
tareas = ["Lavar ropa", "Estudiar Python", "Hacer ejercicio"]
print(f"Lista inicial de tareas: {tareas}")

# 2. Acceso por Índice (O(1))
primera_tarea = tareas
print(f"La primera tarea es (O(1)): {primera_tarea}")

# 3. Modificación (Mutabilidad)
tareas[0] = "Lavar los platos"
print(f"Lista con la primera tarea modificada: {tareas}")

# 4. Inserción al final (O(1) amortizado)
tareas.append("Leer un libro")
print(f"Lista después de añadir una tarea al final (append): {tareas}")

# 5. Inserción en una posición específica (O(n))
# Todos los elementos desde el índice 1 se desplazan a la derecha
tareas.insert(1, "Pasear al perro")
print(f"Lista después de insertar en el índice 1 (insert): {tareas}")

# 6. Eliminación del final (O(1))
ultima_tarea_eliminada = tareas.pop()
print(f"Se eliminó la última tarea: '{ultima_tarea_eliminada}'. Lista actual: {tareas}")

# 7. Eliminación de una posición específica (O(n))
# Todos los elementos desde el índice 1 se desplazan a la izquierda
primera_tarea_eliminada = tareas.pop(0)
print(f"Se eliminó la primera tarea: '{primera_tarea_eliminada}'. Lista actual: {tareas}")

# 8. Búsqueda por valor (O(n))
if "Estudiar Python" in tareas:
    print("Sí, 'Estudiar Python' está en la lista de tareas.")

# 9. Iteración
print("Tareas pendientes:")
for tarea in tareas:
    print(f"- {tarea}")


# --- Demostración de Tuplas (Arrays Estáticos e Inmutables) ---

print("\n--- TUPLAS ---")

# 1. Creación
# Las coordenadas son un buen caso de uso para tuplas, ya que no deberían cambiar.
coordenadas = (10.0, 25.5, -5.0)
print(f"Coordenadas iniciales: {coordenadas}")

# 2. Acceso por Índice (O(1))
coordenada_x = coordenadas
print(f"La coordenada X es (O(1)): {coordenada_x}")

# 3. Inmutabilidad (Intentar modificarla dará un error)
try:
    coordenadas = 15.0
except TypeError as e:
    print(f"Error al intentar modificar una tupla: {e}")

# 4. Búsqueda por valor (O(n))
if -5.0 in coordenadas:
    print("Sí, el valor -5.0 existe en las coordenadas.")

# 5. Iteración
print("Valores de las coordenadas:")
for valor in coordenadas:
    print(f"- {valor}")