from tkinter import Frame, Menu, StringVar
from tkinter import ttk
from x_vistas.vista_main import widgets_alta
from x_vistas.vista_panel_control import widgets_panel_control
from x_vistas.vista_reportes import widgets_reportes
from x_vistas.vista_transacciones import widgets_transacciones


class App():
    def __init__(self, root, tree=None):
        self.root = root
        self.tree = tree

        self.var_nombre = StringVar()
        self.var_categoria = StringVar()
        self.var_prioridad = StringVar()
        self.var_descripcion = StringVar()

        root.title("Administrador de Tareas")
        root.geometry("1000x700")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.main = Frame(self.notebook)
        self.panel_control = Frame(self.notebook)
        self.transacciones = Frame(self.notebook)
        self.reportes = Frame(self.notebook)

        self.notebook.add(self.main, text='Main')
        self.notebook.add(self.panel_control, text='Panel de control')
        self.notebook.add(self.transacciones, text='Transacciones')
        self.notebook.add(self.reportes, text='Reportes')

        widgets_alta(self.main).pack(fill='both', expand=True)
        widgets_panel_control(self.panel_control).pack(fill='both',
                                                       expand=True)
        widgets_transacciones(self.transacciones).pack(fill='both',
                                                       expand=True)
        widgets_reportes(self.reportes).pack(fill='both', expand=True)

        self.menu_navegacion()

    def mostrar_vista(self, vista):
        if vista == "main":
            self.notebook.select(self.main)
        elif vista == "panel_control":
            self.notebook.select(self.panel_control)
        elif vista == "transacciones":
            self.notebook.select(self.transacciones)
        elif vista == "reportes":
            self.notebook.select(self.reportes)

    def menu_navegacion(self):
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.navegar_menu = Menu(self.menubar, tearoff=0)
        self.navegar_menu.add_command(label="Main",
                                      command=lambda:
                                          self.mostrar_vista("main"))
        self.navegar_menu.add_command(label="Panel de control",
                                      command=lambda:
                                          self.mostrar_vista("panel_control"))
        self.navegar_menu.add_command(label="Vista de Transacciones",
                                      command=lambda:
                                          self.mostrar_vista("transacciones"))
        self.navegar_menu.add_command(label="Panel de reportes",
                                      command=lambda:
                                          self.mostrar_vista("reportes"))
        self.navegar_menu.add_separator()
        self.navegar_menu.add_command(label="Salir", command=self.root.quit)
        self.menubar.add_cascade(label="Navegar", menu=self.navegar_menu)
