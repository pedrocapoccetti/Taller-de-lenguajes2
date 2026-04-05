def calcular_puntaje_ronda(scores):
    """Suma los puntajes de los jueces para cada participante en una ronda."""
    resultados = {}
    for participante, jueces in scores.items():
        resultados[participante] = sum(jueces.values())
    return resultados

def ganador_ronda(resultados):
    """Devuelve el ganador de la ronda y su puntaje."""
    ganador = max(resultados, key=resultados.get)
    return ganador, resultados[ganador]

def actualizar_tabla(tabla, resultados, ganador):
    """Actualiza la tabla acumulada con los resultados de la ronda."""
    for participante, puntaje in resultados.items():
        if participante not in tabla:
            tabla[participante] = {
                "total": 0,
                "rondas_ganadas": 0,
                "mejor_ronda": 0,
                "puntajes": []
            }
        tabla[participante]["total"] += puntaje
        tabla[participante]["puntajes"].append(puntaje)
        if puntaje > tabla[participante]["mejor_ronda"]:
            tabla[participante]["mejor_ronda"] = puntaje
    tabla[ganador]["rondas_ganadas"] += 1
    return tabla

def generar_tabla_final(tabla):
    # Convertimos el diccionario en lista de filas
    filas = list(tabla.values())
    
    # Ordenamos primero por total de puntos y luego por rondas ganadas
    filas_ordenadas = sorted(
        filas,
        key=lambda fila: (fila["total"], fila["rondas_ganadas"]),
        reverse=True
    )
    
    return filas_ordenadas

