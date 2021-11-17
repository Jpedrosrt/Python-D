aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'O Nome é {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]:.1f}')
if aluno['media'] >= 7:
    aluno['situ'] = 'Aprovado'
else:
    aluno['situ'] = 'Reprovado'
print(f'A situação é igual a {aluno["situ"]}')
