def triang(n):
    s = 1
    for a in range(1, n + 1):
        print(' ' * (n - a) + '*' * (s))
        s += 2

triang(50)