val = list()

while True:
    x = int(input('Digite um valor: '))
    if x not in val:
        val.append(x)
    else:
        print('Esse número já foi digitado. Tente novamente!')
    if len(val) == 10:
        break

print(val)