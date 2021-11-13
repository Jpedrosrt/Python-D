x = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = 0
for l in range(0, 3):
    for c in range(0, 3):
        x[l][c] = int(input(f'Digite um valor para {[l + 1, c + 1]}: '))
print('=-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{x[l][c]:^5}]', end='')
    print()
