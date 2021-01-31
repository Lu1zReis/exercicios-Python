Lado1 = float(input())
Lado2 = float(input())
Lado3 = float(input())

if Lado1 == Lado2 != Lado3:
    ladosIguais = 0

if Lado2 == Lado3 != Lado1:
    ladosIguais = 0

if Lado1 == Lado3 != Lado2:
    ladosIguais = 0

if ladosIguais == 0:
    print('Existe dois numeros iguais')
else:
    print('Nao existe numeros iguais')
