ancho = int(input("Introduce el ancho del rectángulo: "))
alto = int(input("Introduce el alto del rectángulo: "))
for i in range(alto):
    for j in range(ancho):
        if i == j:
            print("O", end="")
        else:
            print("*", end="")
    print()