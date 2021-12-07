val = list()
aux = list()

for a in range(15):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

for a in val:
    if a != 0:
        aux.append(a)

print(aux)
