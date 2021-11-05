x = int(input('Digite um número para ver sua tabuada:'))
y = ''
print(f'{y:->11}')
for a in range (1, 11):
    print(f'{x} x {a:2} = {x * a:2}')
    a += 1
print(f'{y:->11}')
