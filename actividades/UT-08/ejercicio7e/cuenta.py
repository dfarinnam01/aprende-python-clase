from movimiento import Movimiento,TipoMovimiento

class Cuenta:
    def __init__(self, iban:str,titular_principal:str,ingreso:float):
        self.__iban=iban
        self.__titulares=[titular_principal]
        self.__movimientos=[]
        movimiento=Movimiento(
            concepto=f'Creacion de la cuenta - {titular_principal}',
            tipo=TipoMovimiento.INGRESO,
            cantidad=ingreso,
            saldo=ingreso,
        )
        self.__movimientos.append(movimiento)
    def nuevo_titular(self,titular:str):
            self.__titulares.append(titular)

    def nuevo_movimiento(self, movimiento:Movimiento):
        movimiento.saldo = self.__movimientos[-1].saldo + movimiento.cantidad
        self.__movimientos.append(movimiento)

    @property
    def iban(self)->str:
        return self.__iban
    @iban.setter
    def iban(self,iban:str):
        self.__iban=iban

    @property
    def titulares(self)->list:
        return self.__titulares
    @titulares.setter
    def titulares(self,titulares:list):
        self.__titulares = titulares
    @property
    def movimientos(self)->list:
        return self.__movimientos
    @movimientos.setter
    def movimientos(self,cuentas:list):
        self.__movimientos = cuentas