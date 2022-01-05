def oparacao(a, b, s):
    if s == '+':
        return a + b
    elif s == '-':
        return a - b
    elif s == '/':
        return a / b
    elif s == '*':
        return a * b
    return 'Parâmetro inválido'

print(oparacao(5,3, '+'))
print(oparacao(5,3, '-'))
print(oparacao(5,3, '/'))
print(oparacao(5,3, '*'))
print(oparacao(5,3, '~'))