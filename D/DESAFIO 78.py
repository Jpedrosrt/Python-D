x = list()  #ou x = []
for n in range(0, 5):
    x.append(int(input(f'Digite o valor da posição {n}: ')))
print('-=-' * 30)
print(f'Você digitou os valores {x}')
ma = max(x)
mi = min(x)
print(f'O maior valor digitado foi {ma} nas posições ', end='')
for pos, b in enumerate(x):
    if b == ma:
        print(pos, end='...')
print(f'\nO menor valor digitado foi {mi} nas posições ', end='')
for pos, b in enumerate(x):
    if b == mi:
        print(pos, end='...')
