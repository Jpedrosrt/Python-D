x = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
     'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
y = int(input('Digite um número entre 0 e 20: '))
while y < 0 or y > 20:
    y = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {x[y]}')