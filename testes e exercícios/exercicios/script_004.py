a = input('Digite algo: ')
print(type(a))
print('É alphaNumérico:', format(a.isalnum()))
print('É só letras:', format(a.isalpha()))
print('É decimal:', format(a.isdecimal()))
print('É só letras mínusculas:', format(a.islower()))
print('É só letras grandes:', format(a.isupper()))
print('É só números:', format(a.isnumeric()))
print('Tem espaço:', format(a.isspace()))
print('Está capitalizada:', format(a.istitle()))
