from services.api_entradas import APIEntradas

if __name__ == '__main__':
    api_entradas = APIEntradas()
    print("Test: Añadir entradas")
    num_entrada= input("Ingrese un numero de entrada: ")
    status,data =api_entradas.create(num_entrada)
    if status == 200:
        print(f"Entrada guardada con el id {data['posicion']}")
    else:
        print(f"No se ha podido guardar la entrada:{num_entrada}")

    print("-"*30)
    num_entrada = input("Ingrese un numero de entrada: ")
    status, data = api_entradas.list_all()
    print(data)

    print("Test: Consultar entrada")
    entrada_id = input("Ingrese un numero de entrada: ")
    status, data = api_entradas.get(entrada_id)
    print(data)
    if (status == 200):
        print(f"Entrada guardada")
    else:
        print(f"No se ha podido guardar la entrada:{num_entrada}")
