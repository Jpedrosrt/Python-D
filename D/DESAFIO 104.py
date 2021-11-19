def leiaint(num):
    while True:
        a = input(num).strip()
        if a.isnumeric():
            return a
        else:
            print('\033[31mERRO ! Digite um número inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
