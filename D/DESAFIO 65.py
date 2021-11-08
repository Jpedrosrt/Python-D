a = ''
b = s = d = m = 0
while a != 'N':
    x = int(input('Digite um número: '))
    a = str(input('Quer continuar? [S/N] ')).upper().strip()
    b += 1
    s += x
    m = x
    if x > d:
        d = x
    if x < m:
        m = x
print(f'Você digitou {b} números e a média foi {s / b}\n'
      f'O maior valor foi {d} e o menor foi {m}')
