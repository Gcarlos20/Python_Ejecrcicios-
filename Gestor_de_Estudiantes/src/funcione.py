# lista de estudiantes
estudiantes = []


def agregar_estudiante(nombre, apellido, edad, notas):
    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "notas": notas
    }
    estudiantes.append(estudiante)
    print("Estudiante agregado correctamente.")


def eliminar_estudiante(nombre, apellido):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre and estudiante["apellido"] == apellido:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado correctamente.")
            return
    print("Estudiante no encontrado.")


def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for est in estudiantes:
        print(f'{est["nombre"]} {est["apellido"]} - Edad: {est["edad"]}')


def calcular_promedio(notas):
    return sum(notas) / len(notas)


def mostrar_promedios():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for est in estudiantes:
        promedio = calcular_promedio(est["notas"])
        print(f'{est["nombre"]} {est["apellido"]} - Promedio: {promedio:.2f}')
