num = list()
pares = list()
ímpares = list()
while True: #Estrutura de repetição infinita
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer Continuar [S/N] '))
    if resp in 'Nn': #Parar a Estrutura de repetição
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
