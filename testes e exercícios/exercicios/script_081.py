lista = list()
reversa = list()
sair = 'n'
while 's' not in sair:
    lista.append(int(input('Adicione um valor: ')))
    sair = str(input('Sair? '))
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores na lista')
print(f'A lista em ordem decrescente é: {lista}')
print(f'O número 5 está na lista na pos {lista.index(5)}' if lista.count(5) > 0 else 'O numero 5 não está na lista')
