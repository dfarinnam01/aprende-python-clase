import mysql.connector
from faker import Faker

#pip install mysql-connector-python faker
#pip3 install mysql-connector-python faker

# Crear objeto faker
fake = Faker()

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="192.168.60.54",
    port=33060,
    user="cepy",
    password="castelar2026",
    database="aprende01"
)

cursor = conexion.cursor()

# Insertar 100 registros
sql_insert = "INSERT INTO libros (isbn) VALUES (%s)"

for i in range(4):
    isbn = fake.isbn13()
    cursor.execute(sql_insert, (isbn,))

conexion.commit()

print("Se insertaron 100 registros correctamente\n")

# Listado de registros
cursor.execute("SELECT id, isbn FROM libros")

print("LISTADO DE LIBROS")
print("------------------")

for fila in cursor.fetchall():
    print(f"ID: {fila[0]}  ISBN: {fila[1]}")

# Cerrar conexión
cursor.close()
conexion.close()