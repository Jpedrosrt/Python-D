val = list()

for a in range(20):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

print(f'Os valores digitados sem repetições foram {set(val)} ')

"""
from collections import Counter

val = list()

for a in range(20):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

val = Counter(val)

print(f'Os valores digitados sem repetição foram ', end='')
for a, b in val.items():
    print(f'{a}', end='-')
print('FIM')
"""
