idade = maior = menor = homens = 0
while True:
    sexo = contin = ''
    idade = int(input('Digite sua idade: '))
    while sexo != 'F' and sexo != 'M': 
        sexo = str(input('Digite o seu sexo: ')).upper()[0]
    
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            menor += 1
    
    while contin != 'S' and contin != 'N': 
        contin = str(input('Deseja continuar? [S/N]')).upper()[0]
                    
    if contin == 'N':
        break

print(f'A quantidade de pessoas maiores de 18 são {maior}')
print(f'A quantidade de homens cadastrados são {homens}')
print(f'A quantidade de meninas abaixo dos 20 anos são {menor}')
