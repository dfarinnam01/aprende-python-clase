ANSI_AZUL = "\033[34m"
ANSI_VERDE = "\033[92m"
ANSI_ROJO = "\033[31m"
ANSI_AMARILLO = "\033[33m"
ANSI_CYAN = "\033[36m"
ANSI_RESET = "\033[0m"

opcion=0
while opcion !=5:
    print(f"{ANSI_AZUL}\n1______________Sumar")
    print("2______________Restar")
    print("3______________Multiplicar")
    print("4______________Dividir")
    print(f"5______________Salir\n{ANSI_RESET}")
    try:
        opcion = int(input(f"{ANSI_CYAN}Selecciona una opcion: {ANSI_RESET}"))
        if opcion in [1,2,3,4]:
            num1 = int(input(f"{ANSI_AMARILLO}Ingresa un numero: "))
            num2 = int(input(f"Ingresa otro numero: {ANSI_RESET}"))

            if opcion == 1:
                total = num1 + num2
            elif opcion == 2:
                total = num1 - num2
            elif opcion == 3:
                total = num1 * num2
            elif opcion == 4:
                try:
                    total = num1 / num2
                except:
                    print(f"{ANSI_ROJO}Error en la division{ANSI_RESET}")
                    continue

            print(f"\n{ANSI_VERDE}El resultado es: {total}{ANSI_RESET}")
        elif opcion == 5:
                print(f"{ANSI_AMARILLO}FIN DEL PROGRAMA{ANSI_RESET}")
        else:
            print(f"{ANSI_ROJO}No has elegido un número del menú.{ANSI_RESET}")

    except ValueError:
        print(f"{ANSI_ROJO}Por favor, introduce solo números válidos.{ANSI_RESET}")