from tkinter import Frame, Label, W, E


def crear_main(parent):
    main = Frame(parent)

    titulo = Label(main, text="Ingrese los datos",
                   bg="DarkOrchid3", fg="thistle1", height=1, width=144)
    titulo.grid(row=0, column=0, columnspan=6, padx=1, pady=1, sticky=W+E)

    return main
