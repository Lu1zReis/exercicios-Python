# Podemos importar um fatorial com um from math import factorial
valor = int(input('Digite um fatorial: '))
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
print('{}'.format(fat))
