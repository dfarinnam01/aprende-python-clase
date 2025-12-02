from sucursal import Sucursal
from cuenta import Cuenta
from movimiento import Movimiento


def pedir_cuenta(sucursal):
    iban = input("Introduce IBAN: ")
    cuenta = sucursal.get_cuenta(iban)

    if not cuenta:
        print("Cuenta no encontrada")

    return cuenta


def crear_cuenta(sucursal):
    iban = input("IBAN: ")
    titular = input("Titular principal: ")
    ingreso = float(input("Ingreso inicial: "))

    cuenta = Cuenta(iban, titular, ingreso)
    sucursal.nueva_cuenta(cuenta)

    print("Cuenta creada correctamente")


def hacer_ingreso(sucursal):
    cuenta = pedir_cuenta(sucursal)
    if not cuenta:
        return

    cantidad = float(input("Cantidad a ingresar: "))

    movimiento = Movimiento("Ingreso", Movimiento.INGRESO, cantidad)
    cuenta.nuevo_movimiento(movimiento)

    print("Ingreso realizado")


def hacer_reintegro(sucursal):
    cuenta = pedir_cuenta(sucursal)
    if not cuenta:
        return

    cantidad = float(input("Cantidad a retirar: "))
    print(cuenta.get_saldo())
    if cantidad > cuenta.get_saldo():
        print("Saldo insuficiente")
        return

    movimiento = Movimiento("Reintegro", Movimiento.REINTEGRO, cantidad)
    cuenta.nuevo_movimiento(movimiento)

    print("Reintegro realizado")


def hacer_transferencia(sucursal):
    print("Cuenta origen")
    origen = pedir_cuenta(sucursal)
    if not origen:
        return

    print("Cuenta destino")
    destino = pedir_cuenta(sucursal)
    if not destino:
        return

    cantidad = float(input("Cantidad a transferir: "))

    if cantidad > origen.get_saldo():
        print("Saldo insuficiente")
        return

    mov_origen = Movimiento(
        "Transferencia enviada",
        Movimiento.TRANSFERENCIA,
        cantidad
    )

    mov_destino = Movimiento(
        "Transferencia recibida",
        Movimiento.INGRESO,
        cantidad
    )

    origen.nuevo_movimiento(mov_origen)
    destino.nuevo_movimiento(mov_destino)

    print("Transferencia realizada")


def listar_movimientos(sucursal):
    cuenta = pedir_cuenta(sucursal)
    if not cuenta:
        return

    print("\n--- MOVIMIENTOS ---")
    for m in cuenta.get_movimientos():
        print(m)


def menu():
    print("\n------ MENÚ ------")
    print("1. Crear cuenta")
    print("2. Ingreso")
    print("3. Reintegro")
    print("4. Transferencia")
    print("5. Listar movimientos")
    print("0. Salir")

    return input("Opción: ")
sucursal = Sucursal()

while True:
    opcion = menu()

    if opcion == "1":
        crear_cuenta(sucursal)

    elif opcion == "2":
        hacer_ingreso(sucursal)

    elif opcion == "3":
        hacer_reintegro(sucursal)

    elif opcion == "4":
        hacer_transferencia(sucursal)

    elif opcion == "5":
        listar_movimientos(sucursal)

    elif opcion == "0":
        print("Saliendo del programa")
        break

    else:
        print("Opción no válida")
