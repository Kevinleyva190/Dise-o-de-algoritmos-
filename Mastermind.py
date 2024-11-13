digitos = ('1','2','3','4','5','6','7','8')
codigo = '1134'
print ("Algoritmo de Mastermind")
propuesta = input("Intento: ")

intentos = 1
while propuesta != codigo:
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0
    for i in range(4):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    print ("Tu propuesta (", propuesta, ") tiene", aciertos, \
           "aciertos y ", coincidencias, "coincidencias.")

    propuesta = input("Propón otro codigo: ")

print ("numero de intentos: ", intentos)