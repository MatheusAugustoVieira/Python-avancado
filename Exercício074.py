from random import randint
número = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in número:
    print(f' {n} ', end='')
print(f'\nO maior valor sorteado foi {max(número)}')
print(f'O menor valor sorteado foi {min(número)}')
