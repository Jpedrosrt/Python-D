def fator_primo(a):
    cont = 2
    m = x = 0
    aux = a
    while True:
        if aux % cont == 0:
            x = cont
            aux /= cont
        else:
            cont += 1
        if x > m:
            m = x
        if cont == a or aux == 1:
            return m
        

print(fator_primo(64))
print(fator_primo(2205))
print(fator_primo(25645))
