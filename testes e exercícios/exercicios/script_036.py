CompraCasa = float(input('Qual o valor da casa: '))
Salario = float(input('Qual o seu salário mensal: '))
AnosPagamento = float(input('Em quantos anos você quer pagar: '))
prestacao = CompraCasa / (AnosPagamento * 12)
PorcentagemSalario = Salario * 0.30

print('O valor da casa será R${:.2f} e o seu salário é de R${:.2f}, sua prestação será de {:.2f}'.format(CompraCasa, Salario, prestacao))

if PorcentagemSalario < prestacao:
    print('Desculpe empréstimo NEGADO!')

elif PorcentagemSalario >= prestacao:
    print('Empréstimo CONCEDIDO!')
