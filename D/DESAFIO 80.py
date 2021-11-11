x = list()
cont = cont2 = 0
for a in range(0, 5):
    x.append(int(input('Digite um valor: ')))
    if len(x) > 1:
        while x[cont - 1] > x[cont]:
            aux = x[cont - 1]
            x[cont - 1] = x[cont]
            x[cont] = aux
            cont -= 1
            cont2 += 1
            if cont == 0:
                break
    print(f'Adicionado na lista na posição {x.index(x[cont])}')
    cont += cont2 + 1
    cont2 *= 0
print(x)
