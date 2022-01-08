def pares_impares(*args):
    A = list()
    B = list()
    for a in args:
        if a % 2 == 0:
            A.append(a)
        else:
            B.append(a)
    print(f'A => {A}\nB => {B}')



pares_impares(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)