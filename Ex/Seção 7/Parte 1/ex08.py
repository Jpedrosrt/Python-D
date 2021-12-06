val = list()

for a in range(0, 6):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

print(val[::-1])
