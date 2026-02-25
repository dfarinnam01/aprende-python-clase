import numpy as np

array = np.arange(10)
print("Original:", array)

impares = array[array % 2 != 0]
print("Impares:", impares)

array[array % 2 == 0] = 99
print("Pares reemplazados:", array)