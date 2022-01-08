def troque(x, y):
    global a
    global b
    aux = x
    a = y
    b = aux


a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

troque(a, b)

print(f'A = {a}\nB = {b}')
