import sqlite3


class LibroDB:
    def __init__(self,db_name="libros2.db"):
        self.conexion = sqlite3.connect(db_name)
        self.cursor = self.conexion.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Libros (
                id integer PRIMARY KEY AUTOINCREMENT,
                isbn varchar(15) UNIQUE NOT NULL,
                titulo varchar(100) NOT NULL,
                autor varchar(100) NOT NULL,
                editorial varchar(100) NOT NULL,
                fecha_publicacion integer NOT NULL,
                descripcion varchar(100) NULL)
        ''')
        self.conexion.commit()

    def add_libro(self, libro):
        sql = """INSERT INTO Libros 
                 (isbn, titulo, autor, editorial, fecha_publicacion)
                 VALUES (?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(sql, (
                libro["isbn"],
                libro["titulo"],
                libro["autor"],
                libro["editorial"],
                libro["fecha_publicacion"],
            ))
            self.conexion.commit()
            print("Libro guardado exitosamente")
        except Exception as e:
            print(f"Error al añadir el libro: {e}")

    def delete_libro(self,id):
        sql = "SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM libros"
        self.cursor.execute(sql)
        libros = self.cursor.fetchall()
        for libro in libros:
            if libro[0] == id:
                sql = "DELETE FROM Libros WHERE id=?"
                self.cursor.execute(sql, (id,))
                break

    def update_libro(self,id):
        pass

    def get_libro(self,id):
        sql = "SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM libros"
        self.cursor.execute(sql)
        libros = self.cursor.fetchall()
        for libro in libros:
            if libro[0] == id:
                print(libro)
                break
    def get_all_libros(self):
        sql = "SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM libros"
        self.cursor.execute(sql)
        libros = self.cursor.fetchall()
        if len(libros) == 0:
            print("No hay libros")
        else:
            for libro in libros:
                print(libro)

    def close(self):
        pass

if __name__ == "__main__":
    db=LibroDB()
    db.add_libro({"isbn":231214,"titulo":"Libro 1","editorial":"Paco y yo","autor":"Paco","fecha_publicacion":15})
    db.get_all_libros()
    db.get_libro(1)
    db.delete_libro(1)
    db.get_all_libros()
