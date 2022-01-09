def smatriz4(*args):
    s = 0
    tam = len(args)
    for i in range(tam):
        for j in range(tam):
            if j == 0:
                s += args[i][tam - (i + 1)]
    return s


print(smatriz4([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]))
