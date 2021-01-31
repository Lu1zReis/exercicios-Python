print('PROGRAMA DE AGENDAR COMPROMISSOS')
# Variaveis Globais
testando = 0
k = 0
lista_ativi = []
Longo_Prazo = []
Curto_Prazo = []
atividade_import = []
atividade_MenosImp = []
# Loop's do menu
while True:
    print('O que deseja fazer: ')
    print('1 - Adicionar um novo item\n2 - Exibir os itens existentes\n3 - Separar os itens\n4 - Sair')
    escolha = int(input(': '))
    # escolha do menu: 
    if escolha == 1:
        adicionar_novosCompro = (input('Qual atividade você deseja adicionar? '))
        testando = len(adicionar_novosCompro)
        if testando > 0:
            lista_ativi.append(adicionar_novosCompro)
            print('---------\nAdicionado :), {}'.format(adicionar_novosCompro))
    elif escolha == 2:
        if testando > 0:
            print('Essa é a lista de atividade:\n', lista_ativi)
            if k > 0:
                print('Essa é a lista de atividade de longo prazo:\n', Longo_Prazo)
                print('Essa é a lista de atividade de curto prazo:\n', Curto_Prazo)
                print('Essa é a lista de atividade de relevancia mais importante:\n', atividade_import)
                print('Essa é a lista de atividade de relevancia menos importante:\n', atividade_MenosImp)
        else:
            print('desculpe, você não adicionou nada ainda')
    elif escolha == 3:
        k = 1
        if testando > 0:
            # Separar e dividir melhor a lista de atividade
            aux = len(lista_ativi)
            print('Aqui está sua lista: {}'.format(lista_ativi))
            print('Há nessa lista: {} item(s)'.format(aux))
            i = int(input('Deseja remover algo? 1 - [S] || 2 - [N]: '))
            if i == 1:
                remover = int(input('Qual item da lista você deseja remover: '))
                lista_ativi.pop(remover)
                print('Nova lista {}'.format(lista_ativi))

            n = 0
            while True: # Lista de longo prazo
                n = int(input('Qual desses vão na lista de longo prazo? '))
                Longo_Prazo.append(lista_ativi[n])
                op = int(input('Deseja sair: 1 - [S] || 2 - [N]\n: '))
                if op == 1:
                    break

            j = 0
            while True: # Lista de curto Prazo
                j = int(input('Qual desses vão na lista de curto prazo? '))
                Curto_Prazo.append(lista_ativi[j])
                op = int(input('Deseja sair: 1 - [S] || 2 - [N]\n: '))
                if op == 1:
                    break

            h = 0
            while True: # Lista de atividade importante
                h = int(input('Qual dessas atividades é mais importante? '))
                atividade_import.append(lista_ativi[h])
                op = int(input('Deseja sair: 1 - [S] || 2 - [N]\n: '))
                if op == 1:
                    break

            f = 0
            while True:
                f = int(input('Qual dessas atividades é menos importante? '))
                atividade_MenosImp.append(lista_ativi[f])
                op = int(input('Deseja sair: 1 - [S] || 2 - [N]\n: '))
                if op == 1:
                    break

        else:
            print('Você não adiconou nada ainda...')

    else:
        quit() # Sair do programa, que poderiamos usar um break para sair do loop
