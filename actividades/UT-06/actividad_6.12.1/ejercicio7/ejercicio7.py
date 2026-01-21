with open("ejemplo.txt", "r", encoding="UTF-8") as f:
    lineas = f.readlines()

with open("copia_ejemplo.txt", "w", encoding="UTF-8") as nuevo_fichero:
    contador = 1
    for linea in lineas:
        if linea.strip():
            nuevo_fichero.write(f"{contador}. {linea}")
            contador += 1

print("El archivo se ha copiado correctamente.")

# with open("ejemplo.txt", "r", encoding="UTF-8") as f:
#     lineas = f.readlines()
#
# with open("copia_ejemplo.txt", "w", encoding="UTF-8") as nuevo_fichero:
#     contador = 1
#     for index,linea in enumerate(lineas,start=1):
#         if linea.strip():
#             nuevo_fichero.write(f"{index}. {linea}")
#
# print("El archivo se ha copiado correctamente.")
