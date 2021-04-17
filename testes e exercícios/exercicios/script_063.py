print('SEQUÊNCIA DE FIBONNACI')
print('-=' * 13)

# Quantidade de vezes que queremos printar
quant = int(input('Quantos valores você deseja mostrar? '))
print('~' * 13)

# Estamos começando pelo cont = 2, pois já estamos printando os dois valores básicos na sequência de fibonnaci, 0 e 1
cont = 2

# As variaveis necessárias para a sequência
t1 = t3 = 0
t2 = 1


print(t1, end=' -> ')
print(t2, end=' -> ')

while cont < quant:
    cont += 1

    # t3 vai somar sempre os dois valores anteriores e atribuir, em sequência, t1 vai pegar o próximo valor e t2 a mesma coisa. Assim t3 vai sempre vai sempre fazer esse looping.
    t3 = t1 + t2
    t1 = t2
    t2 = t3

    print(t3, end=' -> ')

print('FIM', end='')
