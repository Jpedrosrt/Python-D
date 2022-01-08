def pares(*args):
    cont = 0
    for a in args:
        if a % 2 == 0:
            cont += 1
    return cont

print(pares(5, 4, 3, 58, 2, 3, 4, 7, 10))