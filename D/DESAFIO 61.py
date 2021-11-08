print(25 * '=')
print('   10 TERMOS DE UMA PA')
print(25 * '=')
x = int(input('Primeiro termo: '))
y = int(input('Razão: '))
cont = 0
while cont < 10:
    cont += 1
    print(f'{x + (cont - 1) * y} → ', end='')
print('Fim')
