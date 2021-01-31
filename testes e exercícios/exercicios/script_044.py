print('===== LOJA =====')
preco = float(input('Preço a pagar do produto: '))
print('Como será o pagamento?')
print('1 - À vista dinheiro/cheque \n2 - À vista no cartão')
print('3 - Em até 2x no cartão \n4 - 3x ou mais no cartão')
escolha = int(input('Qual a opção de pagamento: '))

if escolha == 1:
    valor = preco * 0.10
    print('Escolha a vista, então você terá 10% de desconto que será de {}\nPreço final: {}'.format(valor, preco - valor))
elif escolha == 2:
    valor = preco * 0.05
    print('Escolha a vista no cartão, então você terá 5% de desconto que será de {}\nPreço final: {}'.format(valor, preco - valor))
elif escolha == 3:
    valor = preco / 2
    print('Escolha em até 2x no cartão, então o preço será normal e em 2x que vai ser de {}\nPreço final: {}'.format(valor, preco))
elif escolha == 4:
    vezes = int(input('Quantas vezes no cartão: '))
    valor = preco + (preco * 0.20)
    quant = valor / vezes
    print('Escolha em até 3x ou mais no cartão\nSua compra será parcelada em {}x de {:.2f} com JUROS'.format(vezes, quant))
    print('Então terá 20% de juros que será de {}'.format(valor))
    print('Preço final: {}'.format(valor))
else:
    final = preco
    print('Opcão Inválida. Tente NOVAMENTE!')
    print('Sua compra de {} vai ficar com {:.2f}'.format(preco, final))