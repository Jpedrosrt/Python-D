import moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatacao(n)} é {moeda.formatacao(moeda.metade(n))}')
print(f'O dobro de {moeda.formatacao(n)} é {moeda.formatacao(moeda.dobro(n))}')
print(f'Aumentando 10%, temos {moeda.formatacao(moeda.aumentar(n, 10))}')
print(f'Reduzindo 13%, temos {moeda.formatacao(moeda.diminuir(n, 13))}')
