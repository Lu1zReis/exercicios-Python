from math import pow
# Entrada de dados
Lado1, Lado2, Lado3 = input().split(" ") # pega 3 valores na mesma linha e atribui a variáveis

# Converte o valor para os tipos necessários 
Lado1 = float(Lado1)
Lado2 = float(Lado2)
Lado3 = float(Lado3)
ladosIguais = 0

# Ordenar
if Lado1 > Lado2 and Lado1 > Lado3:
    Lado_a = Lado1
    if Lado2 > Lado3:
        Lado_b = Lado2
        Lado_c = Lado3
    else:
        Lado_b = Lado3
        Lado_c = Lado2

if Lado2 > Lado1 and Lado2 > Lado3:
    Lado_a = Lado2
    if Lado1 > Lado3:
        Lado_b = Lado1
        Lado_c = Lado3
    else:
        Lado_b = Lado3
        Lado_c = Lado1

if Lado3 > Lado1 and Lado3 > Lado2:
    Lado_a = Lado3
    if Lado1 > Lado2:
        Lado_b = Lado1
        Lado_c = Lado2
    else:
        Lado_b = Lado2
        Lado_c = Lado1

if Lado1 == Lado2 != Lado3:
    ladosIguais = 1
    if Lado3 > Lado1 and Lado3 > Lado2:
        Lado_a = Lado3
        Lado_b = Lado1 
        Lado_c = Lado2
    else:
        Lado_a = Lado1
        Lado_b = Lado2
        Lado_c = Lado3

if Lado2 == Lado3 != Lado1:
    ladosIguais = 1
    if Lado1 > Lado2 and Lado1 > Lado3:
        Lado_a = Lado1
        Lado_b = Lado2 
        Lado_c = Lado3
    else:
        Lado_a = Lado2
        Lado_b = Lado3
        Lado_c = Lado1

if Lado1 == Lado3 != Lado2:
    ladosIguais = 1
    if Lado2 > Lado1 and Lado2 > Lado3:
        Lado_a = Lado2
        Lado_b = Lado1 
        Lado_c = Lado3
    else:
        Lado_a = Lado1
        Lado_b = Lado3
        Lado_c = Lado2

if Lado1 == Lado2 == Lado3:
    Lado_a = Lado1
    Lado_b = Lado2
    Lado_c = Lado3

# Fórmulas: 

Lados_BC = Lado_b + Lado_c
Lados_Elevados = (pow(Lado_b, 2)) + (pow(Lado_c, 2))
LadoA_Elevado = pow(Lado_a, 2)

if Lado_a >= Lados_BC:
    print('NAO FORMAM UM TRIANGULO')

else:
    if LadoA_Elevado == Lados_Elevados:
        print('TRIANGULO RETANGULO')

    if LadoA_Elevado > Lados_Elevados:
        print('TRIANGULO OBTUSANGULO')
    
    if LadoA_Elevado < Lados_Elevados:
        print('TRIANGULO ACUTANGULO')

    if Lado1 == Lado2 and Lado2 == Lado3 and Lado3 == Lado1:
        print('TRIANGULO EQUILATERO')
    
    if ladosIguais == 1:
        print('TRIANGULO ISOSCELES')
