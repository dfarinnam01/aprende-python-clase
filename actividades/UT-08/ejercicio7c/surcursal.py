class Sucursal:
    def __init__(self):
        self.__cuentas={}

    def nueva_cuenta(self,cuenta):
        c_iban=cuenta.get_iban()
        self.__cuentas[c_iban]=cuenta
    def get_cuenta(self,iban):
        return self.__cuentas[iban]