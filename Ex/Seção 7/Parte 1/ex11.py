val = list()

for a in range(0, 10):
     val.append(float(input(f'Digite o {a + 1}° valor: ')))

cont = s = 0
for a in val:
    if a < 0:
        cont += 1
    elif a > 0:
        s += a

print(f'Foram digitados {cont} números negativos e a soma dos valores positivos foi {s}.')