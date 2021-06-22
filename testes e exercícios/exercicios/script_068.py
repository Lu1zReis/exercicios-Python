import time
from random import randint

print('=' * 25)
print('Jogo do PAR ou IMPAR')
print('=' * 25)
vitorias = 0

while True:
    # Entrada do usuário
    valorUsu = int(input('Digite um valor: '))
    ValorParImpar_usu = ' '
    while ValorParImpar_usu not in 'PI':
        ValorParImpar_usu = str(input('Escolha, PAR ou Impar: ')).upper().strip()[0]

    # Ações do PC
    valorPC = randint(0, 10)
    soma = valorPC + valorUsu

    if 'P' in ValorParImpar_usu:
        if soma % 3 == 1:
            print('-=-' * 5, 'Você perdeu', '-=-' * 5)
            print(f'A soma total é {soma}, deu IMPAR')
            break
        else:
            print(f'Você ganhou, deu PAR, {soma}. O número escolhido pelo pc foi {valorPC}')
            print('-=-' * 20)

    elif 'I' in ValorParImpar_usu:
        if soma % 2 == 0:
            print('-=-' * 5, 'Você perdeu', '-=-' * 5)
            print(f'A soma total é {soma}, deu PAR')
            break
        else:
            print(f'Você ganhou, deu IMPAR, {soma}. O número escolhido pelo pc foi {valorPC}')
            print('-=-' * 20)

    # Contagem de vitórias
    vitorias += 1

print(f'O valor escolhido pelo PC é: {valorPC}')
print(f'O valor escolhido pelo Usu é: {valorUsu}')
print(f'Você venceu {vitorias} vez(es)')
