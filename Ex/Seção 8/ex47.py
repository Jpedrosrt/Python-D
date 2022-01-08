def maiorq10(*args):
    cont = 0
    for a in args:
        for i in a:
            for n in i:
                if n > 10:
                    cont += 1
    return cont

print(maiorq10([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))