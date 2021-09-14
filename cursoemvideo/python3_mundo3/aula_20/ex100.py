from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando...', end=' ')
    for c in range(0, 5):
        n = randint(0, 9)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'\nSomando os valores pares de {lista}, temos {soma}.')


numeros = []
sorteia(numeros)
somapar(numeros)
