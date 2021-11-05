from datetime import date
x = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if x == 0:
    x = date.today().year
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:

    print(f'O ano {x} é BISSEXTO')
else:
    print(f'O ano {x} NÃO é BISSEXTO')

"""if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print(f'O ano {x} é BISSEXTO')
        else:
            print(f'O ano {x} NÃO é BISSEXTO')
    else:
        print(f'O ano {x} é BISSEXTO')
else:
    print(f'O ano {x} NÃO é BISSEXTO')"""
