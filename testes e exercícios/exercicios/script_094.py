pessoa = dict()
pessoas = list()
mulheres = list()
idadeAcima = list()
quantPessoa = 0
mediaIdade = 0.0

while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Sigite o sexo[M/F]: ')).lower()
    pessoa['idade'] = int(input('Digite a idade: '))

    pessoas.append(pessoa.copy())

    # quant de pessoas:
    quantPessoa += 1
    # média de idade:
    mediaIdade += pessoa['idade']
    # adicionando sexo feminino
    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa.copy())
    # adicionando pessoas acima da idade:
    if pessoa['idade'] >= 18:
        idadeAcima.append(pessoa.copy())
    
    continua = str(input('Deseja continuar?[S/N]: ')).lower()
    if continua == 'n':
        mediaIdade /= quantPessoa
        break

print(pessoas)
print(f'quantidade de pessoas: {quantPessoa}')
print(f'média de idade: {mediaIdade}')
print(f'mulheres: {mulheres}')
print(f'pessoas acima da idade: {idadeAcima}')
