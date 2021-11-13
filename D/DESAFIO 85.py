x = [[], []]
for a in range(1, 8):
    y = int(input(f'Digite o {a}° valor: '))
    if y % 2 == 0:
        x[0].append(y)
    else:
        x[1].append(y)
print(x)
print('-=-' * 30)
print(f'Os valores pares foram: {sorted(x[0])}')
print(f'Os valores ímpares foram: {sorted(x[1])}')
