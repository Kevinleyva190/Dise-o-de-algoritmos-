N = 8
movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]
def es_valido(x, y, tablero):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1
def resolver_tour(x, y, movimiento, tablero):
    if movimiento == N * N:
        return True  
    for i in range(8):
        siguiente_x = x + movimientos_x[i]
        siguiente_y = y + movimientos_y[i]
        if es_valido(siguiente_x, siguiente_y, tablero):
            tablero[siguiente_x][siguiente_y] = movimiento  
            if resolver_tour(siguiente_x, siguiente_y, movimiento + 1, tablero):
                return True  
            tablero[siguiente_x][siguiente_y] = -1  
    return False
def tour_del_caballo():
    tablero = [[-1 for _ in range(N)] for _ in range(N)]
    tablero[0][0] = 0
    if resolver_tour(0, 0, 1, tablero):
        for fila in tablero:
            print(fila)
tour_del_caballo()