# Inserção dos dados
escolha1 = input()
escolha2 = input()
escolha3 = input()

if escolha1 == 'vertebrado':
    if escolha2 == 'ave':
        if escolha3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else: # vai entrar na condição de mamifero
        if escolha3 == 'onivoro':
            print('homem')
        else:
            print('vaca')

else:
    if escolha2 == 'inseto':
        if escolha3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else: # vai entrar em anelídeo
        if escolha3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
