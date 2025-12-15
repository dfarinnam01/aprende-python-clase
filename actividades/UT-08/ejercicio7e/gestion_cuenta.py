from cuenta import Cuenta
from movimiento import Movimiento,TipoMovimiento
from menu import pulsar_continuar
from codigos_ansi import CodigosAnsi as CA

def _titulo(titulo):
    CA.activa(CA.BLUE)
    CA.activa(CA.BG_WHITE)
    print('='*20,titulo,'='*20)
    CA.desactiva()
    print()

def cuenta_operacion(cuenta:Cuenta):
    _titulo("NUEVO MOVIMIENTO")
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
    _titulo("MOVIMIENTOS")
    print(f"{'Concepto':<30} {'Tipo':12} {'Cantidad':<10} {'Fecha':17} {'Saldo':<10}")
    print("-"*79)
    for m in cuenta.movimientos:
        fecha= m.fecha.strftime("%d/%m/%Y %H:%M")
        concepto= m.concepto if len(m.concepto)<=25 else m.concepto[0:25]+"..."
        print(f"{concepto[0:29]:<30} {m.tipo.name.capitalize():12} {m.cantidad:<10} {fecha:17} {m.saldo:<10}")
    pulsar_continuar()
def ver_movimiento(movimiento:Movimiento):
    print("Movimiento: ")
    print("\tConcepto: ",movimiento.concepto)
    print("\tTipo: ",movimiento.tipo)
    print("\tCantidad: ",movimiento.cantidad)
    print("\tFecha: ",movimiento.fecha)
    print("\tSaldo: ",movimiento.saldo)