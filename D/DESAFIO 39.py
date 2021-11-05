from datetime import date
x = int(input('Ano de nascimento:'))
y = date.today().year
z = y - x
print(f'Quem nasceu em {x} tem {z} anos em {y} ')
if z < 18:
    print(f'Ainda falta {18 - z} anos para o alistamento\nSeu alistamento será em {y + (18 - z)}.')
elif z > 18:
    print(f'Você já deveria ter se alistado há {z - 18} anos\nSeu alistamento foi em {y - (z - 18)}.')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
