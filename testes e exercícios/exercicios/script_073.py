times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Ceará', 'Santos', 'Atlético-GO', 'Bahia', 'Internacional', 'Corinthians', 'Fluminense', 'Juventude', 'Sport Recife', 'São Paulo', 'América-MG', 'Cuiabá', 'Grêmio', 'Chapecoense')

CincoPrimeiros = times[:5]
z4 = times[16:]
pos = times.index('Chapecoense')
print('-=' * 30)
print(f'A classificação do Brasileirão é: {times}')
print('-=' * 30)
print(f'Os cinco Primeiros são: {CincoPrimeiros}')
print('-=' * 30)
print(f'Os ultimos 4 colocados são: {z4}')
print('-=' * 30)
print(f'Os times em ordem são alfabética: {sorted(times)}')
print('-=' * 30)
print(f'A posição da chapecoense na tabela é a {pos+1}º colocação')
