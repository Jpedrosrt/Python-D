from math import factorial

x = int(input('Digite um número para\n'
              'calcular o seu fatorial: '))
f = factorial(x)
a = x
print(f'Calculando {x}! = ', end='')
while a > 0:
    print(a, end='')
    print(' x ' if a > 1 else ' = ', end='')
    a -= 1
print(f)

"""x = int(input('Digite um número para\n'
              'calcular o seu fatorial: '))
a = 1
p = x
while x > 1:
    a = a * x
    x = x - 1
print(f'Calculando {p}! =', end=' ')
for b in range(p, 1, -1):
    print(b, end=' x ')
print(f'1 = {a}')"""
