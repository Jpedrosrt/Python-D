from time import sleep


def lin(msg, s=0, t=97, f=36):
    print(f'\033[{s};{t};{f}m~' * (len(msg) + 4))
    print(f'\033[{s};{t};{f}m  {msg}')
    print(f'\033[{s};{t};{f}m~' * (len(msg) + 4))


def ch(fb):
    lin(f"Acessando o manual do comando '{fb}'", t=30, f=42)
    sleep(2)
    print('\033[0;30;107m', end='')
    help(fb)
    print('\033[0;30;107m', end='')


while True:
    lin('SISTEMA DE AJUDA PyHELP', t=30, f=46)
    com = str(input('\033[mFunção ou Biblioteca > '))
    if com.upper() == 'FIM':
        break
    ch(com)
lin('ATÉ LOGO', t=30, f=41)
