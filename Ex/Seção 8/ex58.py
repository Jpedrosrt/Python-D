def prodmatriz(a, b, c):

    if len(a) != len(b):
        return 'As matrizes tem ordens diferentes'

    
    tam = len(a)

    for i in range(tam):
        aux = list()
        for d in range(tam):
            s = 0
            
            for j in range(tam):
                s += A[i][j] * B[j][d]
            aux.append(s)
        c.append(aux)
    return c        
    

A = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
B = [[17, 18, 19], [21, 22, 23], [25, 26, 27]]
j = list()
print(prodmatriz(A, B, j))
print(j)
