libros = []
def menu():
    try:
        print("\n1______________Nueva libro")
        print("2______________Consultar libro")
        print("3______________Listado de libros")
        print("4______________Borrar libro")
        print("0______________Salir\n")

        opcion = int(input("Selecciona una opción: "))
        return opcion
    except:
        print("OPCION NO VALIDA")
def nuevo_libro():
    isbn = input("Introduce ISBN del libro: ")
    if isbn not in [libro["isbn"] for libro in libros]:
        titulo = input("Ingrese titulo del libro: ")
        autor = input("Ingrese autor: ")
        libros.append({
            "isbn": isbn,
            "titulo": titulo,
            "autor": autor
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

if __name__ == "__main__":
    help(menu)

    # datos_entradas = []
    # nueva_entrada()
    # listado()