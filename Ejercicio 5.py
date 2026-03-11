import numpy as np

def f(x): return np.log(x**2 + 1) - np.exp(x**2 - 1) + 2
def df(x): return (2*x)/(x**2 + 1) - 2*x * np.exp(x**2 - 1)

xi, tol, error, it = 1.5, 0.001, 100.0, 0
print("EJERCICIO 5 - NEWTON")
while error > tol:
    xn = xi - f(xi)/df(xi)
    if it > 0: error = abs((xn - xi) / xn) * 100
    xi, it = xn, it + 1
    print(f"Iter {it}: x = {xi:.6f}, Error = {error:.6f}%")
