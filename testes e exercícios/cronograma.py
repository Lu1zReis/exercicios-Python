import datetime
tarefa = ('Química', '11/09', '', '14/10')
hoje = datetime.date.today()
hoje = str(hoje).split('-')
aux1 = aux2 = 0
for i in range(1, len(tarefa), 2):
    prazo = tarefa[i].split('/')
    prazo1 = int(prazo[1])
    dia1 = int(hoje[1])

    if dia1 == prazo1:
        aux1 = int(prazo[0])
        aux2 = int(hoje[2])
        print(f'Aula de quimica faltam {aux1} dias. Prazo {aux2}')

print(hoje[2], hoje)
