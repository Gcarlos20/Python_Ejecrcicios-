# nombre del codigo TYRE
from funcione import *

def menu():
    print("\n== Bienvenido al Gestor de Estudiantes ==")


def main():
    menu()

    while True:
        print("\n1. Agregar Estudiante")
        print("2. Eliminar Estudiante")
        print("3. Mostrar Estudiantes")
        print("4. Mostrar Promedios")
        print("5. Salir")

        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            print("\nIngrese los datos del estudiante:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))

            notas = []
            for i in range(3):
                nota = float(input(f"Nota {i+1}: "))
                notas.append(nota)

            agregar_estudiante(nombre, apellido, edad, notas)

        elif opcion == 2:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            eliminar_estudiante(nombre, apellido)

        elif opcion == 3:
            mostrar_estudiantes()

        elif opcion == 4:
            mostrar_promedios()

        elif opcion == 5:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
