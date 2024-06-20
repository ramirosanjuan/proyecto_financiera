from tkinter import Frame, Label, Button, Entry
from tkinter import DoubleVar, StringVar, OptionMenu, font
from tkcalendar import DateEntry


def crear_main(parent):
    main = Frame(parent)

    var_monto = DoubleVar()
    var_razon = StringVar()
    var_categoria = StringVar()
    var_tipo = StringVar()

    # Labels

    titulo = Label(main, text="Ingrese los datos",
                   bg="DarkOrchid3", fg="thistle1", height=1, width=144)
    titulo.grid(row=0, column=0, columnspan=6, padx=1, pady=1, sticky="we")

    frame_monto = Frame(main, borderwidth=2, relief="groove")
    frame_monto.grid(row=3, column=0, sticky="we", padx=5, pady=5)
    nombredato_1 = Label(frame_monto, text="monto:")
    nombredato_1.pack(padx=4, pady=1)

    frame_fecha = Frame(main, borderwidth=2, relief="groove")
    frame_fecha.grid(row=4, column=0, sticky="we", padx=5, pady=5)
    nombredato_2 = Label(frame_fecha, text="fecha:")
    nombredato_2.pack(padx=4, pady=1)

    frame_categoria = Frame(main, borderwidth=2, relief="groove")
    frame_categoria.grid(row=5, column=0, sticky="we", padx=5, pady=5)
    nombredato_3 = Label(frame_categoria, text="categoria:")
    nombredato_3.pack(padx=4, pady=1)

    frame_tipo = Frame(main, borderwidth=2, relief="groove")
    frame_tipo.grid(row=6, column=0, sticky="we", padx=5, pady=5)
    nombredato_3 = Label(frame_tipo, text="Tipo:")
    nombredato_3.pack(padx=4, pady=1)

    frame_razon = Frame(main, borderwidth=2, relief="groove")
    frame_razon.grid(row=7, column=0, sticky="we", padx=5, pady=5)
    nombredato_4 = Label(frame_razon, text="razon:")
    nombredato_4.pack(padx=4, pady=1)

    # Entries

    dato_1 = Entry(main, textvariable=var_monto, width=25,
                   font=('Helvetica', 13), borderwidth=3)
    dato_1.grid(row=3, column=2)

    dato_2 = DateEntry(main, width=35, background='darkblue',
                       foreground='white', borderwidth=3)
    dato_2.grid(row=4, column=2, padx=10, pady=10)

    dato_3 = Entry(main, textvariable=var_razon, width=25,
                   font=('Helvetica', 13), borderwidth=3)
    dato_3.grid(row=7, column=2)

    var_categoria.set("Categoria")
    opciones_categoria = ["comida", "electronica", "indumentaria",
                          "educacion", "transporte", "otros"]

    fuente_grande = font.Font(family="Helvetica", size=14)

    frame_menu_categoria = Frame(main, width=100)
    frame_menu_categoria.grid(row=5, column=2)
    menu_categoria = OptionMenu(frame_menu_categoria,
                                var_categoria, *opciones_categoria)
    menu_categoria.config(font=fuente_grande)
    menu_categoria.grid(row=5, column=3)

    var_tipo.set("Tipo")
    opciones_tipo = ["Ingreso", "Gastos"]

    fuente_grande = font.Font(family="Helvetica", size=14)

    frame_menu_tipo = Frame(main, width=100)
    frame_menu_tipo.grid(row=6, column=2)
    menu_tipo = OptionMenu(frame_menu_tipo,
                           var_tipo, *opciones_tipo)
    menu_tipo.config(font=fuente_grande)
    menu_tipo.grid(row=6, column=3)

    # button

    boton_alta = Button(main, text="Alta")
    boton_alta.grid(row=8, column=2, sticky="n")

    boton_modificar = Button(main, text="Modificar")
    boton_modificar.grid(row=9, column=2, sticky="n")

    boton_borrar = Button(main, text="Borrar")
    boton_borrar.grid(row=10, column=2, sticky="n")

    return main
