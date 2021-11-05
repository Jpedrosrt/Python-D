x = float(input('Qual é o salário do funcionário? R$'))
if x <= 1250:
    print(f'Quem ganhava R${x:.2f} passa a ganhar R${(x*1.15):.2f} agora.')
else:
    print(f'Quem ganhava R${x:.2f} passa a ganhar R${(x*1.10):.2f} agora.')
