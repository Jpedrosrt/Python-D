x = int(input('Que valor você quer sacar? R$ '))
c50 = x // 50
aux = x - c50 * 50
c20 = aux // 20
aux = aux - c20 * 20
c10 = aux // 10
aux = aux - c10 * 10
if c50 != 0:
      print(f'Total de {c50} cédulas de R$ 50')
if c20 != 0:
      print(f'Total de {c20} cédulas de R$ 20')
if c10 != 0:
      print(f'Total de {c10} cédulas de R$ 10')
if aux != 0:
      print(f'Total de {aux} cédulas de R$ 1')