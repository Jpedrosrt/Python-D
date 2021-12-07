from math import factorial

n = int(input('Digite o número de linhas do Triangulo de Pascal que você gostaria de ver: '))

for a in range(n):
    for b in range(n):
        if b <= a:
            print (int(factorial(a) / (factorial(b) * factorial(a - b))), end=' ')
    print()