x = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        x[l][c] = int(input(f'Digite o valor de [{l + 1}, {c + 1}]: '))
print('-=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{x[l][c]:^3}]', end='')
    print()
print('-=-' * 30)
s = sc = ma = 0
for l in range(0, 3):
    for c in range(0, 3):
        if x[l][c] % 2 == 0:
            s += x[l][c]
        if c == 2:
            sc += x[l][c]
        if l == 1:
            if ma < x[l][c]:
                ma = x[l][c]
print(f'A soma dos valores pares é {s}.')
print(f'A soma dos valores da terceira coluna é {sc}.')
print(f'O maior valor da segunda linha é {ma}.')
            