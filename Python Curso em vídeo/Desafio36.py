print('=~='*15)

vc = int(input('Qual o valor da casa? '))
s = int(input('Quanto você ganha mensalmente? '))
qa = int(input('Por quantos anos você quer pagar essa casa? '))
x = vc/(qa*12) 
y = (s*30)/100
if x <= y:
    print(f'Você pagará mensalmente R${x}')
else:
    print('Você não poderá pagar o  emprestimo')

print('=~='*15)
