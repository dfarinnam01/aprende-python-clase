with open("ejemplo.txt", "r",encoding="UTF-8") as f:
    for linea in f:
        print(linea.strip())

# with open("ejemplo.txt", "r",encoding="UTF-8") as f:
#     lineas=f.readlines()
#     for linea in lineas:
#         print(linea.strip())