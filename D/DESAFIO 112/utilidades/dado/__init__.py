def leiadin(num=0):
    while True:
        num = str(input(num)).strip().replace(',', '.')
        if num.replace('.', '').isdigit():
            num = float(num)
            return num
        else:
            print(f'\033[0;31mERRO: "{num}" é um valor inválido!\033[m')
