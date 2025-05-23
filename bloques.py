def ordenar_bloques_arreglo(myArray):
    bloques_procesados = []
    bloque_actual = []

    for numero in myArray:
        if numero == 0:
            bloques_procesados.append(procesar(bloque_actual))
            bloque_actual = []
        else:
            bloque_actual.append(numero)

    else:
        bloques_procesados.append(procesar(bloque_actual))

    return " ".join(bloques_procesados)

def procesar(bloque_actual) -> str:
    bloque_actual.sort()
    if not bloque_actual:
        return "X"
    return "".join(map(str, bloque_actual))