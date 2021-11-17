from random import randint
from time import sleep
from operator import itemgetter
sleep(1)
joga = dict()
for a in range(1, 5):
    x = randint(1, 6)
    joga[f'jogador {a}'] = x
    print(f'O jogador {a} tirou {x}')
    sleep(1)
print('Ranking dos jogadores:')
sleep(1)
rank = sorted(joga.items(), key=itemgetter(1), reverse=True)  # 1 => para pegar o valor e 0 => para pegar a chave
for pos, c in enumerate(rank):
    print(f'{pos + 1}° Lugar: {c[0]} com {c[1]}')

# from random import randint
# from time import sleep
# print('Jogando os dados:')
# sleep(1)
# joga = dict()
# for a in range(1, 5):
#     x = randint(1, 6)
#     joga[f'jogador {a}'] = x
#     print(f'O jogador {a} tirou {x}')
#     sleep(1)
# print('Ranking dos jogadores:')
# sleep(1)
# b = 0
# for i in sorted(joga, key=joga.get, reverse=True):
#     b += 1
#     print(f'{b}º Lugar: {i} com {joga[i]}')
#     sleep(1)
