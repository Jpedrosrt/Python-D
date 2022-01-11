def sdpm(*args):
    sp = ss = 0
    tam = len(args)
    aux2 = tam - 1
    for i in range(tam):
        sp += args[i][i]
        ss += args[i][aux2]
        aux2 -= 1
    print(f'A soma da diagonal principal é {sp}')
    print(f'A soma da diagonal secundaria é {ss}')

sdpm([1, 2, 3], [4, 5, 6], [125, 8, 9])