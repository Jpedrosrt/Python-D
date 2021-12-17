from random import uniform

var = list()

for i in range(10):
    aux = list()
    for j in range(3):
        aux.append(round(uniform(0, 10), 1))
    var.append(aux)

for pos, a in enumerate(var):
    print(f'Aluno {pos + 1:>2}: {a}')

pos = 0
for j in range(3):
    m = 10
    for i in range(10):
        if var[i][j] < m:
           m = var[i][j]
           pos = i
    print(f'A menor nota da prova {j + 1} foi {m} do aluno {pos + 1}')
    var.pop(pos)
    var.insert(pos, [11, 11, 11])
