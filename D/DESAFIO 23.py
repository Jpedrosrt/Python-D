"""x = str(input('Informe um número: ')).strip()
print(f'Analisando o número {x}')
a = x + '000'
print('Unidade: {}'.format(a[len(x) - 1]))
print('Dezena: {}'.format(a[len(x) - 2]))
print('Centena: {}'.format(a[len(x) - 3]))
print('Milhar: {}'.format(a[len(x) - 4]))
print(a)
print(a[-3])"""


x = int(input('Informe um número: '))
print(f'Analisando o número {x}')
print(f'Unidade: {x % 10}')
print(f'Dezena: {(x % 100)//10}')
print(f'Centena: {x % 1000//100}')
print(f'Milhar: {x % 10000//1000}')