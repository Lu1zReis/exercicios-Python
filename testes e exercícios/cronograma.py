import datetime

tarefa = ('História', '8/9/2', 'Física', '24/09/0')

# o primeiro valor é o prazo final da tarefa
# o valor do meio é o mês final da tarefa
# o último valor é a data que foi iniciada

hoje = datetime.date.today()
hoje = str(hoje).split('-')
aux1 = aux2 = dia1 = prazo1 = 0
aula = ''

# prazo[0] vai receber o dia da tarefa e prazo[1] vai receber o mês
# hoje[1] vai receber o mês e hoje[2] vai receber o dia atual

for i in range(0, len(tarefa)):

    if i % 2 == 0:
        aula = tarefa[i]

    if i % 2 == 1:
        prazo = tarefa[i].split('/')
        MesPrazo = int(prazo[1])
        MesAtual = int(hoje[1])

        diaFinal = int(prazo[0])
        diaAtual = int(hoje[2])
        diaInicial = int(prazo[2])

        quant = porcentagem = 0.0

        if MesAtual == MesPrazo:
            quant = diaFinal - diaAtual
            porcentagem = (diaAtual * 100) / diaFinal

        else:
            quant = (30 - diaAtual) + diaFinal
            porcentagem = (diaAtual * 100) / diaFinal

        print(f'Na matéria {aula} falta {quant} dias para o fim do prazo, e já se passaram {porcentagem:.2f}% de progresso até o dia final chegar.') 
