import sqlite3

DATABASE_NAME = 'libros.db'
conexion = sqlite3.connect(DATABASE_NAME)
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Libros (
        id integer PRIMARY KEY AUTOINCREMENT,
        isbn varchar(15) UNIQUE NOT NULL,
        titulo varchar(100) NOT NULL,
        autor varchar(100) NOT NULL,
        editorial varchar(100) NOT NULL,
        fecha_publicacion integer NOT NULL,
        descripcion varchar(100) NULL)
''')
conexion.commit()
isbn = input('ISBN: ')
titulo = input('TITULO: ')
autor = input('Autor: ')
editorial = input('Editorial: ')
fecha_publicacion = input('Fecha publicacion: ')
sql = """INSERT INTO libros(isbn,titulo,autor,editorial,fecha_publicacion)
            VALUES(?,?,?,?,?)"""
try:
    cursor.execute(sql,(isbn,titulo,autor,editorial,fecha_publicacion))
    conexion.commit()
    print('Libro guardado exitosamente')
except Exception as e:
    print(f"Error al añadir el libro: {e}")
sql="SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM libros"
cursor.execute(sql)
libros = cursor.fetchall()
print("----Prueba 1-------")
print(libros)
print("-----------")
print("----Prueba 2-------")
print(libros[0])
print("-----------")
print("----Prueba 3-------")
for libro in libros:
    print(libro)
print("-----------")
print("----Prueba 4-------")
for libro in libros:
    print(libro[0],libro[1])
print("-----------")
cursor.close()
conexion.close()