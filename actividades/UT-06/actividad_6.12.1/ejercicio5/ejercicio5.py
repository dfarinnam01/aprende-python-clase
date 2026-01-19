with open("ejemplo.txt", "r",encoding="UTF-8") as f:
    palabra=input("Ingresa una palabra: ")
    for linea in f:
        for letra in linea:
            if letra!="\n":
                cl=cl+1
    print(cl)