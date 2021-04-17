import time
a = b = x = maior = 0
c = 4
sair = False
while not sair:
    if c == 4:
        a = int(input('Digite o primeiro valor: '))
        b = int(input('Digite o segundo valor: '))
        c = 0
    else:
        print('-=-=-=-= DIGITE O QUE PRETENDE FAZER -=-=-=-=')
        print('[ 1 ] - somar\n[ 2 ] - multiplicar\n[ 3 ] - maior\n[ 4 ] - novos números')
        print('[ 5 ] - sair')

        x = int(input('\nEscolha um valor: '))

        if x == 1:
            print('\nA soma entre {} e {} é {}\n'.format(a, b, a+b))

        elif x == 2:
            print('\nA multiplicação entre {} e {} é {}\n'.format(a, b, a*b))

        elif x == 3:
            if a > b:
                maior = a
            elif b > a:
                maior = b
            
            print('\nEntre {} e {} o maior número é {}\n'.format(a, b, maior))
        
        elif x == 4:
            c = 4

        elif x == 5:
            sair = True
            print('\nFinalizando programa...')
            time.sleep(2)
        
        else:
            print('\nPor favor, escolhe um número válido\n')

print('Programa finalizado com sucesso!')
