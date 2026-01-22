class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.transacciones = []
        self.gastos = []
    def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def agregar_gasto(self, gasto):
        self.gastos.append(gasto)
        
    def mostrar_transacciones(self):
        if not self.transacciones:
            print("No hay transacciones registradas.")
        for t in self.transacciones:
            print(t.mostrar())
