import numpy as np

# Configuración a 4 decimales según el inciso b
np.set_printoptions(precision=4, suppress=True)

# Ingreso de datos para el problema 10
print("--- Problema 10: Aleaciones ---")
# Datos calculados del enunciado
A = np.array([[0.20, 0.45], [0.50, 0.20]], dtype=float)
b = np.array([15, 18], dtype=float).reshape(2, 1)

# Matriz aumentada
Ab = np.hstack([A, b])

# --- ELIMINACIÓN MANUAL (Sin bucles ni linalg.solve) ---

# Paso 1: Hacer cero el elemento debajo del primer pivote (columna 0)
factor = Ab[1, 0] / Ab[0, 0]
Ab[1] = Ab[1] - factor * Ab[0]

# Paso 2: Hacer cero el elemento arriba del segundo pivote (columna 1)
factor = Ab[0, 1] / Ab[1, 1]
Ab[0] = Ab[0] - factor * Ab[1]

# Paso 3: Normalizar diagonales a 1
Ab[0] = Ab[0] / Ab[0, 0]
Ab[1] = Ab[1] / Ab[1, 1]

# Extracción de resultados
x_res = Ab[0, 2]
y_res = Ab[1, 2]

print("\n--- RESULTADOS ---")
print(f"Cantidad de Aleación 1 (x): {x_res:.4f} kg")
print(f"Cantidad de Aleación 2 (y): {y_res:.4f} kg")

# Verificación rigurosa
print("\n--- VERIFICACIÓN ---")
print(f"Oro esperado (15 kg): {0.20*x_res + 0.45*y_res:.4f}")
print(f"Litio esperado (18 kg): {0.50*x_res + 0.20*y_res:.4f}")
