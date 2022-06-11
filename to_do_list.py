from rich.console import Console
from rich.table import Table

to_do_list = [('1', '01/01/2022', '01/01/2022', 'Tarea 1', 'Proyecto A', 'Carpeta A'),
              ('2', '01/02/2022', '01/01/2022', 'Tarea 2', 'Proyecto B', 'Carpeta B')]

table = Table("Prioridad",
              "Fecha creación",
              "Fecha objetivo",
              "Tarea",
              "Proyecto",
              "Carpeta",
              title="TO DO LIST", show_lines=True, caption="Texto debajo de la tabla")

for i in range(len(to_do_list)):
    table.add_row(to_do_list[i][0],
                  to_do_list[i][1],
                  to_do_list[i][2],
                  to_do_list[i][3],
                  to_do_list[i][4],
                  to_do_list[i][5])

console = Console()
console.print(table)