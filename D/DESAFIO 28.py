from secrets import randbelow
from time import sleep
x = randbelow(6)
print('\033[33m-=\033[m' * 30)
print('\033[33mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-=\033[m' * 30)
y = int(input('Em que número pensei? '))
print('\033[31mPROCESSANDO...\033[m')
sleep(3)
if y == x:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {x} e não no {y}!')
