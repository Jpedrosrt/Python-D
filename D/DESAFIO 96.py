def area(a, b):
    print(f'A área de um terreno {a}x{b} é de {a * b}m².')


print('-' * 30)
print('     CONTROLE DE TERRENO')
print('-' * 30)
x = float(input('LARGURA (m): '))
y = float(input('COMPRIMENTO (m): '))
area(x, y)
