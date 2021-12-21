from random import randint

var1 = list()
var2 = list()

for i in range(3):
    aux1 = list()
    for j in range(3):
        aux1.append(randint(1, 100))
    var1.append(aux1)

print('Matriz A:')
for i in range(3):
    print(var1[i])

for i in range(3):
    aux1 = list()
    x = var1[i]
    for i1 in range(3):
        s = 0
        for j in range(3):
            s += x[j] * var1[j][i1]
        aux1.append(s)
    var2.append(aux1)

print('\nMatriz B (A^2):')
for i in range(3):
    print(var2[i])