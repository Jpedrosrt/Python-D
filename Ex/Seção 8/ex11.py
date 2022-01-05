def notas(n1, n2, n3, l):
    if l.upper() == 'A':
        return (n1 + n2 + n3)/3
    elif l.upper() == 'P':
        return (n1 * 5 + n2 * 3 + n3 * 2) / 10
    return 'Parâmetro inválido'


print(notas(8, 8, 8, 'p'))