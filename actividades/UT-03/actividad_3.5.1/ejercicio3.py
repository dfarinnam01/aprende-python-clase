usuario=input("Introduce su usuario: ")
contrasena=input("Introduce contraseña: ")
contrasena2=input("Introduce de nuevo la contraseña: ")

if usuario=="":
    print("Debe indicar el usuario")
elif contrasena=="" or contrasena2=="":
    print("La contraseña no puede estar vacia")
elif contrasena!=contrasena2:
    print("Las contraseñas no coinciden")
else:
    print("Usuario registrado correctamente")