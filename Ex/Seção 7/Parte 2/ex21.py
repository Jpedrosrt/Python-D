from random import uniform

var1 = list()
var2 = list()

for i in range(2):
    aux1 = list()
    aux2 = list()
    for j in range(2):
        aux1.append(round(uniform(1, 100), 1))
        aux2.append(round(uniform(1, 100), 1))
    var1.append(aux1)
    var2.append(aux2)

print('Matriz A:')
for i in range(2):
    print(var1[i])

print('\nMatriz B:')
for i in range(2):
    print(var2[i])

print('\nOpções:\n[ 1 ] Somar as duas matrizes\n[ 2 ] Subtrair a primeira matriz da segunda\n[ 3 ] Adicionar uma constante às duas matrizes')

while True:
    x = int(input('Escolha uma opção: '))
    if x == 1 or x == 3 or x == 2:
        break

if x == 1:
    for i in range(2):
        for j in range(2):
            var1[i][j] = round(var1[i][j] + var2[i][j], 1)

    print('\nSoma das matrizes A e B:')
    for i in range(2):
        print(var1[i])

if x == 2:
    for i in range(2):
        for j in range(2):
            var1[i][j] = round(var1[i][j] - var2[i][j], 1)

    print('\nSubtração das matrizes A e B:')
    for i in range(2):
        print(var1[i])

if x == 3:
    c = float(input(f'Digite a constante: '))
    for i in range(2):
        for j in range(2):
            var1[i][j] += c
            var2[i][j] += c

    print(f'\nAdicionadno a constante {c}:')
    print('Matriz A:')
    for i in range(2):
        print(var1[i])

    print('\nMatriz B:')
    for i in range(2):
        print(var2[i])
