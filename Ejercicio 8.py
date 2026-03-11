import numpy as np

# Configuración de 3 dígitos decimales según pedido
np.set_printoptions(precision=3, suppress=True)

# a) Ingreso de datos
# Copia esto al ejecutar: [[1, 1, -1], [-2, 1, 1], [1, 1, 2]]
print("Ingrese la matriz A (ejemplo: [[1,1,-1],[-2,1,1],[1,1,2]]):")
A = np.array(eval(input()), dtype=float)

# Copia esto al ejecutar: [1, 3, 2]
print("Ingrese el vector b (ejemplo: [1,3,2]):")
b = np.array(eval(input()), dtype=float).reshape(3, 1)

# Crear matriz aumentada [A|b]
Ab = np.hstack([A, b])

# --- PROCESO DE ELIMINACIÓN GAUSS-JORDAN (Sin bucles) ---

# Paso 1: Eliminar x de fila 2 y 3
Ab[1] = Ab[1] - (Ab[1,0] / Ab[0,0]) * Ab[0]
Ab[2] = Ab[2] - (Ab[2,0] / Ab[0,0]) * Ab[0]

# Paso 2: Normalizar pivote de fila 2 y eliminar y de fila 3
Ab[2] = Ab[2] - (Ab[2,1] / Ab[1,1]) * Ab[1]

# Paso 3: Eliminar hacia arriba (Jordan)
Ab[1] = Ab[1] - (Ab[1,2] / Ab[2,2]) * Ab[2]
Ab[0] = Ab[0] - (Ab[0,2] / Ab[2,2]) * Ab[2]
Ab[0] = Ab[0] - (Ab[0,1] / Ab[1,1]) * Ab[1]

# Paso 4: Normalizar todos los pivotes a 1
Ab[0] = Ab[0] / Ab[0,0]
Ab[1] = Ab[1] / Ab[1,1]
Ab[2] = Ab[2] / Ab[2,2]

# b) Separar resultados y mostrar
x_sol = Ab[:, 3]
print("\n--- MATRIZ AUMENTADA FINAL ---")
print(Ab)
print("\n--- RESULTADOS ---")
print(f"Solución x: {x_sol[0]:.3f}")
print(f"Solución y: {x_sol[1]:.3f}")
print(f"Solución z: {x_sol[2]:.3f}")

# Verificación automática
print("\n--- VERIFICACIÓN (A * x) ---")
print(np.dot(A, x_sol))
