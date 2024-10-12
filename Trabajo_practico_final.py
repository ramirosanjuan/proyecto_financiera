from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor
import re

################################################
# BASE DE DATOS
################################################

def conexion():
    con = sqlite3.connect("base_trabajo_final.db")
    return con, con.cursor()

def crear_tabla():
    con, cursor = conexion()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='datos'")
    if not cursor.fetchone():
        sql = """CREATE TABLE datos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nombre TEXT NOT NULL,
                 telefono int,
                 correo TEXT)
        """
        cursor.execute(sql)
        con.commit()
    con.close()

crear_tabla()

################################################
# BUTTONS FUNCTIONS
################################################

def alta(tree):
    con, cursor = conexion()
    nombre = var_nombre.get().strip()
    telefono = var_telefono.get().strip()
    correo = var_correo.get().strip()
    nombre_pattern = r"^[A-Za-z\s]+$"
    telefono_pattern = r"^[0-9]+$"
    correo_pattern = r"^\S+@\S+\.\S+$"
    data = (nombre, telefono, correo)
    if (re.match(nombre_pattern, nombre) and
        re.match(telefono_pattern, telefono) and
        re.match(correo_pattern, correo)):
        sql = "INSERT INTO datos(nombre, telefono, correo) VALUES(?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        actualizar_treeview(tree)
        resetear_entrys()
    else:
        showerror("Error", """Todos los campos son requeridos y deben tener caracteres validos""")
    con.close()

def modificar(tree):
    seleccionado = tree.selection()
    if seleccionado:
        con, cursor = conexion()
        for item in seleccionado:
            id = tree.item(item, 'values')[0]
            try:
                nombre = var_nombre.get()
                telefono = int(var_telefono.get())
                correo = var_correo.get()
                data = (nombre, telefono, correo, id)
            except ValueError:
                showerror("Error","""Todos los campos son requeridos y cantidad y precio deben
                          ser números enteros""")
                return
            if nombre and telefono and correo:
                sql = "UPDATE datos SET nombre=?, telefono=?, correo=? WHERE id=?;"
                cursor.execute(sql, data)
                con.commit()
                actualizar_treeview(tree)
                resetear_entrys()
            else: 
                showerror("Error", "Todos los campos son requeridos")
        con.close()
    else:
        showerror("Error", "Seleccione un registro para modificar")

def borrar(tree):
    seleccionado = tree.selection()
    if seleccionado:
        con, cursor = conexion()
        for item in seleccionado:
            id = tree.item(item, 'values')[0]
            sql = "DELETE FROM datos WHERE id = ?;"
            cursor.execute(sql, (id,))
            con.commit()
        actualizar_treeview(tree)
        con.close()
    else:
        showerror("Error", "Selecione un campo")

def resetear_entrys():
    dato_1.delete(0, END)
    dato_1.insert(0, 'nombre')

    dato_2.delete(0, END)
    dato_2.insert(0, 'telefono')

    dato_3.delete(0, END)
    dato_3.insert(0, 'correo')

def actualizar_treeview(tree):
    for item in tree.get_children():
        tree.delete(item)
    con, cursor = conexion()
    cursor.execute("SELECT * FROM datos")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)
    con.close()

def cambiar_color_fondo():
    resultado = askcolor(color="#00ff00", title="Elegi el MEJOR color!!")
    root.config(bg=resultado[1])

    nombredato_1.config(bg=resultado[1])
    nombredato_2.config(bg=resultado[1])
    nombredato_3.config(bg=resultado[1])

    frame_nombre.config(bg=resultado[1])
    frame_telefono.config(bg=resultado[1])
    frame_correo.config(bg=resultado[1])

    dato_1.config(bg=resultado[1])
    dato_2.config(bg=resultado[1])
    dato_3.config(bg=resultado[1])

    frame_personalizacion.config(bg=resultado[1])
    personalizacion.config(bg=resultado[1])
    boton_fondo_1.config(bg=resultado[1])
    boton_fondo_2.config(bg=resultado[1])
    boton_fondo_3.config(bg=resultado[1])

    boton_alta.config(bg=resultado[1])
    boton_borrar.config(bg=resultado[1])
    boton_modificar.config(bg=resultado[1])

    showinfo("Genial", "Cambiaste el fondo con exito!")

def cambiar_color_titulo():
    resultado = askcolor(color="#00ff00", title="Elegi el MEJOR color!!")
    titulo.config(bg=resultado[1])

    showinfo("Genial", "Cambiaste el fondo con exito!")

def cambiar_color_treeview():
    resultado = askcolor(color="#00ff00", title="Elegi el MEJOR color!!")
    style.configure("Treeview", background=resultado[1],
                    fieldbackground=resultado[1])

    showinfo("Genial", "Cambiaste el fondo con exito!")

###############################################
# VISUAL
###############################################

root = Tk()

var_nombre = StringVar()
var_telefono = StringVar()
var_correo = StringVar()

###############################################
# LABELS
###############################################

titulo = Label(root, text="Ingrese los datos", bg="DarkOrchid3", fg="thistle1", height=1, width=80)
titulo.grid(row=0, column=0, columnspan=6, padx=1, pady=1, sticky=W+E)

frame_nombre = Frame(root, borderwidth=2, relief="groove")
frame_nombre.grid(row=3, column=0, sticky=W+E, padx=5, pady=5)
nombredato_1 = Label(frame_nombre, text="nombre:")
nombredato_1.pack(padx=4, pady=1)

frame_telefono = Frame(root, borderwidth=2, relief="groove")
frame_telefono.grid(row=4, column=0, sticky=W+E, padx=5, pady=5)
nombredato_2 = Label(frame_telefono, text="telefono:")
nombredato_2.pack(padx=4, pady=1)

frame_correo = Frame(root, borderwidth=2, relief="groove")
frame_correo.grid(row=5, column=0, sticky=W+E, padx=5, pady=5)
nombredato_3 = Label(frame_correo, text="correo:")
nombredato_3.pack(padx=4, pady=1)

frame_personalizacion = Frame(root, borderwidth=2, relief="groove")
frame_personalizacion.grid(row=11, column=2, sticky=N, padx=5, pady=5)
personalizacion = Label(frame_personalizacion, text="Personalizacion de pagina:")
personalizacion.pack(padx=4, pady=1)

################################################
# ENTRYS
################################################

dato_1 = Entry(root, textvariable=var_nombre, width=25, font=('Helvetica', 13), borderwidth=3)
dato_1.grid(row=3, column=2)
dato_1.insert(0, 'Ingrese el nombre')

dato_2 = Entry(root, textvariable=var_telefono, width=25, font=('Helvetica', 13), borderwidth=3)
dato_2.grid(row=4, column=2)
dato_2.insert(0, 'numero')

dato_3 = Entry(root, textvariable=var_correo, width=25, font=('Helvetica', 13), borderwidth=3)
dato_3.grid(row=5, column=2)
dato_3.insert(0, 'correo')

###############################################
# MENU BAR
###############################################

menubar = Menu(root)

menu_archivo = Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=menu_archivo)

root.config(menu=menubar)

###############################################
# TREEVIEW
###############################################

frame_treeview = Frame(root, borderwidth=2, relief="groove")
frame_treeview.grid(column=0, row=10, columnspan=6, padx=0, pady=0)

tree = ttk.Treeview(frame_treeview)
tree["columns"] = ("ID", "Nombre", "Telefono", "Correo")
tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=CENTER, width=80)
tree.column("Nombre", anchor=W, width=120)
tree.column("Telefono", anchor=W, width=120)
tree.column("Correo", anchor=W, width=180)

tree.heading("ID", text="ID", anchor=CENTER)
tree.heading("Nombre", text="Nombre", anchor=W)
tree.heading("Telefono", text="Telefono", anchor=W)
tree.heading("Correo", text="Correo", anchor=W)

tree.grid(column=0, row=0)

frame_treeview.grid_rowconfigure(0, weight=1)
frame_treeview.grid_columnconfigure(0, weight=1)

################################################
# PERSONALIZACION DE TREEVIEW
################################################

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                background="#E8E8E8",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3"
                )

style.map('Treeview',
          background=[('selected', '#347083')])

################################################
# BUTTONS
################################################

boton_alta = Button(root, text="Alta", command=lambda: alta(tree))
boton_alta.grid(row=6, column=2, sticky=N)

boton_modificar = Button(root, text="Modificar", command=lambda: modificar(tree))
boton_modificar.grid(row=7, column=2, sticky=N)

boton_borrar = Button(root, text="Borrar", command=lambda: borrar(tree))
boton_borrar.grid(row=8, column=2, sticky=N)

boton_fondo_1 = Button(root, text="Color de fondo", command=cambiar_color_fondo)
boton_fondo_1.grid(row=12, column=1, sticky=E)

boton_fondo_2 = Button(root, text="Color de fondo titulo", command=cambiar_color_titulo)
boton_fondo_2.grid(row=12, column=3, sticky=W)

boton_fondo_3 = Button(root, text="Color de fondo treeview", command=cambiar_color_treeview)
boton_fondo_3.grid(row=12, column=2, sticky=N)

actualizar_treeview(tree)

root.mainloop()
