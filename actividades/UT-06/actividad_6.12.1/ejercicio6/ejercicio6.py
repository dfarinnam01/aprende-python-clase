with open("ejemplo.txt", "r", encoding="UTF-8") as f:
    contenido = f.read()

with open("copia_ejemplo.txt", "w", encoding="UTF-8") as nuevo_fichero:
    nuevo_fichero.write(contenido)

print("El archivo se ha copiado correctamente.")
