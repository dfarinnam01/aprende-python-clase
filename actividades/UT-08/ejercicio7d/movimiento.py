from datetime import datetime
from enum import Enum
class TipoMovimiento(Enum):
    REINTEGRO = 1
    INGRESO = 2
    TRANSFERENCIA = 3
class Movimiento:

    def __init__(self,concepto:str,tipo:TipoMovimiento,cantidad:float,saldo:float=0):
        if not isinstance(tipo,TipoMovimiento):
            raise ValueError("Tipo de movimiento invalido")
        self.__concepto = concepto
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__saldo = saldo
        self.__fecha= datetime.now()

    @property
    def tipo(self)->TipoMovimiento:
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo=tipo

    @property
    def concepto(self):
        return self.__concepto
    @concepto.setter
    def concepto(self,concepto):
        self.__concepto=concepto

    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad

    @property
    def saldo(self)->float:
        return self.__saldo
    @saldo.setter
    def saldo(self,saldo:float):
        self.__saldo = saldo
    @property
    def fecha(self)->datetime:
        return self.__fecha
    @fecha.setter
    def fecha(self,fecha:datetime):
        self.__fecha = fecha

    def __str__(self):
        fecha = self.__fecha.strftime("%d/%m/%Y")
        return f"{self.__concepto} {self.__tipo} {self.__cantidad} {self.__saldo} {fecha}"

