from random import randint, choice

var = dict()
alt = ['a', 'b', 'c', 'd', 'e']
gab = list()

for i in range(3):
    x = int(input(f'Matricula do {i + 1}° aluno: '))
    aux = list()
    gab = list()
    for j in range(10):
        aux.append(choice(alt))
        gab.append(choice(alt))
    var[x] = aux

print(f'Gabarito: {gab}')

g = 0
for a in var.keys():
    s = 0
    for pos, i in enumerate(var[a]):
        if i == gab[pos]:
            s += 1
    if s >= 7:
        g += 1
    print('-=-' * 20)
    print(f'Matricula: {a}\nRepostas: {var[a]}\nNota: {s}')

print('-=-'* 20)
print(f'O percentual de aprovação foi {(g / 3) * 100:.2f}%')