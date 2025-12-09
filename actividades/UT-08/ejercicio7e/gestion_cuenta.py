from cuenta import Cuenta
from movimiento import Movimiento,TipoMovimiento
from menu import pulsar_continuar

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