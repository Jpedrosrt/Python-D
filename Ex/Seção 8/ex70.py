def reduz(a, b):
    return [a , b]



def neg(a):
    return [-a[0], a[1]]



def soma(a, b):
    d = a[1] * b[1]
    n = (d // a[1]) * a[0] + (d // b[1]) * b[0] 
    return [n ,d]



def div(a, b):
    b = [b[1], b[0]]
    return [a[0]* b[0], a[1] * b[1]]


x = reduz(1, 5)

print(x)

y = reduz(1, 4)

n = neg(x)

print(n)

s = soma(x, y)

print(s)

d = div(x, y)

print(d)