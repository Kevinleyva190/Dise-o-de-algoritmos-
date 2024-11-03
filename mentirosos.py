import random

def generar_respuestas(n):
    return [random.choice(["sí", "no"]) for _ in range(n)]

def formar_parejas(respuestas):
    parejas = []
    i = 0
    while i < len(respuestas) - 1:
        pareja = (respuestas[i], respuestas[i + 1])
        parejas.append(pareja)
        i += 2
    if len(respuestas) % 2 != 0:
        parejas.append((respuestas[-1],))
    return parejas

def evaluar_parejas(parejas):
    resultados = []
    for pareja in parejas:
        if len(pareja) == 1:
            resultados.append(pareja[0])
        elif pareja[0] == "sí" and pareja[1] == "sí":
            resultados.append("sí")
        elif pareja[0] == "no" and pareja[1] == "no":
            resultados.append("no")
    return resultados

def verificar_mayoria(respuestas):
    conteo_si = respuestas.count("sí")
    conteo_no = respuestas.count("no")
    total = len(respuestas)
    if conteo_si > total // 2:
        return "sí"
    elif conteo_no > total // 2:
        return "no"
    else:
        return None

def realizar_simulacion(n=100):
    respuestas = generar_respuestas(n)
    ronda = 1
    while len(respuestas) > 1:
        print(f"Ronda {ronda}:")
        parejas = formar_parejas(respuestas)
        print(f"Parejas: {parejas}")
        respuestas = evaluar_parejas(parejas)
        mayoria = verificar_mayoria(respuestas)
        if mayoria:
            print(f"Ronda {ronda}: Mayoría de '{mayoria}' (resultado final)")
            break
        else:
            print(f"Ronda {ronda}: Sin mayoría clara, continuando...")
            print(f"Resultados de la ronda {ronda}: {respuestas}")
            print("-----")
            ronda += 1
    else:
        print("No se alcanzó una mayoría en las rondas.")


realizar_simulacion()
