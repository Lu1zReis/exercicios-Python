def area(lar, com):
    area = lar * com
    print('=-' * 20)
    print(f'A área de {lar} x {com} é igual a {area:.2f} m²')

larg = float(input('Digite a largura: '))
comp = float(input('Digite o comprimento: '))

area(larg, comp)
