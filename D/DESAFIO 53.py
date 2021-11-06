x = str(input('Digite uma frase: ')).strip().upper()
y = x.split()
z = ''.join(y)
w = ''
for v in range(len(z) - 1, -1, -1):
    w += z[v]
print(f'O inverso de {z} é {w}')
if z == w:
    print('A frase digitada é um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um PALÍNDROMO!')

""" y = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
print(f'O inverso de {y} é {y[::-1]}')
if y == y[::-1]:
    print('A frase digitada é um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um PALÍNDROMO!')"""
