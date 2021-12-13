var = list()

for i in range(5):
    aux = list()
    for j in range(5):
        if i == j:
            aux.append(1)
        else:
            aux.append(0)
    var.append(aux)

print(var)