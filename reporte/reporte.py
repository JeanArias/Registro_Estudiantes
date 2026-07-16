#Grupo 3: Reporte Final#
# Uso correcto de importación con alias (as)
import math as m

def generar_reporte(participantes):
    """
    1-Recibir la lista global de participantes procesada. 
    2-Generar e imprimir un reporte formateado exactamente con la siguiente estructura visual 
    empleando un ciclo for:
    """
    # 1. MÉTODOS DE LISTAS: Clonar la lista para no alterar la original y ordenarla

    lista_ordenada = participantes.copy()
    
    # Uso de sort() y manejo de índices mediante una función lambda interna
    lista_ordenada.sort(key=lambda x: x["nombre"])

    print("============================")
    print("REGISTRO DEL EVENTO")
    print("============================")
    print("Participantes registrados\n")

    # Recorrido iterativo con for y control de índices manual
    for indice in range(len(lista_ordenada)):
        persona = lista_ordenada[indice]
        
        # EXCEPCIONES: Bloque robusto de control requerido
        try:
            # 1. VALIDACIÓN DE EDAD (Debe ser mayor de edad)
            if "edad" not in persona:
                raise ValueError("Falta el campo de edad en el registro.")
            
            # Convertimos a entero por seguridad si viene como string
            edad_usuario = int(persona["edad"]) 
            if edad_usuario < 18:
                raise ValueError(f"El participante es menor de edad ({edad_usuario} años). Registro no permitido.")

            # 2. VALIDACIÓN DE CORREO
            if "@" not in persona["correo"]:
                raise ValueError("El formato del correo electrónico es inválido.")
                
            # 3. MÉTODOS DE STRINGS: 
            # Uso de split() y len() para verificar el nombre completo
            palabras_nombre = persona["nombre"].split()
            if len(palabras_nombre) < 1:
                raise ValueError("El nombre no contiene caracteres válidos.")
            
            # Formateo visual usando upper(), lower(), strip() y replace()
            nombre_formateado = persona["nombre"].strip().upper()
            empresa_formateada = persona["empresa"].strip().replace("_", " ").upper()
            correo_formateado = persona["correo"].strip().lower()

            # Imprimir la estructura visual exacta solicitada (Índice inicia en 1)
            print(f"{indice + 1}.")
            print(f"Nombre: {nombre_formateado}")
            print(f"Edad: {edad_usuario} años")  # <- Añadido al reporte visual
            print(f"Empresa: {empresa_formateada}")
            print(f"Correo: {correo_formateado}")
            print("---------------------")

        except ValueError as error_validacion:
            # Captura específica de errores de valor (incluyendo si no es mayor de edad)
            print(f"❌ Error en registro #{indice + 1}: {error_validacion}")
            
        finally:
            # Bloque finally obligatorio que se ejecuta siempre al procesar cada elemento
            pass

    # Conteo final obligatorio usando len()
    total_registrados = len(lista_ordenada)
    
    print("============================")
    print(f"Total registrados en lista: {total_registrados}")
    print("============================")

def eliminar_participante_por_nombre(participantes, nombre_buscar):
    """
    Función auxiliar para cumplir con el requisito obligatorio de remove() en listas
    y el uso del operador de pertenencia 'in'.
    """
    nombre_limpio = nombre_buscar.strip().upper()
    
    # Uso de recorrido iterativo con for para buscar el elemento
    for persona in participantes:
        if nombre_limpio in persona["nombre"].upper():
            # Uso de remove() en listas
            participantes.remove(persona)
            print(f"✔ Se ha eliminado a {persona['nombre']} de la lista.")
            return participantes
            
    print("⚠️ No se encontró ningún participante con ese nombre.")
    return participantes
    
