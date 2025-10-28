nombre1 = input("Introduce el primer nombre: ")
nombre2 = input("Introduce el segundo nombre: ")
nombre3 = input("Introduce el tercer nombre: ")

if nombre1 <= nombre2 and nombre1 <= nombre3:
    primero = nombre1
    if nombre2 <= nombre3:
        segundo = nombre2
        tercero = nombre3
    else:
        segundo = nombre3
        tercero = nombre2
elif nombre2 <= nombre1 and nombre2 <= nombre3:
    primero = nombre2
    if nombre1 <= nombre3:
        segundo = nombre1
        tercero = nombre3
    else:
        segundo = nombre3
        tercero = nombre1
else:
    primero = nombre3
    if nombre1 <= nombre2:
        segundo = nombre1
        tercero = nombre2
    else:
        segundo = nombre2
        tercero = nombre1

print("Los nombres ordenados alfabéticamente son:")
print(primero)
print(segundo)
print(tercero)