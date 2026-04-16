import logging
from .database import Database


class LibrosDao:
    logger = logging.getLogger(__name__)
    table_name = "libros"

    SELECT = f"""
        SELECT id, isbn, titulo, fecha_publicacion, descripcion, editorial_id
        FROM {table_name}
    """

    def add(self, libro: dict) -> int:
        sql = f"""INSERT INTO {self.table_name} 
                  (isbn, titulo, fecha_publicacion, descripcion, editorial_id)
                  VALUES (%s, %s, %s, %s, %s)"""

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, (
                libro.get('isbn'),
                libro.get('titulo'),
                libro.get('fecha_publicacion'),
                libro.get('descripcion'),
                libro.get('editorial_id')
            ))
            conn.commit()
            return cursor.lastrowid

        except Exception as e:
            conn.rollback()
            self.logger.exception(f"Error al insertar libro: {e}")
            return -1

        finally:
            if cursor:
                cursor.close()

    def add_list(self, libros: list[dict]) -> int:
        if not libros:
            return 0

        sql = f"""INSERT INTO {self.table_name} 
                  (isbn, titulo, fecha_publicacion, descripcion, editorial_id)
                  VALUES (%s, %s, %s, %s, %s)"""

        datos = [
            (
                libro.get('isbn'),
                libro.get('titulo'),
                libro.get('fecha_publicacion'),
                libro.get('descripcion'),
                libro.get('editorial_id')
            )
            for libro in libros
        ]

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.executemany(sql, datos)
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            self.logger.exception("Error al insertar lista de libros")
            return 0

        finally:
            if cursor:
                cursor.close()

    def delete(self, id: int) -> int:
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.table_name} WHERE id = %s", (id,))
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            self.logger.exception("Error al eliminar libro")
            return -1

        finally:
            if cursor:
                cursor.close()

    def update(self, id: int, libro: dict) -> int:
        sql = f"""UPDATE {self.table_name} SET 
                  isbn=%s, titulo=%s, fecha_publicacion=%s, 
                  descripcion=%s, editorial_id=%s 
                  WHERE id=%s"""

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, (
                libro.get('isbn'),
                libro.get('titulo'),
                libro.get('fecha_publicacion'),
                libro.get('descripcion'),
                libro.get('editorial_id'),
                id
            ))
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            self.logger.exception("Error al actualizar libro")
            return -1

        finally:
            if cursor:
                cursor.close()

    ###############
    # Consultas
    ###############
    def get(self, id: int) -> dict:
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(f"{self.SELECT} WHERE id = %s", (id,))
            return cursor.fetchone()

        except Exception:
            self.logger.exception("Error al obtener libro por id")
            return None

        finally:
            if cursor:
                cursor.close()

    def get_all(self) -> list:
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(self.SELECT)
            return cursor.fetchall()

        except Exception:
            self.logger.exception("Error al obtener todos los libros")
            return []

        finally:
            if cursor:
                cursor.close()

    def get_by_isbn(self, isbn: str) -> dict:
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(f"{self.SELECT} WHERE isbn = %s", (isbn,))
            return cursor.fetchone()

        except Exception:
            self.logger.exception("Error al obtener libro por ISBN")
            return None

        finally:
            if cursor:
                cursor.close()