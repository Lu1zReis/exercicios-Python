# cedulas de 50, 20, 10 e 1 real
print('-='*10, '\nBANCO\n', '-='*10)

valor = nota50 = nota20 = nota10 = nota1 = 0
valor = int(input('Digite o valor para ser sacado: R$'))
nota50 = valor // 50
nota20 = (valor - (50 * nota50)) // 20
nota10 = (valor - ((50 * nota50) + (20 * nota20))) // 10
nota1 = (valor - ((50 * nota50) + (20 * nota20) + (10 * nota10))) // 1

print(f'\nVALOR RETIRADO R${valor}')
if nota50 > 0:
    print(f'São {nota50} nota(s) de R$50')
if nota20 > 0:   
    print(f'São {nota20} nota(s) de R$20')
if nota10 > 0:
    print(f'São {nota10} nota(s) de R$10')
if nota1 > 0:
    print(f'São {nota1} nota(s) de R$1')
