from random import randint
print('=' * 150)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=' * 150)
cont = 0
while True:
    x = ' '
    while x not in 'PI':
        x = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    y = int(input('Diga um valor: '))
    z = randint(0, 10)
    s = y + z
    if s % 2 == 0:
        print('-' * 150)
        print(f'Você jogou {y} e o computador {z}. Total de {s} DEU PAR')
        print('-' * 150)
        if x == 'P':
            print('Você VENCEU!\n'
                  'Vamos jogar novamente...')
        elif x == 'I':
            print('Você PERDEU!')
            break
    else:
        print('-' * 150)
        print(f'Você jogou {y} e o computador {z}. Total de {s} DEU ÍMPAR')
        print('-' * 150)
        if x == 'P':
            print('Você PERDEU!')
            break
        elif x == 'I':
            print('Você VENCEU!\n'
                  'Vamos jogar novamente...')
    cont += 1
print('=' * 150)
print(f'GAME OVER! Você venceu {cont} vezes.')
