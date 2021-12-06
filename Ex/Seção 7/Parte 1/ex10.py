notas = list()

for a in range(0, 15):
    notas.append(float(input(f'Digite a nota do {a + 1}° aluno: ')))

print(f'Média geral: {sum(notas) / len(notas)}')
