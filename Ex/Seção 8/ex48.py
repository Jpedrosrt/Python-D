def smatriz1(*args):
    s = 0
    for i in range(3):
        for j in range(3):
            if i < 2 and j > 0 and i != j:
                s += args[i][j] 
    return s


print(smatriz1([1, 2, 10], [4, 5, 6], [7, 8, 9]))