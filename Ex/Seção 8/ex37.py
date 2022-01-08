def h_fatorial(x):
    m = 1
    for a in range(1, x + 1):
        m *= a**a
    return m

print(h_fatorial(4))