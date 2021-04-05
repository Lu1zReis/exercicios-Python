dias = float(input('Digite a o tempo em dias do uso do carrro: '))
KM = float(input("Digite o valor rodado em KM:  "))
KM *= 0.15
dias *= 60
aPagar = KM+dias
input('O preço total a pagar será : {}'.format(aPagar))
