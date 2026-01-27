from models.tareas import Tarea
from utils.archivo import cargar_tareas, guardar_tareas

class GestorTareas:
    def __init__(self):
        self.tareas = cargar_tareas()

    def agregar(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea.to_dict())
        guardar_tareas(self.tareas)

    def listar(self):
        return self.tareas

    def completar(self, indice):
        self.tareas[indice]["completada"] = True
        guardar_tareas(self.tareas)
