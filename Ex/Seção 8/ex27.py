from math import factorial

def sen(n):
    s = 0
    for a in range(6):
        s += (((-1)**a) * (n ** (2*a + 1)))/ factorial(2*a + 1)
    return s

print(sen(10))