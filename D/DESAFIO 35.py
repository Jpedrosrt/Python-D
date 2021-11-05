print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
x = float(input('Primeiro segmento: '))
y = float(input('Segundo segmento: '))
z = float(input('Terceiro segmento: '))
if abs(z - y) < x < z + y and abs(z - x) < y < z + x and abs(y - x) < z < x + y:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
