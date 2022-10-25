valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('\033[1;31m-=\033[m' * 30)
print(f'Você digitou {len(valores)} elementos. ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O número 5 foi encontrado na lista na posição {valores.index(5) +1}!')
else:
    print(f'O número 5 não foi encontrado na lista!')
