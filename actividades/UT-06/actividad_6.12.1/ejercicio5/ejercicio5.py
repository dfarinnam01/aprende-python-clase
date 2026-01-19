# with open("ejemplo.txt", "r", encoding="UTF-8") as f:
#     palabra = input("Introduce una palabra: ")
#     c=0
#     for linea in f:
#         palabras=linea.split()
#         c=c+palabras.count(palabra)
#
# print(f"La palabra '{palabra}' aparece {c} veces en el fichero.")

# with open("ejemplo.txt", "r", encoding="UTF-8") as f:
#     palabra_a_buscar = input("Introduce una palabra: ")
#     num_ocurrencias=0
#     for linea in f:
#         palabras=linea.split()
#         for palabra in palabras:
#             if palabra.lower()==palabra_a_buscar.lower():
#                 num_ocurrencias=num_ocurrencias+1
# print(f"La palabra aparece {num_ocurrencias} veces en el fichero.")

mapa_tildes= str.maketrans(
    "áéíóúÁÉÍÓÚ",
    "aeiouAEIOU"
)
palabra_a_buscar=input("Introduce una palabra a buscar: ")
with open("ejemplo.txt", "r", encoding="UTF-8") as f:
    num_ocurrencias=0
    for linea in f:
        palabra=linea.split()
        for palabra in palabra:
            palabra=palabra.translate(mapa_tildes)
            if palabra.lower() in palabra_a_buscar.lower():
                num_ocurrencias=num_ocurrencias+1
print(num_ocurrencias)