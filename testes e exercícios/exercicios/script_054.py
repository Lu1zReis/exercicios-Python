from datetime import date

# variaveis do código geral
data = date.today().year
anos = []
maiorIdade = []
menorIdade = []

for c in range(0, 7):
    # entrada de valores
    ano = int(input('Digite o {}º valor: '.format(c+1)))

    # colocando esses valores nas listas
    if data - ano >= 21:
        maiorIdade.append(ano)
    else:
        menorIdade.append(ano)
    anos.append(ano)

# vendo o tamanho delas para usar depois 
SizeIdades = len(anos)
SizeMaior = len(maiorIdade)
SizeMenor = len(menorIdade)

# exibindo os dados
print('São {} - {} valores'.format(anos, SizeIdades))
print('Maior idade: {} - {} valor(es)'.format(maiorIdade, SizeMaior))
print('Menor idade: {} - {} valor(es)'.format(menorIdade, SizeMenor))
