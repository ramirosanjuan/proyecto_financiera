from tkinter import Frame, Label, Entry, Button, ttk, messagebox

def widgets_panel_control(parent):
    panel_control = Frame(parent)

    # Título
    titulo = Label(panel_control, text="Panel de control",
                   bg="DarkOrchid3", fg="thistle1", height=2, width=80,
                   font=(30))
    titulo.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

    # Gestión de Categorías
    Label(panel_control, text="Gestión de Categorías").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    # Agregar nuevas categorías
    Label(panel_control, text="Nueva Categoría:").grid(row=2, column=0, sticky="w", padx=10)
    entry_nueva_categoria = Entry(panel_control)
    entry_nueva_categoria.grid(row=2, column=1, padx=10)
    Button(panel_control, text="Agregar", command=lambda: agregar_categoria(entry_nueva_categoria)).grid(row=2, column=2, padx=10)

    # Editar y eliminar categorías
    Label(panel_control, text="Categorías Existentes:").grid(row=3, column=0, sticky="w", padx=10)
    lista_categorias = ttk.Combobox(panel_control, values=["Salud", "Viajes", "Alquiler"])
    lista_categorias.grid(row=3, column=1, padx=10)
    Button(panel_control, text="Editar", command=lambda: editar_categoria(lista_categorias)).grid(row=3, column=2, padx=10)
    Button(panel_control, text="Eliminar", command=lambda: eliminar_categoria(lista_categorias)).grid(row=3, column=3, padx=10)

    # Presupuestos por Categoría
    Label(panel_control, text="Presupuestos por Categoría").grid(row=4, column=0, sticky="w", padx=10, pady=5)
    Label(panel_control, text="Categoría:").grid(row=5, column=0, sticky="w", padx=10)
    entry_presupuesto_categoria = Entry(panel_control)
    entry_presupuesto_categoria.grid(row=5, column=1, padx=10)
    Button(panel_control, text="Establecer Presupuesto", command=lambda: establecer_presupuesto(entry_presupuesto_categoria)).grid(row=5, column=2, padx=10)

    # Configuración de Moneda y Fecha
    Label(panel_control, text="Configuración de Moneda y Fecha").grid(row=6, column=0, sticky="w", padx=10, pady=5)
    Label(panel_control, text="Moneda:").grid(row=7, column=0, sticky="w", padx=10)
    combobox_moneda = ttk.Combobox(panel_control, values=["USD", "EUR", "ARS"])
    combobox_moneda.grid(row=7, column=1, padx=10)
    Label(panel_control, text="Formato de Fecha:").grid(row=8, column=0, sticky="w", padx=10)
    combobox_formato_fecha = ttk.Combobox(panel_control, values=["dd/mm/aaaa", "mm/dd/aaaa"])
    combobox_formato_fecha.grid(row=8, column=1, padx=10)

    # Configuración de Notificaciones
    Label(panel_control, text="Configuración de Notificaciones").grid(row=9, column=0, sticky="w", padx=10, pady=5)
    Label(panel_control, text="Gasto Grande:").grid(row=10, column=0, sticky="w", padx=10)
    entry_gasto_grande = Entry(panel_control)
    entry_gasto_grande.grid(row=10, column=1, padx=10)
    Button(panel_control, text="Configurar Alerta", command=lambda: configurar_alerta_gasto(entry_gasto_grande)).grid(row=10, column=2, padx=10)

    # Personalización de la Interfaz
    Label(panel_control, text="Personalización de la Interfaz").grid(row=11, column=0, sticky="w", padx=10, pady=5)
    Label(panel_control, text="Tema:").grid(row=12, column=0, sticky="w", padx=10)
    combobox_tema = ttk.Combobox(panel_control, values=["Claro", "Oscuro"])
    combobox_tema.grid(row=12, column=1, padx=10)

    # Sincronización y Respaldo de Datos
    Label(panel_control, text="Sincronización y Respaldo de Datos").grid(row=13, column=0, sticky="w", padx=10, pady=5)
    Button(panel_control, text="Realizar Respaldo", command=realizar_respaldo).grid(row=14, column=0, padx=10)
    Button(panel_control, text="Sincronizar con la Nube", command=sincronizar_nube).grid(row=14, column=1, padx=10)
    Button(panel_control, text="Restaurar Respaldo", command=restaurar_respaldo).grid(row=14, column=2, padx=10)

    return panel_control

def agregar_categoria(entry):
    categoria = entry.get()
    if categoria:
        messagebox.showinfo("Categoría Agregada", f"Categoría '{categoria}' agregada exitosamente.")
    else:
        messagebox.showwarning("Error", "El nombre de la categoría no puede estar vacío.")

def editar_categoria(combobox):
    categoria = combobox.get()
    if categoria:
        messagebox.showinfo("Editar Categoría", f"Editar categoría '{categoria}'.")
    else:
        messagebox.showwarning("Error", "Seleccione una categoría para editar.")

def eliminar_categoria(combobox):
    categoria = combobox.get()
    if categoria:
        messagebox.showinfo("Eliminar Categoría", f"Categoría '{categoria}' eliminada exitosamente.")
    else:
        messagebox.showwarning("Error", "Seleccione una categoría para eliminar.")

def establecer_presupuesto(entry):
    presupuesto = entry.get()
    if presupuesto:
        messagebox.showinfo("Presupuesto Establecido", f"Presupuesto de '{presupuesto}' establecido exitosamente.")
    else:
        messagebox.showwarning("Error", "El presupuesto no puede estar vacío.")

def configurar_alerta_gasto(entry):
    gasto = entry.get()
    if gasto:
        messagebox.showinfo("Alerta Configurada", f"Alerta de gasto grande configurada para '{gasto}'.")
    else:
        messagebox.showwarning("Error", "El valor del gasto no puede estar vacío.")

def realizar_respaldo():
    messagebox.showinfo("Respaldo", "Respaldo realizado exitosamente.")

def sincronizar_nube():
    messagebox.showinfo("Sincronización", "Sincronización con la nube realizada exitosamente.")

def restaurar_respaldo():
    messagebox.showinfo("Restauración", "Restauración de respaldo realizada exitosamente.")