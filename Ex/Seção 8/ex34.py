def fato_duplo(n):
    if n <= 0 or n % 2 == 0:
        return 'Valor inválido'
    else:
        x = 1
        for a in range(1, n + 1, 2):
            x *= a
        return x

print(fato_duplo(7))