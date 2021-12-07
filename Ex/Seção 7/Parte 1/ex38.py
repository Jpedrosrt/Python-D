val = list()
aux = list()

for a in range(10):
    x = int(input(f'Digite o {a + 1}° valor: '))
    if a == 0:
        val.append(x)
    else:
        for b in range(len(val)):
            if val[b] >= x:
                val.insert(b, x)
                break
            elif b == len(val) - 1:
                val.append(x)

print(val)