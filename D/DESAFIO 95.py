dados = dict()
gols = list()
info = list()
t = x = 0
while True:
    print('-=-' * 30)
    dados['nome'] = str(input('Nome do jogador: ')).strip()
    p = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for a in range(1, p + 1):
        g = int(input(f'Quantos gols na partida {a}? '))
        t += g
        gols.append(g)
    dados['gols'] = gols[:]
    dados['total'] = t
    info.append(dados.copy())
    gols.clear()
    y = ' '
    if y not in 'SN':
        y = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if y == 'N':
        break
print('-=-' * 30)
print(f'{"pos":>4}', end=' ')
for d in dados.keys():
    print(f'{d:<15}', end='')
print()
print('-' * 40)
for pos, b in enumerate(info):
    print(f'{pos:^4} ', end='')
    for c in b.values():
        print(f'{str(c):<15}', end='')
    print()
print('-' * 40)
while True:
    x = int(input('Mostrar dados de qual jogador? (999 para cancelar) '))
    if x == 999:
        break
    if x >= len(info):
        print('ERROR! Cod inexistente')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {info[x]["nome"]} -- ')
        for e in range(1, len(info[x]["gols"]) + 1):
            print(f'No jogo {e} fez {info[x]["gols"][e - 1]}.')
    print('-' * 40)

print('FIM')
