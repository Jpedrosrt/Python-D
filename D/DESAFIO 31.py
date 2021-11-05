x = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {x:.1f}Km.')
if x <= 200:
    print(f'E o preço da sua passagem será de R${x * 0.50:.2f}')
else:
    print(f'E o preço da sua passagem será de R${x * 0.45:.2f}')
