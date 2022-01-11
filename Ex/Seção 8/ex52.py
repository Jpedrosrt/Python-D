def transposta(*args):
    tam = len(args)
    x = list()
    for i in range(tam):
        x.append([])
        for j in range(tam):
            x[i].append(0)
    for i in range(tam):
        for j in range(tam):
            x[i][j] = args[j][i]
    return x

print(transposta([1, 2, 3], [4, 5, 6], [7, 8, 9]))