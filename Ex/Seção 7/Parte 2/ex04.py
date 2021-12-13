var = list()
aux = list()

for i in range(4):
    aux =list()
    for j in range(4): 
        aux.append(int(input(f'Digite o valor da linha {i + 1} e da coluna {j + 1}: ')))
    var.append(aux)

print(f'Matriz: {var}')
lm = var.index(max(var))
cm = var[lm].index(max(var[lm]))
print(f'O maior valor da matriz é {var[lm][cm]} localizado na linha {lm + 1} coluna {cm + 1}')
