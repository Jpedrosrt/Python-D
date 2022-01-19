def rotina(A, n):
    while len(A) < n:
        A.append(getchar())
    
    return A


def getchar():
    a = str(input('Digite um caractere: '))
    return a


l = list()
tam = 10

print(rotina(l, tam))