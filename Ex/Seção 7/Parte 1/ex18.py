val = list()

for a in range(10):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))

x = int(input('Digite um número: '))

mult = list()
for a in val:
    if a % x == 0:
        mult.append(a)

print(f'Os múltiplos de {x} no vetor são {mult}')
