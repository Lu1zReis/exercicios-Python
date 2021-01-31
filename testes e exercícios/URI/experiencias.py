# Variaveis
quant = int(input())
listaNome = []
listaValor = []
total = 0
ratos = 0
sapos = 0
coelhos = 0

for c in range(0, quant):
    valor, nome = input().split()
    valor = int(valor)
    nome = str(nome).upper()
    if(nome == 'R'):
        ratos += valor
    elif(nome == 'S'):
        sapos += valor
    else:
        coelhos += valor
    total += valor
    listaNome.append(valor)
    listaValor.append(nome)

nova_lista = [listaNome, listaValor]
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))

def porcentagem(coelhos, ratos, sapos):
    Porcent_coelhos = (coelhos * 100) / total
    Porcent_ratos = (ratos * 100) / total
    Porcent_sapos = (sapos * 100) / total

    print('Percentual de coelhos: {:.2f} %'.format(Porcent_coelhos))
    print('Percentual de ratos: {:.2f} %'.format(Porcent_ratos))
    print('Percentual de sapos: {:.2f} %'.format(Porcent_sapos))

porcentagem(coelhos, ratos, sapos)
