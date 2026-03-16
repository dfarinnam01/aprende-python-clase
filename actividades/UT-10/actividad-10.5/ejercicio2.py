import pandas as pd
import numpy as np
from datetime import datetime

datos = np.arange(50)
matriz = datos.reshape(10, 5)

fecha_inicio = datetime.now().date()
fechas = pd.date_range(start=fecha_inicio, periods=10)

df = pd.DataFrame(
    matriz,
    index=fechas,
    columns=["A", "B", "C", "D", "E"]
)

print("DataFrame completo:\n")
print(df)


print("\nSegunda fila:")
print(df.iloc[1])


print("\nTercera columna:")
print(df.iloc[:, 2])

print("\nFilas 3ª a 6ª:")
print(df.iloc[2:6])

print("\nFilas impares:")
print(df.iloc[0::2])

print("\nColumnas B, C y D:")
print(df[["B", "C", "D"]])

print("\nColumnas A y B de filas 3 y 4:")
print(df.iloc[2:4, 0:2])

filas_pares = df.iloc[1::2]

columnas_pares = filas_pares[["B", "D"]]

suma = columnas_pares.values.sum()

print("\nSuma de filas pares y columnas B y D:")
print(suma)