# Variaveis
i = 1
# Definir o vetor no escopo
lista = []

while i <= 10:
    
    valores = lista.append(input('Digite o {} º valor  = '.format(i)))
    i += 1
    pass

print ('Os valores foram: ')

j = 0
num_Cont = len(lista)

while j < num_Cont:
    print(lista[j])
    j += 1
    pass