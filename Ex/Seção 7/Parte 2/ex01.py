var = list()
aux = list()

cont = 0

for i in range(4):
    for j in range(4):
        x = int(input(f'Digite o valor da linha {i + 1} e da coluna {j + 1}: '))
        aux.append(x)
        if x > 10:
            cont += 1
    var.append(aux.copy())
    aux.clear()

print(f'A matriz tem {cont} valores maiores que 10.')
print(f'Matriz; {var}')