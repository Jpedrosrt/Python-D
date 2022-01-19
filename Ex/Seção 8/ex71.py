def dentrofora(retangulo, p):
    if p[0] >= retangulo[1]['x'] or p[0] <= retangulo[0]['x'] or p[1] >= retangulo[1]['y'] or p[1] <= retangulo[0]['y']:
        return 0
    else:
        return 1


v1 = { 'x': 0, 'y': 0}
v2 = { 'x': 5, 'y': 3}

retangulo = [v1, v2]
p = (1, 1)

print(dentrofora(retangulo, p))
