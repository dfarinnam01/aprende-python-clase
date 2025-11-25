class CuentaBancaria:
    iban="ES"
    def __init__(self, nombre,dinero,iban):
        self.nombre = nombre
        self.dinero = dinero
        self.iban = CuentaBancaria.iban +iban

    def depositar (self, dinero):
        self.dinero += dinero

    def retirar(self,dinero):
        self.dinero= max(self.dinero - dinero,0)
    def saldo(self):
        return f"Tu saldo actualmente es de {self.dinero}"
    def transferencia(self,cuenta,dinero):
       pass


#clase sucursal con un listado de cuentas   Tipo movimiento: ingreso, retirar y transeferencia
#cada cuenta va a tener saldo_actual,iban titulares y movimientos(fecha,concepto,tipo,cantidad)
#dar de alta cuenta todo esto con un menu por ejemplo 1 Ingresar 2 Retirar 3 Tranferencia