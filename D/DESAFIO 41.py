from datetime import date
x = int(input('Ano de Nascimento: '))
y = date.today().year
z = y - x
print(f'O atleta tem {z} anos.')
if z <= 9:
    print('Classificação: MIRIM')
elif z <= 14:
    print('Classificação: INFANTIL')
elif z <= 19:
    print('Classificação: JUNIOR')
elif z <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')


'''from datetime import date
x = int(input('Ano de Nascimento: '))
y = date.today().year
z = y - x
print(f'O atleta tem {z} anos.')
if z <= 9:
    print('Classificação: MIRIM')
elif 9 < z <= 14:
    print('Classificação: INFANTIL')
elif 14 < z <= 19:
    print('Classificação: JUNIOR')
elif 19 < z <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')'''
