from services.api_entradas import APIEntradas
from services.api_auth import APIAuth
CIAN = "\033[96m"
AZUL = "\033[94m"
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
RESET = "\033[0m"

def titulo(texto):
    print(f"{AZUL}{texto}{RESET}")
def peticion(texto):
    print(f"{CIAN}{texto}{RESET}")
def respuesta(texto):
    print(f"{VERDE}{texto}{RESET}")


if __name__ == "__main__":

    auth = APIAuth()
    api_entradas=APIEntradas()

    titulo("Test API AUTH")
    titulo("="*80)

    peticion("Registro solo en desarrollo:")
    username= input("Username: ")
    password = input("Password: ")
    rol= input("Rol:(ADMIN,USER): ")
    status,data = auth.register_developer(username, password,rol)
    respuesta(f"""Resultado de la peticion:
                status: {status}
                data: {data}""")

    print("-"*80)



    peticion(f"Login {username}:")
    status, data = auth.login(username, password)
    respuesta(f"""Resultado de la peticion:
                    status: {status}
                    data: {data}""")
    print("-" * 80)

    peticion("Listado de entradas:")
    status, data = api_entradas.list_all()
    respuesta(data)

    api_entradas.token = auth.token
    peticion("Crear Entrada")

    num_entrada= input("Num entrada: ")
    dni=input("DNI: ")
    json={"num_entrada":num_entrada,"dni":dni}
    status, data = api_entradas.create(json)
    if status == 201:
        entrada = data.get("entrada")
        respuesta(f"Entrada guardada con id {entrada['id']}")
    else:
        respuesta(f"Error al crear entrada: {data}")
    print("-"*80)

    peticion("Listado de entradas:")
    status, data = api_entradas.list_all()
    respuesta(data)
    print("-" * 80)

    peticion("Actualizar entradas:")

    id=int(input("ID: "))
    num_entrada = input("Num entrada: ")
    dni = input("DNI: ")
    json = {"num_entrada": num_entrada, "dni": dni}
    status, data = api_entradas.update(id,data)
    respuesta(data)
    print("-"*80)

    peticion("Eliminar entrada:")
    id = int(input("Introduce ID: "))
    status, data = api_entradas.delete(id)
    respuesta(data)
    print("-" * 80)

    peticion("Listado de entradas:")
    status, data = api_entradas.list_all()
    respuesta(data)
    print("-" * 80)