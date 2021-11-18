def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 70 >= i >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif i > 70 or 18 > i > 16:
        return f'Com {idade} anos: VOTO FACULTATIVO.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


print('-=-' * 30)
i = int(input('Em que ano você nasceu? '))
print(voto(i))
