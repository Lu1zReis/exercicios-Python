jogador = {'nome': '', 'partidas': 0, 'gols': list(), 'total': 0}

jogador['nome'] = str(input('Qual o nome do jogador? '))
jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for i in range(0, jogador['partidas']):
    
    jogador['gols'].append(int(input(f"Quantos gols {jogador['nome']} fez na {i+1}ª partida? ")))
    jogador['total'] += jogador['gols'][i]

print('-=' * 25)
print(jogador)
print('-=' * 25)

for c, v in jogador.items():
    if c != 'partidas':
        print(f'O campo {c} tem o valor {v}.')
print('-=' * 25)

print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")

for c in range(0, jogador['partidas']):
    print(f"   =>Na partida {c}, fez {jogador['gols'][c]}.")
print(f"foi um total de {jogador['total']}")