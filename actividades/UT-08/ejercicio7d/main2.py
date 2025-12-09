from sucursal import Sucursal
from menu import *
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
        print("Cuenta añadida con exito.")
        pulsar_continuar()
    except Exception as e:
        print("-"*50)
        print(e)
        print("-"*50)
def listado_cuentas(sucursal:Sucursal):
    for iban,cuenta in sucursal.cuentas.items():
        print("IBAN: ",iban,"\tTITULAR: ",cuenta.titulares[0])
    pulsar_continuar()

def seleccion_cuenta(sucursal:Sucursal):
    iban=input("Introduce el IBAN: ")
    cuenta=sucursal.obtener_cuenta(iban)
    return cuenta
#OPCIONES DE CUENTA

def cuenta_operacion(cuenta:Cuenta):
    concepto=input("Concepto: ")
    cantidad=abs(float(input("Cantidad: ")))
    tipo_int=int(input("Tipo:Reintegro(1),Ingreso(2),Transferencia(3): "))
    try:
        tipo=TipoMovimiento(tipo_int)
        if tipo==TipoMovimiento.REINTEGRO:
            cantidad=-cantidad
        movimiento=Movimiento(concepto=concepto,cantidad=cantidad,tipo=tipo)
        cuenta.nuevo_movimiento(movimiento)
        ver_movimiento(movimiento)
        pulsar_continuar()

    except ValueError:
        print("TIpo de movimiento invalido")
    pulsar_continuar()

def cuenta_movimientos(cuenta:Cuenta):
    for movimiento in cuenta.movimientos:
        print(movimiento)
    pulsar_continuar()
def ver_movimiento(movimiento:Movimiento):
    print("Movimiento: ")
    print("\tConcepto: ",movimiento.concepto)
    print("\tTipo: ",movimiento.tipo)
    print("\tCantidad: ",movimiento.cantidad)
    print("\tFecha: ",movimiento.fecha)
    print("\tSaldo: ",movimiento.saldo)
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
                cuenta=seleccion_cuenta(sucursal)
                opcion_cuenta = menu_cuenta(cuenta)
                while opcion_cuenta != "0":
                    match opcion_cuenta:
                        case "1":
                            cuenta_operacion(cuenta)
                        case "3":
                            cuenta_movimientos(cuenta)
                    opcion_cuenta = menu_cuenta(cuenta)
        opcion_sucursal = menu_sucursal()