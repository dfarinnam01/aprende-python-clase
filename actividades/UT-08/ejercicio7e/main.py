from sucursal import Sucursal
from menu import menu_sucursal,menu_cuenta
import gestion_cuenta as gc
import gestion_sucursal as gs

if __name__=="__main__":
    sucursal=Sucursal()
    opcion_sucursal=menu_sucursal()
    while opcion_sucursal != "0":
        match opcion_sucursal:
            case "1":
               gs.nueva_cuenta(sucursal)
            case "2":
               gs.listado_cuentas(sucursal)
            case "3":
                cuenta=gs.seleccion_cuenta(sucursal)
                opcion_cuenta = menu_cuenta(cuenta)
                while opcion_cuenta != "0":
                    match opcion_cuenta:
                        case "1":
                            gc.cuenta_operacion(cuenta)
                        case "3":
                            gc.cuenta_movimientos(cuenta)
                    opcion_cuenta = menu_cuenta(cuenta)
        opcion_sucursal = menu_sucursal()