import random

dias = [['segunda'], ['terça'], ['quarta'], ['quinta'], ['sexta']]
atividades = (str(input("Digite '/' para uma nova tarefa: ")).split('/'))

rem = str(input('Deseja remover algum dia [S/N]: ')).upper()

# estrutura de dados que irá remover o(s) dia(s)
if rem == 'S':
    for i in range(0, len(dias)):
        print(f'[{i}]  - {dias[i]}')
    n = str(input("Escolha o(s) número(s) como opção (para mais num, separe por '/'): ")).split('/')

    # deletando os dias que o usuário não quer

    # pegando os dias
    dia = list()
    for j in range(0, len(n)):
        # pos = int(n[j])
        dia.append(dias[int(n[j])])

    # buscando esses dias
    
    for s1 in range(0, len(n)):
        # print(dia[s1])
        s2 = 0
        while True:
            # print(dias[s2])
            if dia[s1] == dias[s2]:
                dias.pop(s2)
                break
            s2 += 1

# parte de adicionar as atividades aos dias:
tamAt = len(atividades)
tamDias = len(dias)
ati = []
pos = []
cont = 0

# condição para ver se há mais atividades do que dias
if tamAt <= tamDias:
    while tamAt > 0:
        vD = random.randint(0, len(dias)-1)
        vA = random.choice(atividades)

        while vD in pos or vA in ati:
            vD = random.randint(0, len(dias)-1)
            vA = random.choice(atividades) 

        dias[vD].append(vA)
        ati.append(vA)
        pos.append(vD)
        tamAt -= 1
else:
    tamDias -= 1
    vD = 0
    while tamAt > 0:
        vA = random.choice(atividades)
        
        while vA in ati:
            vA = random.choice(atividades) 

        dias[tamDias].append(vA)
        ati.append(vA)
        tamAt -= 1
        if tamDias > 0:
            tamDias -= 1
        else:
            tamDias = random.randint(0, len(dias)-1)

for dia in range(0, len(dias)):
    
    print(f'{dias[dia]}')
