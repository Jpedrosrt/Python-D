x = float(input('Primeira nota: '))
y = float(input('Segunda nota: '))
m = (x+y)/2
print(f'Tirando {x:.1f} e {y:.1f}, a média do aluno é {m:.1f} ')
if m >= 7:
    print('Aluno está APROVADO.')
elif 5 <= m < 7:
    print('Aluno está em RECUPERAÇÃO.')
else:
    print('Aluno REPROVADO.')
