from random import randint
from time import sleep
a = ['PEDRA', 'PAPEL', 'TESOURA']
b = randint(0, 2)
print('Suas opções:'
      '\n[ 0 ] PEDRA'
      '\n[ 1 ] PAPEL'
      '\n[ 2 ] TESOURA')
c = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 10)
print(f'Computador jogou {a[b]}')
print(f'Jogador jogou {a[c]}')
print('-=-' * 10)
if c == 0 and b == 0 or c == 1 and b == 1 or c == 2 and b == 2:
    print('EMPATE')
elif c == 0 and b == 1 or c == 1 and b == 2 or c == 2 and b == 0:
    print('JOGADOR PERDE!')
elif c == 0 and b == 2 or c == 1 and b == 0 or c == 2 and b == 1:
    print('JOGADOR VENCE!')


"""from secrets import randbelow
from time import sleep
print('Suas opções:'
      '\n[ 1 ] PEDRA'
      '\n[ 2 ] PAPEL'
      '\n[ 3 ] TESOURA')
x = int(input('Qual é a sua jogada: '))
y = randbelow(2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 10)
if y == 0:
    print('Computador jogou PEDRA')
elif y == 1:
    print('Computador jogou PAPEL')
else:
    print('Computador jogou TESOURA')
if x == 1:
    print('Jogador jogou PEDRA')
elif x == 2:
    print('Jogador jogou PAPEL')
else:
    print('Jogador jogou TESOURA')
print('-=-' * 10)
if x == 1 and y == 0 or x == 2 and y == 1 or x == 3 and y == 2:
    print('EMPATE')
elif x == 1 and y == 1 or x == 2 and y == 2 or x == 3 and y == 0:
    print('JOGADOR PERDE!')
elif x == 1 and y == 2 or x == 2 and y == 0 or x == 3 and y == 1:
    print('JOGADOR VENCE!')"""