quant = int(input())

# VARIAVEIS
# int
idade = 0
maior = 0
medio = 0
menor = 0
maior2 = 0
medio2 = 0
menor2 = 0
grupo = 0
divi = 1
Size_Group = 0
aux = quant
m = 0

# str
nome = ''

#lista
idades = []
nomes = []
lider = []
entregador = []
piloto = []
grupo1_nome = []
grupo1_idade = []
grupo2_nome = []
grupo2_idade = []
grupo3_nome = []
grupo3_idade = []

# achar a quantidade do grupo 
for k in range(0, quant):
    grupo = aux / divi
    if(grupo == 3): 
        Size_Group = divi
    divi += 1

for c in range(0, quant):
    nome, idade = input().split(' ')
    nome = str(nome)
    idade = int(idade)
    nomes.append(nome)
    idades.append(idade)

for i in range(0, quant):
    if i == 0:
        maior = idades[i]
        menor = idades[i]
        medio = idades[i]
        lider.append(nomes[i])
        piloto.append(nomes[i])
        entregador.append(nomes[i])
        m = 0

    else:
        if idades[i] < menor:
            menor = idades[i]
            piloto.insert(0, nomes[i])

        elif idades[i] > maior:
            maior = idades[i]
            lider.insert(0, nomes[i])

        elif idades[i] > menor and idades[i] < maior:
            medio = idades[i]
            entregador.insert(0, nomes[i])

        else:

            if idades[i] < maior and idades[i] > medio:
                maior2 = idades[i]
                lider.insert(1, nomes[i])

            elif idades[i] > menor and idades[i] < medio:
                medio2 = idades[i]
                entregador.insert(1, nomes[i])

            else:
                menor2 = idades[i]
                piloto.insert(1, nomes[i])

# print(nomes)
# print(idades)
print('Lideres {}: {} e {}'.format(lider, maior, maior2))
print('Entregadores {}: {} e {}'.format(entregador, medio, medio2))
print('Pilotos {}: {} e {}'.format(piloto, menor, menor2))

print('Quantidade de grupos: {}'.format(Size_Group))
