import numpy as np

# Configuración a 3 decimales
np.set_printoptions(precision=3, suppress=True)

# Datos del Problema 11
A = np.array([[1, 1, 1], [1, -1, 2], [1, -1, -3]], dtype=float)
b = np.array([6, 5, -10], dtype=float).reshape(3, 1)

# Matriz aumentada
Ab = np.hstack([A, b])

# --- PROCESO MANUAL PASO A PASO ---
# Limpiar columna 0
Ab[1] = Ab[1] - (Ab[1,0]/Ab[0,0]) * Ab[0]
Ab[2] = Ab[2] - (Ab[2,0]/Ab[0,0]) * Ab[0]

# Limpiar columna 1
Ab[2] = Ab[2] - (Ab[2,1]/Ab[1,1]) * Ab[1]
Ab[0] = Ab[0] - (Ab[0,1]/Ab[1,1]) * Ab[1]

# Limpiar columna 2
Ab[0] = Ab[0] - (Ab[0,2]/Ab[2,2]) * Ab[2]
Ab[1] = Ab[1] - (Ab[1,2]/Ab[2,2]) * Ab[2]

# Normalizar pivotes a 1
Ab[0] = Ab[0] / Ab[0,0]
Ab[1] = Ab[1] / Ab[1,1]
Ab[2] = Ab[2] / Ab[2,2]

# b) Mostrar resultados
x_sol = Ab[:, 3]
print("--- MATRIZ ESCALONADA REDUCIDA ---")
print(Ab)
print("\n--- SOLUCIONES ---")
print(f"x = {x_sol[0]:.3f}")
print(f"y = {x_sol[1]:.3f}")
print(f"z = {x_sol[2]:.3f}")
