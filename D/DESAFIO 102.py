def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor Fatorial de um número n
    """
    c = 1
    print('-' * 30)
    for a in range(n, 0, -1):
        c *= a
        if show:
            print(a, end=' x ')
            if a == 1:
                print(a, end=' = ')
    return c


print(fatorial(5))
help(fatorial)
