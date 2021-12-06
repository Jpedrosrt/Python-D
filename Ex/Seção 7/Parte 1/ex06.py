val = list()

for a in range(0, 10):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))
print(f'O maior valor digitado foi {max(val)} e o menor {min(val)}.')