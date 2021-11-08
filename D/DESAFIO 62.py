print('Gerador de PA')
print(5 * '=-=')
x = int(input('Primeiro termo: '))
y = int(input('Razão da PA: '))
a = 0
b = 10
cont = 10
p = 0
while b != 0:
    for a in range(1, b + 1):
        p = x + (a - 1) * y
        print(f'{p} → ', end='')
    print('PAUSA')
    b = int(input('Quantos termos você quer mostrar a mais? '))
    cont += b
    x = p + y
print(f'Progressão finalizada com {cont} termos mostrados')
