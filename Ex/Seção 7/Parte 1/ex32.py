from random import randint

X = set()
Y = set()

while True:
    x = randint(1, 100)
    y = randint(1, 100)
    if x not in X:
        X.add(x)
    if y not in Y:
        Y.add(y)
    if len(X) == 10 and len(Y) == 10:
        break

aux1 = list(X)
aux2 = list(Y)
s = 0
for a in range(10):
    s += aux1[a] + aux2[a]

p = 1
for a in range(10):
    p += aux1[a] * aux2[a]

d = X.difference(Y)
i = X.intersection(Y)
if len(i) == 0:
    i = 0
u = X.union(Y)

print(f'A soma: {s}\nO produto: {p}\nA diferença: {d}\nA intersecção: {i}\nA união: {u}')