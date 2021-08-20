import math
while True:
    n = int(input('Quantos valores vão ser lidos? '))
    dados = []
    val = media = form = 0
    for c in range(0, n):
        val = int(input(f'Digite o valor {c}: '))
        dados.append(val)
        media += val
    media = media / n
    for i in range(0, n):
        form += (dados[i] - media)**2
    form /= n
    print(f'A variância é: {form}')
    print(f'A DP é: {pow(form, 1/2)}')
    sair = input('Deseja sair? [S/N] ').upper[0]
    if 'S' in sair:
        break
