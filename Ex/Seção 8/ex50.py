def smatriz3(*args):
    s = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                s += args[i][j]
    return s

print(smatriz3([1, 2, 10], [4, 5, 6], [7, 89, 10]))