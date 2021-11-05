x = float(input('Primeiro segmento: '))
y = float(input('Segundo segmento: '))
z = float(input('Terceiro segmento: '))
if abs(z - y) < x < z + y and abs(z - x) < y < z + x and abs(x - y) < z < x + y:
    if x == y == z:
        print('Os segmentos PODEM FORMAR um triângulo EQUILÁTERO!')
    elif x == y or y == z or x == z:
        print('Os segmentos PODEM FORMAR um triângulo ISÓSCELES!')
    else:
        print('Os segmentos PODEM FORMAR um triãngulo ESCALENO!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')
