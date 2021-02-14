PrimeiroTermo = int(input('Digite o primeiro termo: '))
Razao = int(input('Digite a sua razão: '))
for c in range(0, 10):
    valor = PrimeiroTermo + (Razao * c)
    print('{}'.format(valor), end=' -> ')
print('ACABOU')
  