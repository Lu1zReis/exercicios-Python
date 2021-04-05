# exercicio 57
'''
c = ' '
while c != 'M' and c != 'F':
    c = str(input('Digite um valor F ou M: ')).upper()
print(c)    
'''

# exercicio 58
'''
import random
var = 1 
user = quant = 0
while user != var:
    user = int(input('Digite uma entrada: '))
    var = random.randint(0, 10)
    if user != var:
        quant += 1
        print('Tente novamente...')
    else:
        quant += 1

print('CERTA RESPOSTA: NÚMERO {}'.format(var))
print('Foram {} tentativa(s)'.format(quant))
'''
'''
# exercicio 59
escolhas = 4
aux = []
c = 0
while escolhas != 5:
    
    if escolhas == 4:
        aux.clear()
        for c in range(1, 3):
            contador = int(input('Digite a {} º entrada: '.format(c)))
            aux.append(contador)

    print('-=-=-MENU-=-=-')
    print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair\n')
    escolhas = int(input('Escolha um valor: '))

    if escolhas == 1:
        c = aux[0] + aux[1]
        print('A soma é igual a {}'.format(c))

    if escolhas == 2:
        c = aux[0] * aux[1]
        print('A multiplicação é igual a {}'.format(c))

    if escolhas == 3:
        if aux[0] > aux[1]:
            c = aux[0]
            print('O maior valor é {}'.format(c))
        elif aux[1] > aux[0]:
            c = aux[1]
            print('O maior valor é {}'.format(c))
        else:
            print('Os dois valores são iguais ({})'.format(aux[0]))

print('Finalizado')
'''

'''
# exercicio 60
x = int(input('Digite um valor: '))
y = x
a = 0
while y >= 1:
    y -= 1
    a = x * y
    print('{} x {} = {}'.format(x, y, a * y))
    x -= 1
'''
'''
# exercicio 61
n = 0
PrimeiroTermo = float(input('Digite o primeiro termo: '))
Razao = float(input('Digite a razão da PA: '))
while n < 10:
    valor = PrimeiroTermo + (Razao * n)
    print('{}'.format(valor), end=' -> ')
    n += 1
print('FIM')
'''

'''
# exercicio 62
Termo = float(input('\nDigite o primeiro termo: '))
Razao = float(input('Digite a razao: '))
c = Termo
x = 0
n = Termo + 10
while c < n:
    valor = Termo + (Razao * x)
    print('{}'.format(valor), end=' -> ')
    c += 1
    if c == n:
        n += float(input('\nValor 0 para encerrar ou diferente para continuar: '))
    x += 1
print('FIM')
'''

'''
# exercicio 63
from math import ceil

PrimeiroValor = float(input('Digite o primeiro valor: '))
Seq = float(input('Digite o ponto de parada: '))
valor = PrimeiroValor
n = 0
while n < Seq:
    print('{}'.format(ceil(valor)), end=' -> ')
    valor *= 1.630
    n += 1 

print('ACABOU')
'''
'''
# exercicio 64
c = x = quant = 0
while c != 999:
    c = int(input('Digite um valor: '))
    if c != 999:
        x += c
        quant += 1
print('Foram digitados {} número(s) e a soma entre eles foi de {}'.format(quant, x))
'''

# exercicio 65
media = menor = maior = quant = soma = x = 0
flag = 'SIM'
 
while flag != 'NAO' or flag != 'NÃO':
    # Entrada dos dados
    x = int(input('Digite um valor: '))

    # Lógica das contas
    quant += 1
    soma += x
    if quant == 1:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x

    # Ponto de parada 
    flag = str(input('Digite sim para colocar mais um valor e não para sair\n: ')).upper()
    if flag == 'NAO' or flag == 'NÃO':
        # Tirar a média no final
        media = soma / quant

# Exibir os dados
print('O maior valor foi: {}\nO menor valor foi: {}\nA média foi: {}'.format(maior, menor, media))
