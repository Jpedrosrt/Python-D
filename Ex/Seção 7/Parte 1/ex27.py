val = list()

for a in range(10):
    val.append(int(input(f'Digite o {a + 1}° valor: ')))
   
for pos, b in enumerate(val):
    cont = False
    for n in range(2, b):
        if b % n == 0:
            cont = True
    if not cont and b != 1:
        print(f'O número {b} é primo e está na posição {pos}') 
