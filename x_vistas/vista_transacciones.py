from tkinter import Frame, Label, ttk, Button, StringVar
from tkinter import font, OptionMenu
from tkcalendar import DateEntry


def widgets_transacciones(parent):
    transacciones = Frame(parent)

    var_categoria = StringVar()
    var_tipo = StringVar()

    titulo = Label(transacciones, text="Transacciones",
                   bg="DarkOrchid3", fg="thistle1", height=2, width=80,
                   font=(30))
    titulo.grid(row=0, column=0, columnspan=6)

    # Treeview

    tree_frame = Frame(transacciones)
    tree_frame.grid(row=3, column=0, columnspan=6, padx=10, pady=10,
                    sticky="we")

    tree = ttk.Treeview(tree_frame, columns=("id", "monto", "razon",
                                             "categoria", "tipo", "fecha"),
                        show="headings")

    tree.column("id", width=80, stretch="NO")
    tree.column("monto", width=15, anchor="center")
    tree.column("razon", width=100, anchor="center")
    tree.column("categoria", width=20, anchor="center")
    tree.column("tipo", width=20, anchor="center")
    tree.column("fecha", width=20, anchor="center")

    tree.heading("id", text="ID", anchor="center",
                 command=lambda: tree.focus(""))
    tree.heading("monto", text="Monto", anchor="w")
    tree.heading("razon", text="Razon", anchor="w")
    tree.heading("categoria", text="Categoria", anchor="w")
    tree.heading("tipo", text="Tipo", anchor="w")
    tree.heading("fecha", text="Fecha", anchor="w")

    tree.pack(fill="both", expand=True)

    # Labels

    frame_filtro_busqueda = Frame(transacciones, borderwidth=2,
                                  relief="groove")
    frame_filtro_busqueda.grid(row=1, column=2, sticky="we", padx=5,
                               pady=5, columnspan=3)
    nombredato_1 = Label(frame_filtro_busqueda, font=(40),
                         text="Ingrese los datos para filtrar y buscar:")
    nombredato_1.pack(padx=4, pady=1)

    # Entry

    var_categoria.set("Categoria")
    opciones_categoria = ["comida", "electronica", "indumentaria",
                          "educacion", "transporte", "otros"]

    fuente_grande = font.Font(family="Helvetica", size=14)

    frame_menu_categoria = Frame(transacciones, width=100)
    frame_menu_categoria.grid(row=2, column=2)
    menu_categoria = OptionMenu(frame_menu_categoria,
                                var_categoria, *opciones_categoria)
    menu_categoria.config(font=fuente_grande)
    menu_categoria.grid(row=2, column=2)

    var_tipo.set("Tipo")
    opciones_tipo = ["Ingreso", "Gastos"]

    fuente_grande = font.Font(family="Helvetica", size=14)

    frame_menu_tipo = Frame(transacciones, width=100)
    frame_menu_tipo.grid(row=2, column=3)
    menu_tipo = OptionMenu(frame_menu_tipo,
                           var_tipo, *opciones_tipo)
    menu_tipo.config(font=fuente_grande)
    menu_tipo.grid(row=2, column=3)

    dato_filtro_3 = DateEntry(transacciones, width=35, background='darkblue',
                              foreground='white', borderwidth=3)
    dato_filtro_3.grid(row=2, column=4, padx=10, pady=10)

    # buttons

    boton_borrar = Button(transacciones, text="Borrar", width=20,
                          height=2, font=(23))
    boton_borrar.grid(row=4, column=2, sticky="e")

    boton_modificar = Button(transacciones, text="Modificar", width=20,
                             height=2, font=(23))
    boton_modificar.grid(row=4, column=4, sticky="w")

    boton_resetear_filtro = Button(transacciones, text="Borrar filtros",
                                   width=10, height=2, font=(11))
    boton_resetear_filtro.grid(row=6, column=3, sticky="n")

    return transacciones
