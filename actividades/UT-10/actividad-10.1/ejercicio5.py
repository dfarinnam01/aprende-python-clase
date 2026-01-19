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
print(id_usuario)

consulta2 = ("UPDATE tb_usuarios SET tipo=%s , nombre=%s, email=%s, password=%s, fecha=%s WHERE id=%s")

cnx.commit()
cursor1.close()
cnx.close()
