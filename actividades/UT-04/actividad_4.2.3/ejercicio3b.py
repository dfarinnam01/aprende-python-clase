lista_usuarios = [
    {"usuario": "Juan", "contrasena": "1234", "correo": "juan@gmail.com"},
    {"usuario": "Pablo", "contrasena": "456", "correo": "pablo@gmail.com"}
]

intentos_usuarios = {}

while True:
    usuario_introducido = input("Introduce un usuario: ")
    contrasena_introducida = input("Introduce contraseña: ")

    usuario_encontrado = False
    usuario_valido =""

    for usuario in lista_usuarios:
        if usuario_introducido == usuario["usuario"]:
            usuario_encontrado = True
            usuario_valido = usuario

    if usuario_encontrado:
        if usuario_introducido not in intentos_usuarios:
            intentos_usuarios[usuario_introducido] = 1
        else:
            intentos_usuarios[usuario_introducido] += 1

        if intentos_usuarios[usuario_introducido] < 4:
            if contrasena_introducida == usuario_valido["contrasena"]:
                print("El usuario es correcto\n")
                intentos_usuarios[usuario_introducido] = 0
            else:
                print("La contraseña no es correcta\n")
        else:
            print("Intentos excedidos\n")
    else:
        print("Usuario no existe\n")