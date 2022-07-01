pessoa = dict()
pessoas = list()
mulheres = list()
idadeAcima = list()
quantPessoa = 0
mediaIdade = 0.0

while True:
    
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Sigite o sexo[M/F]: ')).lower()

    while pessoa['sexo'] not in 'mf':
        pessoa['sexo'] = str(input('Por favor, somente "m ou n": ')).lower()  
      
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
    while continua not in 'sn':
       continua = str(input('Por favor, digite [S/N] para continuar: ')).lower()

    if continua == 'n':
        mediaIdade /= quantPessoa
        break

print(f'quantidade de pessoas: {quantPessoa}')
print(f'média de idade: {mediaIdade:.2f}')
print(f'mulheres: {mulheres}')
print(f'pessoas acima da idade: {idadeAcima}')

for i in range(0, quantPessoa):
    print(f"     |==> nome = {pessoas[i]['nome']}, sexo = {pessoas[i]['sexo']}, idade = {pessoas[i]['idade']}")
