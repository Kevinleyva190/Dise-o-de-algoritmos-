import random
def esta_ordenada(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
def bogosort(arr):
    intentos = 0
    while not esta_ordenada(arr):
        random.shuffle(arr)
        intentos += 1
        
    return arr, intentos
arr = [3, 1, 4, 1, 5,8,9]
print("Lista original:", arr)

arr_ordenada = bogosort(arr)
print("Lista ordenada:", arr_ordenada)
