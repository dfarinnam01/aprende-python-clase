from movimiento import Movimiento

class Cuenta:
    def __init__(self, iban,titular_principal,ingreso):
        self.__iban=iban
        self.__titulares=[titular_principal]
        self.__movimientos=[]

        movimiento=Movimiento(
            concepto=f'Creacion de la cuenta - {titular_principal}',
            tipo=Movimiento.INGRESO,
            cantidad=ingreso,
        )
        self.__movimientos.append(movimiento)
    def nuevo_titular(self,titular):
            self.__titulares.append(titular)

    def nuevo_movimiento(self, movimiento):
        nuevo_saldo = self.__movimientos[-1].get_saldo() + movimiento.get_cantidad()
        movimiento.set_saldo(nuevo_saldo)
        self.__movimientos.append(movimiento)
    def get_iban(self):
        return self.__iban
    def get_movimientos(self):
        return self.__movimientos