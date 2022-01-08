def desv(*args):
    m = sum(args)/len(args)
    s = 0
    for a in args:
        s += (a - m)**2
    return ( ( 1 / (len(args) - 1) ) * s ) ** 0.5

print(desv(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30))