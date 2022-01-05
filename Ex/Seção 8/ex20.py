def fatorial(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f

print(fatorial(6))