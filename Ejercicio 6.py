import numpy as np

def f(x): return np.cos(3*x - np.log(x)) + 2*x**3

a, b, tol_abs = 0.6, 0.9, 0.005
it = 1
print("EJERCICIO 6 - ERROR ABSOLUTO")
while (b - a) / 2 > tol_abs:
    xr = (a + b) / 2
    print(f"Iter {it}: xr = {xr:.4f}, Error Abs = {(b-a)/2:.4f}")
    if f(a) * f(xr) < 0: b = xr
    else: a = xr
    it += 1
