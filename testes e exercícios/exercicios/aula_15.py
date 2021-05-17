# Exercício 66
'''
cont = soma = x = 0
while True:
    x = int(input('Digite um valor (999 para parar): '))
    if x == 999:
        break
    cont += 1
    soma += x
print(f'A soma do(s) {cont} valor(es) foi {soma}')

# Ecercicio 67
tab = 0
while True:
    tab = int(input('Qual é o valor da tabuada que deseja ser mostrado? '))
    if tab < 0:
        break
    else:
        c = 0
        while c <= 10:
            print(f'{tab} x {c} = {tab * c}')
            c += 1

# Exercício 68
import random
j = 0
while True:
    
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    esc = int(input('Escolha um número: '))
    pi = str(input('Escolha [P/I]: ')).upper().split()[0]
    escPC = random.choice(lista)
    soma = esc + escPC

    if pi == 'P':
        if soma % 2 == 0:
            print(f'Parabénss, você ganhou, deu PAR: {soma}')
            print('Vamos jogar novamente')
            j += 1
        if soma % 2 == 1:
            print(f'O pc ganhou, deu IMPAR: {soma}')
            break
    if pi == 'I':
        if soma % 2 == 1:
            print(f'Parabénss, você ganhou, deu IMPAR: {soma}')
            j += 1
        if soma % 2 == 0:
            print(f'O pc ganhou, deu IMPAR: {soma}')
            break
print(f'Programa finalizado... Você ganhou {j}x')


# Exercicio 69:

# Variáveis para serem usadas depois
MaiorIdade = Quant_Homem = Mulheres_Menos_20 = 0

while True:
    # Entrada do usuário
    idade = int(input('\nQual a idade? '))
    sexo = str(input('Qual seu sexo? ')).upper().split()[0]
    continuar = str(input('Quer continuar? [s/n] ')).upper().split()[0]

    if idade > 18:
        MaiorIdade += 1

    if 'M' in sexo:
        Quant_Homem += 1

    if 'F' in sexo:
        if idade < 20:
            Mulheres_Menos_20 += 1

    if continuar == 'N':

        print(f'A quantidade de pessoas maior de 18 anos é: {MaiorIdade}')
        print(f'A quantidade de homens cadastrados é: {Quant_Homem}')
        print(f'A quantidade de mulheres com menos de 20 é: {Mulheres_Menos_20}')

        break
'''
# Exercicio 71:
print('-=' * 10, 'CAIXA ELETRÔNICO', '-=' * 10)
while True:
    # Cédulas:
    cedula50 = cedula20 = cedula10 = cedula1 = 0

    saque = int(input('Digite o valor a ser sacado R$: '))

    cedula50 = saque // 50
    cedula20 = (saque - (cedula50 * 50)) // 20
    cedula10 = (saque - ((cedula50 * 50) + (cedula20 * 20))) // 10
    cedula1 = (saque - ((cedula50 * 50) + (cedula20 * 20) + (cedula10 * 10))) // 1

    print('=' * 60)

    if cedula50 > 0:
        print(f'São {cedula50} cédula(s) de 50R$')
    if cedula20 > 0:
        print(f'São {cedula20} cédula(s) de 20R$')
    if cedula10 > 0:
        print(f'São {cedula10} cédula(s) de 10R$')
    if cedula1 > 0:
        print(f'São {cedula1} cédula(s) de 1R$')

    print('=' * 60)

    sair = str(input('Deseja sair [S/N]: ')).upper().split()[0].strip()
    if 'S' in sair:
        break
