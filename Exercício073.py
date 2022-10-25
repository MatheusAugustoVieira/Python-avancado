times = ('Atlético GO', 'América MG', 'Atlético MG',
         'Atlético PR', 'Ceará', 'Chapecoense',
         'Flamengo', 'Cuiabá', 'Bahia', 'Juventude',
         'Fluminense', 'Fortaleza', 'Grêmio',
         'Bragantino', 'Santos', 'São Paulo',
         'Corinthians', 'Inter', 'Sport Recife',
         'Palmeiras')
print('-=' * 15)
'''for t in times:
    print(t)'''
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times [0:5]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')

