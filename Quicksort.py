import random


arr = [random.randint(1, 100) for _ in range(10)]
print("Array original:", arr)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

#de menor a mayor
arrOrg = quicksort(arr)
print("Array ordenado de menor a mayor:", arrOrg)

#de mayor a menor
arrOrg.reverse()
print("Array ordenado de mayor a menor:", arrOrg)


