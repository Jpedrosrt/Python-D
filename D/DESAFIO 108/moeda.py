def metade(num=0):
    return num/2


def aumentar(num=0, ti=0):
    res = num * (1 + ti/100)
    return res


def diminuir(num=0, ti=0):
    res = num * (1 - ti/100)
    return res


def dobro(num=0):
    res = num * 2
    return res


def formatacao(num=0, moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.', ',')
