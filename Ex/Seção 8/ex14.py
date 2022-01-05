def consumo(km, l):
    if km/l < 8:
        return 'Venda o carro!'
    elif 8 <= km/l <= 12:
        return 'Econômico!'
    return 'Super Econômico!'

print(consumo(30, 2))
