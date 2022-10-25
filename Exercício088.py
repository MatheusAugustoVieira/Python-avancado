from random import randint
from time import sleep
import mysql.connector

lista = list()
jogos = list()

# Interface do conector do phpMyAdmin
print('{:=^40}'.format('\033[1;31mLOGIN phpMyAdmin\033[m'))
host = input("\033[7;30;41mDigite o host que você deseja conectar! >>> \033[m")
user = input("\033[7;30;44mDigite o seu login! >>> \033[m")
passwd = input("\033[7;30;41mDigite a sua senha! >>> \033[m")
database = input("\033[7;30;44mQual a base de dados que você deseja acessar? >>> \033[m")

# Declaração antes do while
host = "167.99.252.245"
user = "BES_E5"
passwd = "unscaraae"
database = "BES_E5"

# O conector é a função que conecta o usuário na base de dados com base nas informações previamente levantadas
conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

# O cursor é a função que irá coletar os comandos a serem passados para a base de dados.
cursor = conector.cursor()

# Interface do jogo
print('\033[1;31m_\033[m' * 30)
print('      \033[1;34mJOGA NA MEGA SENA\033[m     ')
print('\033[1;31m_\033[m' * 30)
nome = str(input("Digite seu nome: "))
quant = int(input(f'\033[7;34;31mQuantos jogos você quer que eu sorteie {nome}?\033[m'))

tot = 1
var = 0
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('\033[1;31m-=\033[m' * 5, '\033[1;34m<BOA SORTE>\033[m', '\033[1;31m-=\033[m' * 5)
