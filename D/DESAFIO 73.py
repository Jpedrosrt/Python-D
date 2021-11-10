x = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Bragantino', 'Fortaleza', 'Corinthians', 'Internacional', 'Fluminense',
     'Cuiabá', 'Ceará SC', 'Athletico-PR', 'América-MG', 'Atlético-GO', 'São Paulo', 'Bahia', 'Santos', 'Sport Recife',
     'Juventude', 'Grêmio', 'Chapecoense')
print('=-=' * 150)
print(f'Lista de times do Brasileirão: {x}')
print('=-=' * 150)
print(f'Os 5 primeiros são: {x[:6]}')
print('=-=' * 150)
print(f'Os 4 últimos são: {x[-4:]}')
print('=-=' * 150)
print(f'Times em ordem alfabética: {sorted(x)}')
print('=-=' * 150)
print(f'O Chapecoense está na {x.index("Chapecoense") + 1}° posição')
