def leit():
    dados = dict()
    for a in range(5):
        d = dict()
        print(f'Digite os dados da {a + 1}° pessoa')
        s = str(input('Sexo: [M/F] ')).upper()[0]
        o = str(input('Cor dos olhos: [A - Azuis, C - Castanhos] ')).upper()[0]
        c = str(input('Cor dos cabelos: [L - Louros,P - Pretos , C - Castanhos] ')).upper()[0]
        i = int(input('Idade: '))
        d = {'sexo': s, 'olhos_cor': o, 'cabelos_cor': c, 'idade': i}
        dados[f'pessoa{a + 1}'] = d
    return dados



def media1(dados):
    s = 0
    cont = 0
    for i in dados:
        if dados[i]['olhos_cor'] == 'C' and dados[i]['cabelos_cor'] == 'P':
            s += dados[i]['idade']
            cont += 1
    if cont == 0:
        return 0
    return s / cont



def maiorid(dados):
    m = 0
    for i in dados:
        if dados[i]['idade'] > m:
            m = dados[i]['idade']
    return m



def femal(dados):
    cont = 0
    for  i in dados:
        if dados[i]['olhos_cor'] == 'A' and dados[i]['cabelos_cor'] == 'L' and dados[i]['sexo'] == 'F' and 18 <= dados[i]['idade'] <= 35:
            cont += 1
    return cont



dados = leit()

print(f"A media de idades entre as pessoas com olhos castanhos e cabelos pretos é {media1(dados)}")

print(f'A maior idade é {maiorid(dados)}')

print(f'O número de indivíduos com o sexo feminino, olhos azuis, cabelos louros e com a idade entre 18 e 35 anos é {femal(dados)}')