from cuenta import Cuenta

class Sucursal:
    def __init__(self):
        self.cuentas = []

    def crear_cuenta(self, iban, titular):
        self.cuentas.append(Cuenta(iban, titular))

    def buscar_cuenta(self, iban):
        for c in self.cuentas:
            if c.iban == iban:
                return c
        return None

    def mostrar_todas(self):
        if not self.cuentas:
            print("No hay cuentas creadas.")
            return

        for c in self.cuentas:
            c.mostrar()
