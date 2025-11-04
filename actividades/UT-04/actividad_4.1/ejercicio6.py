USUARIO_VALIDO="David"
CONTRASENA_VALIDA="1234"

usuario=input("Ingresa un usuario: ")
contrasena=input("Introduce la contraseña: ")
if usuario==USUARIO_VALIDO and contrasena==CONTRASENA_VALIDA:
    print("Acceso concedido")
else:
    print("Acceso denegado")