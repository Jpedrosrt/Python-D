dados = dict()
gols = list()
t = 0
dados['nome'] = str(input('Nome do jogador: ')).strip()
p = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for a in range(1, p + 1):
    g = int(input(f'Quantos gols na partida {a}? '))
    t += g
    gols.append(g)
dados['gols'] = gols
dados['total'] = t   # ou usa dados['total'] = sum(gols)
print('-=-' * 30)
print(dados)
print('-=-' * 30)
for b in dados:
    print(f'O campo {b} tem valor {dados[b]}.')
print('-=-' * 30)
print(f'O jogador {dados["nome"]} jogou {p} partidas.')
d = 0
for c in dados['gols']:
    d += 1
    print(f'     => Na partida {d}, fez {c} gols.')
print(f'Foi um total de {dados["total"]} gols.')
