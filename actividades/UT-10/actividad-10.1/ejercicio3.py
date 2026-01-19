import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mibasededatos"
)
cursor1 = cnx.cursor()

consulta = (
    "SELECT u.nombre, u.email, t.nombre_tipo "
    "FROM tb_usuarios AS u "
    "INNER JOIN tb_usuarios_tipos AS t ON u.tipo_usuario_id = t.id "
    "ORDER BY (t.nombre_tipo <> 'administrador'), u.nombre"
)

cursor1.execute(consulta)
resultados = cursor1.fetchall()
for (nombre, email, tipo) in resultados:
    print(f"{nombre} - ({email}) - {tipo}")

cursor1.close()
cnx.close()
