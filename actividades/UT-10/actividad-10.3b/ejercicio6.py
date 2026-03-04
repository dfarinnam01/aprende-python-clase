import numpy as np

# Matriz 6x5 del 1 al 30
matriz = np.arange(1, 31).reshape(6, 5)
print("Matriz original:\n", matriz)

# 1 Submatriz 3x4 solicitada
submatriz = matriz[2:5, 1:5]
print("\nSubmatriz 3x4:\n", submatriz)

# 2️ Extraer número 20
numero_20 = matriz[3, 4]
print("\nNúmero 20:", numero_20)

# 3️ Extraer 2, 7, 12 en matriz 1x3
numeros = matriz[[0, 1, 2], 1].reshape(1, 3)
print("\n2, 7, 12:\n", numeros)

# 4️ Última fila
ultima_fila = matriz[-1]
print("\nÚltima fila:\n", ultima_fila)

# 5️ Dos últimas filas
dos_ultimas = matriz[-2:]
print("\nDos últimas filas:\n", dos_ultimas)

# 6️ Sumar todos los elementos
suma = matriz.sum()
print("\nSuma total:", suma)