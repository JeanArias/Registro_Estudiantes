from datos.captura import capturar_participante
from procesamiento.procesar import procesar_registro
from reporte.reporte import generar_reporte

def main():
    participantes = []

    print("Sistema de Registro de Participantes")

    participante = capturar_participante()

    procesar_registro(participantes, participante)

    generar_reporte(participantes)

if __name__ == "__main__":
    main()
