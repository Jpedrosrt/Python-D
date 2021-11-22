def leiaint(i):
    while True:
        try:
            i = int(input('Digite um inteiro: '))
        except(ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return i


def leiafloat(r):
    while True:
        try:
            r = float(input('Digite um Real: '))
        except(ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return r


print(f'O valor inteiro digitado foi {leiaint("Digite um Inteiro: ")} e o real foi {leiafloat("Digite um Real: ")}')
