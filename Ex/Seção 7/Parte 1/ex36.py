val = list()

for a in range(10):
    val.append(float(input(f'Digite o {a + 1}° valor: ')))

print(f'O vetor ordenado é {sorted(val)}')
