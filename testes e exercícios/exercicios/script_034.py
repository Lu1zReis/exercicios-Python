salario = float(input('Digite seu salário: R$ '))
if salario >= 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

Salario_Final = aumento + salario

print('Seu salario era R$ {}\nAgora houve um aumento de R$ {}'.format(salario, Salario_Final))
