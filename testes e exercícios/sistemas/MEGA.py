import random
import time

def sorteio(sorte):
    num = random.randint(1, 60)
    sorte.append(num)
    time.sleep(2)
    print(num)
    for i in range(0, 5):
        while num in sorte:
            num = random.randint(1, 60)
        sorte.append(num)
        time.sleep(2)
        print(num)

    sorte.sort()

def numeros():
    for i in range(1, 61):
        print(i, end=' ')
        if(i%10) == 0:
            print()

def simulador():
    qntApostas  = int(input('Quantas apostas fizeram? '))
    total = list()
    vals = list()
    acerto = 0
    acertos = list()
    for i in range(0, qntApostas):
        cartela = input(f'{i+1}o jogo: ').split(' ')
        total.append(cartela)

    print('Começando a simulação...')
    sorteio(vals)
    print(f'Valores sorteados: {vals}')
    print('Lista das cartelas que chegaram mais perto: ')
    
    for i in range(0, qntApostas):
        acerto = 0
        for c in range(0, 5):
            for j in range(0, 5):
                k = int(total[i][j])
                if k == vals[c]:
                    acerto += 1
        acertos.append(acerto)

    print(acertos)

    for l in range(0, qntApostas):
        menor = l
        for c in range(l, qntApostas):
            if acertos[c] < acertos[menor]:
                menor = c
                print(menor)
        print(menor)
        print(f'{l+1}o lugar: {total[menor]}')


sorteados = list()

while True:
    print('-=-=-=-=-Bem vindo a máquina da sorte-=-=-=-=-')
    print('1) Sortear números')
    print('2) Visualizar valores de 1 à 60')
    print('3) Verificar as chances')
    print('4) Simular sorteio')
    print('5) Sair')

    x = int(input('Escolha um valor: '))

    if x == 1:
        print('-='*30)
        print('Sorteando os valores de 1 à 60')
        sorteio(sorteados)
        print(sorteados)

    if x == 2:
        print('-='*30)
        print('mostrando os valores de 1 à 60')
        numeros()

    if x == 3:
        print('-='*30)
        print('Mostrando chances de ganhar na Mega da Virada 2022') 
        time.sleep(2)       
        print('A população brasileira está estimada em: 214.018.345')
        time.sleep(2)
        print('Então supondo que se - pelo menos - cada pessoa fizer 2 apostas, será: 214.018.345 x 2')
        time.sleep(4)
        print(f'Isso dá {214018345*2} milhões de apostas (ao total)')
        time.sleep(4)
        print(f'Sendo assim, isso seria 1/{214018345*2} milhões. As chances são mais ou menos de {1/(214018345*2)} %')
        time.sleep(5)
        n = int(input('Porém, podemos aumentar as chances com mais apostas, quantas apostas fizeram? '))
        print(f'As chances agora então são mais ou menos de {n/(214018345*2)} %')

    if x == 4:
        simulador()
    if x == 5:
        break
