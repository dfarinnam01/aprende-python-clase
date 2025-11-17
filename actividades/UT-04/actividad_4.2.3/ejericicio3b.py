# lista_usuarios=["Juan",["1234","Juan@gmail.com"],"Pablo",["4567","Pablo@gmail.com"]]
lista_usuarios=[
{"usuario":"Juan","contrasena":"1234","correo":"juan@gmail.com"},
{"usuario":"Pablo","contrasena":"456","correo":"pablo@gmail.com"}
]
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
        if contrasena==lista_usuarios[usuario]["contrasena"]:
            print("El usuario es correcto\n")
            intentos_usuarios[usuario]=0
        else:
            print("La contraseña no es correcta\n")

    elif usuario not in lista_usuarios:
        print("Usuario no existe\n")
    else:
        print("Intentos excedidos\n")