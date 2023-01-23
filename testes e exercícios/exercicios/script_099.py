from time import sleep
def maior(*nums):
    print('=-' * 25)
    maior = 0
    quant = len(nums)

    for valor in nums:
        if maior < valor: 
            maior = valor

    print('Analisando os valores passados...')
    for v in nums:
        print(v, end=' ', flush=True)
        sleep(0.5)

    print(f'Foram informados {quant} valor(es) ao todo')

    print(f'O maior valor informado foi {maior}')


maior(9, 2, 10, 4, -11)
maior(8, 2)
maior(10, 10.1)
maior(2, 3, 1, 2)
maior()
