lista_usuarios={"Juan":"1234","Pablo":"4567"}
intentos_usuarios={}
while True:
    usuario = input("Introduce un usuario: ")
    contrasena=input("Introduce contraseña: ")
    if usuario in lista_usuarios:
        if usuario not in intentos_usuarios:
            intentos_usuarios[usuario] = 1
        else:
            intentos_usuarios[usuario] += 1

    if usuario in lista_usuarios and intentos_usuarios[usuario]<4:
        if contrasena==lista_usuarios[usuario]:
            print("El usuario es correcto\n")
            intentos_usuarios[usuario]=0
        else:
            print("La contraseña no es correcta\n")

    elif usuario not in lista_usuarios:
        print("Usuario no existe\n")
    else:
        print("Intentos excedidos\n")