from cuenta import Cuenta
class Sucursal:
    def __init__(self):
        self.__cuentas={}

    def nueva_cuenta(self,cuenta):
        if cuenta.iban not in self.__cuentas:
            self.__cuentas[cuenta.iban]=cuenta
        else:
            raise Exception("Cuenta ya existente")
    @property
    def cuentas(self)->dict[str,Cuenta]:
        return self.__cuentas
    @cuentas.setter
    def cuentas(self,cuentas:dict):
        self.__cuentas=cuentas