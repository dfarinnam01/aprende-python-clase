import lista_usuarios as us

acceso_permitido=False
while not acceso_permitido:
    usuario_introducido = input("Introduce un usuario: ")
    contrasena_introducida = input("Introduce contraseña: ")

    usuario = us.get(usuario_introducido)
    if usuario and us.login(usuario_introducido, contrasena_introducida):
        if us.get_intentos(usuario_introducido) < us.INTENTOS_MAX - 1:
            us.reset_intentos(usuario_introducido)
            print("Acceso Permitido")
            acceso_permitido=True
        else:
            print("El usuario estaba bloqueado")
    elif usuario:
        if us.excedidos_intentos(usuario_introducido):
            print("El usuario bloqueado")
        else:
            us.inc_intentos(usuario_introducido)
            print("Credenciales incorrectas")
    else:
        print("El usuario no existe")


# while True:
#     usuario_introducido = input("Introduce un usuario: ")
#     contrasena_introducida = input("Introduce contraseña: ")
#
#     usuario= us.get(usuario_introducido)
#     if usuario and us.login(usuario_introducido,contrasena_introducida):
#         if us.get_intentos(usuario_introducido)< us.INTENTOS_MAX -1:
#             us.reset_intentos(usuario_introducido)
#             print("Acceso Permitido")
#         else:
#             print("El usuario estaba bloqueado")
#     elif usuario:
#         if us.get_intentos(usuario_introducido)>= us.INTENTOS_MAX -1:
#             print("El usuario bloqueado")
#         else:
#             us.inc_intentos(usuario_introducido)
#             print("Credenciales incorrectas")
#     else:
#         print("El usuario no existe")

