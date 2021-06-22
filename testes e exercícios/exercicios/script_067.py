while True:
    print('-=-' * 20)
    valor = int(input('Escolha um número para a tabuada: '))
    print('-=-' * 20)

    if valor < 0:
        break

    for c in range(1, 11):
        print(f'{c} x {valor} = {c * valor}')
        c += 1

print('-' * 21, 'TABUADA ENCERRADA', '-' * 20)
