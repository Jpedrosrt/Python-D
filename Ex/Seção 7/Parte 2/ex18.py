from random import randint

var = list()

print('Matriz:')
for i in range(3):
    aux = list()
    for j in range(3):
        x = randint(-100, 100)
        aux.append(x)
        print(f'{x:>3}', end=' ')
    var.append(aux)
    print()

som = list()

for j in range(3):
    s = 0
    for i in range(3):
        s += var[i][j]
    som.append(s)

print(f'Soma das colunas: {som}')
