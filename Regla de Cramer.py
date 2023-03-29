import numpy as np

# Pedimos el número de incógnitas
n = int(input('Ingrese el número de incógnitas: '))

# Creamos una matriz de n x n para los coeficientes de las incógnitas
A = np.zeros((n, n))

# Creamos un vector de n para los términos independientes
B = np.zeros(n)

# Pedimos los coeficientes y términos independientes del sistema
print('Ingresa los coeficientes:')
for i in range(n):
    for j in range(n):
        A[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
print("A:\n", A)
B = np.zeros(n)
print('Ingresa los términso independientes:')
for i in range(n):
    B[i] = float(input( 'b['+str(i)+']='))
# Calculamos el determinante de la matriz de coeficientes
detA = np.linalg.det(A)
if detA == 0:
    print('El sistema no tiene solución única.')
else:
    # Resolvemos el sistema de ecuaciones usando la regla de Cramer
    for i in range(n):
        A_i = A.copy()
        # Reemplazamos la columna i-ésima con el vector de términos independientes
        A_i[:, i] = B
        # Calculamos el determinante de la matriz resultante
        detA_i = np.linalg.det(A_i)
        # La solución de la i-ésima incógnita es el determinante anterior dividido por el determinante de la matriz de coeficientes original
        x_i = detA_i / detA
        print('x[' + str(i+1) + '] = ' + str(round(x_i, 3)),'toneladas' )