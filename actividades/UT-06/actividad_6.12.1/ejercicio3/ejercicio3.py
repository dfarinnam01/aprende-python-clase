with open("ejemplo.txt", "r",encoding="UTF-8") as f:
    cl=0
    for linea in f:
        for letra in linea:
            cl=cl+1
