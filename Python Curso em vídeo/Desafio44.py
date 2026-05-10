print('=-'*20)
print('CALCULADOR DE JUROS')
print('=-'*20)
p = float(input('Qual o preço do produto comprado? '))
print('=-'*20)
print('QUAL FORMA DE PAGAMENTO')
print('=-'*20)
print('[1] = À vista/Cheque = 10% De Desconto')
print('[2] = À vista no cartão = 5% De Desconto ')
print('[3] = 2x no Cartão = Preço Normal')
print('[4] = 3x ou mais no Cartão = 20% De Desconto')
print('=-'*20)
e = int(input('Qual a sua escolha? '))
f1 = (p*10)/100+p
f2 = (p*5)/100+p
f4 = (p*20)/100+p
if e == 1:
    print(f'Você pagará {f1}')
elif e == 2:
    print(f'Você pagará {f2}')
elif e == 3:
    print(f'Você Pagará {p}')
elif e == 4:
    print(f'Você pagará {f4}')
else:
    print('ERROR')
    print('Refaz o progama :D')
