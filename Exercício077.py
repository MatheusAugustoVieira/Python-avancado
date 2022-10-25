palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMAR',
            'FUTURO')
for p in palavras:
    print(f'\nNa palavra \033[1;31m{p}\033[m temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')