x = input('Digite algo:')
print(f'O tipo primitivo desse valor é ', type(x))
print('É alfanúmerico?', x.isalnum())
print('É um número?', x.isnumeric())
print('É alfabetico?', x.isalpha())
print('Só tem espaços?', x.isspace())
print('Está somente em maiúsculas?', x.isupper())
print('Está somente em minúsculas?', x.islower())
print('Está capitalizada?', x.istitle())
