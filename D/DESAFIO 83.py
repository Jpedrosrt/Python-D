x = list()
y = str(input('Digite a expressão: ')).strip()
list(y)
cont = cont2 = 0
for pos, a in enumerate(y):
    x.append(a)
    if a == '(':
        cont += 1
    elif a == ')':
        cont2 += 1
if cont == cont2:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
