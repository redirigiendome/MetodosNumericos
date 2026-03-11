def f(x): return x**3 + 2*x**2 + 10*x - 20

x0, x1, tol, error, it = 1.0, 2.0, 0.001, 100.0, 1
print("EJERCICIO 11 - MÉTODO DE LA SECANTE")
print(f"{'Iter':<5}|{'x_next':<12}|{'Error %':<10}")
while error > tol:
    x_next = x1 - (f(x1)*(x1 - x0)) / (f(x1) - f(x0))
    if it > 1: error = abs((x_next - x1) / x_next) * 100
    print(f"{it:<5}|{x_next:<12.6f}|{error:<10.4f}%")
    x0, x1, it = x1, x_next, it + 1
