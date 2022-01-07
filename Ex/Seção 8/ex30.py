from math import factorial

def cosh(n):
    s = 0
    for a in range(800):
        s += (n ** (2*a))/ factorial(2*a)
    return s

print(cosh(10))