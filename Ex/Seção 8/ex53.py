def identidade(*args):
    tam = len(args)
    cont = 0
    for i in range(tam):
        for j in range(tam):
            if i == j and args[i][j] == 1:
                cont += 1
    if cont == tam:
        print('É uma Matriz Identidade')
    else:
        print('Não é uma Matriz Identidade')


identidade([1, 0, 0], [0, 1, 0], [0, 0, 1])
identidade([1, 0, 0], [1, 0, 0], [0, 0, 1])
