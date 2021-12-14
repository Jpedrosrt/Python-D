from random import randint, choice

var = set()
matriz = list()

m = 5 # tamanho da matriz
while len(var) < (m*m):
    var.add(randint(1, 99))


for i in range(m):
    aux = list()
    for j in range(m):
        x = choice(list(var))
        aux.append(x)
        var.remove(x)
    matriz.append(aux)
    

print(f'Matriz: {matriz}')
