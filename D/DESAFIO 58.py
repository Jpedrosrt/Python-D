from secrets import randbelow

"""from random import randint               Exemplo
x = randint(0, 10)"""

x = randbelow(11)
print('Sou seu computador...\n'
      'Acabei de PENSAR em número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?')
cont = 0
y = 0
while y != x:
    y = int(input('Qual é o seu palpite? '))
    cont += 1
    if y < x:
        print('Mais... Tente novamente.')
    elif y > x:
        print('Menos... Tente novamente')
print(f'Acertou com {cont} tentativas. Parabéns!')
