import logging
from database import Database


class LibrosDao:
    logger= logging.getLogger('LibrosDao')
    table_name = 'Libros'

    SELECT=f'''SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM {table_name}'''

    def __init__(self):
        self.conn=Database.conect()

    def add(self, libro):
        sql = f"""INSERT INTO {self.table_name} 
                 (isbn, titulo, autor, editorial, fecha_publicacion,descripcion)
                 VALUES (?, ?, ?, ?, ?, ?)"""
        try:
            with self.conn:
                cur= self.conn.execute(sql, (
                    libro.get("isbn",None),
                    libro.get("titulo",None),
                    libro.get("autor",None),
                    libro.get("editorial",None),
                    libro.get("fecha_publicacion",None),
                    libro.get("descripcion",None)
                ))
            self.logger.info(f"Se ha añadido el libro de isbn {libro.get('isbn',None)}")
            return cur.lastrowid
        except Exception as e:
            self.logger.error(f"No se ha añadido el libro de isbn {libro.get('isbn',None)}: {e}")
            return -1

    def get(self, id:int) -> dict:
        with self.conn:
            sql = f"{self.SELECT} WHERE id=?"
            cur= self.conn.execute(sql, (id,))
        row = cur.fetchone()
        return dict(row) if row else None

    def get_all(self)->list:
        with self.conn:
            cur = self.conn.execute(self.SELECT)
            lista = cur.fetchall()
            #libros_dict = [dict(e) for e in lista]
            #libros_dict = [dict(libro) for libro in lista]
            return [dict(row)for row in lista]

    def delete_libro(self,id):
        sql = f"DELETE FROM {self.table_name} WHERE id=?"
        self.cursor.execute(sql, (id,))
        self.conexion.commit()

    def update_libro(self,id):
        sql="UPDATE {table_name} SET isbn=?,titulo=?, autor=?,editorial=?,fecha_publicacion=? WHERE id=?"
        isbn=input("ISBN: ")
        titulo=input("TITULO: ")
        autor=input("AUTOR: ")
        editorial=input("EDITORIAL: ")
        fecha_publicacion=input("FECHA PUBLICADA: ")
        self.cursor.execute(sql,(isbn,titulo,autor,editorial,fecha_publicacion,id))
        self.conexion.commit()





    def get_by_isbn(self,isbn)->dict:
        sql = "SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM {table_name} WHERE isbn=?"
        self.cursor.execute(sql, (isbn,))
        libro = self.cursor.fetchone()
        return dict(libro)

    def get_filter_autor(self,autor)->dict:
        sql = "SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM {table_name} WHERE autor=?"
        self.cursor.execute(sql, (autor,))
        libros = self.cursor.fetchall()
        return dict(libros)

    def update_by_isbn(self,isbn):
        sql = "UPDATE {table_name} SET titulo=?, autor=?,editorial=?,fecha_publicacion=? WHERE isbn=?"
        isbn = input("ISBN: ")
        titulo = input("TITULO: ")
        autor = input("AUTOR: ")
        editorial = input("EDITORIAL: ")
        fecha_publicacion = input("FECHA PUBLICADA: ")
        self.cursor.execute(sql, (titulo, autor, editorial, fecha_publicacion, isbn))
        self.conexion.commit()

    def delete_by_isbn(self,isbn):
        sql = "DELETE FROM {table_name} WHERE isbn=?"
        self.cursor.execute(sql, (isbn,))
        self.conexion.commit()


    def close(self):
        self.cursor.close()
        self.conexion.close()
