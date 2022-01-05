def n_primos(n):
    var = list()
    for a in range(1, n + 1):
        var.append(a)
    aux = var.copy()
    p = 2
    aux2 = list()
    while p * p < n:
        for a in var:
            x = p * a
            if a >= p and x < n and x not in aux2:
                aux.remove(x)
            aux2.append(x)
            if x > n:
                break

        for a in aux:
            if a > p:
                p = a
                break
    aux.remove(1)
    aux.remove(n)
    return aux
    


print(n_primos(100))