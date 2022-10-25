def escreva(msg):
    tam = len(msg) + 4
    print('\033[1;34m~\033[m' * tam)
    print(f'  \033[1;31m{msg}\033[m')
    print('\033[1;34m~\033[m' * tam)


# Programa Principal
escreva('Matheus Augusto')
escreva('Curso de Python no youTube')
escreva('CeV')
