import datetime

# calculo em data para chegar o dia
dataAtual = {'dia': datetime.date.today().day, 'mes': datetime.date.today().month}
dataFinal = {'dia': 18, 'mes': 8}
tempo = dict()
dia = dataAtual['dia']
mesSub = 0

if dia >= 18:
    if dataAtual['dia'] != dataFinal['dia']:
        mesSub = 1

if dataAtual['dia'] >= dataFinal['dia']:
    
    if dataFinal['dia'] != dataAtual['dia']:
        tempo['dia'] = dataFinal['dia'] - (dataAtual['dia'] - (dataFinal['dia'] + 12))
    else:
        tempo['dia'] = 0
    tempo['mes'] = (dataFinal['mes'] - dataAtual['mes']) - mesSub

else:
    tempo['dia'] = dataFinal['dia'] - dataAtual['dia']
    tempo['mes'] = dataFinal['mes'] - dataAtual['mes']

# porcentagem para a contagem
diasAtual = (30 * tempo['mes']) + tempo['dia']
diasTotal = (30 * 6) + 18 # já feito a contagem desde o dia que comecei a trabalhar
porcent = 100 - ((diasAtual * 100) / diasTotal)
diferen = (diasTotal - diasAtual)

print(f"TOTAL: {diasTotal} <==== {porcent:.2f}% ====> DIA ATUAL: {diferen}")
print(f"\n       faltam {tempo['mes']} meses e {tempo['dia']} dia(s).")
