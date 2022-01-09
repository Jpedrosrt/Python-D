def smatriz2(*args):
    s = 0 
    for i in range(3):
        for j in range(3):
            if i > 0 and j < 2 and i != j:
                s += args[i][j]
    return s


print(smatriz2([1, 2, 10], [10, 5, 6], [7, 8, 9]))