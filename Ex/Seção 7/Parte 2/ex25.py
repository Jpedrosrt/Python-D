from random import randint
from time import sleep


def jogada(n=False):
    x = 0
    while True:
        if n:
            i = randint(0, 2)
            j = randint(0, 2)
            x = f'{i}'+ f'{j}'

            if 0 <= i <= 2 and 0 <= j <= 2 and (x) not in jogadas:
                jogadas.append(x)
                var[i][j] = c
                return True
        else:
            print('=' * 30)
            print('TABULEIRO')
            for a in var:
                print()
                for b in a:
                    print(f'{b:>2}', end=' ')
            print()
            print('=' * 30)
            i = int(input('Escolha a linha da posição que você quer jogar: '))
            j = int(input('Escolha a coluna da posição que você quer jogar: '))
            x = f'{i}'+ f'{j}'

            if 0 <= i <= 2 and 0 <= j <= 2 and (x) not in jogadas:
                jogadas.append(x)
                var[i][j] = jo
                return False


def verificador():
    for a in var:
        if a[0] == a[1] == a[2] != 0:
            w = a[0]
            return w
    if var[0][0] == var[1][1] == var[2][2] != 0:
        w = var[0][0]
        return w
    if var[0][2] == var[1][1] == var[2][0] != 0:
        w = var[0][2]
        return w
    for a in range(3):
        if var[0][a] == var[1][a] == var[2][a] != 0:
            w = var[0][a]
            return w
                


var = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
jogadas = list()

print('=' * 30)
print(f"{'JOGO DA VELHA':^30}")
print('=' * 30)

while True:
    jo = input('Escolha X ou O para jogo: ').upper()
    print('=' * 30)
    if jo == 'X':
        c = 'O'
        break
    elif jo == 'O':
        c = 'X'
        break

if jo == 'X':
    print('=' * 30)
    print(f'Você Joga Primeiro')
    fj = True 
else:
    fj = False
    print('=' * 30)
    print('O Computador Joga Primeiro')



while True:
    if fj:
        w = verificador()
        if w == 'X' or w == 'O':
            break
        if len(jogadas) == 9:
            w = 'E'
            break
        fj = jogada()
    else:
        w = verificador()
        if w == 'X' or w == 'O':
            break
        if len(jogadas) == 9:
            w = 'E'
            break
        print(f'O Computador Vai jogar...')
        sleep(2)
        fj = jogada(True)

if w == jo:
    print('=' * 30)
    print('PARABÉNS! Você Ganhou')
    print('=' * 30)
    print('TABULEIRO')
    for a in var:
        print()
        for b in a:
            print(f'{b:>2}', end=' ')
elif w == c:
    print('=' * 30)
    print('Você Perdeu! ¯\(°_o)/¯')
    print('=' * 30)
    print('TABULEIRO')
    for a in var:
        print()
        for b in a:
            print(f'{b:>2}', end=' ')
else:
    print('=' * 30)
    print('EMPATE')
    print('=' * 30)
    print('TABULEIRO')
    for a in var:
        print()
        for b in a:
            print(f'{b:>2}', end=' ')
