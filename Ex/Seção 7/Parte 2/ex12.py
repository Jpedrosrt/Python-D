from random import randint

var =list()
var2 = list()

m = 3 # tamanho da matriz
for i in range(m):
    aux = list()
    aux2 = list()
    for j in range(m):
        x = randint(1, 100)
        aux.append(x)
        aux2.append(0)
    var.append(aux)
    var2.append(aux2)

print(f'Matriz: {var}')

for i in range(m):
    for j in range(m):
        if i == j:
            var2[i].pop(j)
            var2[i].insert(j, var[i][j])
        elif i != j:
            var2[i].pop(j)
            var2[i].insert(j, var[j][i])

print(f'Matriz transposta: {var2}')