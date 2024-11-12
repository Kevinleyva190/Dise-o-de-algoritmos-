class Box:
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

    def __lt__(self, other):
        return self.d * self.w < other.d * other.w

def maxStackHeight(arr, n):
    rot = [Box(0, 0, 0) for _ in range(3 * n)]
    index = 0

    for i in range(n):
        rot[index].h = arr[i].h
        rot[index].d = max(arr[i].d, arr[i].w)
        rot[index].w = min(arr[i].d, arr[i].w)
        index += 1

        rot[index].h = arr[i].w
        rot[index].d = max(arr[i].h, arr[i].d)
        rot[index].w = min(arr[i].h, arr[i].d)
        index += 1

        rot[index].h = arr[i].d
        rot[index].d = max(arr[i].h, arr[i].w)
        rot[index].w = min(arr[i].h, arr[i].w)
        index += 1

    n *= 3
    rot.sort(reverse=True)

    msh = [0] * n

    for i in range(n):
        msh[i] = rot[i].h

    for i in range(1, n):
        for j in range(0, i):
            if rot[i].w < rot[j].w and rot[i].d < rot[j].d:
                if msh[i] < msh[j] + rot[i].h:
                    msh[i] = msh[j] + rot[i].h

    maxm = -1
    for i in range(n):
        maxm = max(maxm, msh[i])

    return maxm

if __name__ == "__main__":
    C = [
        [2, 1, 3],
        [5, 4, 1],
        [3, 3, 4],
        [2, 7, 3],
        [1, 9, 2],
        [5, 1, 4],
        [7, 7, 3],
        [2, 9, 1],
        [4, 8, 7],
        [3, 7, 9]
    ]
    arr = [Box(h, w, d) for h, w, d in C]

    n = len(arr)
    print("La altura máxima es:", maxStackHeight(arr, n))