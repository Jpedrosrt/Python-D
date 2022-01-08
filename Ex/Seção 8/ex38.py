def expo_fatorial(x):
    m = x
    for a in range(1, x):
        m = m ** (x - a)
    return m

print(expo_fatorial(5))