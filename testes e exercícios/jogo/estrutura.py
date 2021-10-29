import random
posicoes = []
jogador = []
n = 0
pos = 1
caçador = investigador = ''

for i in range(0, 4):
    posicoes.append(random.randint(1,5))

for j in range(0, 4):
    for k in range(0, 4):
        if j != k:
            while posicoes[k] == posicoes[j]:
                posicoes[j] = random.randint(1,5)

jogadores = ('Pedrinho', posicoes[0], 'Nai', posicoes[1], 'Luiz', posicoes[2], 'Fael', posicoes[3])

for nome in range(0, 8, 2):
    jogador.append(jogadores[nome])
    while n < 1:
        print(f'{jogadores[nome]}:{jogadores[pos]}')
        n += 1
        pos += 2
    n = 0

while caçador == investigador:
    caçador = random.choice(jogador)
    investigador = random.choice(jogador)
print(f'Caçador: {caçador}\ninvestigador: {investigador}')
