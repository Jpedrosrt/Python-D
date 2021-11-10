cont = n = 0
while True:
    x = int(input('Digite um valor (999 para parar): '))
    if x == 999:
        break
    n += x
    cont += 1
print(f'A soma dos {cont} valores foi {n}')
