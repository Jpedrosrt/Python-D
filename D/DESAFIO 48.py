a = 0
s = 0
for c in range(3, 500, 3):
    if c % 2 != 0:
        a += 1
        s += c
print('A soma de todos os {} valores solicitados é {}'.format( a, s))
