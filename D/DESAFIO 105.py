def notas(*n, sit=False):
    """
    -> Função para analisar notas e situaçõesde vários alunos.
    :param n: uma ou mais notas dos aluns (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    d = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': (sum(n)/len(n))}
    if sit:
        if d['média'] < 5:
            d['situação'] = 'RUIM'
        elif 7 > d['média'] >= 5:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'BOA'
    return d


r = notas(5.4, 8, 3.8, 10, sit=True)
print(r)
help(notas)
