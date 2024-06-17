from tkinter import *
from modelo import Transacciones


class App():
    def __init__(self, root, tree=None):
        self.transcciones = Transacciones()
        self.root = root
        self.tree = tree

    def widgets(self,):

        ########################################
        # Labels
        ########################################

        self.titulo = Label(self.root,
                            text="Ingrese la transaccion",
                            heigh=2,
                            width=100)
        self.titulo.grid(row=0, column=0, columnspan=6,
                         padx=1, pady=1, sticky=W + E)

        ########################################
        # TREEVIEW
        ########################################
