A = list()
B = list()

for a  in range(5):
    A.append(float(input(f'Digite {a + 1}° valor do vetor A: ')))
for a  in range(5):
    B.append(float(input(f'Digite {a + 1}° valor do vetor B: ')))

p = 0
for a in range(5):
    p = p + A[a] * B[a]

print(f'Vetor A: {A}\nVetor B: {B}\nProduto Escalar: {p}')