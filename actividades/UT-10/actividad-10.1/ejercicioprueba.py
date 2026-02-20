import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mibasededatos"
)

cursor1=cnx.cursor()

consulta = "SELECT nombre, email FROM tb_usuarios"

cursor1.execute(consulta)

resultado=cursor1.fetchall()

for (nombre, email) in resultado:
    print(f"{nombre} - ({email})")

#cursor1.commit() si es totalmente otra cosa q no sea un select
cursor1.close()
cnx.close()