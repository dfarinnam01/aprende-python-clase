with open("ejemplo.txt", "r",encoding="UTF-8") as f:
    for linea in f:
        print(linea.strip())