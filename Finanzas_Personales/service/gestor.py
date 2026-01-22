class GestorFinanzas:
    def __init__(self, usuario):
        self.usuario = usuario

    def total_ingresos(self):
        return sum(t.monto for t in self.usuario.transacciones if t.tipo == "ingreso")

    def total_gastos(self):
        return sum(t.monto for t in self.usuario.transacciones if t.tipo == "gasto")

    def mostrar_resumen(self):
        print("\n--- RESUMEN FINANCIERO ---")
        print(f"Ingresos: ${self.total_ingresos()}")
        print(f"Gastos: ${self.total_gastos()}")
        print(f"Balance: ${self.total_ingresos() - self.total_gastos()}")

    def agregar_transaccion(self, transaccion):
        self.usuario.transacciones.append(transaccion)

    def mostrar_transacciones(self):
        if not self.usuario.transacciones:
            print("No hay transacciones.")
        else:
            for t in self.usuario.transacciones:
                print(t.mostrar())
