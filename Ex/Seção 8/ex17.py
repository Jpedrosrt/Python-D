def soma_entre(a, b):
    if a <= 0 or b <= 0:
        return 'Valores inválidos'
    s = 0
    if a > b:
        while a >= b:
            s += a 
            a -= 1
        return s
    else:
        while b >= a:
            s += b
            b -= 1
        return s

print(soma_entre(10, 5))
print(soma_entre(5, 10))
print(soma_entre(5, 5))