lado = int(input('Adicione o primeiro seguimento: '))
lado2 = int(input('Adicione o segundo seguimento: '))
lado3 = int(input('Adicione o terceiro seguimento: '))

if lado == lado2 == lado3:
    print('Todos os lados são iguais - EQUILÁTERO')

else:
    if lado > lado2 and lado > lado3:
        maiorlado = lado
        ladob = lado2
        ladoc = lado3

    elif lado2 > lado and lado2 > lado3:
        maiorlado = lado2
        ladob = lado
        ladoc = lado3

    elif lado3 > lado and lado3 > lado2:
        maiorlado = lado3
        ladob = lado
        ladoc = lado2

    lados_bc = ladob + ladoc

    if maiorlado >= lados_bc:
        print('Não tem como formar um triângulo')
    elif ladob == ladoc:
        print('Dois lados iguais - ISÓSCELES')
    else:
        print('Todos os lados diferentes - ESCALENO')
