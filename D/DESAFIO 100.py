from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for b in range(0, 5):
        lista.append(randint(1, 10))
        sleep(0.4)
        print(lista[b], end=' ')
    print('Fim!')


def soma(lista):
    s = 0
    for b in lista:
        if b % 2 == 0:
            s += b
    print(f'Somando os valores pares de {lista}, temos {s}')


numeros = list()
sorteia(numeros)
soma(numeros)
