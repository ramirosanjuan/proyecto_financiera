from tkinter import Tk
from vista import App

if __name__ == "__main__":
    """Punto de entrada principal de la aplicación"""
    root = Tk()
    """Crear una instancia de la ventana principal de Tkinter"""
    obj = App(root)
    """Crear una instancia de la clase App"""
    root.mainloop()
    """Iniciar el bucle principal de eventos de la aplicación"""
