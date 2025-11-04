opcion=0
while opcion !=5:
    print("\n1______________Sumar")
    print("2______________Restar")
    print("3______________Multiplicar")
    print("4______________Dividir")
    print("5______________Salir\n")
    try:
        opcion = int(input("Selecciona una opcion: "))
        if opcion in [1,2,3,4]:
            num1 = int(input("Ingresa un numero: "))
            num2 = int(input("Ingresa otro numero: "))

            if opcion == 1:
                total = num1 + num2
                print("El resultado es:", total)
            elif opcion == 2:
                total = num1 - num2
                print("El resultado es:", total)
            elif opcion == 3:
                total = num1 * num2
                print("El resultado es:", total)
            elif opcion == 4:
                try:
                    total = num1 // num2
                    print("El resultado es:", total)
                except:
                    print("Error en la division")
        elif opcion == 5:
                print("FIN DEL PROGRAMA")
        else:
            print("No has eligido un numero del menu")

    except:
        print("Por favor, introduce solo números válidos")