from datetime import datetime
class Movimiento:
    REINTEGRO=1
    INGRESO=2
    TRANSFERENCIA=3
    def __init__(self,concepto,tipo,cantidad,saldo=0):
        if not tipo in [Movimiento.REINTEGRO,Movimiento.INGRESO,Movimiento.TRANSFERENCIA]:
            raise ValueError("Tipo de movimiento invalido")
        self.__concepto = concepto
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__saldo = saldo
        self.__fecha= datetime.now()
    def get_cantidad(self):
        return self.__cantidad
    def set_cantidad(self,cantidad):
        self.__cantidad = cantidad
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self,saldo):
        self.__saldo = saldo
    def __str__(self):
        fecha = self.__fecha.strftime("%d/%m/%Y")
        return f"{self.__concepto} {self.__tipo} {self.__cantidad} {self.__saldo} {fecha}"

