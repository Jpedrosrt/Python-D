A = list()
for a in range(1, 9):
    A.append(int(input(f'Digite o {a}° valor: ')))
x = int(input('Escolha uma posição do vetor: '))
y = int(input('Escolha outra posição do vetor: '))

print(f'A soma dos valores das posições {x} e {y} é {A[x - 1] + A[y - 1]}')
