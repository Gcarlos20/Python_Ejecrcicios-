class Tarea:

    def __init__(self, descripcion, fecha, hora, estado):
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
  
    def __str__(self):
        return (
            f"Tarea: {self.descripcion} | "
            f"Fecha: {self.fecha} | "
            f"Hora: {self.hora} | "
            f"Estado: {self.estado}"
        )
