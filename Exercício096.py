def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Program Principal
print('Controle de Terrenos')
print('_' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
