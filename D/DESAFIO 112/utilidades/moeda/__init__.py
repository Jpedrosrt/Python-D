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
    return f'{moeda:}{num:.2f}'.replace('.', ',')


def resumo(num=0, tia=0, tir=0, form=True):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analisado: \t{formatacao(num)}')
    print(f'Dobro do valor: \t{dobro(num, form=form)}')
    print(f'Metade do valor: \t{metade(num, form=form)}')
    print(f'{tia}% de aumento: \t{aumentar(num,ti=tia, form=form)}')
    print(f'{tir}% de redução: \t{diminuir(num,ti=tir, form=form)}')
    print('-' * 30)
