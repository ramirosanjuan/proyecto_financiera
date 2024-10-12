from tkinter import Frame, Label, Button, Entry
from tkinter import DoubleVar, StringVar, OptionMenu, font
from tkinter import ttk
from tkcalendar import DateEntry


def widgets_alta(parent):
    main = Frame(parent)

    var_monto = DoubleVar()
    var_razon = StringVar()
    var_categoria = StringVar()
    var_tipo = StringVar()

    # Labels

    titulo = Label(main, text="Ingrese los datos",
                   bg="DarkOrchid3", fg="thistle1", height=2, width=80,
                   font=(30))
    titulo.grid(row=0, column=0, columnspan=6, padx=1, pady=1, sticky="we")

    frame_monto = Frame(main, borderwidth=2, relief="groove")
    frame_monto.grid(row=3, column=1, sticky="we", padx=5, pady=5)
    nombredato_1 = Label(frame_monto, text="Monto:")
    nombredato_1.pack(padx=4, pady=1)

    frame_fecha = Frame(main, borderwidth=2, relief="groove")
    frame_fecha.grid(row=3, column=3, sticky="we", padx=5, pady=5)
    nombredato_2 = Label(frame_fecha, text="Fecha y varios:")
    nombredato_2.pack(padx=4, pady=1)

    frame_razon = Frame(main, borderwidth=2, relief="groove")
    frame_razon.grid(row=5, column=1, sticky="we", padx=5, pady=5)
    nombredato_4 = Label(frame_razon, text="razon:")
    nombredato_4.pack(padx=4, pady=1)

    frame_balance = Frame(main, borderwidth=2, relief="groove")
    frame_balance.grid(row=20, column=3, sticky="we", padx=5, pady=5)
    nombredato_5 = Label(frame_balance, text=f"Balance actual: {None}")
    nombredato_5.pack(padx=4, pady=1)

    # Entries

    dato_1 = Entry(main, textvariable=var_monto, width=25,
                   font=('Helvetica', 13), borderwidth=3)
    dato_1.grid(row=4, column=1)

    dato_2 = DateEntry(main, width=35, background='darkblue',
                       foreground='white', borderwidth=3)
    dato_2.grid(row=4, column=3, padx=10, pady=10)

    dato_3 = Entry(main, textvariable=var_razon, width=25,
                   font=('Helvetica', 13), borderwidth=3)
    dato_3.grid(row=6, column=1)

    var_categoria.set("Categoria")
    opciones_categoria = ["comida", "electronica", "indumentaria",
                          "educacion", "transporte", "otros"]

    fuente_grande = font.Font(family="Helvetica", size=14)

    frame_menu_categoria = Frame(main, width=100)
    frame_menu_categoria.grid(row=5, column=3)
    menu_categoria = OptionMenu(frame_menu_categoria,
                                var_categoria, *opciones_categoria)
    menu_categoria.config(font=fuente_grande)
    menu_categoria.grid(row=5, column=3)

    var_tipo.set("Tipo")
    opciones_tipo = ["Ingreso", "Gastos"]

    fuente_grande = font.Font(family="Helvetica", size=14)

    frame_menu_tipo = Frame(main, width=100)
    frame_menu_tipo.grid(row=6, column=3)
    menu_tipo = OptionMenu(frame_menu_tipo,
                           var_tipo, *opciones_tipo)
    menu_tipo.config(font=fuente_grande)
    menu_tipo.grid(row=6, column=3)

    # button

    boton_implementar = Button(main, text="Implementar", width=20, height=2,
                               font=(23))
    boton_implementar.grid(row=7, column=2)

    # Treeview

    tree_frame = Frame(main)
    tree_frame.grid(row=8, column=0, columnspan=6, padx=10, pady=10,
                    sticky="we")

    tree = ttk.Treeview(tree_frame, columns=("info", "monto"), show="headings")
    tree.column("info", width=100)
    tree.column("monto", width=10, anchor="center")

    tree.heading("monto", text="Monto: ")
    tree.heading("info", text="Ingresos al sistema:")

    tree.pack(fill="both", expand=True)

    tree.insert("", "end",
                values=(
                    """Se ingresó un gasto/ingreso al sistema el 01/01/2023""",
                    "+32"))

    return main
