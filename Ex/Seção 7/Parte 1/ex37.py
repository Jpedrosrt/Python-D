from random import randint

val = list()
aux = list()

while True:
    x = randint(1, 100)
    if x not in val:
        val.append(x)
    if len(val) == 11:
        break

aux = sorted(val[:6]).copy()
aux.extend(sorted(val[6::], reverse=True))

print(val)
print(aux)
