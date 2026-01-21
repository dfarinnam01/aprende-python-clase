import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mibasededatos"
)
cursor1 = cnx.cursor()

consulta = ("SELECT * FROM tb_usuarios where id=%s")

id=int(input("Ingrese id de usuario: "))
datos_consulta = (id,)
cursor1.execute(consulta,datos_consulta)
resultados = cursor1.fetchall()
for (id_usuario, tipo, nombre, email, password,fecha) in resultados:
    print(id_usuario, tipo,nombre, email,password)


tipo_m=int(input(f"Tipo[{tipo}]: "))
nombre_m=input(f"Nombre[{nombre}]: ")
email_m=input(f"Email[{email}]: ")
password_m=input(f"Password[{password}]: ")

cursor2 = cnx.cursor()
consulta2 = ("UPDATE tb_usuarios SET tipo_usuario_id=%s , nombre=%s, email=%s, password=%s WHERE id=%s")
datos_consulta2 = (tipo_m, nombre_m, email_m, password_m,id)
cursor2.execute(consulta2,datos_consulta2)

print("Fila modificada correctamente")
cnx.commit()
cursor1.close()
cnx.close()
