def triang(n):
    for a in range(n + 1):
        print('*' * a)
    for a in range(1, n + 1):
        print('*' * (n - a))
    
triang(100)