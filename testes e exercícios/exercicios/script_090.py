from pickletools import float8


aluno = {'nome': '', 'media': 0, 'situa': ''}
aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = float(input(f"Digite a média de {aluno['nome']}: "))
if(aluno['media'] > 6):
    aluno['situa'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situa'] = 'Recuperação'
else:
    aluno['situa'] = 'Reprovado'
print(f"A média é igual a {aluno['media']:.2f}")
print(f"A situação de {aluno['nome']} consta como {aluno['situa']}(a)")
