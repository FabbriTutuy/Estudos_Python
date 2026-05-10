f = str(input('Digite uma frase ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j)-1 ,-1 , -1 ):
    i +=j[l]
print(f'O inverso de {f} é {i} ')
if i == j:
    print('Temos um Palíndromo')
else:
    print('Não temos um Palíndromo')
