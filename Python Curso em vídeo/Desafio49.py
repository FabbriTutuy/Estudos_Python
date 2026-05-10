t = int(input('Escolha o número para fazer a tabuada '))
e = int(input('Escolha até que número você quer? '))
print('=-'*8)
for  c in range(1,e+1):
    print(f'{t} x {c} = {t*c}')
print('=-'*8)
