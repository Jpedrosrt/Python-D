a = x = s = 0
while x != 999:
    x = int(input('Digite um número [999 para parar]: '))
    if x != 999:
        s = s + x
    a += 1
print(f'Você digitou {a - 1} números e a soma entre eles foi {s}.')