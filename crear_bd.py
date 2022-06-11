'''Código para creación de la base de datos.'''

import sqlite3

conexion = sqlite3.connect('to_do.db')

cursor = conexion.cursor()

crear_tabla_proyectos = '''
CREATE TABLE proyectos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_proyecto varchar(100) NOT NULL,
    prioridad int NOT NULL
);
'''

cursor.execute(crear_tabla_proyectos)
conexion.commit()

crear_tabla_tareas = '''
CREATE TABLE tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_creacion date NOT NULL,
    fecha_objetivo date DEFAULT NULL,
    nombre_tarea text,
    carpeta varchar(255) DEFAULT NULL,
    id_proyecto INT,
    duracion float DEFAULT 0.5,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos (id)
);
'''

cursor.execute(crear_tabla_tareas)
conexion.commit()

conexion.close()