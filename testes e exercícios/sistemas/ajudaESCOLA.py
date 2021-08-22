from datetime import date

data =  date.today()
dia = data.weekday()

seg = ['Inst. Hidráulica', 'ed. Física']
ter = ['Q. C. C.', 'Geografia']
qua = ['Filosofia', 'Matemática', 'CAD']
qui = ['Orçamentos', 'Inst. Elétricas']
sex = ['Português']

materiasSemana = [qua[1], ter[1], qui[0]]
materiasMensais = [sex[0], seg[0], seg[1], qua[2], ter[0], qua[0]]
materiasTotais = [materiasMensais, materiasSemana]

tam0 = len(materiasSemana + materiasMensais)
tam1 = len(materiasMensais)
tam2 = len(materiasSemana)

while True:
    print(f'Aulas de hoje (seg) {seg}' if dia == 0 else 'Seg OK')
    print(f'Aulas de hoje (ter) {ter}' if dia == 1 else 'Ter OK')
    print(f'Aulas de hoje (qua) {qua}' if dia == 2 else 'Qua OK')
    print(f'Aulas de hoje (qui) {qui}' if dia == 3 else 'Qui OK')
    print(f'Aulas de hoje (sex) {sex}' if dia == 4 else 'Sex OK')
    print(f'Fim de semana (sab)' if dia == 5 else '')
    print(f'Fim de semana (dom)' if dia == 6 else '')
    print(f'''
          Data: {data}

    [1] Ver todas as matérias
    [2] Ver as matérias que tem que fazer semanais
    [3] Ver as matérias que não são semanais
    [4] Sair do programa

    ''')

    esc = 0
    while esc != 1 and esc != 2 and esc != 3 and esc != 4:
        esc = int(input('Escolha um valor (inteiro): '))
    
    if esc == 1:
        t = c = 0
        cont1 = len(materiasTotais[0])
        cont2 = len(materiasTotais[1])

        print('-' * 10, 'Exibindo todas as matérias', '-' * 10)
        while cont1 > t:
            print(materiasTotais[0][t])
            t += 1

        while cont2 > c:
            print(materiasTotais[1][c])
            c += 1
        print('-' * 30)

    elif esc == 2:
        print('-' * 10, 'Exibindo as matérias semanais', '-' * 10) 
        for c in range(0, tam2):
            print(materiasSemana[c])   
        print('-' * 30)

    elif esc == 3:
        print('-' * 10, 'Exibindo as matérias mensais', '-' * 10)
        for k in range(0, tam1):
            print(materiasMensais[k])
        print('-' * 30)
    
    elif esc == 4:
        print('Programa encerrado...')
        break
