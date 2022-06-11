create database to_do;
USE to_do;

CREATE TABLE proyectos (
	id INT NOT NULL AUTO_INCREMENT,
    nombre_proyecto VARCHAR(100),
    PRIMARY KEY (id)
);

ALTER TABLE proyectos ADD COLUMN prioridad INT;
ALTER TABLE proyectos MODIFY COLUMN prioridad INT UNIQUE;

CREATE TABLE tareas (
	id INT NOT NULL AUTO_INCREMENT,
    fecha_creacion DATE,
    fecha_objetivo DATE,
    nombre_tarea TEXT,
    carpeta VARCHAR(255),
    id_proyecto INT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id)
);

ALTER TABLE tareas ADD COLUMN duracion FLOAT DEFAULT 0.5;

SHOW CREATE TABLE proyectos;
SHOW CREATE TABLE tareas;
DROP TABLE tareas;