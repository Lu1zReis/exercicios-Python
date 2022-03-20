from random import randint as r
from time import sleep as s
jogador = {'j1': r(1, 6), 'j2': r(1, 6), 'j3': r(1, 6), 'j4': r(1, 6)}

print('Valores sorteados:')
s(1)
print(f"     Jogador 1 - {jogador['j1']}")
s(1)
print(f"     Jogador 2 - {jogador['j2']}")
s(1)
print(f"     Jogador 3 - {jogador['j3']}")
s(1)
print(f"     Jogador 4 - {jogador['j4']}")

for c, v in jogador.items():
    print(c, ' = ', v)

print('\nRanking dos jogadores:')
print(jogador)
