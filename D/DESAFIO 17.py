from math import sqrt as r, hypot as h
x = float(input('Comprimento do cateto oposto: '))
y = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {r(x**2 + y**2):.2f}')
print(f'A hipotenusa vai medir {(x**2 + y**2)**(1/2):.2f}')
print(f'A hipotenusa vai medir {h(x, y):.2f}')
