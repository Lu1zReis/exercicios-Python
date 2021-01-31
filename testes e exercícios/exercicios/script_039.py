from datetime import date
Nascimento = int(input('Digite o ano do seu nascimento: '))
anoAtual = date.today().year # var que guarda o Ano atual
data = anoAtual - Nascimento

if data < 18:
    D = 18 - data
    print('Você tem {} ano(s) de idade, e ainda falta {} ano(s) para se alistar, e será em {}'.format(data, D, anoAtual+D))
elif data == 18:
    print('Você tem {} ano(s) de idade, deve se alistar IMEDIATAMENTE!'.format(data))
else:
    D = data - 18
    print('Você tem {} ano(s) de idade, já se passou {} ano(s) desde o alistamento, que devia ter sido no ano de {}'.format(data, D, anoAtual-D))
