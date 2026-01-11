
# Sistema de validación de edad y acceso

edad = input("Ingrese su edad: ")

if not edad.isdigit(): # 
    print("Edad no válida")
else:
    edad = int(edad)
    documento = input("¿Tiene documento de identidad? (si/no): ").lower()

    if edad < 0:
        print("Edad no válida")
    elif edad < 18:
        print("Acceso denegado: eres menor de edad")
    elif documento != "si":
        print("Acceso denegado: documento requerido")
    else:
        print("Acceso permitido")



#nombre de programa LIUSX