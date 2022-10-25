from time import sleep

def lin():
    print('-=' * 20)

def contador(i, f, p):
    # Permissão para contar de números negativos
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    # ‘Interface’ do sistema
    lin()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)


    # Permissão para contar números menores que o seu fim
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')

    # Permissão para contar números maiores que o seu fim
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicío: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)