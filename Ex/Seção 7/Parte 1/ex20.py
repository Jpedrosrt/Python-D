val = list()
imp = list()

while True:
    x = int(input(f' Digite um número entre [0, 50]: '))
    if 0 <= x <= 50:
        val.append(x)
        if x % 2 != 0:
            imp.append(x)
    else:
        print('Digite um número válido!')
    if len(val) == 10:
        break

print(f'Vetor: {val}\nValores ímpares: {imp}')
    