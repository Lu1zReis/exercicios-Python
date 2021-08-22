import math

while True:
    # Primeira parte
    vazao = []
    contVaz = 0
    while True:
        val = float(input('Digite um valor de vazao: '))
        vazao.append(val)
        digi = str(input('Deseja parar de adicionar a vazao? ')).upper()
        contVaz += 1
        if 'S' in digi:
            break

    # quantidade de valores de vazões
    quant = len(vazao)

    f1 = []
    f2 = 0.0
    form = []
    for c in range(0, contVaz):
        f1.append(4*(vazao[c]*(10**-3)))
        f2 = 3*math.pi
        form.append(math.sqrt(f1[c] / f2))
    print('Determinação do (dm): ', form, '\n')
    

    # Segunda parte
    f1_2 = []
    f2_2 = 0.0
    form2 = []
    diametro = float(input('Digite o diametro usado: '))
    for i in range(0, contVaz):
        f1_2.append(4*(vazao[i]*(10**-3)))
        f2_2 = (diametro**2)*math.pi
        form2.append(f1_2[i] / f2_2)
    print('Identificação da velocidade: ', form2, '\n')

    # Terceira parte
    print('Calcular a perda de cargas')
    j = []
    cont = 0
    for h in range(0, contVaz):
        j.append(8.69*(10**6)*(vazao[h]**1.75)*((diametro*1000)**-4.75))

    for k in range(0, contVaz):
        print(f'Valores: {k}º valor: {j[k]}')

    sair = str(input('\nDeseja sair? ')).split()[0].lower()
    if 's' in sair:
        break

