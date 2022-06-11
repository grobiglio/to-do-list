from rich import print
from rich.panel import Panel
from menu import Menu
from clean_console import clean_console
import bd_proyectos
import bd_tareas
# Add here another imports
# Consider PEP 8 for imorts -> https://www.python.org/dev/peps/pep-0008/#imports

# Set menu options.
# By default, last option will be Exit, there's no need to specify it.
# Menu options will be auto numerated
OPTIONS = """
Listar tareas
Agregar tarea
Modificar tarea
Cerrar tarea
Listar proyectos
Agregar proyecto
Modificar prioridades
Eliminar proyecto
"""

clean_console()
menu = Menu(OPTIONS)
menu_options = Panel(menu.get_menu(),
                     expand=False,
                     title="[bold] M E N U [/]",
                     padding=(1, 5, 0, 2),
                     highlight=True)

option = ""
while option != "Exit":
    print(menu_options)
    option = menu.request_option() 
    if option == 1: # Listar tareas
        bd_tareas.listar()
    elif option == 2: # Agregar tarea
        bd_tareas.agregar()
    elif option == 3: # Modificar tarea
        bd_tareas.modificar()
    elif option == 4: # Cerrar tarea
        bd_tareas.cerrar()
    elif option == 5: # Listar proyectos
        bd_proyectos.listar()
    elif option == 6: # Agregar proyecto
        bd_proyectos.agregar()
    elif option == 7: # Modificar prioridades
        bd_proyectos.modificar_prioridad()
    elif option == 8: # Eliminar proyecto
        bd_proyectos.eliminar()

# Code to execute befor exit main program