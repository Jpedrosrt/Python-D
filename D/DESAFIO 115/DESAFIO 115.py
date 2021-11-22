from lib.interface import menu
from lib.arquivos import *
from time import sleep

arq = 'pessoas.txt'

if not arqE(arq):
    carq(arq)

while True:
    r = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if r == 3:
        break
    elif r == 1:
        larq(arq)
    elif r == 2:
        n = str(input('Nome: ')).strip()
        i = int(input('Idade: '))
        cadarq(arq, n, i)
    sleep(1)
