def f(x): return x**4 - 5*x**2 + 4
def df(x): return 4*x**3 - 10*x

xi, tol, error, it = 2.5, 0.001, 100.0, 0
print("EJERCICIO 8 - RAÍZ MAYOR")
while error > tol:
    xn = xi - f(xi)/df(xi)
    if it > 0: error = abs((xn - xi) / xn) * 100
    xi, it = xn, it + 1
    print(f"Iter {it}: x = {xi:.6f}, Error = {error:.6f}%")
