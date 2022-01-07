from math import factorial

def cos(n):
    n = n * (3.141593/180)
    s = 0
    for a in range(6):
        s += (((-1)**a) * (n ** (2*a)))/ factorial(2*a)
    return s

print(cos(10))