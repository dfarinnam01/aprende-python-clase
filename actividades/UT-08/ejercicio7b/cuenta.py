from movimiento import Movimiento


class Cuenta:
    def __init__(self, iban, titular):
        self.iban = iban
        self.titular = titular
        self.saldo_actual = 0
        self.movimientos = []

    def ingresar(self, fecha, cantidad, concepto="Ingreso"):
        self.saldo_actual += cantidad
        self.movimientos.append(
            Movimiento(fecha, concepto, "INGRESO", cantidad)
        )

    def retirar(self, fecha, cantidad, concepto="Retiro"):
        if cantidad > self.saldo_actual:
            print("Saldo insuficiente")
            return False

        self.saldo_actual -= cantidad
        self.movimientos.append(
            Movimiento(fecha, concepto, "RETIRO", cantidad)
        )
        return True

    def transferir(self, fecha, cuenta_destino, cantidad):
        if cantidad > self.saldo_actual:
            print("Saldo insuficiente")
            return False

        self.saldo_actual -= cantidad
        self.movimientos.append(
            Movimiento(
                fecha,
                f"Transferencia a {cuenta_destino.iban}",
                "TRANSFERENCIA",
                cantidad
            )
        )

        cuenta_destino.saldo_actual += cantidad
        cuenta_destino.movimientos.append(
            Movimiento(
                fecha,
                f"Transferencia desde {self.iban}",
                "TRANSFERENCIA",
                cantidad
            )
        )

        print("Transferencia realizada")
        return True

    def mostrar(self):
        print("\n--------------------------")
        print(f"IBAN: {self.iban}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo_actual}€")

        print("\nMOVIMIENTOS:")
        if not self.movimientos:
            print("   Sin movimientos")
        else:
            for mov in self.movimientos:
                print("  ", mov)