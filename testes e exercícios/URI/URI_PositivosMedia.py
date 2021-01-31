# Variaveis
i = 1
# Definir o vetor no escopo
lista = []
a = 0
while i <= 6:
    lista.append(float(input()))
    if(lista[i] > 0):
        a += 1
    i += 1
    pass

print ('Os valores foram: ')

j = 0
num_Cont = len(a)

while j < num_Cont:
    print(a)
    j += 1
    pass