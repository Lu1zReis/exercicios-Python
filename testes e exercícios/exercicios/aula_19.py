dados = {'nome': 'Luiz', 'idade': 19} # Podemos declarar um dicionário com chaves '{}' ou dict()
dados['sexo'] = 'M' # Podemos atribuir assim um valor, mesmo não declarando antes

print(dados) # Assim printamos todo o dicionário

print('\n')

print(dados.keys()) # Mostrando as chaves do dicionário
print(dados.values()) # Mostrando os valores contido nas chaves
print(dados.items()) # Mostra as chaves e os valores do dicionário

print('\n')

print(f"{dados['nome']} tem {dados['idade']} anos, e seu sexo é {dados['sexo']}")

print('\n')

# Podemos usar em função das funções keys, values e items do dicionário
for k in dados.keys():
    print(k)
for v in dados.values():
    print(v)
for k, v in dados.items():
    print(f'{k} = {v}')

print('\n')

# para deletar uma chave em conjunto com um item
del dados['sexo']
print(dados.items())

# Criando dicionários dentro de uma lista

estado1 = {'uf': 'Mato Grosso', 'sigla': 'MT'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = [estado1, estado2]
print(brasil[0]['uf'])

# Criando dicionários dentro de uma lista com for
eletronico = dict()
aparelhos = list()
for i in range(0, 3):
    eletronico['cel'] = str(input('Digite um celular: '))
    eletronico['marca'] = str(input('Digite sua marca: '))
    aparelhos.append(eletronico.copy()) # como aqui não podemos usar o fatiamento já que é um dicionário, usamos o copy()

print(aparelhos)
