x = float(input('Qual a velocidade atual do carro? '))
if x <= 80:
    print('Tenha um bom dia! Diriga com segurança!')
else:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${(x-80)*7:.2f}!')
    print('Tenha um bom dia! Diriga com segurança!')
