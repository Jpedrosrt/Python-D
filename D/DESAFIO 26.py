x = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(x.upper().count('A')))
print('A primeira letra A apareceu na posição {}'.format(x.upper().find('A') + 1))
print('A última letra A apareceu na posição {}'.format(x.upper().rfind('A') + 1))
