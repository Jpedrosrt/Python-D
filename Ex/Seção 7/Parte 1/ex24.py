dados = dict()

for a in range(3):
    x = int(input(f'\nDigite o número do {a + 1}° aluno: '))
    dados[x] = float(input(f'Digite a altura do {a + 1}° aluno em metros: '))

alto = max(dados.values())
baixo = min(dados.values())

for a, b in dados.items():
    if b == alto:
        print(f'O aluno mais alto tem o número {a} e altura {b}m')
    elif b == baixo:
        print(f'O aluno mais baixo tem o número {a} e altura {b}m')