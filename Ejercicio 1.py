import numpy as np
#Primero para verificará si un número es primo o no.
def es_primo(p):
    if p <= 1:
        return False
    for i in range(2, int(np.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True
# se solicita al usuario la dimensión n de la matriz
n = int(input("Introduce la dimensión n de la matriz: "))

#Se construye la matriz cuadrada de n x n con los primeros números primos
#Posteriorme se relizará la suma de los elementos que se encuentran sobre y en  la diagonal principal
def suma_diagonal_se(n):
    
    matriz = np.zeros((n, n), dtype=int)
    v= 2
    for i in range(n):
        for j in range(n):
            while not es_primo(v):
                v += 1
            matriz[i][j] = v
            v += 1
    
    print("La matriz de números primos es:")
    print(matriz)
    
    suma = 0
    for i in range(n):
        for j in range(i, n):
            suma += matriz[i][j]
    
    return suma

# Calcula la suma de todos los elementos en y por encima de la diagonal principal y muestra la matriz de números primos
suma = suma_diagonal_se(n)
print("La suma de los elementos en y por encima de la diagonal principal es:", suma)
