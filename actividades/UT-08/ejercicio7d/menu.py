

def menu_sucursal()->str:
    opcion="X"
    while opcion not in ("1","2","3","0"):
        opcion=input(''':
                    1. Nueva cuenta
                    2. Listado de cuentas
                    3. Seleccionar cuenta
                    0. Salir
                    OPCION: ''')
        return opcion

def menu_cuenta()->str:
    opcion="X"
    while opcion not in ("1","2","3","0"):
        opcion=input(''':
                    1. Operacion
                    2. Consulta
                    3. Movimientos
                    0. Salir
                    OPCION: ''')
        return opcion