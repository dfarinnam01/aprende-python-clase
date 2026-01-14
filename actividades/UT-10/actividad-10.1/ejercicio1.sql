CREATE DATABASE MiBaseDeDatos;

CREATE TABLE tb_usuarios_tipos (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre_tipo VARCHAR(50) NOT NULL
);


CREATE TABLE tb_usuarios (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo_usuario_id INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    fecha_registro DATETIME,

    FOREIGN KEY (tipo_usuario_id) REFERENCES tb_usuarios_tipos(id)
);
