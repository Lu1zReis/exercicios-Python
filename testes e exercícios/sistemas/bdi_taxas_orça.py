I = float(input('Taxa de adm central: '))
R = float(input('Taxa de risco de empreendimento: '))
cf = float(input('Taxa do custo finan do empreendimento: '))
t = float(input('Tributos: '))
c = float(input('Taxa de comercialização: '))
l = float(input('Lucro: '))

denominador = 1 - ((t + c + l) / 100)
numerador = (1 + (I/100)) * (1 + (R/100)) * (1 + (cf/100))

bdi = ((numerador / denominador) - 1) * 100

print(f'O BDI é de {bdi:.2f}%')
