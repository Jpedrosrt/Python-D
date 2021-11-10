from random import randint
x = (randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), )
print('Os valores sorteados foram:', end=' ')
for a in range(0, 5):
    print(x[a], end=' ')
print(f'\nO maior valor sorteado foi {sorted(x)[4]}')  #ou usa max(x)
print(f'O menor valor sorteado foi {sorted(x)[0]}')  #ou usa min(x)
