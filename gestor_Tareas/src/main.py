from service.gestor_tareas import GestorTareas
from service.validaciones import validar_texto, validar_fecha, validar_hora, validar_estado
from models.tarea import Tarea



gestor = GestorTareas()

while True:
    print("\n1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == "1":
            descripcion = input("Descripción: ")
            validar_texto(descripcion)

            fecha = input("Fecha: ")
            validar_fecha(fecha)

            hora = input("Hora: ")
            validar_hora(hora)

            estado = input("Estado (pendiente/completada): ")
            validar_estado(estado)

            tarea = Tarea(descripcion, fecha, hora, estado)
            gestor.agregar_tarea(tarea)
            print("Tarea agregada correctamente.")

        elif opcion == "2":
            descripcion = input("Descripción de la tarea a eliminar: ")
            validar_texto(descripcion)
            gestor.eliminar_tarea(descripcion)
            print("Tarea eliminada.")

        elif opcion == "3":
            gestor.mostrar_tareas()

        elif opcion == "4":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida.")

    except ValueError as e:
        print(f"Error: {e}")
