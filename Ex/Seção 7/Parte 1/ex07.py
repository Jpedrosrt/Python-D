val = list()

for a in range(0, 10):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

print(f'O vetor digitado foi {val} o seu maior valor é {max(val)} na posição {val.index(max(val))}')