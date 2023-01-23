lista = ['Nainara', 'Lucas']

print(f'LISTA ANTES: {lista}')

lista.append(input(': '))

print(f'LISTA DEPOIS: {lista}')


for i in range(0, len(lista)):
    if 'Daniel' == lista[i]:
        print('Existe o nome Daniel')
    else:
        print('Não existe o nome Daniel')
