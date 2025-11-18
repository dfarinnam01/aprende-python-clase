import lista_usuarios as us

while True:
    usuario_introducido = input("Introduce un usuario: ")
    contrasena_introducida = input("Introduce contraseña: ")

    if not us.exists(usuario_introducido):
        print("Usuario no existe\n")
        continue

    if us.excedidos_intentos(usuario_introducido):
        print("Intentos excedidos\n")
        continue

    if us.login(usuario_introducido, contrasena_introducida):
        print("El usuario es correcto\n")
    else:
        print("La contraseña no es correcta\n")
