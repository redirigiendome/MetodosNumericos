# Resolución Ejercicio 3b - Método de Bisección sin estructuras de control
# Ecuación: 6x^3 - 6x + 2 = 0

print(f"{'iter':>4} | {'a':>7} | {'b':>7} | {'xr':>7} | {'f(a)':>7} | {'f(b)':>7} | {'f(xr)':>7} | {'f(a)f(xr)':>10} | {'ea %':>7} | {'tol %':>5}")
print("-" * 88)

tol = 12.0000

# --- ITERACIÓN 1 ---
a1 = -2.0000
b1 = -1.0000
xr1 = (a1 + b1) / 2.0
fa1 = 6*(a1**3) - 6*a1 + 2
fb1 = 6*(b1**3) - 6*b1 + 2
fxr1 = 6*(xr1**3) - 6*xr1 + 2
prod1 = fa1 * fxr1
ea1 = 0.0 # No hay error en la iteración 1

print(f"{1:4} | {a1:7.4f} | {b1:7.4f} | {xr1:7.4f} | {fa1:7.4f} | {fb1:7.4f} | {fxr1:7.4f} | {prod1:10.4f} | {'-':>7} | {tol:5.2f}")

# --- ITERACIÓN 2 ---
# prod1 es positivo (314.5000), por lo que la raíz está en [xr1, b1]. Se reemplaza 'a'.
a2 = xr1 
b2 = b1
xr2 = (a2 + b2) / 2.0
fa2 = 6*(a2**3) - 6*a2 + 2
fb2 = 6*(b2**3) - 6*b2 + 2
fxr2 = 6*(xr2**3) - 6*xr2 + 2
prod2 = fa2 * fxr2
ea2 = abs((xr2 - xr1) / xr2) * 100

print(f"{2:4} | {a2:7.4f} | {b2:7.4f} | {xr2:7.4f} | {fa2:7.4f} | {fb2:7.4f} | {fxr2:7.4f} | {prod2:10.4f} | {ea2:7.4f} | {tol:5.2f}")

# --- ITERACIÓN 3 ---
# prod2 es positivo (20.5234), por lo que se vuelve a reemplazar 'a'.
a3 = xr2
b3 = b2
xr3 = (a3 + b3) / 2.0
fa3 = 6*(a3**3) - 6*a3 + 2
fb3 = 6*(b3**3) - 6*b3 + 2
fxr3 = 6*(xr3**3) - 6*xr3 + 2
prod3 = fa3 * fxr3
ea3 = abs((xr3 - xr2) / xr3) * 100

print(f"{3:4} | {a3:7.4f} | {b3:7.4f} | {xr3:7.4f} | {fa3:7.4f} | {fb3:7.4f} | {fxr3:7.4f} | {prod3:10.4f} | {ea3:7.4f} | {tol:5.2f}")
