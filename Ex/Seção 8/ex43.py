from random import randint

def preencher(n, *args):
    args = set(args)
    cont = 0
    while cont < n:
        x = randint(1, 1000)
        if x not in args:
            args.add(x)
            cont += 1
    return args


j = int(input('Digite o número de valores que vai ser adicionado: '))
print(preencher(j , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
