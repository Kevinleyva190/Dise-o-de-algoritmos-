str1 = "aabcakcac"
str2 = "aabcabacba"
resultado = 0
cadena = ""

for i in range(len(str1)):
    for j in range(len(str2)):
        k = 0
        while (i + k) < len(str1) and (j + k) < len(str2) and str1[i + k] == str2[j + k]:
            k += 1
        if k > resultado:
            resultado = k
            cadena = str1[i:i + k]

print("La subacadena mas larga es: ", cadena)
