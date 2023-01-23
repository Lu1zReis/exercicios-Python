def maxMini(arr):
    somas = []
    maior = menor = 0

    # pegando as somas dessa lista
    for c in range(0, len(arr)):
        soma = 0
        for j in range(0, len(arr)):
            if c != j:
                soma +=  arr[j]
        somas.append(soma)
    
    # mostrando o maior e o menor
    for i in range(0, len(arr)):
        if i == 0:
            maior = somas[i]
            menor = somas[i]
        else:
            if somas[i] < menor:
                menor = somas[i]
            if somas[i] > maior:
                maior = somas[i]
    
    print(menor, maior)

vals = [1,3,5,7,9]
maxMini(vals)
