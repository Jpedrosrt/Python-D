while True:
    a = int(input('Digite um valor a menor que 10000: '))
    b = int(input('Digite um valor b menor que 10000: '))
    if a < 10000 and b < 10000:
        x = list(str(a)[::-1].strip())
        y = list(str(b)[::-1].strip())
        while len(x) != 4:
            x.append(0)
        while len(y) != 4:
            y.append(0)
        s = list()
        cont = 0
        while True:
            c = int(x[cont]) + int(y[cont])
            if c >= 10:
                c -= 10
                s.insert(0, c)
                if cont != len(x):
                    x[cont + 1] = int(x[cont + 1]) + 1
                elif cont != len(y):
                    y[cont + 1] = int(y[cont + 1]) + 1
            else:
                s.insert(0, c)
            cont += 1
            if cont == 4:
                break
        break
    else:
        print('O valor digitado é maior que 10000')

print(f'A soma entre {a} e {b} é ', end='')
for i in s:
    print(i, end='')