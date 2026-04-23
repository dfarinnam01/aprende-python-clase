from services.api_entradas import APIEntradas

if __name__ == '__main__':
    api_entradas = APIEntradas()

    print("Test: Añadir entradas")
    num_entrada= input("Ingrese un numero de entrada: ")
    dni = input("Ingrese DNI: ")

    data = {"num_entrada":num_entrada,"dni":dni}
    status,data =api_entradas.create(data)
    if status == 200:
        entrada= data["entrada"]
        print(f"Entrada guardada con el id {entrada['id']}")
    else:
        print(f"No se ha podido guardar la entrada:{num_entrada}")

    print("-"*30)
    status, data = api_entradas.list_all()
    print(data)

    print("Test: Consultar entrada")
    entrada_id = input("Ingrese un numero de entrada: ")
    status, data = api_entradas.get(entrada_id)
    print(data)
    if (status == 200):
        print(f"Entrada encontrada con el id {entrada_id}")
    else:
        print(f"No se ha podido guardar la entrada:{num_entrada}")
