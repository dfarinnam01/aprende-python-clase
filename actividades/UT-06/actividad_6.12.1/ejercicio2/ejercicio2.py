with open("ejemplo.txt", "r",encoding="UTF-8") as f:
    c=0
    for linea in f:
        c=c+1
    print(c)