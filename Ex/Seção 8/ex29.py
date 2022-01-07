from math import factorial

def senh(n):
    s = 0
    for a in range(800):
        s += (n ** (2*a + 1))/ factorial(2*a + 1)
    return s

print(senh(10))