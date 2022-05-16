jogadores = list()
cont = 'S'
mostrar = 0 
while 'S' in cont:
    jogador = {'nome': '', 'partidas': 0, 'gols': list(), 'total': 0}

    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['partidas'] = int(input(f"Digite a quantidade de partidas de {jogador['nome']}: "))

    for i in range(0, jogador['partidas']):
        jogador['gols'].append(int(input(f"Quantos gols fez na partida {i+1}: ")))
        jogador['total'] += jogador['gols'][i]

    jogadores.append(jogador.copy())
    jogador.clear()
    cont = str(input('Deseja continuar?[S/N] ')).upper()

    print('-' * 20)

print('=-' * 20)
print(jogadores)
print('=-' * 20)

print('cod  nome      gols          total')
for i in range(0, len(jogadores)):
    print(f" {i:^2}{jogadores[i]['nome']:^8}    {jogadores[i]['gols']}{jogadores[i]['total']:>10}")
print('=-' * 20)

while mostrar != 999:
    mostrar = int(input('Mostrar os dados de qual jogador?(999 para) '))

    print(f"\nLEVANTAMENTO DO JOGADOR {jogadores[mostrar]['nome']}")
    quant = jogadores[mostrar]['partidas']

    for p in range(0, quant):
        print(f"no jogo {p} fez {jogadores[mostrar]['gols'][p]}")
