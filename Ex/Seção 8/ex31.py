from math import factorial

def neperiano(n):
    s = 0
    for a in range(n):
        s += 1 / factorial(a)
    return s

print(neperiano(500))