def validar_texto(texto):
    if not texto.strip():
        raise ValueError("El texto no puede estar vacío.")

def validar_fecha(fecha):
    if not fecha.strip():
        raise ValueError("La fecha no puede estar vacía.")

def validar_hora(hora):
    if not hora.strip():
        raise ValueError("La hora no puede estar vacía.")

def validar_opcion(opcion):
    if opcion not in ["1", "2", "3", "4"]:
        raise ValueError("Opción no válida.")

def validar_estado(estado):
    if estado not in ["pendiente", "completada"]:
        raise ValueError("Estado inválido.")
