valorInicial = float(input('Digite aqui o valor inicial: '))
razao = float(input('Digite aqui o valor que sera constante: '))
x = 1
while x <= 10:
    print('{} º = {}'.format(x, valorInicial))
    valorInicial *= razao
    x += 1
