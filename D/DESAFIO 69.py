cont18 = conth = contm20 = 0
while True:
    p = s = ' '
    print('-=-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-=-' * 20)
    i = int(input('Idade: '))
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while p not in 'SN':
        p = str(input('\nQuer continuar? [S/N] ')).upper().strip()[0]
    if i >= 18:
        cont18 += 1
    if s == 'M':
        conth += 1
    if s == 'F' and i < 20:
        contm20 += 1
    if p == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont18}\n'
      f'Ao todo temos {conth} homens cadastrados\n'
      f'E temos {contm20} mulheres com menos de 20 anos')

