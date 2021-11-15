from random import randint
from time import sleep
print('=' * 25)
print('    JOGA NA MEGA SENA')
print('=' * 25)
y = list()
z = list()
w = 0
x = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {x} JOGOS -=-=-=')
for a in range(0, x):
    while len(z) != 6:
        w = randint(1, 60)
        if w not in z:
            z.append(w)
    y.append(z[:])
    z.clear()
    print(f'JOGO {a + 1}: {sorted(y[a])}')
    sleep(1)
print('-=-=-= < BOA SORTE > =-=-=-')