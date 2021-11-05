x = float(input('Qual é o seu peso? (Kg) '))
y = float(input('Qual é a sua altura? (m) '))
z = x / (y**2)
print(f'O IMC dessa pessoa é de {z:.1f}')
if z < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= z < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= z < 30:
    print('Você está em SOBREPESO')
elif 30 <= z < 40:
    print('Você está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
