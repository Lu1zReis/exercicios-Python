listaNome = []
ListaIdade = []
ListaSexo = []

Media = 0

MaisVelho = ''
aux1 = 0
aux2 = 0

for c in range(0, 4):
    print('---{}º PESSOA---'.format(c+1))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('(M / F): ')).upper()

    listaNome.append(nome)
    ListaIdade.append(idade)
    ListaSexo.append(sexo)

    if ListaSexo[c] == 'M':
        if ListaIdade[c] > aux1:
            aux1 = ListaIdade[c]
            MaisVelho = listaNome[c]
    if ListaSexo[c] == 'F':
        if ListaIdade[c] < 20:
            aux2 += 1

    if c == 3:
        Media = (ListaIdade[0] + ListaIdade[1] + ListaIdade[2] + ListaIdade[3]) / 4


print('A média do grupo é: {}'.format(Media))
print('O homem mais velho tem {} anos e se chama {}'.format(aux1, MaisVelho))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(aux2))