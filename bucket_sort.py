import random
arr = [random.randint(1, 11) for _ in range(10)]
def bucket_sort(arr):
    # Encontrar el valor máximo en la lista para determinar el rango
    max_value = max(arr)
    size = len(arr)

    # Crear cubos vacíos (listas vacías)
    buckets = [[] for _ in range(size)]

    # Distribuir los elementos en los cubos
    for i in range(size):
        index = int(arr[i] * size / (max_value + 1))
        buckets[index].append(arr[i])

    # Ordenar cada cubo individualmente
    for bucket in buckets:
        bucket.sort()

    # Combinar los cubos ordenados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Ejemplo de uso

print("Array original:", arr)

arr_ordenada = bucket_sort(arr)
print("Array ordenado:", arr_ordenada)
