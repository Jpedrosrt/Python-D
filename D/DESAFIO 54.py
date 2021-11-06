from datetime import date
cont1 = 0
cont2 = 0
ano = date.today().year
for a in range(1, 8):
    x = int(input(f'Em que ano a {a}° pessoa nasceu? '))
    y = ano - x
    if y >= 18:
        cont1 += 1
    else:
        cont2 += 1
print(f'\nAo todo tivemos {cont1} pessoas maiores de idade\n'
      f'E também tivemos {cont2} pessoas menores de idade')
