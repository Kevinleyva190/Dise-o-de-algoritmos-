def mochila(capacidad, elementos, n):
    
    tabla = [[0 for x in range(capacidad + 1)] for y in range(n + 1)]


    for i in range(1, n + 1):
        peso = elementos[i - 1][0]
        valor = elementos[i - 1][1]
        for w in range(capacidad + 1):
            if peso <= w:
                tabla[i][w] = max(valor + tabla[i - 1][w - peso], tabla[i - 1][w])
            else:
                tabla[i][w] = tabla[i - 1][w]

    return tabla[n][capacidad]

elementos = [[1, 1],[3, 4],[4, 5],[5, 7]]
capacidad =9 
n = len(elementos)
resultado = mochila(capacidad, elementos, n)
print(f"El valor máximo que se puede obtener es: {resultado}")

