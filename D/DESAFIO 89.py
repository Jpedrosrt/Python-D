x = list()
y = list()
c = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    x.append(nome)
    x.append(n1)
    x.append(n2)
    x.append((n1 + n2)/2)
    y.append(x[:]) # Com uma lista é possível usar y.append([nome, n1, n2, media])
    x.clear()
    a = ' '
    while a not in 'SN':
        a = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if a == 'N':
        break
print('{:<5} {:<10} {:<5}'.format('No.', 'NOME', 'MÉDIA'))
print('-' * 35)
for pos, b in enumerate(y):
    print('{:<5} {:<10} {:<5}'.format(pos, b[0],  b[3]))
while True:
    print('-' * 35)
    c = int(input('Quer mostrar as notas de qual aluno? (999 para interromper) '))
    if c == 999:
        break
    print(f'As notas de {y[c][0]} são {y[c][1:-1]}')
