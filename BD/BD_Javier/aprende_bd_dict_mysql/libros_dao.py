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
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        try:
            with self.conn:
                cursor=self.conn.cursor()
                cursor.execute(sql, (
                    libro.get("isbn",None),
                    libro.get("titulo",None),
                    libro.get("autor",None),
                    libro.get("editorial",None),
                    libro.get("fecha_publicacion",None),
                    libro.get("descripcion",None)
                ))
            #self.conn.commit()
            cursor.close()
            last_id = cursor.lastrowid
            self.logger.info(f"Se ha añadido el libro de isbn {libro.get('isbn',None)} con el id {last_id}")
            return last_id
        except Exception as e:
            self.logger.error(f"No se ha añadido el libro de isbn {libro.get('isbn',None)}: {e}")
            return -1

    def add_list(self, libros):
        sql = f"""INSERT INTO {self.table_name} 
                         (isbn, titulo, autor, editorial, fecha_publicacion,descripcion)
                         VALUES (%s, %s, %s, %s, %s, %s)"""
        datos=[(libro.get("isbn",None),libro.get("titulo",None),libro.get("autor",None),libro.get("editorial",None),
               libro.get("fecha_publicacion",None),libro.get("descripcion",None)) for libro in libros]

        try:
            with self.conn:
                cur = self.conn.execute(sql, datos)
                return cur.rowcount
        except Exception as e:
            self.logger.error(f"No se pudieron añadir los libros: {e}")
            return 0

    def delete(self,id):
        sql = f"DELETE FROM {self.table_name} WHERE id=?"
        try:
            with self.conn:
                self.conn.execute(sql, (id,))
                self.logger.info(f"Se ha eliminado el libro {id}")
                return True
        except Exception as e:
            self.logger.error(f"No se ha eliminado el libro {id}: {e}")
            return False

    def delete_by_isbn(self,isbn):
        sql = f"DELETE FROM {self.table_name} WHERE isbn=?"
        try:
            with self.conn:
                self.conn.execute(sql, (isbn,))
                self.logger.info(f"Se ha eliminado el libro {isbn}")
                return True
        except Exception as e:
            self.logger.error(f"No se ha eliminado el libro {isbn}: {e}")
            return False

    def delete_all(self):
        sql = f"DELETE FROM {self.table_name} WHERE 1"
        try:
            with self.conn:
                self.conn.execute(sql)
                self.logger.info(f"Se han eliminado todos los libros")
                return True
        except Exception as e:
            self.logger.error(f"No se han eliminadon todos los libros: {e}")
            return False


    def update_libro(self,id,libro):
        sql = "UPDATE {table_name} SET titulo=?, autor=?,editorial=?,fecha_publicacion=? WHERE id=?"
        try:
            with self.conn:
                cur = self.conn.execute(sql, (
                    libro.get("isbn"),
                    libro.get("titulo"),
                    libro.get("autor"),
                    libro.get("editorial"),
                    libro.get("fecha_publicacion"),
                    libro.get("descripcion"),
                    id
                ))
                return cur.rowcount
        except Exception as e:
            self.logger.error(e)
            return -1

    def update_by_isbn(self, isbn, libro):
        sql = "UPDATE {table_name} SET titulo=?, autor=?,editorial=?,fecha_publicacion=? WHERE isbn=?"
        try:
            with self.conn:
                cur = self.conn.execute(sql, (
                    libro.get("isbn"),
                    libro.get("titulo"),
                    libro.get("autor"),
                    libro.get("editorial"),
                    libro.get("fecha_publicacion"),
                    libro.get("descripcion"),
                    isbn
                ))
                return cur.rowcount
        except Exception as e:
            self.logger.error(e)
            return -1

    def get(self, id:int) -> dict:
        with self.conn:
            sql = f"{self.SELECT} WHERE id=?"
            cur= self.conn.execute(sql, (id,))
        row = cur.fetchone()
        return dict(row) if row else None

    def get_by_isbn(self,isbn)->dict:
        with self.conn:
            sql = f"{self.SELECT} WHERE isbn=?"
            cur = self.conn.execute(sql, (isbn,))
        row = cur.fetchone()
        return dict(row) if row else None

    def get_all(self)->list:
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.SELECT)
            libros = cursor.fetchall()
            cursor.close()
            return libros
        except Exception as e:
            self.logger.error(e)
            return []


    def get_filter_autor(self,autor)->list:
        with self.conn:
            sql = f"{self.SELECT} WHERE autor=?"
            cur= self.conn.execute(sql, (autor,))
            return [dict(libro) for libro in cur.fetchall()]
