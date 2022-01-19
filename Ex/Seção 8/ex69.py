def fra(a, b):
    if a[1] == 0 or b[1] == 0:
        return print('Indeterminável')
    
    a = mdc(a)
    b = mdc(b)

    print(f'Frações Simplificadas:\n{a[0]}/{a[1]}\n{b[0]}/{b[1]}')

    s = soma(a, b)

    print(f'Somando: {s}')

    sub = subtr(a, b)

    print(f'Subtraindo: {sub}')

    p = prod(a, b)

    print(f'Multiplicando: {p}')

    di = div(a,b)

    print(f'Dividindo: {di}')



def mdc(a):
    for i in range(2, max(a)):
        if a[0] % i == 0 and a[1] % i == 0:
            while a[0] % i == 0 and a[1] % i == 0:
                a = [a[0] // i, a[1] // i]
    return a

    return a, b



def soma(a, b):
    d = a[1] * b[1]
    n = (d // a[1]) * a[0] + (d // b[1]) * b[0] 
    return [n ,d]



def subtr(a, b):
    d = a[1] * b[1]
    n = (d // a[1]) * a[0] - (d // b[1]) * b[0] 
    return [n ,d]



def prod(a, b):
    return [a[0]* b[0], a[1] * b[1]]



def div(a, b):
    b = [b[1], b[0]]
    return prod(a, b)



fra([40320, 362880], [362880, 40320])