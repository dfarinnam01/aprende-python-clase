import logging
from .database import Database


class EditorialesDao:
    logger = logging.getLogger(__name__)
    table_name = "editoriales"

    SELECT = f"""
        SELECT id, nombre
        FROM {table_name}
    """

    def add(self, editorial: dict) -> int:
        sql = f"INSERT INTO {self.table_name} (nombre) VALUES (%s)"

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, (
                editorial.get('nombre'),
            ))
            conn.commit()
            return cursor.lastrowid

        except Exception as e:
            conn.rollback()
            self.logger.exception(f"Error al insertar editorial: {e}")
            return -1

        finally:
            if cursor:
                cursor.close()

    def add_list(self, editoriales: list[dict]) -> int:
        if not editoriales:
            return 0

        sql = f"INSERT INTO {self.table_name} (nombre) VALUES (%s)"

        datos = [
            (editorial.get('nombre'),)
            for editorial in editoriales
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
            self.logger.exception("Error al insertar lista de editoriales")
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
            self.logger.exception("Error al eliminar editorial")
            return -1

        finally:
            if cursor:
                cursor.close()

    def update(self, id: int, editorial: dict) -> int:
        sql = f"UPDATE {self.table_name} SET nombre=%s WHERE id=%s"

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, (
                editorial.get('nombre'),
                id
            ))
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            self.logger.exception("Error al actualizar editorial")
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
            self.logger.exception("Error al obtener editorial")
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
            self.logger.exception("Error al obtener editoriales")
            return []

        finally:
            if cursor:
                cursor.close()

    def get_by_nombre(self, nombre: str) -> dict:
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(f"{self.SELECT} WHERE nombre = %s", (nombre,))
            return cursor.fetchone()

        except Exception:
            self.logger.exception("Error al obtener editorial por nombre")
            return None

        finally:
            if cursor:
                cursor.close()