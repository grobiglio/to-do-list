'''Módulo para gestión de la base de dato de los proyectos.
Lista proyectos
Agrega proyectos
Modifica prioridades a proyectos
Elimina proyectos
'''
import sqlite3

def listar():
    con = sqlite3.connect('to_do.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM proyectos")
    lista_proyectos = cur.fetchall()
    for proyecto in lista_proyectos:
        print(proyecto)
    con.close()

def agregar():
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    con = sqlite3.connect('to_do.db')
    cur = con.cursor()
    cur.execute("INSERT INTO proyectos VALUES (NULL, ?, ?)", (nombre_proyecto, 3))
    con.commit()
    con.close()


def modificar_prioridad():
    id_a_modificar = int(input("Ingrese el número de proyecto al que se va a actualizar prioridad: "))
    nueva_prioridad = int(input("Ingrese nueva prioridad: "))
    con = sqlite3.connect('to_do.db')
    cur = con.cursor()
    cur.execute ("UPDATE proyectos SET prioridad=:nueva_prioridad WHERE id=:id_a_modificar", {"nueva_prioridad": nueva_prioridad, "id_a_modificar": id_a_modificar})
    con.commit()
    con.close()


def eliminar():
    id_a_eliminar = int(input("Ingrese el número de proyecto a eliminar: "))
    con = sqlite3.connect('to_do.db')
    cur = con.cursor()
    cur.execute("DELETE FROM proyectos WHERE id=:id_a_eliminar", {"id_a_eliminar": id_a_eliminar})
    con.commit()
    con.close()