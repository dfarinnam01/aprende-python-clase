with open("ejemplo.txt", "r", encoding="UTF-8") as f:
    palabra = input("Introduce una palabra: ")
    c=0
    for linea in f:
        palabras=linea.split()
        c =c+palabras.count(palabra)

print(f"La palabra '{palabra}' aparece {c} veces en el fichero.")
