import moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatacao(n)} é {moeda.metade(n, False)}')
print(f'O dobro de {moeda.formatacao(n)} é {moeda.dobro(n)}')
print(f'Aumentando 10%, temos {moeda.aumentar(n, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(n, 13, True)}')
