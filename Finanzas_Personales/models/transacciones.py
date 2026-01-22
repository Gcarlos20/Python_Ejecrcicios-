import datetime

class Transaccion:
    def __init__(self, tipo, monto, categoria, fecha=None):
        self.tipo = tipo
        self.monto = monto
        self.categoria = categoria
        self.fecha = fecha or datetime.date.today()

    def mostrar(self):
        return f"{self.tipo.upper()} | {self.monto} | {self.categoria} | {self.fecha}"
