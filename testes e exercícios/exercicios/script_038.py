Primeiro = int(input('Coloque o primeiro número: '))
Segundo = int(input('Coloque o segundo número: '))

if(Primeiro > Segundo):
    print('O primeiro número: {}, é maior que o segundo: {}.'.format(Primeiro, Segundo))
elif(Segundo > Primeiro):
    print('O segundo número: {}, é maior que o primeiro: {}.'.format(Segundo, Primeiro))
else:
    print('Os dois números são iguais')
