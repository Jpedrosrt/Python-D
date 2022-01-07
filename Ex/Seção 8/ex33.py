from math import factorial

def soma_algo_fato(n):
    n = ' '.join(str(factorial(n))).split()
    s = 0
    for a in n:
        s += int(a)
    return s

print(soma_algo_fato(5))