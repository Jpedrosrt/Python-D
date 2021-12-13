var = list()
aux = list()

for i in range(4):
    aux = list()
    for j in range(4): 
        aux.append(int(input(f'Digite o valor da linha {i + 1} e da coluna {j + 1} da matriz 1: ')))
    var.append(aux)
print('-=' * 30)
var2 = list()

for i in range(4):
    aux = list()
    for j in range(4): 
        aux.append(int(input(f'Digite o valor da linha {i + 1} e da coluna {j + 1} da matriz 2: ')))
    var2.append(aux)

print(f'Matriz 1: {var}')
print(f'Matriz 2: {var2}')

var3 = list()

for i in range(4):
    aux = list()
    for j in range(4):
        if var[i][j] >= var2[i][j]:
            aux.append(var[i][j])
        else:
            aux.append(var2[i][j])
    var3.append(aux)
        
print(f'Matriz 3: {var3}')