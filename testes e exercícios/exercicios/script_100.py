from random import randint
from time import sleep

def sorteio(nums): # sortear 5 numeros
    print('Os valores sorteados foram:', end=' ')
    for v in range(0, 5):
        
        n = randint(0, 9)
        nums.append(n)
        print(f'{n}', end=' ', flush=True)  
        sleep(0.5)
  

def somaPar(nums): # somar os pares dos numeros sorteados
    soma = 0
    pares = []
    for val in nums:
        if val % 2 == 0:
            soma += val
            pares.append(val)
    print(f'\nA soma da lista entre os valores pares({pares}) é {soma}')


numeros = list()

sorteio(numeros)
somaPar(numeros)
