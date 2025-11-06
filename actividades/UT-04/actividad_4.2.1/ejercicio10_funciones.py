#=====================================================
#                    FUNCIONES
#=====================================================
def menu():
    print(f"{ANSI_AZUL}\n1______________Sumar")
    print("2______________Restar")
    print("3______________Multiplicar")
    print("4______________Dividir")
    print(f"5______________Salir\n{ANSI_RESET}")
    opcion = 0
    while opcion not in [1, 2, 3, 4, 5]:
        opcion = int(input(f"{ANSI_CYAN}Selecciona una opcion: {ANSI_RESET}"))
    return opcion

def sumar():
    try:
        num1 = int(input(f"{ANSI_AMARILLO}Ingresa un numero: "))
        num2 = int(input(f"Ingresa otro numero: {ANSI_RESET}"))
        print(num1 + num2)
    except:
        print("No se pudo realizar la operacion")

def restar():
    num1 = int(input(f"{ANSI_AMARILLO}Ingresa un numero: "))
    num2 = int(input(f"Ingresa otro numero: {ANSI_RESET}"))
    print(num1 - num2)

def multiplicar():
    num1 = int(input(f"{ANSI_AMARILLO}Ingresa un numero: "))
    num2 = int(input(f"Ingresa otro numero: {ANSI_RESET}"))
    print( num1 * num2)

def dividir():
    try:
        num1 = int(input(f"{ANSI_AMARILLO}Ingresa un numero: "))
        num2 = int(input(f"Ingresa otro numero: {ANSI_RESET}"))
        print(num1 / num2)
    except:
        print(f"{ANSI_ROJO}Error en la division{ANSI_RESET}")


#=====================================================

ANSI_AZUL = "\033[34m"
ANSI_VERDE = "\033[92m"
ANSI_ROJO = "\033[31m"
ANSI_AMARILLO = "\033[33m"
ANSI_CYAN = "\033[36m"
ANSI_RESET = "\033[0m"

opcion=0

while opcion !=5:
    opcion= menu()
    match opcion:
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            dividir()
print(f"{ANSI_AMARILLO}FIN DEL PROGRAMA{ANSI_RESET}")


