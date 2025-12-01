from surcursal import Sucursal
from cuenta import Cuenta
from movimiento import Movimiento
sucursal=Sucursal()
def menu():
    try:
        print("\n1______________Nueva Cuenta")
        print("2______________Hacer Movimiento Ingreso")
        print("3______________Movimiento Reintegro")
        print("4______________Movimiento Transferencia")
        print("5______________ Listado de Movimientos Realizados")
        print("0______________Salir\n")

        opcion = int(input("Selecciona una opción: "))
        return opcion
    except:
        print("OPCION NO VALIDA")
salida=True
while salida:
    opcion = menu()
    if opcion == 1:
        cuenta = Cuenta(input("Introduce el iban: "),
                        input("Introduce el titular principal: "),
                        int(input("Introduce el ingreso inicial: ")))
        sucursal.nueva_cuenta(cuenta)
    elif opcion == 2:
        iban = input("Introduce el IBAN de la cuenta: ")
        cuenta = sucursal.get_cuenta(iban)
        if cuenta:
            movimiento = Movimiento("Ingreso", Movimiento.INGRESO, int(input("Cantidad: ")))
            cuenta.nuevo_movimiento(movimiento)
        else:
            print("Cuenta no encontrada")
    elif opcion == 3:
        movimiento2 = Movimiento("Curso ingles", Movimiento.REINTEGRO, 100)
        cuenta.nuevo_movimiento(movimiento2)
    elif opcion == 4:
        pass
    elif opcion == 5:
        for m in cuenta.get_movimientos():
            print(m)
    else:
        salida=False
