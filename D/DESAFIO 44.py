x = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO'
      '\n[ 1 ] à vista dinheiro/cheque'
      '\n[ 2 ] à vista cartão'
      '\n[ 3 ] 2x no cartão'
      '\n[ 4 ] 3x ou mais no cartão')
y = float(input('Qual é a opção: '))
if y == 1:
    print(f'Sua compra de R${x:.2f} vai custar R${(x * 0.9):.2f} no final.')
elif y == 2:
    print(f'Sua compra de R${x:.2f} vai custar R${(x * 0.95):.2f} no final.')
elif y == 3:
    print(f'Sua compra vai ser parcelada em 2x de R${(x / 2):.2f} SEM JUROS'
          f'\nSua compra vai custar R${x:.2f}')
elif y == 4:
    a = int(input('Quantas parcelas? '))
    print(f'Sua compra vai ser parcelada em {a}x de R${(x / a):.2f} COM JUROS'
          f'\nSua compra de R${x:.2f} vai custar R${(x * 1.2):.2f} no final')
else:
    print('Opção de pagamento INVÁLIDA. Tente Novamente!')
