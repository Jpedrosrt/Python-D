from random import randint

var =list()

m = 4 # tamanho da matriz
for i in range(m):
    aux = list()
    for j in range(m):
        x = randint(1, 20)
        aux.append(x)
    var.append(aux)

print(f'Matriz: {var}')

for i in range(m):
    for j in range(m):
        if j > i:
            var[i][j] = 0
        
print(f'Matriz triangular inferior: {var}')