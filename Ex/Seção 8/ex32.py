def simplifica(n, d):
    x = 1
    aux1 = n
    aux2 = d
    if n > d:
        for a in range(2, n):
            while aux1 % a == 0 and aux2 % a == 0:
                if aux1 % a == 0 and aux2 % a == 0:
                    aux1 /= a
                    aux2 /= a
                    x *= a
        return f'A fração ({n}/{d}) simplificada é:\nNumerador: {n / x}\nDenominador: {d / x}'
    elif d > n:
        for a in range(2, d):
            while aux1 % a == 0 and aux2 % a == 0:
                if aux1 % a == 0 and aux2 % a == 0:
                    aux1 /= a
                    aux2 /= a
                    x *= a
        return f'A fração ({n}/{d}) simplificada é:\nNumerador: {n / x}\nDenominador: {d / x}'
    return 1

print(simplifica(120, 48))