from random import randint

var = list()

s = 0
m = 3 # tamanho da matriz
aux2 = 1
for i in range(m):
    aux = list()
    for j in range(m):
        x = randint(1, 100)
        aux.append(x)
        if j == (m - aux2):
            s += x
    aux2 += 1
    var.append(aux)

print(f'Matriz: {var}')
print(f'A soma dos valores na diagonal secundária é {s}')
