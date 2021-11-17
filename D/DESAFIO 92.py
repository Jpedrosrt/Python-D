from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip()
dados['Idade'] = date.today().year - int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
print('=-=' * 30)
for a in dados:
    print(f'{a} tem o valor {dados[a]}')
    if dados[a] == float:
        print(f'{a} tem o valor {dados[a]:.2f}')
