val = list()

for a in range(10):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))
    if val[a] < 0:
        val[a] = 0
    
print(val)
