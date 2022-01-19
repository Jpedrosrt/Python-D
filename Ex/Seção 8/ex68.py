def interstr(a, b):
    a = ' '.join(a).split()
    cont = 1
    for pos, i in enumerate(b):
        a.insert(pos + cont, i)
        cont += 1

    a = ''.join(a)

    return a


print(interstr('ACEGIKLM', 'BDFHJ'))