x = int(input('Digite um valor: '))
tot = 0
lista = []
for c in range(1, x+1):
    if x % c == 0:
        print('\033[34m', end=' ')
        tot += 1
        lista.append(c) # para pegar os valores e armazená-los em uma lista
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vez(es)\nOs valores são {}'.format(x, tot, lista))
# \033[m quebra a cor