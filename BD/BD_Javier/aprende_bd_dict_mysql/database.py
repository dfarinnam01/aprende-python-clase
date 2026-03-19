import logging
import mysql.connector
import mysql.connector

'''CREATE TABLE IF NOT EXISTS Libros (id integer PRIMARY KEY AUTO_INCREMENT,
    isbn varchar(25) UNIQUE NOT NULL,
    titulo varchar(100) NOT NULL,
    autor varchar(100) NOT NULL,
    editorial varchar(100) NOT NULL,
    fecha_publicacion integer NOT NULL,
    descripcion varchar(100) NULL);'''

class Database:
    logger = logging.getLogger("Database")
    SELECT="SELECT id,isbn,titulo,autor,editorial, fecha_publicacion FROM libros"
    __conn = None

    _config={
        'user': 'cepy01',
        'password': 'castelar2026',
        'host': 'localhost',
        'port': 33060,
        'database': 'aprende01',
        'raise_on_warnings': True,
    }

    def __new__(cls):
        raise(TypeError("Database es un singleton no puede ser instanciado"))

    @classmethod
    def conect(cls):
        if cls.__conn is None:
            try:
                cls.__conn = mysql.connector.connect(**cls._config)
            except Exception as e:
                cls.logger.critical(e)
                raise
        return cls.__conn

    @classmethod
    def close(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None