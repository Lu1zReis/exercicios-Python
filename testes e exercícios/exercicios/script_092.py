import datetime
# pegar a data atual
ano = datetime.date.today().strftime('%Y')
ano = int(ano)

pessoa = dict()
pessoa['nome'] = str(input('Digite o seu nome: '))
pessoa['idade'] = int(input('Digite o ano do seu nascimento: '))
pessoa['ctps'] = int(input('Digite a sua ctps: '))

if pessoa['ctps'] != 0:

    pessoa['contratato'] = int(input('Digite o ano que foi contratado: '))
    pessoa['salario'] = float(input('Digite o seu salário: $'))
    pessoa['aposentadoria'] = (35 + pessoa['contratato']) - pessoa['idade']
    pessoa['idade'] = ano - pessoa['idade']

    print(pessoa)
    
    for c, v in pessoa.items():
        print(f'{c} tem o valor {v}')

else:
    print(pessoa)

    for c, v in pessoa.items():
        print(f'{c} tem o valor {v}')