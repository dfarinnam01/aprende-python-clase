matriz = [
    [9, 3, 1, 0],  # Fila 1
    [8, 7, 5, 21],  # Fila 2
    [2, 6, 5, 9],  # Fila 3
    [1, 2, 34, 8]   # Fila 4
]
entrada_encontrada= False
numero_buscar=int(input("Ingrese el numero a buscar: "))
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == numero_buscar:
            entrada_encontrada = True
            print(i,j)

if entrada_encontrada:
    print("Entrada encontrada")
else:
    print("Entrada no encontrada")

