import numpy as np
import matplotlib.pyplot as plt

def f(x): return x**3 - 3*x**2 - 4*x + 6
def df(x): return 3*x**2 - 6*x - 4

# Gráfico pedido
x_plt = np.linspace(-15, 15, 1000)
plt.plot(x_plt, f(x_plt))
plt.ylim(-100, 100) # Ajuste para ver el cruce por cero
plt.axhline(0, color='black')
plt.title("Análisis en [-15, 15]")
plt.grid()
plt.show()

# Newton
xi, tol, error, it = -1.0, 0.05, 100.0, 0
print(f"{'Iter':<5}|{'xi':<12}|{'Error %':<10}")
while error > tol:
    xi_next = xi - f(xi)/df(xi)
    if it > 0: error = abs((xi_next - xi) / xi_next) * 100
    xi, it = xi_next, it + 1
    print(f"{it:<5}|{xi:<12.5f}|{error:<10.4f}%")
