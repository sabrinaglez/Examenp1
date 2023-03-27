import numpy as np

# Matriz A y B
A = np.array([[0.25, 0.15, 0], [0.45, 0.5, 0.75],[0.3, 0.35, 0.25]])

B = np.array([1.5, 5, 3])

# Solución del sistema de ecuaciones lineales
sol = np.linalg.solve(A, B)

# Soluciones por fertilizante
print("La cantidad diaria que se debe producir de cada tipo de fertilizante es:")
print(f"Tipo A: {sol[0]:.3f} toneladas")
print(f"Tipo B: {sol[1]:.3f} toneladas")
print(f"Tipo C: {sol[2]:.3f} toneladas")

