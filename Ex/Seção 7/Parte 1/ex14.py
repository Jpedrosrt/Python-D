val = list()

for a in range(0, 10):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

reps = dict() 

for a in val:
    reps[a] = val.count(a)

for a, b in reps.items():
    print(f'O número {a} apareceu {b} vezes')

"""from collections import Counter
val = list()

for a in range(0, 10):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

val = Counter(val)

for a, b in val.items():
    print(f'O número {a} apareceu {b} vezes.')"""
