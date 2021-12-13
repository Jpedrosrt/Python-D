var = list()

for i in range(10):
    aux = list()
    for j in range(10):
        if i < j:
            aux.append(2 * i + 7 * j - 2)
        elif i == j:
            aux.append(3 * i ** 2 - 1)
        elif i > j:
            aux.append(4 * i ** 3 - 5 * j ** 2 + 1)
    var.append(aux)   
for a in var:
    print(a)