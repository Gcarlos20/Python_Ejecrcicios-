from models.tarea import Tarea

class GestorTareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea: Tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, descripcion):
        for tarea in self.tareas:
            if tarea.descripcion == descripcion:
                self.tareas.remove(tarea)
                return
        raise ValueError("Tarea no encontrada.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return
        for tarea in self.tareas:
            print(tarea)

    def modificar_estado(self, descripcion, estado):
        for tarea in self.tareas:
            if tarea.descripcion == descripcion:
                tarea.estado = estado
                return
        raise ValueError("Tarea no encontrada.")
