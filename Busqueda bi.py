import random


arr = [random.randint(1, 11) for _ in range(10)]
print("Array original: ", arr)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

arrOrg=quicksort(arr)
print("Array ordenada: ", arrOrg)

def busqueda_binaria(arrOrg, objetivo):
    inicio = 0
    fin = len(arrOrg) - 1
    
    while inicio <= fin:
        
        medio = (inicio + fin) // 2
        if arrOrg[medio] == objetivo:
            return medio
    
        elif arrOrg[medio] > objetivo:
            fin = medio - 1
        
        else:
            inicio = medio + 1
    
    return -1


objetivo = 2

resultado = busqueda_binaria(arrOrg, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("Elemento no encontrado")
