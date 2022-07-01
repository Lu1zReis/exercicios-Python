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

print('cod   nome         gols           total')
for i in range(0, len(jogadores)):
    print(f" {i:>2} {jogadores[i]['nome']:^8}    {str(jogadores[i]['gols']):^10}", end='')
    print(f"{jogadores[i]['total']:>10}")
print('=-' * 20)

while True:
    mostrar = int(input('Mostrar os dados de qual jogador?(999 para) '))
    if mostrar == 999:
        break
    else:
        while True:
            if mostrar >= len(jogadores) or mostrar < 0:
                mostrar = int(input('Digite um jogador existente!(999 para) '))
                if mostrar == 999:
                    break
            else:
                break
    if mostrar != 999:    
        print(f"\nLEVANTAMENTO DO JOGADOR {jogadores[mostrar]['nome']}")
        quant = jogadores[mostrar]['partidas']

        for p in range(0, quant):
            print(f"no jogo {p} fez {jogadores[mostrar]['gols'][p]}")
    else:
        break
