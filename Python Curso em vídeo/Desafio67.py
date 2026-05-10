t = 0 
vt = 0
while True:
    t = int(input(' Quer ver a tabuada de qual número (-1 para desligar ) '))
    print('=-'*15)
    while vt != 11:
        print(f'{t} x {vt} = {t*vt}')
        vt += 1
    vt -= 10
    if t == -1 :
        break
    print('=-'*15)
print('Fim ... ')