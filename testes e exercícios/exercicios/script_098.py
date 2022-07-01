# from time import sleep 

def contador(passos):
    print('')
    
    # primeiro algoritmo (0 até 10, de 1 em 1)
    for i in range(0, 11, 1):
        print(i, end=' ')
    print('\n')

    # segundo algoritmo (10 até 0, de 1 em 1)
    for j in range(10, -1, -1):
        print(j, end=' ')

    print('\n')

    # terceiro algoritmo (personalizado pelo usuário)
    inicio = passos[0]
    fim = passos[1]
    passo = passos[2]

    

contador(0)
