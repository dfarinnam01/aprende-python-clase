import mysql.connector

def connect():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mibasededatos"
    )
    return cnx
def menu():
    op=""
    while op not in [1,2,3,4,5]:
        print("1.Listado de usuarios")
        print("2.Añadir Usuario")
        print("3.Modificar Usuario")
        print("4.Eliminar Usuario")
        print("5.Salir")
        op=int(input("Introduce una opcion: "))
    return op

def listarUsuarios():
    cnx=connect()
    cursor1 = cnx.cursor()

    consulta = (
        "SELECT u.id,u.nombre, u.email, t.nombre_tipo "
        "FROM tb_usuarios AS u "
        "INNER JOIN tb_usuarios_tipos AS t ON u.tipo_usuario_id = t.id "
        "ORDER BY (t.nombre_tipo <> 'administrador'), u.nombre"
    )

    cursor1.execute(consulta)
    resultados = cursor1.fetchall()
    for (id,nombre, email, tipo) in resultados:
        print(f"({id}) {nombre} - ({email}) - {tipo}")

    cursor1.close()
    cnx.close()

def addUsuario():
    cnx = connect()
    cursor1 = cnx.cursor()

    consulta = ("INSERT INTO tb_usuarios (tipo_usuario_id, nombre, email, password)values(%s, %s, %s,%s)")

    tipo = -1
    while tipo != 1 and tipo != 2:
        tipo = int(input("Ingrese tipo de usuario: Admin (1) o Cliente (2) "))
    nombre = input("Ingrese nombre: ")
    email = input("Ingrese email: ")
    password = input("Ingrese password: ")

    datos_consulta = (tipo, nombre, email, password)

    cursor1.execute(consulta, datos_consulta)
    ultimo_id = cursor1.lastrowid
    print(f"último id: {ultimo_id}")

    cnx.commit()
    cursor1.close()
    cnx.close()
def modUsuario():
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
def delUsuario():
    cnx = connect()
    cursor1 = cnx.cursor()

    consulta = ("SELECT * FROM tb_usuarios where id=%s")

    id = int(input("Ingrese id de usuario: "))
    datos_consulta = (id,)
    cursor1.execute(consulta, datos_consulta)
    resultados = cursor1.fetchall()
    id=resultados[0][0]

    cursor2 = cnx.cursor()
    consulta2 = ("DELETE FROM tb_usuarios WHERE id=%s")
    datos_consulta2 = (id,)
    cursor2.execute(consulta2, datos_consulta2)

    print("Fila borrada correctamente")
    cnx.commit()
    cursor1.close()
    cnx.close()


while True:
    op=menu()
    match op:
        case 1:
            listarUsuarios()
        case 2:
            addUsuario()
        case 3:
            modUsuario()
        case 4:
            delUsuario()
        case 5:
            break
