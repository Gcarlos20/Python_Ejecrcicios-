import csv
from datetime import datetime

ARCHIVO = "Datos_financieros.csv"

transacciones = []

def cargar_datos():
    try:
        with open(ARCHIVO, mode="r", newline="", encoding="utf-8") as file: # esto es para que el archivo sea abierto en modo de lectura
            reader = csv.DictReader(file) 
            for row in reader: 
                row["monto"] = float(row["monto"]) 
                transacciones.append(row)  
    except FileNotFoundError:
        pass

def guardar_datos():
    with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as file:
        campos = ["tipo", "categoria", "monto", "fecha", "descripcion"]
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(transacciones)
    
def agregar_transaccion(tipo):
    categoria = input("Categoría: ")
    monto = float(input("Monto: "))
    descripcion = input("Descripción: ")
    fecha = datetime.now().strftime("%Y-%m-%d")

    transaccion = {
        "tipo": tipo,
        "categoria": categoria,
        "monto": monto,
        "fecha": fecha,
        "descripcion": descripcion
    }

    transacciones.append(transaccion)
    guardar_datos()
    print("Transacción registrada correctamente.\n")

def mostrar_resumen():
    ingresos = sum(t["monto"] for t in transacciones if t["tipo"] == "ingreso")
    gastos = sum(t["monto"] for t in transacciones if t["tipo"] == "gasto")
    balance = ingresos - gastos

    print("\n----- RESUMEN FINANCIERO -----")
    print(f"Ingresos totales: ${ingresos:.2f}")
    print(f"Gastos totales:   ${gastos:.2f}")
    print(f"Balance neto:     ${balance:.2f}")
    print("------------------------------\n")

def listar_transacciones():
    if not transacciones:
        print("No hay transacciones registradas.\n")
        return

    print("\n--- LISTA DE TRANSACCIONES ---")
    for i, t in enumerate(transacciones):
        print(f"{i} | {t['tipo']} | {t['categoria']} | ${t['monto']} | {t['fecha']} | {t['descripcion']}")
    print("-------------------------------\n")

def eliminar_transaccion():
    listar_transacciones()

    if not transacciones:
        return

    try:
        indice = int(input("Ingrese el número de la transacción a eliminar: "))

        if 0 <= indice < len(transacciones):
            confirmacion = input("¿Seguro que desea eliminarla? (s/n): ")

            if confirmacion.lower() == "s":
                transacciones.pop(indice)
                guardar_datos()
                print("Transacción eliminada correctamente.\n")
            else:
                print("Operación cancelada.\n")
        else:
            print("Índice inválido.\n")

    except ValueError:
        print("Debe ingresar un número válido.\n")



def menu():
    cargar_datos()
    while True:
        print("1. Agregar ingreso")
        print("2. Agregar gasto")
        print("3. Ver resumen")
        print("4. Eliminar transacción")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_transaccion("ingreso")
        elif opcion == "2":
            agregar_transaccion("gasto")
        elif opcion == "3":
            mostrar_resumen()
        elif opcion == "4":
            eliminar_transaccion()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    menu()