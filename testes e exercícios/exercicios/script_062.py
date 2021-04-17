
print('GERADOR DE PA')
print('-=' * 10)

# Variaveis:
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

pa = termo
parar = 10
adic = 0

# Execução:
while adic < parar:

    print('{}'.format(pa), end=' -> ')
    # Função da PA
    pa += razao

    # Função de adicionar mais valores para a condição do while se tornar falsa
    adic += 1

    # Quando a função acima chegar ao valor parar, vai entrar nessa condição para adicionarmos + valores ou não
    if adic == parar:
        print('PAUSA', end='')
        parar += int(input('\nDeseja adicionar mais valores? '))

# Usando a variável adic como contador, para mostrar quantas PA exibidas
print('Progressão finalizada com {} termos mostrados.'.format(adic))
