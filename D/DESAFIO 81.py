x = list()
while True:
    x.append(int(input('Digite um valor: ')))
    y = ' '
    while y not in 'SN':
        y = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if y == 'N':
        break
print('-=-' * 30)
print(f'Você digitou {len(x)} elementos')
print(f'Os valores em ordem decrescente são: {sorted(x, reverse=True)}')
if 5 in x:
    print(f'O valor 5 faz parte da lista nas posições: ', end='')
    for pos, a in enumerate(x):
        if a == 5:
            print(pos, end='...')
else:
    print('O valor 5 não foi encontrado na lista!')
