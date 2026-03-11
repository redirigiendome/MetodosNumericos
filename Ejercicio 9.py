import numpy as np

# Configuración de 5 dígitos decimales
np.set_printoptions(precision=5, suppress=True)

# a) Ingreso de datos
n = int(input("Ingrese el número de ecuaciones (n): "))
print("Ingrese la matriz A (ej: [[1,1,1],[2,1,1],[1,1,-2]]):")
A = np.array(eval(input()), dtype=float)
print("Ingrese el vector b (ej: [1,2,3]):")
b = np.array(eval(input()), dtype=float).reshape(n, 1)

# Crear matriz aumentada
Ab = np.hstack([A, b])

# --- PROCESO DE GAUSS-JORDAN MANUAL (Sin bucles for) ---
# Nota: Se realiza paso a paso para cumplir con la restricción de estructuras de control

# Fila 1 como pivote para limpiar columna 0
Ab[1] = Ab[1] - (Ab[1,0]/Ab[0,0]) * Ab[0]
Ab[2] = Ab[2] - (Ab[2,0]/Ab[0,0]) * Ab[0]

# Fila 2 como pivote para limpiar columna 1 y 2
# (Como Ab[2,1] es 0 en este sistema, no hace falta operar sobre fila 3)
Ab[0] = Ab[0] - (Ab[0,1]/Ab[1,1]) * Ab[1]

# Fila 3 como pivote para limpiar columna 2
Ab[0] = Ab[0] - (Ab[0,2]/Ab[2,2]) * Ab[2]
Ab[1] = Ab[1] - (Ab[1,2]/Ab[2,2]) * Ab[2]

# Normalizar diagonales a 1
Ab[0] = Ab[0] / Ab[0,0]
Ab[1] = Ab[1] / Ab[1,1]
Ab[2] = Ab[2] / Ab[2,2]

# b) Resultados
x_sol = Ab[:, n]
print("\n--- MATRIZ FINAL (FORMA ESCALONADA REDUCIDA) ---")
print(Ab)

print("\n--- RESULTADOS FINALES ---")
print(f"x = {x_sol[0]:.5f}")
print(f"y = {x_sol[1]:.5f}")
print(f"z = {x_sol[2]:.5f}")

# Verificación rigurosa
print("\n--- VERIFICACIÓN DE RESULTADOS (A * x) ---")
verif = np.dot(A, x_sol)
print(f"Resultado: {verif} | Esperado: {b.flatten()}")
