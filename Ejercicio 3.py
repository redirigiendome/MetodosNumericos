import numpy as np
import matplotlib.pyplot as plt

def f(x): return 6*x**3 - 6*x + 2

# Parte Gráfica
x_vals = np.linspace(-2, 1, 100)
plt.plot(x_vals, f(x_vals), label="f(x)")
plt.axhline(0, color='red', linestyle='--')
plt.title("Método Gráfico - Ejercicio 3")
plt.grid()
plt.show()

# Bisección
a, b, tol = -2.0, -1.0, 12.0
error, xr_old, it = 100.0, 0, 1
print(f"{'Iter':<5}|{'xr':<10}|{'Error %':<10}")
while error > tol:
    xr = (a + b) / 2
    if it > 1: error = abs((xr - xr_old) / xr) * 100
    print(f"{it:<5}|{xr:<10.4f}|{error:<10.2f}%")
    if f(a) * f(xr) < 0: b = xr
    else: a = xr
    xr_old, it = xr, it + 1
