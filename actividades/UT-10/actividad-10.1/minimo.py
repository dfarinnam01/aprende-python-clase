import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mibasededatos"
)
cursor1 = cnx.cursor()

consulta = ()

cursor1.execute(consulta)
resultados = cursor1.fetchall()

cursor1.close()
cnx.close()
