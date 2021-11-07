from time import sleep
x = int(input('Primeiro valor: '))
y = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('      [ 1 ] Somar\n'
          '      [ 2 ] Multiplicar\n'
          '      [ 3 ] Maior\n'
          '      [ 4 ] Novos valores\n'
          '      [ 5 ] Sair do programa')
    op = int(input('>>>>> Qual é a sua opção? '))
    if op == 1:
        print(f'A soma entre {x} e {y} é {x + y}\n'
              f'===-===-===-===-===-===-===-===')
    elif op == 2:
        print(f'A multiplicação entre {x} e {y} é {x * y}\n'
              f'===-===-===-===-===-===-===-===')
    elif op == 3:
        if x > y:
            print(f'Entre {x} e {y} o maior valor é {x}\n'
                  f'===-===-===-===-===-===-===-===')
        elif x == y:
            print(f'{x} e {y} tem o mesmo valor\n'
                  f'===-===-===-===-===-===-===-===')
        else:
            print(f'Entre {x} e {y} o maior valor é {y}\n'
                  f'===-===-===-===-===-===-===-===')
    elif op == 4:
        x = int(input('Primeiro valor: '))
        y = int(input('Segundo valor: '))
        print('===-===-===-===-===-===-===-===')
    elif op < 1 or op > 5:
        print('Opção inválida. Tente novamente\n'
              '===-===-===-===-===-===-===-===')
print('Finalizando...')
sleep(2)
print('===-===-===-===-===-===-===-===\n'
      'Fim do programa! Volte sempre!')
