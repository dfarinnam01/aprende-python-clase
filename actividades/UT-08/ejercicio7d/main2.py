from sucursal import Sucursal
from menu import menu_cuenta,menu_sucursal
from cuenta import Cuenta
# CREAR MENU SUCURSAL
# CREAR MENU CUENTA
#
# CREAR FUNCIONES
#
# BUCLE SUCURSAL
#     LEER OPCION(AÑADIR CUENTA,LISTAR CUENTAS,SALIR)
#     BUCLE CUENTA
#         LEER OPCION(NUEVO MOVIMIENTO,CONSULTA,LISTADO_MOVIMIENTOS,SALIR)

#FUNCIONES OPERATIVAAS
def nueva_cuenta(sucursal:Sucursal):
    iban=input("Introduce el IBAN: ")
    titular=input("Introduce el titular: ")
    ingreso=float(input("Introduce el ingreso: "))

    try:
        cuenta=Cuenta(iban=iban,titular_principal=titular,ingreso=ingreso)
        sucursal.nueva_cuenta(cuenta)
    except Exception as e:
        print("-"*50)
        print(e)
        print("-"*50)
def listado_cuentas(sucursal:Sucursal):
    print(sucursal.cuentas)

#PROGRAMA PRINCIPAL
if __name__=="__main__":
    sucursal=Sucursal()
    opcion_sucursal=menu_sucursal()
    while opcion_sucursal != "0":
        match opcion_sucursal:
            case "1":
               nueva_cuenta(sucursal)
            case "2":
               listado_cuentas(sucursal)
            case "3":
                pass
        opcion_sucursal = menu_sucursal()