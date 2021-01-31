from datetime import date
print('CONFEDERAÇÃO DE NATAÇÃO')
data = int(input('Digite sua data de nascimento: '))
idade =  date.today().year - data
if idade > 25:
    print('Sua categoria é MASTER')
else:
    if idade <= 9:
        print('Sua categoria é MIRIM')
    elif idade > 9 and idade <= 14:
        print('Sua categoria é INFANTIL')
    elif idade > 14 and idade <= 19:
        print('Sua categoria é SÊNIOR')        
    elif idade > 19 and idade <= 25:
        print('Sua categoria é SÊNIOR')        
