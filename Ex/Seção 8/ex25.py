def serie(n):
    s = 0
    for a in range(1, n + 1):
        s += (a**2 + 1)/ (a + 3)
    return s

print(serie(30))