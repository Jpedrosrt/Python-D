A = [1, 0, 5, -2, -5, 7]

soma = A[0] + A[1] + A[5]
print(f'A soma dos valores nas posições 0, 1 e 5 é igual a {soma}')

A[4] = 100

for a in A:
    print(a)