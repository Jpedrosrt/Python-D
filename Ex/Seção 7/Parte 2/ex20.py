from random import uniform

var =list()

s = 0
sb = 0
for i in range(3):
    aux = list()
    for j in range(6):
        x = round(uniform(1, 100), 1)
        aux.append(x)
        if j % 2 != 0:
            s += x
        if j == 1 or j == 3:
            sb += x
    var.append(aux)

print('Matriz:')
for i in range(3):
    print(var[i])
print(f'\nA soma dos dos elementos das colunas ímpares é {s:.1f}\nConsiderando a primeira coluna 0')
print(f'\nA média aritmética dos elementos da segunda e quarta colunas é {sb/6:.2f}\n')

for i in range(3):
    s = 0
    for j in range(6):
        if j == 2 or j == 1:
            s += var[i][j]
    var[i][5] = round(s, 1)


print('Matriz modificada:')
for i in range(3):
    print(var[i])