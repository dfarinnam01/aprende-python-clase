datos_entradas = []
opcion = -1

while opcion != 0:
    print("\n1______________Nueva entrada")
    print("2______________Consultar entrada")
    print("3______________Listado entradas")
    print("0______________Salir\n")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
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
        else:
            print("Acceso Denegado")

    elif opcion == 2:
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
    elif opcion == 3:
        for dato in datos_entradas:
            print(f"Asistente {dato["nombre"]}", "es mayor de edad" if dato["mayor_edad"]==1 else "es menor de edad")
    elif opcion == 0:
        print("FIN DEL PROGRAMA")
    else:
        print("No has elegido un número del menú")