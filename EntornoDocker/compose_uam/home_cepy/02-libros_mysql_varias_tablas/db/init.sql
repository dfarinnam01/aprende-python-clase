

CREATE DATABASE cepy_libros_V1;
use cepy_libros_v1;
CREATE USER 'cepy'@'%' IDENTIFIED BY 'castelar';
GRANT ALL PRIVILEGES ON `cepy_%`.* TO 'cepy'@'%';
#GRANT ALL PRIVILEGES ON *.* TO 'cepy'@'%';
FLUSH PRIVILEGES;


CREATE TABLE editoriales (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE autores (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE libros (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    isbn VARCHAR(25) UNIQUE NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    fecha_publicacion INTEGER NOT NULL,
    descripcion TEXT,
    editorial_id INTEGER,
    FOREIGN KEY (editorial_id) REFERENCES editoriales(id) ON DELETE SET NULL
);

CREATE TABLE libro_autor (
    libro_id INTEGER,
    autor_id INTEGER,
    PRIMARY KEY (libro_id, autor_id),
    FOREIGN KEY (libro_id) REFERENCES libros(id) ON DELETE CASCADE,
    FOREIGN KEY (autor_id) REFERENCES autores(id) ON DELETE CASCADE
);