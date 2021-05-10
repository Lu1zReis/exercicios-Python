# Podemos importar um fatorial com um from math import factorial
valor = int(input('Digite um fatorial: '))
dividir = int(input('Digite a divisão: '))
dividir2 = int(input('Digite a segunda divisão: '))
geral = 0
# Primeira parte
cont = valor
fat = 1

print('{}! = '.format(valor), end='')
while(cont > 0):
    if cont > 1:
        print('{}'.format(cont), end=' x ')
    else:
        print('{}'.format(cont), end=' = ')
    fat *= cont
    cont -= 1

# Segunda parte
cont2 = dividir
fat2 = 1

print('{}! = '.format(dividir), end='')
while(cont2 > 0):
    if cont2 > 1:
        print('{}'.format(cont2), end=' x ')
    else:
        print('{}'.format(cont2), end=' = ')
    fat2 *= cont2
    cont2 -= 1

# terceira parte
cont3 = dividir2
fat3 = 1

print('{}! = '.format(dividir2), end='')
while(cont3 > 0):
    if cont3 > 1:
        print('{}'.format(cont3), end=' x ')
    else:
        print('{}'.format(cont3), end=' = ')
    fat3 *= cont3
    cont3 -= 1

geral = fat / (fat2 * fat3)

print('{}'.format(geral))
