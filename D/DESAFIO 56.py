soma = 0
ve = 0
cont = 0
cont2 = 0
for a in range(1, 5):
    cont2 += 1
    print(f'----- {a}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade
    if sexo == 'M' and idade > ve:
        ve = idade
        ven = nome
    if sexo == 'F' and idade < 20:
        cont += 1
media = soma/cont2
print(f'A média de idade do grupo é de {media:.1f} anos.\n'
      f'O homem mais velho tem {ve} anos e se chama {ven}.\n'
      f'Ao todo são {cont} mulheres com menos de 20 anos.')








