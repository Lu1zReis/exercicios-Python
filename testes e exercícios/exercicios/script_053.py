# já colocando .strip() para tirar os espaços do início e fim da string e o upper() para maiúscula
frase = str(input('Digite a frase: ')).strip().upper()


# para separar as palavras como em uma lista
palavras = frase.split()

# aqui abaixo a função join aglutina as palavras da lista
juntar_palavras = ''.join(palavras)

size = len(juntar_palavras)
inverso = ''

# size-1 / vai começar do fim da palavra, -1 / mostra até onde o programa tem que ir, -1 / vai pulando de 1 em 1 negativamente
for c in range(size-1, -1, -1):
    inverso += juntar_palavras[c]

if inverso == juntar_palavras:
    print('Há um Palíndromo na frase: {}\nSendo ela: {} de trás para frente'.format(frase, inverso))
else:
    print('Não há um Palíndromo na frase: {} / {}'.format(frase, inverso))
