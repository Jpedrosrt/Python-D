from random import choice as ch
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
print(f'O aluno escolhido foi {ch([a, b, c, d])}')
