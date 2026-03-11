import numpy as np

# Datos del Problema 12
A = np.array([[2, 2, -1], [1, 1, 1], [2, -1, 1]], dtype=float)
b = np.array([2, -2, 1], dtype=float).reshape(3, 1)
Ab = np.hstack([A, b])

# Proceso Manual (Siguiendo los pasos del cuaderno)
Ab[[0, 1]] = Ab[[1, 0]] # Intercambio F1 y F2
Ab[1] = Ab[1] - 2*Ab[0]
Ab[2] = Ab[2] - 2*Ab[0]
Ab[[1, 2]] = Ab[[2, 1]] # Intercambio F2 y F3 para evitar pivote 0

# Normalización y Jordan
Ab[2] = Ab[2] / Ab[2, 2]
Ab[1] = (Ab[1] - Ab[1, 2]*Ab[2]) / Ab[1, 1]
Ab[0] = Ab[0] - Ab[0, 2]*Ab[2]
Ab[0] = Ab[0] - Ab[0, 1]*Ab[1]

print("Solución Problema 12:")
print(f"x = {Ab[0, 3]:.1f}, y = {Ab[1, 3]:.1f}, z = {Ab[2, 3]:.1f}")
