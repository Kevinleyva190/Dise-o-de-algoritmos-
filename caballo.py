# Dimensiones del tablero
N = 8

# Posibles movimientos del caballo
movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Función para verificar si la posición (x, y) es válida en el tablero y no visitada
def es_valido(x, y, tablero):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

# Función recursiva para resolver el problema del tour del caballo
def resolver_tour(x, y, movimiento, tablero):
    if movimiento == N * N:
        return True  # Se visitaron todas las casillas

    # Intentar todos los movimientos posibles del caballo
    for i in range(8):
        siguiente_x = x + movimientos_x[i]
        siguiente_y = y + movimientos_y[i]
        if es_valido(siguiente_x, siguiente_y, tablero):
            tablero[siguiente_x][siguiente_y] = movimiento  # Marcar como visitado
            if resolver_tour(siguiente_x, siguiente_y, movimiento + 1, tablero):
                return True  # Si se logra completar, devolver True
            tablero[siguiente_x][siguiente_y] = -1  # Deshacer el movimiento

    return False  # No se encontró solución desde esta posición

# Función principal para inicializar el tablero y llamar a la función recursiva
def tour_del_caballo():
    # Inicializar el tablero con -1, indicando que ninguna casilla ha sido visitada
    tablero = [[-1 for _ in range(N)] for _ in range(N)]

    # Colocar el caballo en la primera posición (0, 0)
    tablero[0][0] = 0

    # Llamar a la función recursiva desde la posición inicial
    if resolver_tour(0, 0, 1, tablero):
        # Imprimir el recorrido del caballo
        for fila in tablero:
            print(fila)
    else:
        print("No se encontró una solución.")

# Llamar a la función principal
tour_del_caballo()
