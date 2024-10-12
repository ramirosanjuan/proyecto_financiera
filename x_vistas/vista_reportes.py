from tkinter import Frame, Label, ttk, Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime


def widgets_reportes(parent):
    reportes = Frame(parent)
    reportes.pack(fill='both', expand=True)

    titulo = Label(reportes, text="Reportes mensuales",
                   bg="DarkOrchid3", fg="thistle1", height=2, width=80,
                   font=(30))
    titulo.grid(row=0, column=0, columnspan=6, padx=1, pady=1, sticky="we")

    fechas = ['Enero', 'Febrero', 'Marzo']
    ingresos = [1000, 1500, 1200]
    gastos = [800, 1100, 900]
    categorias = ['Alquiler', 'Comida', 'Transporte']

    boton_actualizar_graficos = Button(reportes, text="Actualizar grafico",
                                       width=20, font=(23), height=2)
    boton_actualizar_graficos.grid(row=2, column=0, columnspan=2)

    frame_eleccion_mes = Frame(reportes, width=10)
    frame_eleccion_mes.grid(row=1, column=0, sticky="nsew")

    # Crear Combobox para seleccionar el mes
    meses = [datetime(2000, i, 1).strftime('%B') for i in range(1, 13)]
    combobox_mes = ttk.Combobox(frame_eleccion_mes,
                                values=meses, state="readonly")
    combobox_mes.set("Seleccione el mes")
    combobox_mes.pack(padx=4, pady=1)

    frame_eleccion_año = Frame(reportes, width=10)
    frame_eleccion_año.grid(row=1, column=1, sticky="nsew")

    # Crear Combobox para seleccionar el año
    años = [str(año) for año in range(2000, datetime.now().year + 1)]
    combobox_año = ttk.Combobox(frame_eleccion_año,
                                values=años, state="readonly")
    combobox_año.set("Seleccione el año")
    combobox_año.pack(padx=4, pady=1)

    frame_grafico_ingresos_gastos = Frame(reportes, width=10)
    frame_grafico_ingresos_gastos.grid(row=3, column=0,
                                       sticky="nsew")

    frame_grafico_distribucion_categorias = Frame(reportes, width=10)
    frame_grafico_distribucion_categorias.grid(row=3, column=1, padx=5,
                                               pady=5, sticky="nsew")

    # Configurar las filas y columnas para que se expandan
    reportes.grid_rowconfigure(3, weight=1)
    reportes.grid_columnconfigure(0, weight=1)
    reportes.grid_columnconfigure(1, weight=1)

    def plot_ingresos_vs_gastos(frame, fechas, ingresos, gastos):
        fig, ax = plt.subplots()
        ax.plot(fechas, ingresos, label='Ingresos')
        ax.plot(fechas, gastos, label='Gastos')
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def plot_distribucion_categorias(frame, gastos, categorias):
        fig, ax = plt.subplots()
        ax.pie(gastos, labels=categorias, autopct='%1.1f%%')
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    plot_ingresos_vs_gastos(frame_grafico_ingresos_gastos, fechas,
                            ingresos, gastos)
    plot_distribucion_categorias(frame_grafico_distribucion_categorias,
                                 gastos, categorias)

    return reportes
