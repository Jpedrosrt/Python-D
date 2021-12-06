val = list()

for a in range(5):
    val.append(float(input(f'Digite o {a + 1}° valor: ')))

while True:
    print('-=' * 30)
    x = int(input('[ 0 ] Sair\n[ 1 ] Vetor na ordem direta\n[ 2 ] Vetor na ordem inversa\nEscolha uma opção: '))
    if x == 0:
        break
    elif x == 1:
        print(f' O vetor na ordem direta: {val}')
    elif x == 2:
        print(f'O vetor na ordem inversa: {val[::-1]}')
    else:
        print('Código inválido. Tente Novamente!')