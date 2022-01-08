def s_fatorial(n):
    m = 1
    for a in range(n, 0, -1):
        for b in range(a, 0, -1):
            m *= b
    return m


print(s_fatorial(6))