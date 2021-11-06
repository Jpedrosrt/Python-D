x = int(input('Digite um número: '))
cont = 0
for a in range (1, x + 1):
    if x % a == 0:
        print(f'\33[33m{a}\33[m', end=' ')
        cont += 1
    else:
        print(f'\33[31m{a}\33[m', end=' ')
print(f'\nO número {x} foi divisível {cont} vezes')
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
