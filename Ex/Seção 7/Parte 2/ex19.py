from random import randint, uniform

var = list()

s = 0
ma = 0
for i in range(5):
    aux = list()
    m = int(input(f'Digite o número da matricula do {i + 1}° aluno: '))
    aux.append(m)
    mp = round(uniform(1, 10), 1)
    aux.append(mp)
    mt = round(uniform(1, 10), 1)
    aux.append(mt)
    nf = round((mp + mt), 1)
    aux.append(nf)
    var.append(aux)
    if nf > ma:
        ma = nf
        md = m
    s += nf

print(var)
print('-=-' * 20)
print(f'A maior nota foi {ma} do aluno com matricula {md}')
print('-=-' * 20)
print(f'A média das notas finais foi {s / len(var):.2f}')
print('-=-' * 20)
