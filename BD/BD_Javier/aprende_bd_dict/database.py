import logging
import sqlite3


class Database:
    logger = logging.getLogger("Database")
    SELECT="SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM libros"


    __conn = None
    __db_name="libros_v04.db"
    @classmethod
    def __new__(cls):
        raise(TypeError("Database es un singleton no puede ser instanciado"))

    @classmethod
    def conect(cls):
        if cls.__conn is None:
            cls.__conn = sqlite3.connect(cls.__db_name)
            cls.__conn.row_factory=sqlite3.Row
            with cls.__conn:
                cursor=cls.__conn.cursor()
                cursor.execute("PRAGMA foreign_keys = ON")
            cls._crear_tablas()
            cls.logger.info("Conexion cn la BD realizada con exito")
        return cls.__conn

    @classmethod
    def close(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None

    @classmethod
    def _crear_tablas(cls):
        with (cls.__conn):
            cursor=cls.__conn.cursor()
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Libros (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        isbn varchar(25) UNIQUE NOT NULL,
                        titulo varchar(100) NOT NULL,
                        autor varchar(100) NOT NULL,
                        editorial varchar(100) NOT NULL,
                        fecha_publicacion integer NOT NULL,
                        descripcion varchar(100) NULL)
                ''')
