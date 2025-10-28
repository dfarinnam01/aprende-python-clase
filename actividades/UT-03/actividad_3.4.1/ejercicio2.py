nombre1 = input("Introduce el primer nombre: ")
nombre2 = input("Introduce el segundo nombre: ")
nombre3 = input("Introduce el tercer nombre: ")

nombres = [nombre1, nombre2, nombre3]

# Ordenamos alfabéticamente
nombres.sort()

print("Los nombres ordenados alfabéticamente son:")
for nombre in nombres:
    print(nombre)