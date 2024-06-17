from tkinter import ttk, Tk, Label, Frame, Menu
from x_vistas.vista_main import crear_main
from x_vistas.vista_panel_control import crear_panel_control
from x_vistas.vista_transacciones import crear_transacciones
from x_vistas.vista_reportes import crear_reportes

# Crear la ventana principal
root = Tk()
root.title("Presupuesto Personal")
root.geometry("1000x700")

# Crear el Frame contenedor para las vistas
container = Frame(root)
container.pack(fill='both', expand=True)


# Crear las vistas
main = crear_main(container)
panel_control = crear_panel_control(container)
transacciones = crear_transacciones(container)
reportes = crear_reportes(container)


# Función para mostrar una vista específica
def mostrar_vista(vista):
    vista.tkraise()


# Colocar las vistas en el mismo lugar en el contenedor
for vista in (main, panel_control, transacciones, reportes):
    vista.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

# Crear el MenuBar
menubar = Menu(root)
root.config(menu=menubar)

# Crear un menú "Navegar"
navegar_menu = Menu(menubar, tearoff=0)
navegar_menu.add_command(label="Main",
                         command=lambda: mostrar_vista(main))
navegar_menu.add_command(label="Panel de control",
                         command=lambda: mostrar_vista(panel_control))
navegar_menu.add_command(label="Vista de Transacciones",
                         command=lambda: mostrar_vista(transacciones))
navegar_menu.add_command(label="Panel de reportes",
                         command=lambda: mostrar_vista(reportes))
menubar.add_cascade(label="Navegar", menu=navegar_menu)

# Mostrar la vista inicial
mostrar_vista(main)

# Iniciar el bucle principal
root.mainloop()
