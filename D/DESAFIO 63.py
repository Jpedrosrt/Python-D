print(25 * '-')
print('Sequência de Fibonacci')
print(25 * '-')
x = int(input('Quantos termos você quer mostrar? '))
cont = 0
while cont < x:
    y = ((((1 + 5 ** 0.5) / 2) ** cont) - (((1 - (5 ** 0.5)) / 2) ** cont)) / 5 ** 0.5
    print(f'{y:.0f} → ', end='')
    cont += 1
print('FIM')

"""print(25 * '-')
print('Sequência de Fibonacci')
print(25 * '-')
x = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
cont = 2
print(f'\n{a} → {b} → ', end='')
while cont < x:
    f = a + b
    print(f'{f} → ', end='')
    a = b
    b = f
    cont += 1
print('FIM')"""
