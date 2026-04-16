import logging
from .database import Database


class AutoresDao:
    logger = logging.getLogger(__name__)
    table_name = "autores"

    SELECT = f"""
        SELECT id, nombre
        FROM {table_name}
    """

    def add(self, autor: dict) -> int:
        sql = f"INSERT INTO {self.table_name} (nombre) VALUES (%s)"

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, (
                autor.get('nombre'),
            ))
            conn.commit()
            return cursor.lastrowid

        except Exception as e:
            conn.rollback()
            self.logger.exception(f"Error al insertar autor: {e}")
            return -1

        finally:
            if cursor:
                cursor.close()

    def add_list(self, autores: list[dict]) -> int:
        if not autores:
            return 0

        sql = f"INSERT INTO {self.table_name} (nombre) VALUES (%s)"

        datos = [
            (autor.get('nombre'),)
            for autor in autores
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
            self.logger.exception("Error al insertar lista de autores")
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
            self.logger.exception("Error al eliminar autor")
            return -1

        finally:
            if cursor:
                cursor.close()

    def update(self, id: int, autor: dict) -> int:
        sql = f"UPDATE {self.table_name} SET nombre=%s WHERE id=%s"

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, (
                autor.get('nombre'),
                id
            ))
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            self.logger.exception("Error al actualizar autor")
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
            self.logger.exception("Error al obtener autor")
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
            self.logger.exception("Error al obtener autores")
            return []

        finally:
            if cursor:
                cursor.close()

    #########################
    # Relación Libro - Autor
    #########################

    def add_to_libro(self, libro_id: int, autor_id: int) -> int:
        sql = """
            INSERT INTO libro_autor (libro_id, autor_id)
            VALUES (%s, %s)
        """

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, (libro_id, autor_id))
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            self.logger.exception("Error al asociar autor con libro")
            return -1

        finally:
            if cursor:
                cursor.close()

    def get_by_libro(self, libro_id: int) -> list:
        sql = """
            SELECT a.id, a.nombre
            FROM autores a
            INNER JOIN libro_autor la ON a.id = la.autor_id
            WHERE la.libro_id = %s
        """

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, (libro_id,))
            return cursor.fetchall()

        except Exception:
            self.logger.exception("Error al obtener autores por libro")
            return []

        finally:
            if cursor:
                cursor.close()