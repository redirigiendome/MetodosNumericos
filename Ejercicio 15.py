import numpy as np
import sympy as sp

def newton_raphson_sistema():
    # 1. Definir variables y funciones simbólicas
    x, y = sp.symbols('x y')
    f1 = y**3 + x*y + 1
    f2 = x**3 + 2*x*y**3 - 2
    
    # 2. Crear el Jacobiano
    funcs = sp.Matrix([f1, f2])
    vars = sp.Matrix([x, y])
    J_sym = funcs.jacobian(vars)
    
    # Convertir a funciones de numpy para velocidad
    f_num = sp.lambdify((x, y), funcs, 'numpy')
    j_num = sp.lambdify((x, y), J_sym, 'numpy')
    
    # 3. Valores iniciales y configuración
    x_n, y_n = 1.5, -1.0
    iteraciones = 2
    
    print(f"{'Iter':<5} | {'x':<10} | {'y':<10} | {'error_x %':<10} | {'error_y %':<10}")
    print("-" * 60)
    print(f"{0:<5} | {x_n:<10.4f} | {y_n:<10.4f} | {'-':<10} | {'-':<10}")

    for i in range(1, iteraciones + 1):
        # Evaluar f y J en el punto actual
        F_eval = f_num(x_n, y_n).astype(float)
        J_eval = j_num(x_n, y_n).astype(float)
        
        # Resolver el sistema J * delta = -F
        delta = np.linalg.solve(J_eval, -F_eval).flatten()
        
        # Guardar valores anteriores para el error
        x_prev, y_prev = x_n, y_n
        
        # Actualizar
        x_n += delta[0]
        y_n += delta[1]
        
        # Calcular errores relativos porcentuales
        err_x = abs(delta[0] / x_n) * 100
        err_y = abs(delta[1] / y_n) * 100
        
        print(f"{i:<5} | {x_n:<10.4f} | {y_n:<10.4f} | {err_x:<10.2f} | {err_y:<10.2f}")

if __name__ == "__main__":
    newton_raphson_sistema()
