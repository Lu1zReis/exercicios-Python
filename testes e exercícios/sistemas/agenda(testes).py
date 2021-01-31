lista_ativi = ['Correr', 'viajar', 'brincar']
Longo_Prazo = []
n = 0
while True:
    n = int(input('Qual desses vão na lista de longo prazo? {}'.format(lista_ativi)))
    Longo_Prazo.append(lista_ativi[n])
    print(Longo_Prazo)
    op = int(input('Deseja sair: 1 - [S] || 2 - [N]\n: '))
    if op == 1:
        break
