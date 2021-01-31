lado1, lado2, lado3 = input().split(" ")
lado1 = float(lado1)
lado2 = float(lado2)
lado3 = float(lado3)

if lado1 > lado2 and lado1 > lado3:
    maior_lado = lado1
    soma_Lados = lado2 + lado3

if lado2 > lado1 and lado2 > lado3:
    maior_lado = lado2
    soma_Lados = lado1 + lado3

if lado3 > lado1 and lado3 > lado2:
    maior_lado = lado3
    soma_Lados = lado1 + lado2

if soma_Lados > maior_lado:
    lados_finais = soma_Lados + maior_lado
    print('Perimetro = {:.1f}'.format(lados_finais))

else:
    lados_finais = lado1 + lado2
    print('Area = {:.1f}'.format(lados_finais))
