x = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 10, 'Estojo', 25.90, 'Transferidor', 8.50, 'Compasso', 4.50,
     'Mochila', 149.99, 'Canetas', 8.50, 'Livro', 37.80)
print('-' * 40)
print('''           LISTAGEM DE PREÇOS      ''')
print('-' * 40)
for a in range(0, len(x), 2):
    print(f'{x[a]:.<30}', 'R$', f'{x[a + 1]:>7.2f}')
