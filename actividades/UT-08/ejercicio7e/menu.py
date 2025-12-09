from cuenta import *
from codigos_ansi import CodigosAnsi as CA

def limpiar_pantalla():
    print("\033[2J\033[H",end="")

def pulsar_continuar():
   # input(f"{CA.BG_RED}Pulse INTRO para continuar...{CA.RESET}")
   input(f"{CA.BG_BRIGHT_GREEN}INTRO para continuar...{CA.RESET}")

def menu_sucursal()->str:
    opcion="X"
    while opcion not in ("1","2","3","0"):
        limpiar_pantalla()
        CA.activa(CA.BG_WHITE)
        CA.activa(CA.MAGENTA)
        print("*"*28)
        print("* 1. Nueva cuenta          *")
        print("* 2. Listado de cuentas    *")
        print("* 3. Seleccionar cuenta    *")
        print("* 0. Salir                 *")
        print("*" * 28)
        CA.desactiva()
        CA.activa(CA.CYAN)
        print("OPCION: ")
        CA.desactiva()
        CA.activa(CA.YELLOW)
        opcion=input()
        CA.desactiva()
        return opcion
        # opcion=input(
        #     f'''{CA.BG_WHITE}{CA.BLACK}
        #             1. Nueva cuenta
        #             2. Listado de cuentas
        #             3. Seleccionar cuenta
        #             0. Salir
        #             OPCION:{CA.RESET} '''
        # )
        # return opcion

def menu_cuenta(cuenta:Cuenta)->str:
    limpiar_pantalla()
    print("-"*20)
    print("Cuenta: ",cuenta.iban)
    print("-" * 20)
    opcion="X"
    while opcion not in ("1","2","3","0"):
        opcion=input(''':¡
                    1. Operacion
                    2. Consulta
                    3. Movimientos
                    0. Salir
                    OPCION: ''')
        return opcion