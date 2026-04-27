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

    peticion(f"Consulta completa de token:")
    data = auth.token_full_info()
    respuesta(f"""Resultado de la peticion:
                       status: {status}
                       data: {data}""")
    print("-" * 80)

    peticion(f"Consulta simple de token:")
    data = auth.token_simple_info()
    respuesta(f"""Resultado de la peticion:
                          status: {status}
                          data: {data}""")
    print("-" * 80)

    peticion("Registro de usuarios:")
    username = input("Username: ")
    password = input("Password: ")
    data = auth.register(username, password)
    respuesta(f"""Resultado de la peticion:
                 data: {data}""")
    print("-" *40)

    peticion("Listado de usuarios:")
    status, data = auth.users()
    respuesta(f"""Resultado de la peticion:""")
    respuesta(f"status: {status}")
    respuesta(f"data: {data}")
    if status == 200:
        for user in data['users']:
            respuesta(user)
    else:
        respuesta("Operacion no realizada",status)
    print("-" * 40)

