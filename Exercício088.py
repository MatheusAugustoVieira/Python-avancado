from random import randint
from time import sleep
lista = list()
jogos = list()
quantidade = int(input("Quantos jogos você quer que eu sorteie? \n"))
total = 1

while total <= quantidade:
    counter = 0
    while True:
        number = randint(1, 60)
        if number not in lista:
            lista.append(number)
            counter += 1
        if counter >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, l in enumerate(jogos):
    print(f"jogo {i + 1}: {l}")
    sleep(1)
