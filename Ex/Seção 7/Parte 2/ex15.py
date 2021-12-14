from random import choice

var = list()
alt = ['a', 'b', 'c', 'd']
gab = list()

for i in range(5):
    aux = list()
    for j in range(10):
        aux.append(choice(alt))
    var.append(aux)

print('Respostas dos alunos: ')
for pos, a in enumerate(var):
    print(f'{pos + 1}° Aluno: {a}')

print('-=-' * 20)
for b in range(10):
    gab.append(choice(alt))
print(f'Gabarito: {gab}')

print('-=-' * 20)
print('Notas: ')
for c in range(5):
    s = 0
    for d in range(10):
        if var[c][d] == gab[d]:
            s +=1 
    print(f'{c + 1}° Aluno: {s}')