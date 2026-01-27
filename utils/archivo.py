import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUTA = os.path.join(BASE_DIR, "data", "tareas.json")

def cargar_tareas():
    if not os.path.exists(RUTA):
        return []
    with open(RUTA, "r") as f:
        return json.load(f)

def guardar_tareas(tareas):
    with open(RUTA, "w") as f:
        json.dump(tareas, f, indent=4)
