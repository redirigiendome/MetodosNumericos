import numpy as np
import matplotlib.pyplot as plt

# --- EJERCICIO 1
def f1(x): return x**2 * np.exp(x + 2) - 1.1 * np.sin(x) - 1
a, b, xr_old = 0.0, 1.0, 0
print("EJERCICIO 1\nIter | a | b | xr | Error %")
for i in range(1, 4):
    xr = (a + b) / 2
    err = abs((xr - xr_old) / xr) * 100 if i > 1 else 0
    print(f"{i:<5}|{a:<8.4f}|{b:<8.4f}|{xr:<8.4f}|{err:.4f}%")
    if f1(a) * f1(xr) < 0: b = xr
    else: a = xr
    xr_old = xr
