from time import sleep


def contador(a, b, c):
    print('-=-' * 30)
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
    if a < b:
        b += 1
        if c < 0:
            c *= -1
    if a > b:
        b -= 1
        if c > 0:
            c *= -1
    for a in range(a, b, c):
        print(a, end=' ')
        sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=-' * 30)
print('Agora é sua vez de personalizar a contagem!')
x = int(input('Início: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
contador(x, y, z)
