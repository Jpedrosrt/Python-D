def leiaop(msg):
    try:
        i = int(input(msg))
    except(ValueError, TypeError):
        print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m')
    try:
        if i == 1:
            lin('PESSOAS CADASTRADAS')
            return i
        elif i == 2:
            lin('NOVO CADASTRO')
            return i
        elif i == 3:
            lin('Saindo do sistema...')
            return i
        elif i < 1 or i > 3:
            print('\033[0;31mERRO: por favor, digite uma opção válida.\033[m')
    except:
        return


def lin(msg, tam=40):
    print('=' * tam)
    print(f'{msg}'.center(tam))
    print('=' * tam)


def menu(ops):
    while True:
        lin('MENU PRINCIPAL', 40)
        b = 1
        for a in ops:
            print(f'\033[0;33m{b} -\033[0;34m {a}\033[m')
        print('=' * 40)
        while True:
            opc = leiaop('\033[0;33mSua opção: \033[m')
            if opc == 1 or opc == 2 or opc == 3:
                break
        return opc
