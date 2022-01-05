def triangulo(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return 'Valores inválidos'
    elif a < b + c and b < a + c and c < a + b:
        print('Os valores podem formar um triangulo ', end='')
    else:
        return 'Os valores não podem formar um triangulo'
    if a == b == c:
        return 'Equilátero'
    elif a == b != c or a == c != b or c == b != a:
        return 'Isósceles'
    return 'Escaleno'

print(triangulo(5, 2, 3))
print(triangulo(5, 4, 3))
print(triangulo(5, 5, 5))
print(triangulo(5, 5, 8))
