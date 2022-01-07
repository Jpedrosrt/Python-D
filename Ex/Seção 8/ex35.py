def fatorial(x):
    n = d = 1
    for a in range(2 * x, 0, -1):
        n *= a
    for a in range(x, 0, -1):
        d *= a
    return n / d

print(fatorial(5))