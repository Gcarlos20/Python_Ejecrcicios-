from service.gestor_tareas import GestorTareas

gestor = GestorTareas()

while True:
    print("\n1. Agregar\n2. Listar\n3. Completar\n4. Salir")
    try:
        op = int(input("Opción: "))
        if op == 1:
            desc = input("Descripción: ").strip()
            if not desc:
                raise ValueError("Descripción vacía")
            gestor.agregar(desc)

        elif op == 2:
            for i, t in enumerate(gestor.listar()):
                estado = "✔" if t["completada"] else "✘"
                print(f"{i}. {t['descripcion']} [{estado}]")

        elif op == 3:
            i = int(input("Índice: "))
            gestor.completar(i)

        elif op == 4:
            break

        else:
            print("Opción inválida")

    except Exception as e:
        print("Error:", e)
