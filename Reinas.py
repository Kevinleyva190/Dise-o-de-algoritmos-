class Arbol:
    def __init__(self, r):
        self.raiz = r

class Nodo:
    def __init__(self, cont):
        self.contenido = cont
        self.hijos = []

    def copia(self, cont):
        return [list(fila) for fila in cont]

    def es_valido(self, fila, col):
        for i in range(8):
            if self.contenido[fila][i] == 1:
                return False
            if self.contenido[i][col] == 1:  
                return False
            if fila + i < 8 and col + i < 8 and self.contenido[fila + i][col + i] == 1:
                return False
            if fila - i >= 0 and col - i >= 0 and self.contenido[fila - i][col - i] == 1:
                return False
            if fila + i < 8 and col - i >= 0 and self.contenido[fila + i][col - i] == 1:
                return False
            if fila - i >= 0 and col + i < 8 and self.contenido[fila - i][col + i] == 1:
                return False
        return True

    def creaHijos(self, n, arbol):
        if n == 8:
            print("Resultado encontrado:")
            for fila in self.contenido:
                print(fila)
            print("\n")
            arbol.detenerBusqueda = True
            return

        for i in range(8):
            if self.es_valido(n, i):
                contHijo = self.copia(self.contenido)
                contHijo[n][i] = 1
                H = Nodo(contHijo)
                H.creaHijos(n + 1, arbol)
                self.hijos.append(H)
                if arbol.detenerBusqueda:
                    return

R = Nodo([[0] * 8 for _ in range(8)])
arbol = Arbol(R)
arbol.detenerBusqueda = False

R.creaHijos(0, arbol=arbol)
