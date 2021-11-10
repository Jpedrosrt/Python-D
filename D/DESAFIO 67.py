while True:
    x = int(input('Quer ver a tabuada de qual número? '))
    if x < 0:
        break
    print('-' * 30)
    for a in range(1, 11):
        print(f'{x} x {a} = {x * a}', end='\n')
    print('-' * 30)
print('-' * 30)
print('PROGRAMA ENCERRADO')
print('-' * 30)
