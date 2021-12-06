val = list()

for a in range(0, 6):
    x = int(input(f'Digite o {a + 1}° valor: '))
    if x % 2 == 0:
        val.append(x)

print(val[::-1])
