salario = float(input())
novoSalario = 0
reajuste = 0
porcentagem = 0
if salario > 2000:
    novoSalario = (salario * 0.04) + salario
    reajuste = salario * 0.04
    porcentagem = 4
else:
    if salario <= 400:
        novoSalario = (salario * 0.15) + salario
        reajuste = salario * 0.15
        porcentagem = 15
    elif salario > 400 and salario <= 800:
        novoSalario = (salario * 0.12) + salario
        reajuste = salario * 0.12
        porcentagem = 12
    elif salario > 800 and salario <= 1200:
        novoSalario = (salario * 0.10) + salario
        reajuste = salario * 0.10
        porcentagem = 10
    elif salario > 1200 and salario <= 2000:
        novoSalario = (salario * 0.07) + salario
        reajuste = salario * 0.07
        porcentagem = 7

print ('Novo salario: {:.2f}'.format(novoSalario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(porcentagem))
