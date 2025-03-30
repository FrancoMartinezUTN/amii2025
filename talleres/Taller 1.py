import numpy as np
import matplotlib.pyplot as plt

# Función para evaluar el método de Euler
def euler(f, x0, y0, x_end, n):
    h = (x_end - x0) / n  # paso
    x_values = [x0]
    y_values = [y0]

    print(f"\nIteración paso a paso (h = {h}):")
    print(f"x_0 = {x0:.4f}, y_0 = {y0:.4f}")

    for i in range(n):
        y_next = y_values[-1] + h * f(x_values[-1], y_values[-1])
        x_next = x_values[-1] + h
        x_values.append(x_next)
        y_values.append(y_next)
        print(f"x_{i+1} = {x_next:.4f}, y_{i+1} = {y_next:.4f}")

    return x_values, y_values

# ========================
#  Entrada del usuario
# ========================

# 1. EDO: f(x, y) como función lambda
# Ejemplo: y' = x + y
f_str = input("Ingresá la EDO como función en términos de x y y (ej: x + y):\n")
f = lambda x, y: eval(f_str)

# 2. Condición inicial
x0 = float(input("x0 = "))
y0 = float(input("y0 = "))

# 3. Valor donde se desea la solución
x_end = float(input("Valor de x donde estimar la solución (x_final): "))

# 4. Número de pasos
n = int(input("Número de pasos (n): "))

# ========================
#  Ejecutar método de Euler
# ========================
x_vals, y_vals = euler(f, x0, y0, x_end, n)

# ========================
#  Graficar resultado
# ========================
plt.plot(x_vals, y_vals, 'bo-', label="Aproximación de Euler")
plt.title("Aproximación usando el Método de Euler")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

# Resultado final
print(f"\n✅ Aproximación final: y({x_vals[-1]:.4f}) ≈ {y_vals[-1]:.4f}")
