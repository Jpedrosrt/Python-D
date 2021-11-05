s = 0
cont = 0
for c in range (1, 7):
    c = int(input('Digite um número:'))
    if c % 2 == 0:
        s += c
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {s}')
