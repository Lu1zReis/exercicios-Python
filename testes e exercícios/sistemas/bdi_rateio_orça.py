faturamento = float(input('Faturamento Mensal da Obra: '))
custo = float(input('Custo Direto Total da Obra (R$): '))
prazoObra = int(input('Prazo da obra em meses: '))

admFatu = 50000 + 116000 + 62500 + 75000 + 67000

despesaMensal = float(input('Qual a despesa mensal da administração? '))
formRateio = ((despesaMensal * faturamento * prazoObra) / (admFatu * custo)) * 100
print(f'O valor de rateio é: {formRateio:.2f}%')
