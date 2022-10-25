# Declarar uma lista
ficha = list()

# Declarando as variáveis que tera na lista em um looping infinito
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    # Adicionando as variáveis na lista
    ficha.append([nome, [nota1, nota2], media])

    # Adicionando limitador ao looping infinito
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)

# Adicionando a estrutura do boletim
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')  # Número com 4 caracteres alinhado a esquerda
print('-' * 26)

# Mostrar os dados da ficha
for i, a in enumerate(ficha):  # Para cada índice e a aluno enumerar a ficha
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

# Mostrar notas individuais de cada aluno em um looping infinito
while True:
    print('-' * 35)

    # Adicionando limitador ao looping infinito
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break

    # Mostrar o número do aluno cadastrados
    if opc <= len(ficha) - 1:

        # Mostrar as notas de [0] Nome e [1] notas
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
