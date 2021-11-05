x = int(input('Digite um número inteiro:'))
y = int(input('Escolha uma das bases para conversão:'
              '\n[ 1 ] converter para BINÁRIO'
              '\n[ 2 ] converter para OCTAL'
              '\n[ 3 ] converter para HEXADECIMAL'
              '\nSua opção:'))
if y == 1:
    print(f'{x} convertido para BINÁRIO é igual a {bin(x)[2:]}')
elif y == 2:
    print(f'{x} convertido para OCTAL é igual a {oct(x)[2:]}')
elif y == 3:
    print(f'{x} convertido para HEXADECIMAL é igual a {hex(x)[2:]}')
else:
    print('Escolha um número válido!')
