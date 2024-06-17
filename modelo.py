class Transccion():
    def __init__(self, id, monto, fecha, categoria, razon):
        self.id = id
        self.monto = monto
        self.fecha = fecha
        self.categoria = categoria
        self.razon = razon


class Ingreso(Transccion):
    pass


class Gasto(Transccion):
    pass


class Gestor_presupuesto(Transccion):
    pass
