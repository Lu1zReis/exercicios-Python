print('GERADOR DE PA')
print('-=' * 10)

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da sequência: '))

cont = 1

while(cont <= 10):
    print('{}'.format(a1), end=' -> ')
    a1 += r
    cont += 1

print('FIM', end='')
