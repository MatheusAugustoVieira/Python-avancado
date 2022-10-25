def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


# Programa Principal
n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')