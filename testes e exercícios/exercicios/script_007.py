a = float(input('Digite um valor que deseja: R$'))
novo = a - ((a*5)/100)
print('O novo valor de R${:.2f} com 5% de desconto será {:.2f}'.format(a, novo))

############################
print('\n')

salario = float(input('Digite o seu salário: R$'))
NovoSalario = salario + ((salario*15)/100)
print('O salário {} com 15% de aumento será {}'.format(salario, NovoSalario))
