x = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou: {x}')
cont9 = cont3 = contp = 0
for a in range(0, 4):
    if x[a] == 9:
        cont9 += 1 # x.count(9)
    if x[a] == 3:
        cont3 += 1
print(f'O valor 9 apareceu {cont9} vezes')
if cont3 == 0:
    print(f'O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {x.index(3) + 1}ª posição')
print(f'Os valores pares digitados foram:', end=' ')
for a in range(0, 4):
    if x[a] % 2 == 0:
        print(x[a], end=' ')
