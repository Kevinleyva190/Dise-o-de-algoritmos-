import heapq

def dijkstra(grafo, inicio):
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[inicio] = 0
    predecesores = {vertice: None for vertice in grafo}
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[vertice_actual]:
            continue

        for vecino, peso in grafo[vertice_actual].items():
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                predecesores[vecino] = vertice_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias, predecesores

def reconstruir_ruta(predecesores, inicio, destino):
    ruta = []
    actual = destino
    while actual is not None:
        ruta.append(actual)
        actual = predecesores[actual]
    ruta.reverse()
    return ruta

grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5, 'E': 3},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 2, 'F': 3},
    'E': {'B': 3, 'D': 2, 'F': 1, 'G': 5},
    'F': {'D': 3, 'E': 1, 'G': 2},
    'G': {'E': 5, 'F': 2}
}

vertice_inicio = 'A'
vertice_destino = 'G'
rutas_mas_cortas, predecesores = dijkstra(grafo, vertice_inicio)
ruta = reconstruir_ruta(predecesores, vertice_inicio, vertice_destino)

print("Distancias más cortas desde el nodo:", vertice_inicio)
for vertice, distancia in rutas_mas_cortas.items():
    print(f"Distancia a {vertice}: {distancia}")

if ruta:
    print("Ruta más corta:", " -> ".join(ruta))
else:
    print("No hay ruta disponible.")
