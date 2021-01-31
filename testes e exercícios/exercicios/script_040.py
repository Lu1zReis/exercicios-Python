print('Notas: menor que 5, REPROVADO / entre 5 e 6.9, RECUPERAÇÃO / maior ou igual a 7, APROVADO')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média é {} e você está REPROVADO!!'.format(media))
elif media >= 5 and media < 7:
    print('Sua média é {} e você está de RECUPERAÇÃO!!'.format(media))
elif media >= 7:
    print('Sua média é {} e você está APROVADO!!'.format(media))
