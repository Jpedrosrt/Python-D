val = list()

for a in range (0, 5):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

print(f'O maior valor digitado foi {max(val)} na posição {val.index(max(val))} e o menor valor foi {min(val)} na posição {val.index(min(val))}.')