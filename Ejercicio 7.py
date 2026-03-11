import numpy as np

def f(x): return np.exp(x) - np.sin(x) - 2

a, b, tol, xr_old, it, error = 0.0, 2.0, 0.01, 0, 1, 100.0
print("EJERCICIO 7 - ERROR RELATIVO 0.01%")
while error > tol:
    xr = (a + b) / 2
    if it > 1: error = abs((xr - xr_old) / xr) * 100
    print(f"Iter {it}: xr = {xr:.5f}, Error = {error:.5f}%")
    if f(a) * f(xr) < 0: b = xr
    else: a = xr
    xr_old, it = xr, it + 1
