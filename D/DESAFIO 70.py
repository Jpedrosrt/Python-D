t = mm = p = m = 0
cont = 1
b = ''
while True:
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$ '))
    t += p
    if p > 1000:
        mm += 1
    if cont == 1:
        m = p
        b = n
    if p < m:
        m = p
        b = n
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if q == 'N':
        break
    cont += 1
print('\nFIM DO PROGRAMA')
print(f'O total da compra foi R$ {t:.2f}\n'
      f'Temos {mm} produtos custando mais de R$ 1000.00\n'
      f'O produto mais barato foi {b} que custa R$ {m:.2f}')
