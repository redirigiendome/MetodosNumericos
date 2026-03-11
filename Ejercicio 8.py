import numpy as np

# Configuración de visualización: 3 dígitos después del punto decimal
np.set_printoptions(precision=3, suppress=True)

# a) Ingreso de datos por teclado
print("Ingrese la matriz de coeficientes A (ejemplo: [[1,1,-1],[-2,1,1],[1,1,2]]):")
A = np.array(eval(input()))

print("Ingrese el vector b (ejemplo: [1,3,2]):")
b = np.array(eval(input()))

# Resolución mediante el método de eliminación (usando el solver de linalg)
# Nota: Internamente usa factorizaciones que equivalen a Gauss/Gauss-Jordan
x = np.linalg.solve(A, b)

# Presentación de resultados
print("\n--- Resultados ---")
print(f"Matriz A:\n{A}")
print(f"Vector b: {b}")
print(f"Solución (x, y, z): {x}")
