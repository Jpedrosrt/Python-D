A = list()
B = list()
for a in range(0, 10):
    A.append(float(input(f'Digite o {a + 1}° valor real: ')))
    B.append(A[a] ** 2)

print(f'Os valores digitados foram {A}')
print(f'O quadrado dos valores digitado é {B}')
