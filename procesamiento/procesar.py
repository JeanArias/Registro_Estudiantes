def procesar_registro(lista_participantes, datos_nuevo_participante):
    # 1. Validar si el correo electrónico es válido comprobando si contiene '@' (operador in)
    if "@" not in datos_nuevo_participante["correo"]:
        print(f"[Alerta]: El correo '{datos_nuevo_participante['correo']}' no es válido. No se registrará.")
        return lista_participantes

    # 2. Uso obligatorio de replace() para estandarizar posibles espacios múltiples accidentales en el nombre
    nombre_limpio = datos_nuevo_participante["nombre"].replace("  ", " ")
    
    # 3. Separar el nombre completo utilizando el método split()
    partes_nombre = nombre_limpio.split()
    primer_nombre = partes_nombre[0] if len(partes_nombre) > 0 else "Sin nombre"
    apellido = partes_nombre[1] if len(partes_nombre) > 1 else "Sin apellido"
    
    print(f"\n[Procesando] Nombre: {primer_nombre} | Apellido: {apellido}")

    # Actualizamos el nombre limpio en el diccionario antes de agregarlo
    datos_nuevo_participante["nombre"] = nombre_limpio

    # 4. Manipular la lista utilizando append()
    lista_participantes.append(datos_nuevo_participante)
    
    # 5. Manipular la lista utilizando sort() (Ordenamos alfabéticamente por nombre)
    lista_participantes.sort(key=lambda x: x["nombre"])
    
    # 6. Mostrar la cantidad total de participantes de manera dinámica con len()
    total = len(lista_participantes)
    print(f"-> Registro exitoso. Total de participantes en memoria: {total}")
    
    # 7. REQUISITO OBLIGATORIO: Recorrer la lista utilizando un ciclo for para mostrar en consola
    print("\n--- Lista Actual de Participantes en Memoria (Grupo 2) ---")
    for participante in lista_participantes:
        print(f"- {participante['nombre']} ({participante['empresa']})")
    print("----------------------------------------------------------")
    
    return lista_participantes


def eliminar_participante(lista_participantes, nombre_a_eliminar):
    # Manipular la lista utilizando remove()
    nombre_buscar = nombre_a_eliminar.strip()
    for p in lista_participantes:
        if p["nombre"].lower() == nombre_buscar.lower():
            lista_participantes.remove(p)
            print(f"\n[Éxito]: El participante '{nombre_buscar}' ha sido eliminado de la lista.")
            
            # Mostramos la cantidad total dinámica usando len() tras la eliminación
            print(f"Total actual de participantes: {len(lista_participantes)}")
            return lista_participantes
            
    print(f"\n[Aviso]: No se encontró ningún participante con el nombre '{nombre_buscar}'.")
    return lista_participantes