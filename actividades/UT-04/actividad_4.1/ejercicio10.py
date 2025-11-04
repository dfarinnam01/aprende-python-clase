numero=0
while numero !=5:
    print("\n1______________Sumar")
    print("2______________Restar")
    print("3______________Multiplicar")
    print("4______________Dividir")
    print("5______________Salir\n")

    numero = int(input("Selecciona una opcion: "))
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))
    if numero == 1:
        total = num1 + num2
        print("El resultado es:", total)
    elif numero == 2:
        total = num1 - num2
        print("El resultado es:", total)
    elif numero == 3:
        total = num1 * num2
        print("El resultado es:", total)
    elif numero == 4:
        try:
            total = num1 // num2
            print("El resultado es:", total)
        except:
            print("Error en la division")
    else:
        print("No has eligido un numero del menu")


