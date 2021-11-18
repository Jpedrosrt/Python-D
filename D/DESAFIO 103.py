def ficha(nome, gols):
    cont = 0
    for a in gols:
        if a in '0123456789':
            cont += 1
    if cont == len(gols):
        gols = int(gols)
    if len(nome) == 0:
        nome = "<desconhecido>"
    if type(gols) == str:
        if len(gols) == 0 or type(gols) == str:
            gols = 0
    return f'O jogador {nome} fez {gols} gols no campeonato.'


n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: ')).strip()
print(ficha(n, g))

