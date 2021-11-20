def metade(num=0, form=False):
    res = num/2
    if form:
        return formatacao(res)
    else:
        return res


def aumentar(num=0, ti=0, form=False):
    res = num * (1 + ti/100)
    if form:
        return formatacao(res)
    else:
        return res


def diminuir(num=0, ti=0, form=False):
    res = num * (1 - ti/100)
    if form:
        return formatacao(res)
    else:
        return res


def dobro(num=0, form=False):
    res = num * 2
    if form:
        return formatacao(res)
    return res


def formatacao(num=float(0), moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.', ',')
