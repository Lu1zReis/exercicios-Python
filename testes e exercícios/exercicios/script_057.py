# Colocamos o .strip() para tirar os espaços e o [0] significa que queremos só a primeira letra que vier do input()
sexo = str(input('Digite um sexo, [M/F]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Por favor, digite um sexo válido: ')).upper().strip()[0]

print('O sexo escolhido foi o {}'.format(sexo))
