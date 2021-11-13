dado = list()
info = list()
ma = me = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(info) == 0:
        ma = me = dado[1]
    else:
        if ma < dado[1]:
            ma = dado[1]
        elif me > dado[1]:
            me = dado[1]
    info.append(dado[:])
    dado.clear()
    y = ' '
    while y not in 'SN':
        y = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if y == 'N':
        break
print('-=-' * 30)
print(f'Ao todo, você cadastrou {len(info)} pessoas.')
print(f'O maior peso foi de {ma}Kg. O peso de ', end='')
for a in info:
    if a[1] == ma:
        print(f'[{a[0]}]', end=' ')
print(f'\nO menor peso foi de {me}Kg. O peso de ', end='')
for a in info:
    if a[1] == me:
        print(f'[{a[0]}]', end=' ')
