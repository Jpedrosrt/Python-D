ma = 0
me = 0
for a in range(1, 6):
    x = float(input(f'Peso da {a}° pessoa: '))
    if a == 1:
        ma = x
        me = x
    elif x > ma:
        ma = x
    elif x < ma:
        me = x
print(f'\nO maior peso lido foi {ma:.1f}Kg\n'
      f'O menor peso lido foi {me:.1f}Kg')
