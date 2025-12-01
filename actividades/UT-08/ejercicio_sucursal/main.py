from sucursal import Sucursal

sucursal = Sucursal()

# Cuentas de ejemplo
sucursal.crear_cuenta("ES01", "Juan Pérez")
sucursal.crear_cuenta("ES02", "Ana López")

while True:
    print("\n====== MENÚ ======")
    print("1. Ingresar")
    print("2. Retirar")
    print("3. Transferir")
    print("4. Mostrar cuentas")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        iban = input("IBAN: ")
        cuenta = sucursal.buscar_cuenta(iban)

        if cuenta:
            fecha = input("Fecha del movimiento: ")
            cantidad = float(input("Cantidad a ingresar: "))
            cuenta.ingresar(fecha, cantidad)
            print("✅ Ingreso realizado")
        else:
            print("❌ Cuenta no encontrada")

    elif opcion == "2":
        iban = input("IBAN: ")
        cuenta = sucursal.buscar_cuenta(iban)

        if cuenta:
            fecha = input("Fecha del movimiento: ")
            cantidad = float(input("Cantidad a retirar: "))
            cuenta.retirar(fecha, cantidad)
        else:
            print("❌ Cuenta no encontrada")

    elif opcion == "3":
        iban_origen = input("IBAN origen: ")
        iban_destino = input("IBAN destino: ")

        origen = sucursal.buscar_cuenta(iban_origen)
        destino = sucursal.buscar_cuenta(iban_destino)

        if origen and destino:
            fecha = input("Fecha del movimiento: ")
            cantidad = float(input("Cantidad a transferir: "))
            origen.transferir(fecha, destino, cantidad)
        else:
            print("❌ Alguna cuenta no existe")

    elif opcion == "4":
        sucursal.mostrar_todas()

    elif opcion == "0":
        print("👋 Saliendo del programa")
        break

    else:
        print("❌ Opción inválida")
