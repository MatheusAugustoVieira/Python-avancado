from random import randint
from time import sleep

# Função para sortear valores em uma lista
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')

# Função para somar valores pares em uma lista
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista},temos {soma}')


# Programa principal
números = list()
sorteia(números)
somaPar(números)
