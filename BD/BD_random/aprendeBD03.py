import sqlite3

from huggingface_hub.cli.inference_endpoints import update

db_name = 'librosv3.db'

# Ejemplo de libro válido
libro = {
    "isbn": "45643",
    "titulo": "44",
    "autor": "Autor X",
    "editorial": "Editorial Y",
    "fecha_publicacion": "2024",
    "descripcion": "Libro de prueba"
}

class libroDB:
    def __init__(self):
        self.conexion = sqlite3.connect(db_name)
        self.cursor = self.conexion.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            isbn VARCHAR(15) UNIQUE NOT NULL,
            titulo VARCHAR(255) NOT NULL,
            autor VARCHAR(100) NOT NULL,
            editorial VARCHAR(100) NOT NULL,
            fecha_publicacion VARCHAR(100) NOT NULL,
            descripcion TEXT
        )
        ''')
        self.conexion.commit()

    def add_libros(self, libro):
        sql = """INSERT INTO libros (isbn, titulo, autor, editorial, fecha_publicacion, descripcion)
                 VALUES (?, ?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(sql, (
                libro["isbn"],
                libro["titulo"],
                libro["autor"],
                libro["editorial"],
                libro["fecha_publicacion"],
                libro.get("descripcion", None)
            ))
            self.conexion.commit()
            print("Libro añadido correctamente")
        except Exception as e:
            print(f"Error al añadir libro: {e}")

    def delete_libro(self, id:int)->bool:
        sql = "DELETE FROM libros WHERE id= ?"
        try:
            self.cursor.execute(sql, (id,))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al eliminar libro: {e}")
            return False

    def update_libros(self,id:int, libro:dict)->:
        sql = """
        UPDATE libros
        SET titulo = ?, autor = ?, editorial = ?, fecha_publicacion = ?
        WHERE id = ?
        """
        self.cursor.execute(sql, (libro["titulo"], libro["autor"], libro["editorial"], libro["fecha_publicacion"], libro["isbn"]))
        self.conexion.commit()

    def get_by_isbn(self, isbn):
        self.cursor.execute("SELECT * FROM libros WHERE isbn= ?", (isbn,))
        libro = self.cursor.fetchone()
        return libro
    def filter_by_autor(self, autor):
        self.cursor.execute("SELECT * FROM libros WHERE autor= ?", (autor,))
        libros = self.cursor.fetchall()
        return libros
    def get_libro(self, id:int)->tuple:
        sql = "SELECT id, isbn, titulo, autor, editorial, fecha-publicacion FROM libros WHERE id= ?"
        self.cursor.execute(sql, (id,))
        libro = self.cursor.fetchone()
        return libro
    def get_all_libros(self)->list:
        self.cursor.execute("SELECT id, isbn, titulo, autor, editorial, fecha_publicacion, descripcion FROM libros")
        libros = self.cursor.fetchall()
        return libros

    def close(self):
        self.cursor.close()
        self.conexion.close()


if __name__ == '__main__':
    db = libroDB()
    db.add_libros(libro)
    print(db.get_all_libros())
    db.close()
