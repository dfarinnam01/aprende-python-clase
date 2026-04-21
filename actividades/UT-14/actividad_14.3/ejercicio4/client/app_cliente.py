from services.api_entradas import APIEntradas
def menu():
    op = "X"
    while op not in ["0" ,"1", "2", "3"]:
        print("-"*30)
        print("1.Añade una entrada")
        print("2.Listado de entradas")
        print("3.Consulta una entrada")
        print("0.Salir")
        op=input("Introduce una opcion: ")
        print("-" * 30)
    return op

def nueva_entrada():
    entrada=input("Introduce una entrada: ")
    status, data = api_entradas.create(entrada)
    if status == 200:
        print(f"Entrada guardada")
    else:
        print(f"No se ha podido guardar la entrada:{entrada}")

def listar():
    print("Listado de entradas")
    status, data = api_entradas.list_all()
    for entrada in data:
        print(f"{entrada}")

def consulta():
    id_entrada=int(input("Introduce el id de entrada: "))
    status, data = api_entradas.get(id_entrada)
    if status == 200:
        print(f"La entrada con id {id_entrada} es: {data["entrada"]}")
    else:
        print("Esa entrada no existe")


if __name__ == '__main__':
    api_entradas=APIEntradas()
    opcion="X"
    while opcion!="0":
        opcion = menu()
        match opcion:
            case "1":
                nueva_entrada()
            case "2":
                listar()
            case "3":
                consulta()