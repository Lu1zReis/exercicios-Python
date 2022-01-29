dados1 = list()
dados2 = list()
pessoa = list()

dados1.append('Fer')
dados1.append(18)
dados2.append('Yum')
dados2.append(12)

pessoa.append(dados1[:]) 
pessoa.append(dados2[:])# usamos o fatiamento para ser só uma cópia da outra lista e não uma ligação

print(pessoa)

lista = list()
galera = list()

for i in range(0, 3):
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Idade: ')))
    galera.append(lista[:])
    lista.clear()

for p in galera:
    print(p[0][1])
