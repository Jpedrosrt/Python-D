def norm(*args):
    print(args)


def inve(*args):
    print(args[::-1])


def media(*args):
    print(sum(args)/ len(args))

norm(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30)
inve(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30)
media(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30)