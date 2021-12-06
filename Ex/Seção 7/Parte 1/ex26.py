from random import randint
val = list()

for a in range(10):
    val.append(randint(1, 100))

me = sum(val) / len(val)
s = 0
for a in val:
    s = s +((a - me) ** 2)

print(f'O desvio padrão do vetor {val} é {((1 / (len(val) - 1)) * s) ** 0.5:.2f}')