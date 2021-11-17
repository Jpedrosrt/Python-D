from time import sleep


def maior(*valor):
    print('-=-' * 30)
    print('Analisando os valores passados...')
    for a in valor:
        print(a, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(valor)} valores ao todo.')
    if len(valor) == 0:
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(valor)}.')


maior(1, 2, 3, 4, 5, 9, 10, 25, 40)
maior(1, 2, 4, 5, 4, 8, 7, 9)
maior(4, 7, 0, 9, 10, 10)
maior(8, 9, 10, 10)
maior(1)
maior()
