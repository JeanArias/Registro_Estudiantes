#Grupo 3: Reporte Final#
def generar_reporte(participantes):
    """
    1-Recibir la lista global de participantes procesada. 
    2-Generar e imprimir un reporte formateado exactamente con la siguiente estructura visual 
    empleando un ciclo for:
    """
    print("============================")
    print("REGISTRO DEL EVENTO")
    print("============================")
    print("Participantes registrados\n")

    # Ciclo for para recorrer y numerar a cada participante
    for i, persona in enumerate(participantes, 1):
        print(f"{i}.")
        print(f"Nombre: {persona['nombre']}")
        print(f"Empresa: {persona['empresa']}")
        print(f"Correo: {persona['correo']}")
        print("---------------------")

    # Conteo final de la lista
    total = len(participantes)
    print("============================")
    print(f"Total registrados: {total}")
    print("============================")
