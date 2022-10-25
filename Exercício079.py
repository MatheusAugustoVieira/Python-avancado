Números = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in Números:
        Números.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if cont in 'Nn':
        break
print('-=' * 30)
Números.sort()
print(f'Você digitou os valores {Números}')
