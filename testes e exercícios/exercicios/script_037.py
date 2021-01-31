num = int(input('Digite um número: '))
print('''Escolha uma opção para converter esse número
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal ''')
opcao = int(input('Escolha uma dessas 3 opções: '))

# Opcão da escolha
if opcao == 1:
    #[2:] serve só para não mostrar os dados que são do tipo que é convertido
    print('O número {} convertido em binário seria {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido em octal seria {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido em hexadecimal seria {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Desculpe, tente novamente.')
