#EJERCICIO 2: NEWTON-RAPHSON 
def f2(x): return np.sin(x) + x * np.cos(x**2) - 2.5
def df2(x): return np.cos(x) + np.cos(x**2) - 2*x**2 * np.sin(x**2)
xi = 5.0 # Punto inicial cercano a la raíz positiva según análisis
print("\nEJERCICIO 2\nIter | xi | Error %")
for i in range(1, 4):
    xi_next = xi - f2(xi)/df2(xi)
    err = abs((xi_next - xi) / xi_next) * 100
    print(f"{i:<5}|{xi_next:<10.4f}|{err:.4f}%")
    xi = xi_next
