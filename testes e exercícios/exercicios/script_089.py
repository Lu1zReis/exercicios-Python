cont = 's'
alun = 0
alunos = list()

while cont in 'Ss':
    nome = str(input('Insira um nome: '))
    nota1 = float(input('Insira a 1a. nota: '))
    nota2 = float(input('Insira a 2a. nota: '))

    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

    cont = str(input('Deseja continuar?[S/N] '))
print(f' Pos.   Aluno     Nota')
for i in range(0, len(alunos)):
    print(f'{i:>4}{alunos[i][0]:^10}{alunos[i][2]:>12}')

while alun != 999:
    alun = int(input('\nDe qual aluno deseja ver a nota?(999 sai) '))
    if alun != 999:
        print(f'{alun} = Aluno {alunos[alun][0]} tem as notas {alunos[alun][1]}')
