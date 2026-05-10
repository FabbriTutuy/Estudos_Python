v = float(input('Qual a distância que você viajará? '))
p1 = v*0.50
p2 = v*0.45
if v >=200:
    print(f'Você pagará {p1}')
else:
    print(f'Você pagará {p2}')
