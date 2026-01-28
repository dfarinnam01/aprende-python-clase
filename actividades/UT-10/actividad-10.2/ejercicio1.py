import re


regex_nombre = re.compile(
    r'^(?=.{10,30}$)([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)(\s[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+$'
)

regex_direccion = re.compile(
    r'^([A-Za-zÁÉÍÓÚÑáéíóúñ\s]+),\s*(\d+)\s*\(([^)]+)\)$'
)

regex_dni = re.compile(
    r'^(\d{8,9})[-\s]?([A-Za-z])$'
)



nombre = input("Introduce tu nombre completo: ")
direccion = input("Introduce tu dirección (Calle, número (localidad)): ")
dni = input("Introduce tu DNI (opcional, pulsa ENTER para omitir): ")

errores = []


if not regex_nombre.match(nombre):
    errores.append("Nombre incorrecto")

match_direccion = regex_direccion.match(direccion)
if not match_direccion:
    errores.append("Dirección incorrecta")

match_dni = None
if dni.strip():
    match_dni = regex_dni.match(dni)
    if not match_dni:
        errores.append("DNI incorrecto")



if errores:
    print("\nERRORES EN LOS DATOS:")
    for error in errores:
        print("-", error)
else:
    calle, numero, localidad = match_direccion.groups()

    print("\nTUS DATOS SON:\n")
    print(f"Nombre: {nombre}")
    print(f"Calle: {calle}")
    print(f"Número: {numero}")
    print(f"Localidad: {localidad}")

    if match_dni:
        dni_limpio = match_dni.group(1) + match_dni.group(2).upper()
        print(f"DNI: {dni_limpio}")
