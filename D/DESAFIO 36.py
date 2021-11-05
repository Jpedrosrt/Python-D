x = float(input('Valor da casa: R$'))
y = float(input('Salario do comprador: R$'))
z = int(input('Quantos anos de financiamento?'))
w = x/(z * 12)
print(f'Para pegar uma casa de R${x:.2f} em {z} anos a prestação será de R${w:.2f}')
if (y * 0.3) >= w:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
