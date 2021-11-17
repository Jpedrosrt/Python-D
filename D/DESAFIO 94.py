dados = dict()
info = list()
s = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip()
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    dados['idade'] = int(input('Idade: '))
    s += dados['idade']
    info.append(dados.copy())
    y = ' '
    if y not in 'SN':
        y = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if y == 'N':
        break
me = s/len(info)
print('-=-' * 30)
print(f'- O grupo tem {len(info)} pessoas.')
print(f'- A média das idades é de {me:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for a in info:
    if a['sexo'] == 'F':
        print(a["nome"], end=' ')
print(f'\n- A lista de pessoas que estão acima da média:')
for a in info:
    if a['idade'] > me:
        for b in a.keys():
            print(f' {b} = {a[b]}', end=';')
        print('\n')
print('<< ENCERRADO >>')
