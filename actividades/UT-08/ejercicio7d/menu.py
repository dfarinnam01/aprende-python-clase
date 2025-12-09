from cuenta import *
def limpiar_pantalla():
    print("\033[2J\033[H",end="")
def pulsar_continuar():
   input("Pulse INTRO para continuar...")
def menu_sucursal()->str:
    limpiar_pantalla()
    opcion="X"
    while opcion not in ("1","2","3","0"):
        opcion=input('''
                    1. Nueva cuenta
                    2. Listado de cuentas
                    3. Seleccionar cuenta
                    0. Salir
                    OPCION: ''')
        return opcion

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