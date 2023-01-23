num = [1, 4, 3, 5]
num[1] = 7 # listas são mutáveis diferente de tuplas
print(num)

# para adicionarmos um valor em uma lista cuja a posição ainda não exista, como posicão 5, da lista num acima, irá retornar um erro se for num[5] = 6

num.append(6) # assim será a forma correta

num.insert(0, 1) # no 1º parametro irá ficar a posição que o valor do 2º parametro será adicionado. 

# num.sort() #irá organizar a lista e sort(reverse=True) irá organizar a lista do maior ao menor

print(num)

num.pop() # irá somente remover o valor da última posição, agora se passarmos a posição do valor como parametro, ele irá remover aquele valor da posição

num.remove(1) # irá remover o valor do parametro

print(num)
print('--------')
for c, v in enumerate(num):
    print(f'Na posição {c} tem o valor {v}')

a = [1, 2, 3, 4]
b = a #em python se usarmos b=a, ele iguala os valores e interliga, então tudo que fazermos em a ou b, mudara no outro, a não ser que fazermos a[:], só assim ele só copiara sem se interligar
a[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')