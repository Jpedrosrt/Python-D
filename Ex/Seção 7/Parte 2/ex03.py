var = list()

for i in range(4):
    aux = list()
    for j in range(4):
        aux.append((i + 1)*(j + 1))
    var.append(aux)

print(var)