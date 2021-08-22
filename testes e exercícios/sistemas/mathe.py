import random
import time
ativi = ['brincar', 'assistir um filme', 'jogar algum jogo']
conve = ['Parece complicado...', 'Eu só sou um programa de PC, mas acho que deve sair dessa', 'O que acha de tentar ir resolver o problema?']
conve2 = ['Você meio que falou que tava triste antes', 'Eu sou só um código cheio de linha, mas acho que você deve não pode ficar pensando muito nisso ._.']
def mal(vezesMal):
    while True: 
        if vezesMal >= 1 and vezesMal < 3:
            print('MATHE: Hmmmmmmm... Quer conversar mais sobre isso? O que se trata o problema?')
            resposta = str(input('ME: '))
            c = random.choice(conve2)
            print(f'MATHE: {c}')
            print(f'MATHE: Não sei se vai ajudar, mas vou escolher uma atividade aqui...')
            time.sleep(3)
            print(f'MATHE: aqui uma atividade: {random.choice(ativi)}')
            break
        if vezesMal >= 3:
            print('MATHE: sei lá, se ficar falando muito com o PC o pessoal pode achar que você está doido rs')
            time.sleep(2)
            print('MATHE: mas pelo visto como você pode ver eu só recomendo atividades... kkk')
            print(f'MATHE: mas aqui está a lista, faça aquilo que te fizer melhor: {ativi}')
            break

        else:
            print('MATHE: O que foi?')
            resposta = str(input('ME: '))
            print(random.choice(conve))
            break

def gerarPerg():
    p1 = random.choice(['Tudo bem?', 'como vai?'])
    return p1

resposta = ' '
vezesMal = 0

while True:
    perg = gerarPerg()
    print(f'MATHE: {perg}')
    resposta = str(input('ME: ')).lower()

    if resposta == 'mal' or resposta == 'triste' or resposta == 'não':
        mal(vezesMal)
        vezesMal += 1

