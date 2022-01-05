def soma_al(n):
    if n <= 0:
        return 'Número inválido'
    x = ' '.join(str(n)).split()
    s = 0
    for a in x:
        s += int(a)
    return s

print(soma_al(123))