class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    def to_dict(self):
        return {
            "descripcion": self.descripcion,
            "completada": self.completada
        }
