var = list()
aux = list()

for i in range(4):
    aux =list()
    for j in range(4): 
        aux.append(int(input(f'Digite o valor da linha {i + 1} e da coluna {j + 1}: ')))
    var.append(aux)

print(f'Matriz: {var}')

x = int(input('Digite um valor: '))
cont = 0
aux2 = list()

for i in var:
    for j in i:
        if j == x:
            l = cont
            c = var[cont].index(j)
            aux2.append([l, c])
    cont += 1
if l == None or c == None:
    print('Não encontrado')
else:  
    print(f'O número {x} foi encontrado: ')
    for a in aux2:
        print(f'Na linha {a[0] + 1} na coluna {a[1] + 1}')
        