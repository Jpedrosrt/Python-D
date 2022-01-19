def soma(a, b):
    s = dict()

    for i in b:
        s[i] = a[i] + b[i]

    return s



x = {'x': 5,'y': 4,'z': 6}
y = {'x': 9,'y': 2,'z': 2}

print(soma(x, y))