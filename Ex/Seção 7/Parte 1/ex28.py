val = list()
v1 = list()
v2 = list()

for a in range(10):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

for i in val:
    if i % 2 != 0:
        v1.append(i)
    else:
        v2.append(i)

print(f'Vetor v: {val}\nVetor v1: {v1}\nVetor v2: {v2}')