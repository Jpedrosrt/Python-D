from random import randint

var1 = list()
var2 = list()
var3 = list()

for i in range(3):
    aux1 = list() 
    aux2 = list()
    for j in range(3):
        aux1.append(randint(1, 100))
        aux2.append(randint(1, 100))
    var1.append(aux1)
    var2.append(aux2)

print('Matriz A:')
for i in range(3):
    print(var1[i])

print('\nMatriz B:')
for i in range(3):
    print(var2[i])

for i in range(3):
    aux1 = list()
    x = var1[i]
    for i1 in range(3):
        s = 0
        for j in range(3):
            s += x[j] * var2[j][i1]
        aux1.append(s)
    var3.append(aux1)

print('\nMatriz C (A x B):')
for i in range(3):
    print(var3[i])