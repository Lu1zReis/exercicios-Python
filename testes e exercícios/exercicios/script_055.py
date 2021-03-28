MaiorPeso = 0.0
MenorPeso = 0.0

for i in range(1, 6):
    peso = float(input('Digite o peso {}: '.format(i)))
    if i == 0:
        MaiorPeso = peso
        MenorPeso = peso
    else:
        if peso > MaiorPeso:
            MaiorPeso = peso
        elif peso < MenorPeso:
            MenorPeso = peso

print('Maior peso: {}'.format(MaiorPeso))
print('Menor peso: {}'.format(MenorPeso))
