from models.transacciones import Transaccion
from models.usuario import Usuario
from service.gestor import GestorFinanzas
import datetime

def menu():
    print("\n--- Sistema de Finanzas Personales ---")
    print("1. Agregar ingreso")
    print("2. Agregar gasto")
    print("3. Mostrar transacciones")
    print("4. Mostrar resumen")
    print("5. Salir")

nombre = input("Ingrese su nombre: ")
usuario = Usuario(nombre)
gestor = GestorFinanzas(usuario)

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        monto = float(input("Monto del ingreso: "))
        categoria = input("Categoría: ")
        gestor.agregar_transaccion(Transaccion("ingreso", monto, categoria, datetime.date.today()))
        print("Ingreso agregado correctamente.")

    elif opcion == "2":
        monto = float(input("Monto del gasto: "))
        categoria = input("Categoría: ")
        gestor.agregar_transaccion(Transaccion("gasto", monto, categoria, datetime.date.today()))
        print("Gasto agregado correctamente.")

    elif opcion == "3":
        gestor.mostrar_transacciones()

    elif opcion == "4":
        gestor.mostrar_resumen()

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")


# nombre del codigo Tyrion 