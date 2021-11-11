x = list()
p = list()
i = list()
while True:
    x.append(int(input('Digite um valor: ')))
    y = ' '
    while y not in 'SN':
        y = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if y == 'N':
        break
for a in x:
    if (a % 2) == 0:
        p.append(a)
    else:
        i.append(a)
print('-=-' * 30)
print(f'A lista completa é {x}')
print(f'A lista de pares é {p}')
print(f'A lista de ímpares é {i}')
