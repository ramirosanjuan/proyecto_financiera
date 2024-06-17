from tkinter import ttk, Tk, Label, Frame, Menu

# Crear la ventana principal
root = Tk()
root.title("Presupuesto Personal")
root.geometry("1000x700")

# Crear el Frame contenedor para las vistas
container = Frame(root)
container.pack(fill='both', expand=True)


# Crear las vistas
def crear_main():
    main = Frame(container)
    titulo = Label(main, text="Contenido de la Vista 1").pack(padx=10, pady=10)
    return main


def crear_panel_control():
    panel_control = Frame(container)
    tit = Label(panel_control, text="Contenido de la Vista 2").pack(padx=10, pady=10)
    return panel_control


def crear_transacciones():
    transacciones = Frame(container)
    tit = Label(transacciones, text="Contenido de la Vista 3").pack(padx=10, pady=10)
    return transacciones


def crear_reportes():
    reportes = Frame(container)
    tit = Label(reportes, text="Contenido de la Vista 3").pack(padx=10, pady=10)
    return reportes


# Inicializar vistas
main = crear_main()
panel_control = crear_panel_control()
transacciones = crear_transacciones()
reportes = crear_reportes()


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
