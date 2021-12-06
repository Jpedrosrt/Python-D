A = list()
par = list()
for a in range(0, 10):
    A.append(int(input(f'Digite o {a + 1}° valor: ')))
    if A[a] % 2 == 0:
        par.append(A[a])

for pos, b in enumerate(par):
    print(f'O {pos + 1}° valor par: {b}')
