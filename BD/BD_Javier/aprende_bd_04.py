import sqlite3


class LibroDB:
    SELECT="SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM libros"
    def __init__(self,db_name="libros2.db"):
        self.conexion = sqlite3.connect(db_name)
        self.conexion.row_factory=sqlite3.Row
        self.cursor = self.conexion.cursor()
        self._crear_tablas()

    def _crear_tablas(self):
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
            return self.cursor.lastrowid
        except Exception as e:
            return 0


    def delete_libro(self,id):
        sql = "DELETE FROM Libros WHERE id=?"
        self.cursor.execute(sql, (id,))
        self.conexion.commit()

    def update_libro(self,id):
        sql="UPDATE libros SET isbn=?,titulo=?, autor=?,editorial=?,fecha_publicacion=? WHERE id=?"
        isbn=input("ISBN: ")
        titulo=input("TITULO: ")
        autor=input("AUTOR: ")
        editorial=input("EDITORIAL: ")
        fecha_publicacion=input("FECHA PUBLICADA: ")
        self.cursor.execute(sql,(isbn,titulo,autor,editorial,fecha_publicacion,id))
        self.conexion.commit()

    def get_libro(self,id)->dict:
        sql = LibroDB.SELECT + " WHERE id=?"
        self.cursor.execute(sql, (id,))
        libro = self.cursor.fetchone()
        return dict(libro)

    def get_all_libros(self)->list:
        sql = LibroDB.SELECT
        self.cursor.execute(sql)
        libros = self.cursor.fetchall()
        libros_dict=[dict(libro) for libro in libros]
        return libros_dict

    def get_by_isbn(self,isbn)->dict:
        sql = "SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM libros WHERE isbn=?"
        self.cursor.execute(sql, (isbn,))
        libro = self.cursor.fetchone()
        return dict(libro)

    def get_filter_autor(self,autor)->dict:
        sql = "SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM libros WHERE autor=?"
        self.cursor.execute(sql, (autor,))
        libros = self.cursor.fetchall()
        return dict(libros)

    def update_by_isbn(self,isbn):
        sql = "UPDATE libros SET titulo=?, autor=?,editorial=?,fecha_publicacion=? WHERE isbn=?"
        isbn = input("ISBN: ")
        titulo = input("TITULO: ")
        autor = input("AUTOR: ")
        editorial = input("EDITORIAL: ")
        fecha_publicacion = input("FECHA PUBLICADA: ")
        self.cursor.execute(sql, (titulo, autor, editorial, fecha_publicacion, isbn))
        self.conexion.commit()

    def delete_by_isbn(self,isbn):
        sql = "DELETE FROM Libros WHERE isbn=?"
        self.cursor.execute(sql, (isbn,))
        self.conexion.commit()


    def close(self):
        self.cursor.close()
        self.conexion.close()

if __name__ == "__main__":
    db=LibroDB()
    db.add_libro({"isbn":231214,"titulo":"Libro 1","editorial":"Paco y yo","autor":"Paco","fecha_publicacion":15})
    for libro in db.get_all_libros():
        print(libro)
    print(db.get_by_isbn(231214))