from datetime import date

def data():
    x = str(date.today()).split('-')
    m = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    print(f'{x[2]} de {m[int(x[1])]} de {x[0]}')

data()
