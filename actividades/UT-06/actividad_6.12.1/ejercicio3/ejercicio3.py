with open("ejemplo.txt", "r",encoding="UTF-8") as f:
    total_palabras = 0
    for linea in f:
        palabras = linea.split()
        total_palabras += len(palabras)
print("Número total de palabras",total_palabras)