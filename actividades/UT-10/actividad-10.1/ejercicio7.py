from operator import truediv

import mysql.connector



def connect():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mibasededatos"
    )
    return cnx
def menu_login():
    op_l = ""
    while op_l not in [1, 2]:
        print("1.Iniciar Sesion")
        print("2.Registrarse")
        op_l = int(input("Introduce una opcion: "))
    return op_l
def iniciar_sesion():
    cnx = connect()
    cursor1 = cnx.cursor()

    consulta = (
        "SELECT u.id,u.nombre,u.password "
        "FROM tb_usuarios AS u "
        "WHERE u.nombre = %s and u.password = %s"
    )
    nombre_usuario=input("Introduce tu nombre de usuario: ")
    contrasena=input("Introduce tu contraseña: ")

    cursor1.execute(consulta, (nombre_usuario,contrasena))
    resultado = cursor1.fetchone()

    cursor1.close()
    cnx.close()

    return resultado

def registrarse():
    pass
def menu_usuario():
    op=""
    while op not in [1,2,3]:
        print("1.Ver mis datos")
        print("2.Modificar mis datos")
        print("3.Salir")
        op=int(input("Introduce una opcion: "))
    return op

def ver_datos_usuario(id):
    cnx=connect()
    cursor1 = cnx.cursor()

    consulta = (
         """
    SELECT u.nombre, u.password, u.email, t.nombre_tipo
    FROM tb_usuarios AS u
    INNER JOIN tb_usuarios_tipos AS t ON u.tipo_usuario_id = t.id
    WHERE u.id = %s
    """
    )

    cursor1.execute(consulta, (id,))
    resultado = cursor1.fetchone()
    if resultado:
        nombre,password, email, tipo = resultado
        print(f"{nombre} - {password} - {email} - Tipo: {tipo}")
    else:
        print("Usuario no encontrado")
    cursor1.close()
    cnx.close()

def modificar_usuario():
    cnx = connect()
    cursor1 = cnx.cursor()

    consulta = ("SELECT * FROM tb_usuarios where id=%s")

    id = int(input("Ingrese id de usuario: "))
    datos_consulta = (id,)
    cursor1.execute(consulta, datos_consulta)
    resultados = cursor1.fetchall()
    for (id_usuario, tipo, nombre, email, password, fecha) in resultados:
        print(id_usuario, tipo, nombre, email, password)

    tipo_m = int(input(f"Tipo[{tipo}]: "))
    nombre_m = input(f"Nombre[{nombre}]: ")
    email_m = input(f"Email[{email}]: ")
    password_m = input(f"Password[{password}]: ")

    cursor2 = cnx.cursor()
    consulta2 = ("UPDATE tb_usuarios SET tipo_usuario_id=%s , nombre=%s, email=%s, password=%s WHERE id=%s")
    datos_consulta2 = (tipo_m, nombre_m, email_m, password_m, id)
    cursor2.execute(consulta2, datos_consulta2)

    print("Fila modificada correctamente")
    cnx.commit()
    cursor1.close()
    cnx.close()


while True:
    op_l = menu_login()
    match op_l:
        case 1:
            usuario=iniciar_sesion()
            if usuario:
                print("Inicio de Sesion Correcto...")
                id=usuario[0]
                op = menu_usuario()
                match op:
                    case 1:
                        ver_datos_usuario(id)
                    case 2:
                        modificar_usuario(id)
                    case 3:
                         break
            else:
                print("Usuario o contraseña incorrectos. Volviendo al menú principal...")
        case 2:
            if registrarse():
                print("Registrado correctamente")
            else:
                print("Error al registrarse. Volviendo al menú principal...")



