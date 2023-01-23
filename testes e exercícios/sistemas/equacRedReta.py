import math

pontA = list()
pontB = list()
pontN = list()

i = 0
m = n = 0

while True:
    # entrando nos dados pela primeira vez
    if i == 0:
        print('============-dados da reta-============')
        graus = input('coeficiente angular da reta (graus): ')
        pontA.append(input('valor x do primeiro ponto: '))
        pontA.append(input('valor y do primeiro ponto: '))
        pontB.append(input('valor x do segundo ponto: '))
        pontB.append(input('valor y do segundo ponto: '))
        n = input('valor do coeficiente linear (n): ')
        i += 1

    # menu
    print()
    print('-='*20)
    print(' '*15, 'MENU')
    print('1) Achar a equação reduzida da reta')
    print('2) Verificar se um ponto pertence a reta')
    print('3) Digitar novos dados')
    print('4) Verificar o ângulo entre duas retas')
    print('5) Sair')
    escolha = int(input('Digite o número da opção: '))

    if escolha == 1:
        # testando para ver se o usuário passou os dados necessários para processar os dados
        if (pontB[1] != '' and pontA[1] != '' and pontB[0] != '' and pontA[0]) or (graus != '' and n != ''):
            print()
            # verificando se podemos usar os pontos da reta para realizar a equação
            if pontB[1] != '' and pontA[1] != '' and pontB[0] != '' and pontA[0] != '':
                # usando o laço para percorrer os vetores e converte-los de str para int para fazer a equação
                for j in range(0, 2):
                    pontA[j] = int(pontA[j])
                    pontB[j] = int(pontB[j])

                m = (pontB[1] - pontA[1]) / (pontB[0] - pontA[0])
                n = pontA[0] - (m * pontA[1])
                n = int(n)
                m = int(m)
                print('-'*35)
                print(f'EQUAÇÃO REDUZIDA DA RETA: y = {m}x + ({n})')

            else:
                graus = int(graus)
                m = math.tan(math.radians(graus))
                print('-'*35)
                print(f'EQUAÇÃO REDUZIDA DA RETA: y = {m:.3f}x + ({n})')
            
            if m > 0:
                print('RETA SERÁ CRESCENTE')
            elif m < 0:
                print('RETA SERÁ DECRESCENTE')
            else: 
                print('RETA SERÁ CONSTANTE')
            print('-'*35)

        else:
            print('\n===falta dados para realizar essa equação===')

    if escolha == 2:
        if m == '' or n == '':
            print('\n===Você ainda não realizou a equação reduzida da Reta===')
        else:
            print(f'\nVerificando se algum ponto passa pela reta y = {m:.2f}x + ({n})')
            x, y = input('digite os pontos (x, y): ').split(' ')
            x = int(x)
            y = int(y)
            m = int(m)
            n = int(n)
            print()
            print('-'*35)
            if y == m*x+n:
                print(f'os pontos ({x}, {y}) passam pela reta: {y} = {m:.2f}x{x} + ({n})')
            else: 
                print(f'os pontos ({x}, {y}) não passam pela reta: {y} != {m:.2f}x{x} + ({n})')
            print('-'*35)
    if escolha == 3:
        i = 0
        pontA.clear()
        pontB.clear()

    if escolha == 4:
        if (pontB[0] != '' and pontA[0] != ''):
            pontA[0] = int(pontA[0])
            pontB[0] = int(pontB[0])    
        
            m = (pontB[0] - pontA[0]) / (1 + (pontB[0] * pontA[0])) 
            print(f'O ângulo entra as duas retas é: tg a = {m}')
        else:
            print('\n===falta dados para realizar essa equação===')

    if escolha == 5:
        break
