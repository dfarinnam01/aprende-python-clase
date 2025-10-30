cadena=input("Ingresa una cadena de texto: ")
print(len(cadena))
print(cadena[0])
print(cadena[-1])
print(cadena.upper())
espacios=(80-len(cadena))//2
print(" "+espacios,cadena.upper())
# print("Centrada en 80 caracteres:")
# print(cadena.center(80))