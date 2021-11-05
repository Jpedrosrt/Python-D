print(25 * '=')
print('   10 TERMOS DE UMA PA')
print(25 * '=')
x = int(input('Primeiro termo: '))
y = int(input('Razão: '))
for a in range (1, 11):
    print(f'{x + (a - 1) * y} → ', end='')
print('Fim')
