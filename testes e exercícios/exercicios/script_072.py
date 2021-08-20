numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
pos = 21
while pos < 0 or pos > 20:
    pos = int(input('Digite um número entre 0 e 20: '))
    if pos < 0 or pos > 20:
        print('Tente novamente...')

print(f'Você digitou o número {numeros[pos]}')
