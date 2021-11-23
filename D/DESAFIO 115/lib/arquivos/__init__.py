def arqE(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def carq(nom):
    try:
        a = open(nom, 'wt+')
        a.close()
    except:
        print('\033[0;31mHouve um erro na criação do arquivo\033[0;31m')
    else:
        print(f'\033[0;33mArquivo {nom} criado com sucesso.\033[m')


def larq(nome):
    d = dict()
    n = list()
    i = list()
    try:
        a = open(nome, 'rt')
    except:
        print('\033[0;31mHouve um erro na leitura do arquivo\033[0;31m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

def cadarq(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[0;31mHouve um erro na abertura do arquivo\033[0;31m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[0;31mHouve um erro no cadastro\033[0;31m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
