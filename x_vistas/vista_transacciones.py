from tkinter import Frame, Label, W, E


def crear_transacciones(parent):
    transacciones = Frame(parent)

    titulo = Label(transacciones, text="Ingrese los datos",
                   bg="DarkOrchid3", fg="thistle1", height=1, width=80)
    titulo.grid(row=0, column=0, columnspan=6, padx=1, pady=1, sticky=W+E)

    return transacciones
