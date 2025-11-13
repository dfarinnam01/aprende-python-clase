#=====================================================
#                    FUNCIONES
#=====================================================
def menu():
    try:
        print("\n1______________Nueva entrada")
        print("2______________Consultar entrada")
        print("3______________Listado entradas")
        print("0______________Salir\n")

        opcion = int(input("Selecciona una opción: "))
        return opcion
    except:
        print("OPCION NO VALIDA")
def nueva_entrada():
    num_entrada = input("Introduce su número de entrada: ")
    if num_entrada not in [dato["entrada"] for dato in datos_entradas]:
        print("Acceso Permitido")
        nombre = input("Ingrese nombre: ")
        dni = input("Ingrese DNI: ")
        mayor_edad = ""
        while mayor_edad != "s" and mayor_edad != "n":
            mayor_edad = input("¿Es mayor de edad? (s/n): ")
        edad = 1 if mayor_edad == "s" else 0
        datos_entradas.append({
            "entrada": num_entrada,
            "nombre": nombre,
            "dni": dni,
            "mayor_edad": edad
        })
def consulta_entrada():
    print("CONSULTA")
    consultar = input("Introduce la entrada que desea consultar: ")
    entrada_encontrada = False
    for dato in datos_entradas:
        if dato["entrada"] == consultar:
            entrada_encontrada = True
    if entrada_encontrada:
        print("Entrada Utilizada")
    else:
        print("Entrada no encontrada")
def listado():
    for dato in datos_entradas:
        print(f"Asistente {dato["nombre"]}", "es mayor de edad" if dato["mayor_edad"] == 1 else "es menor de edad")

#=====================================================

salida=0
datos_entradas = []
while salida!=1:
    opcion=menu()
    match opcion:
        case 1:
            nueva_entrada()
        case 2:
            consulta_entrada()
        case 3:
            listado()
        case 0:
            salida=1
            print("FIN DEL PROGRAMA")