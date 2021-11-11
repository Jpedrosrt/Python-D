x = z = list()
cont = 0
while True:
    z = x[:]
    x.append(int(input('Digite um valor: ')))
    if x[cont] in z:
        print('Valor duplicado! Não vou adicionar.')
        x.pop()
        cont -= 1
    else:
        print('Valor adicionado com sucesso!')
    y = ' '
    while y not in 'SN':
        y = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if y == 'N':
        break
    cont += 1
print('-=-' * 30)
print(f'Você digitou os valores {sorted(x)}')
