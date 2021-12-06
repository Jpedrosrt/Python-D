A = list()
B = list()
C = list()

for a in range(10):
    A.append(int(input(f'Digite o {a + 1}° valor do vetor A: ')))
print('-=' * 30)
for b in range(10):
    B.append(int(input(f'Digite o {a + 1}° valor do vetor B: ')))

for c in range(10):
    C.append(A[c])
    C.append(B[c])

print(f'Vetor A: {A}\nVetor B: {B}\nVetor C: {C}')