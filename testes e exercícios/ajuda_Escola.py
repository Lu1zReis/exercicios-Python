from datetime import date
# VAR GLOBAIS
MateriasSemanais = ['geo', 'orçamentos', 'matemática', 'inst. elétrica', 'filosofia']
Materias_RED = ['português', 'hidraulica','filosfia', 'ed. física']
MateriasTotais = ['português', 'hidraulica', 'filosfia', 'ed. física', 'geo', 'orçamentos', 'matemática', 'inst. elétrica']

# Var dos horários/dias
seg = ['hidráulica', 'Ed. Física']
ter = ['Qual. C. civil', 'Geografia']
qua = ['Filosofia', 'Matemática', 'CAD']
qui = ['Orçamentos', 'Inst. Elétricas']
sex = ['Português']

data = date.today()
dia = data.weekday()
diaSemana = []
d = ''

if dia == 0:
    diaSemana = seg
    d = 'segunda'
elif dia == 1:
    diaSemana = ter
    d = 'terça'
elif dia == 2:
    diaSemana = qua
    d = 'quarta'
elif dia == 3:
    diaSemana = qui
    d = 'quinta'
elif dia == 4:
    diaSemana = sex
    d = 'sexta'


while True:
    # Outras Váriaveis
    escolha = 0
    tam1 = len(MateriasTotais)
    tam2 = len(MateriasSemanais)
    tam3 = len(Materias_RED)

    # Parte do menu
    print('=-=' * 30)
    print(f'	Software de ajuda com as matérias	Data: {data}')
    print(f'    Matérias de hoje: {diaSemana}')
    print('     ', '~' * 20, f'{d}', '~' * 20)
    print('=-=' * 30)

    print('''
        [1] Mostrar todas as matérias
        [2] Matérias semanais
        [3] Matérias para entregar no fim do RED
        [4] Sair
    ''')

    # Ações
    while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
        escolha = int(input('Escolha uma opção do menu: '))

    print('\n')

    if escolha == 1:
        for c in range(0, tam1):
            print(f'	Matérias totais: {MateriasTotais[c]}')
    elif escolha == 2:
        for s in range(0, tam2):
            print(f'	Matérias semanais: {MateriasSemanais[s]}')
    elif escolha == 3:
        for r in range(0, tam3):
            print(f'	Matérias "mensais": {Materias_RED[r]}')
    elif escolha == 4:
        print('Programa finalizado com sucesso...')
        break

    print('\n')
