x = int(input('Primeiro valor: '))
y = int(input('Segundo valor: '))
z = int(input('Terceiro valor: '))
if y < x < z or z < x < y:
    if y > z:
        print(f'O menor valor digitado foi {z}')
        print(f'O maior valor digitado foi {y}')
    else:
        print(f'O menor valor digitado foi {y}')
        print(f'O maior valor digitado foi {z}')
if x < y < z or z < y < x:
    if x > z:
        print(f'O menor valor digitado foi {z}')
        print(f'O maior valor digitado foi {x}')
    else:
        print(f'O menor valor digitado foi {x}')
        print(f'O maior valor digitado foi {z}')
if x < z < y or y < z < x:
    if x > y:
        print(f'O menor valor digitado foi {y}')
        print(f'O maior valor digitado foi {x}')
    else:
        print(f'O menor valor digitado foi {x}')
        print(f'O maior valor digitado foi {y}')
