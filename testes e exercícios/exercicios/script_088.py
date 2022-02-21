import random
import time
sorteados = list()
numeros = list()
v = 0
print('=-'*3, 'JOGO DA MEGA SENA', '-='*3)
quant = int(input('\nQuantos jogos quer sortear? '))

print(f'\n<<<-----SORTEANDO {quant} JOGO(S)----->>>')

for i in range(0, quant):

    while len(numeros) < 6:
        while v in numeros:
            v = random.randint(1, 60)
        numeros.append(v)

    sorteados.append(sorted(numeros[:]))
    numeros.clear()

for pos, val in enumerate(sorteados):
    time.sleep(1.3)
    print(f'Jogo {pos+1}: {val}')
print('<=========> !BOA SORTE! <=========>')
