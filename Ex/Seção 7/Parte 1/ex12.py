val = list()

for a in range(0, 5):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

print(f'Os valores digitados foram {val} o maior valor foi {max(val)}, o menor foi {min(val)} a média dos valores {sum(val) / len(val)}')
