def emparejamiento_estable(preferencias_a, preferencias_b):
    libres_a = list(preferencias_a.keys())
    propuestas = {a: [] for a in preferencias_a}
    parejas = {}

    while libres_a:
        a = libres_a[0]
        lista_preferencias = preferencias_a[a]

        for b in lista_preferencias:
            if b not in propuestas[a]:
                propuestas[a].append(b)

                if b not in parejas:
                    parejas[b] = a
                    libres_a.pop(0)
                    break
                else:
                    otro_a = parejas[b]
                    preferencias_b_actual = preferencias_b[b]

                    if preferencias_b_actual.index(a) < preferencias_b_actual.index(otro_a):
                        parejas[b] = a
                        libres_a.pop(0)
                        libres_a.append(otro_a)
                        break
    return parejas
preferencias_a = {
    'A1': ['B1', 'B2', 'B3'],
    'A2': ['B2', 'B1', 'B3'],
    'A3': ['B1', 'B2', 'B3']
}
preferencias_b = {
    'B1': ['A3', 'A1', 'A2'],
    'B2': ['A1', 'A2', 'A3'],
    'B3': ['A1', 'A2', 'A3']
}
resultado = emparejamiento_estable(preferencias_a, preferencias_b)
print("Parejas estables:", resultado)