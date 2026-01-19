import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mibasededatos"
)
cursor1 = cnx.cursor()

consulta = ("INSERT INTO tb_usuarios (tipo_usuario_id, nombre, email, password)values(%s, %s, %s,%s)")

tipo=-1
while tipo != 1 and tipo != 2:
    tipo = int(input("Ingrese tipo de usuario: Admin (1) o Cliente (2) "))
nombre=input("Ingrese nombre: ")
email=input("Ingrese email: ")
password=input("Ingrese password: ")

datos_consulta = (tipo, nombre, email, password)

cursor1.execute(consulta,datos_consulta)
ultimo_id = cursor1.lastrowid
print(f"último id: {ultimo_id}")

cnx.commit()
cursor1.close()
cnx.close()
