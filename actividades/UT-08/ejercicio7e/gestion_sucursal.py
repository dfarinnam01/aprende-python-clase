from sucursal import Sucursal
from cuenta import Cuenta
from menu import pulsar_continuar
from codigos_ansi import CodigosAnsi as CA

def _titulo(titulo):
    CA.activa(CA.BLUE)
    CA.activa(CA.BG_WHITE)
    print('='*20,titulo,'='*20)
    CA.desactiva()
    print()
def nueva_cuenta(sucursal:Sucursal):
    _titulo('NUEVA CUENTA')
    # print(f'{CA.texto_color('IBAN',CA.GREEN)}',end="")
    CA.print_texto_color('IBAN: ',CA.GREEN)
    iban=input()
    titular=input("Introduce el titular: ")
    ingreso=float(input("Introduce el ingreso: "))

    try:
        cuenta=Cuenta(iban=iban,titular_principal=titular,ingreso=ingreso)
        sucursal.nueva_cuenta(cuenta)
        CA.print_texto_color('Cuenta añadida con exito: ', CA.YELLOW,end="\n")
    except Exception as e:
        print("-"*50)
        CA.print_texto_color(str(e),CA.RED, end="\n")
        print("-"*50)
    pulsar_continuar()
def listado_cuentas(sucursal:Sucursal):
    for iban,cuenta in sucursal.cuentas.items():
        print("IBAN: ",iban,"\tTITULAR: ",cuenta.titulares[0])
    pulsar_continuar()

def seleccion_cuenta(sucursal:Sucursal):
    iban=input("Introduce el IBAN: ")
    cuenta=sucursal.obtener_cuenta(iban)
    return cuenta
