def somamatriz4x4(*args):
    s = 0
    for i in range(4):
        for j in range(4):
            s += args[i][j]
    return s

print(somamatriz4x4([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 17]))