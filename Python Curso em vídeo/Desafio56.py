mdi= 0
mn= 0
hmv= 0
nomehmv= ''
for c in range(0,4):
    nome= str(input('Qual é o seu nome? ')).strip()
    idade= int(input('Qual é a sua idade? '))
    mdi += idade
    mdidade= mdi/4
    sexo= str(input('Qual o seu sexo? ')).strip()
    sexomin= sexo.lower()
    if idade > hmv and sexomin == 'masculino':
        hmv= idade
        nomehmv= nome
    # hmv = Homem Mais Velho
    # mn = mulheres novas
    if idade < 20 and sexomin == 'feminino':
        mn += 1
print('Dos indivíduos(as) analisados(as), temos as seguintes informações:')
print(f'''
A MÉDIA DE IDADE DOS INDIVÍDUOS ANALISADOS É: {mdidade :.1f}
O HOMEM MAIS VELHO É {nomehmv} COM {hmv :.0f} ANOS
E {mn} MULHERES TEM MENOS DE 20 ANOS
''')