import lista_usuarios as us
intentos_usuarios = {}

while True:
    usuario_introducido = input("Introduce un usuario: ")
    contrasena_introducida = input("Introduce contraseña: ")

    usuario_encontrado = False

    for usuario in us.lista_usuarios():
        if usuario_introducido == usuario["usuario"]:
            usuario_encontrado = True

    if usuario_encontrado:
        if usuario_introducido not in intentos_usuarios:
            intentos_usuarios[usuario_introducido] = 1
        else:
            intentos_usuarios[usuario_introducido] += 1

        if intentos_usuarios[usuario_introducido] < 4:
            if contrasena_introducida == usuario["contrasena"]:
                print("El usuario es correcto\n")
                intentos_usuarios[usuario_introducido] = 0
            else:
                print("La contraseña no es correcta\n")
        else:
            print("Intentos excedidos\n")
    else:
        print("Usuario no existe\n")