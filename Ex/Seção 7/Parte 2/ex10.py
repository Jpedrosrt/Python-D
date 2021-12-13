from random import randint

var = list()

s = 0
for i in range(3):
    aux = list()
    for j in range(3):
        x = randint(1, 100)
        aux.append(x)
        if j == i:
            s += x
    var.append(aux)

print(f'Matriz: {var}')
print(f'A soma dos valores na diagonal principal é {s}')