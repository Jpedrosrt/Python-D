x = ('Lapis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro')
for a in x:
    print(f'\nNa palavra {a.upper()} temos', end=' ')
    for b in a:
        if b.lower() in 'aeiou':
            print(b, end=' ')