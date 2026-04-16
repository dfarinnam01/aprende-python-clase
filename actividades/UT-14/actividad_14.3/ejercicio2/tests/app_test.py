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

