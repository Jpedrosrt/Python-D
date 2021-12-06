from random import randint

A = set()
B = set()

while True:
    x = randint(1, 100)
    y = randint(1, 100)
    if x not in A:
        A.add(x)
    if y not in B:
        B.add(y)
    if len(A) == 10 and len(B) == 10:
        break
    
C = A.intersection(B)

if len(C) != 0:
    print(f'A intersecção entre {A} e {B} é {C}')
else:
    print(f'Não há intersecção entre {A} e {B}')