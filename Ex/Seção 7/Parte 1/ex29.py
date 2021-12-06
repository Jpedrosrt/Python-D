from random import randint

val = list()
pares = list()
impares = list()

for a in range(6):
    val.append(randint(1, 100))

for a in val:
    if a % 2 == 0:
        pares.append(a)
    else: 
        impares.append(a)
    
print(f'Na lista {val}\nOs números pares são {pares} e a soma é {sum(pares)}\nOs números ímpares são {impares} o total de {len(impares)} elementos')